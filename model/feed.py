#!/usr/bin/env python
#coding:utf-8

from _db import cursor_by_table, Model, McCache, McLimitA, McCacheA
from zkit.mc_func import mc_func_get_multi
from follow import follow_id_list_by_zsite_id
from zkit.algorithm.merge import imerge

mc_feed_entry_iter = McCacheA("FeedEntryIter:%s")
mc_feed_id_by_zsite_id_cid = McCache("FeedIdByZsiteIdCid:%s")
mc_feed_id_list_by_zsite_id = McCacheA("FeedIdByZsiteId:%s")
mc_feed_id_by_for_zsite_follow = McCache("FeedIdForZsiteFollow.%s")


class Feed(Model):
    pass

cursor = cursor_by_table('feed_entry')

def feed_entry_new(id, zsite_id, cid):
    feed_id = feed_id_by_zsite_id_cid(zsite_id, cid)
    cursor.execute(
        "insert into feed_entry (id, feed_id) values (%s,%s)",
        (id, feed_id)
    )
    cursor.connection.commit()
    mc_feed_entry_iter.delete(feed_id)
    return id

def feed_entry_rm(id):
    o = FeedEntry.mc_get(id)
    if not o:
        return
    feed_id = o.feed_id
    o.delete()
    mc_feed_entry_iter.delete(feed_id)


@mc_feed_id_list_by_zsite_id("{zsite_id}")
def feed_id_list_by_zsite_id(zsite_id):
    return Feed.where(zsite_id=zsite_id).id_list()

@mc_feed_id_by_for_zsite_follow("{zsite_id}")
def feed_id_list_for_zsite_follow(zsite_id):
    key_list = follow_id_list_by_zsite_id(zsite_id)
    key_list.append(zsite_id)
    feed_id_list = mc_func_get_multi(
        mc_feed_id_list_by_zsite_id,
        feed_id_list_by_zsite_id,
        key_list
    )
    return feed_id_list

def mc_flush_zsite_follow(zsite_id):
    for i in follow_id_list_by_zsite_id(zsite_id):
        mc_feed_id_by_for_zsite_follow.delete(i)

from mq import mq_client
mq_mc_flush_zsite_follow = mq_client(mc_flush_zsite_follow)


@mc_feed_id_by_zsite_id_cid("{zsite_id}_{cid}")
def feed_id_by_zsite_id_cid(zsite_id, cid):
    feed = Feed.get_or_create(zsite_id=zsite_id, cid=cid)
    if not feed.id:
        feed.save()
        mc_feed_id_list_by_zsite_id.delete(zsite_id)
        mq_mc_flush_zsite_follow(zsite_id)
    return feed.id


import sys
MAXINT = sys.maxint
PAGE_LIMIT = 42
FEED_ENTRY_ID_LASTEST_SQL = "select id from feed_entry where feed_id=%%s order by id desc limit %s"%PAGE_LIMIT
FEED_ENTRY_ID_ITER_SQL = "select id from feed_entry where feed_id=%%s and id<%%s order by id desc limit %s"%PAGE_LIMIT

@mc_feed_entry_iter("{feed_id}")
def feed_entry_id_lastest(feed_id):
    cursor.execute(FEED_ENTRY_ID_LASTEST_SQL, feed_id)
    return [
        i for i, in cursor
    ]

#TODO : 消息流的合并, feed_entry_id_iter 函数可以考虑用天涯的内存数据库来优化
#http://code.google.com/p/memlink/
def feed_entry_id_iter(id, start_id=MAXINT, ):
    if start_id == MAXINT:
        id_list = feed_entry_id_lastest(id)
        if id_list:
            for i in id_list:
                yield i
            start_id = i
        else:
            return
    while True:
        cursor.execute(FEED_ENTRY_ID_ITER_SQL, (id, start_id))
        c = cursor.fetchall()
        if not c:
            break
        for i, in c:
            yield i
        start_id = i

def feed_entry_cmp_iter(id, start_id=sys.maxint):
    for i in feed_entry_id_iter(id, start_id):
        yield FeedEntryCmp(id, i)

class FeedEntryCmp(object):
    def __init__(self, feed_id, id):
        self.id = id
        self.feed_id = feed_id

    def __cmp__(self, other):
        return other.id - self.id

class FeedMerge(object):
    def __init__(self, feed_id_list):
        self.feed_id_list = feed_id_list

    def merge_iter(self, limit=MAXINT, begin_id=MAXINT):
        feed_id_list = self.feed_id_list

        count = 0
        for i in imerge(
            *[
                feed_entry_cmp_iter(i, begin_id)
                for i in
                feed_id_list
            ]
        ):
            yield i
            count += 1
            if count >= limit:
                break

    def entry_iter(self, limit=MAXINT, begin_id=MAXINT):
        feed_id_set = set()

        r = []
        for i in self.merge_iter(limit, begin_id):
            feed_id_set.add(i.feed_id)
            r.append(i)

        feed_dict = Feed.mc_get_mulit(feed_id_set)




if __name__ == "__main__":
    for i in FeedMerge(feed_id_list_for_zsite_follow(10000000)).merge_iter():
        print i.id, i.feed_id

