#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env
from _db import Model, McModel, redis
from part_time_job import part_time_job_new, PART_TIME_JOB_CID_FEED_IMPORT, id_list_by_part_time_job_cid, part_time_job_count_by_cid
from model.tag_admin import tag_admin_rm
from po_tag import REDIS_REC_CID_DICT, tag_id_list_by_str_list
from operator import itemgetter
from model.zsite import Zsite
from config import ZSITE_DOUBAN_ID, ZSITE_UCD_CHINA_ID
from urllib import quote
FEED_IMPORT_STATE_RM = 0
FEED_IMPORT_STATE_WITHOUT_TAG = 10
FEED_IMPORT_STATE_INIT = 20
FEED_IMPORT_STATE_REVIEWED = 30
FEED_IMPORT_STATE_REVIEWED_WITHOUT_AUTHOR = 40
FEED_IMPORT_STATE_REVIEWED_SYNC = 50
FEED_IMPORT_STATE_REVIEWED_WITHOUT_AUTHOR_SYNC = 60
FEED_IMPORT_STATE_POED = 70

def feed_import_list_count_by_part_time_job(limit , offset):
    cid = PART_TIME_JOB_CID_FEED_IMPORT
    id_list = id_list_by_part_time_job_cid(cid, limit, offset)
    feed_list = map(FeedImport.get, map(itemgetter(0), id_list))
    user_list = Zsite.mc_get_list(map(itemgetter(1), id_list))
    for i, u, t in zip(feed_list, user_list, map(itemgetter(2), id_list)):
        i.admin = u
        i.time = t

    return feed_list, part_time_job_count_by_cid(cid)


class PoMeta(McModel):
    pass

class FeedImport(Model):
    @property
    def tag_list(self):
        tag_id_list = self.tag_id_list
        if tag_id_list:
            tag_id_list = map(int, tag_id_list.split(' '))
            tag_list = Zsite.mc_get_list(tag_id_list)
        else:
            tag_list = []
        return tag_list


class PoMetaUser(McModel):
    @property
    def link(self):
        if self.cid == ZSITE_DOUBAN_ID:
            return 'http://www.douban.com/people/%s'%self.url
        elif self.cid == ZSITE_UCD_CHINA_ID:
            return 'http://ucdchina.com/author/%s'%quote(self.name)

def user_url_by_po_meta_user_id(id):
    user = PoMetaUser.mc_get(id)
    if user:
        return user.link

def feed_next():
    fdlist = FeedImport.where(state=FEED_IMPORT_STATE_INIT)[1:2]
    if fdlist:
        return fdlist[0]

def feed_import_rm(id, current_user_id):
    feed = FeedImport.get(id)
    if feed:
        part_time_job_new(PART_TIME_JOB_CID_FEED_IMPORT, id, current_user_id)
        feed_state_set(id, FEED_IMPORT_STATE_RM)
        tag_admin_rm(
            id,
            feed.tag_id_list.split(' ')
        )

def feed_state_set(id, state):
    feed = FeedImport.get(id)
    if feed:
        feed.state = state
        feed.save()



def feed_review(id, cid, title, txt, tag_id_list, current_user_id, author_rm=False, sync=False):
    feed = FeedImport.get(id)
    if feed:
        tag_admin_rm(id, feed.tag_id_list.split(' '))

        if feed.state == FEED_IMPORT_STATE_INIT:
            if author_rm:
                if sync:
                    feed.state = FEED_IMPORT_STATE_REVIEWED_WITHOUT_AUTHOR_SYNC
                else:
                    feed.state = FEED_IMPORT_STATE_REVIEWED_WITHOUT_AUTHOR
            else:
                if sync:
                    feed.state = FEED_IMPORT_STATE_REVIEWED_SYNC
                else:
                    feed.state = FEED_IMPORT_STATE_REVIEWED

            feed.cid = int(cid)
            feed.title = title
            feed.txt = txt


            feed.tag_id_list = ' '.join(map(str, tag_id_list_by_str_list(tag_id_list)))

            feed.save()
            part_time_job_new(PART_TIME_JOB_CID_FEED_IMPORT, feed.id, current_user_id)



if __name__ == '__main__':
    pass
    #from collections import defaultdict
    #user_count = defaultdict(list)
    from zweb.orm import ormiter
    for i in ormiter(FeedImport,"zsite_id=%s"%ZSITE_UCD_CHINA_ID):
        print i.tag_id_list 
        tag_admin_rm(
            i.id,
            i.tag_id_list.split(' ')
        )
        i.delete()
