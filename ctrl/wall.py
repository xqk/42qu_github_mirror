#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _handler
from zweb._urlmap import urlmap
from model.reply import STATE_SECRET, STATE_ACTIVE
from model.wall import Wall
from model.reply import Reply
from zkit.page import page_limit_offset


PAGE_LIMIT = 42


@urlmap("/wall")
class Index(_handler.LoginBase):
    def get(self):
        zsite = self.zsite
        self.redirect(zsite.link)

    def post(self):
        zsite = self.zsite
        txt = self.get_argument('txt', None)
        if txt:
            secret = self.get_argument('secret', None)
            current_user = self.current_user
            reply = zsite.reply_new(
                current_user.id,
                txt,
                STATE_SECRET if secret else STATE_ACTIVE
            )
        link = zsite.link
        self.redirect(link)


@urlmap("/wall/(\-?\d+)")
class Page(_handler.Base):
    def get(self, page):
        zsite = self.zsite
        zsite_link = zsite.link
        page, limit, offset = page_limit_offset(
            "%s/wall/%%s"%zsite_link,
            zsite.reply_total,
            page,
            PAGE_LIMIT
        )
        reply_list = zsite.reply_list_reversed(limit, offset)

        self.render(
            reply_list=reply_list,
            page=page
        )

@urlmap("/wall/reply2txt/(\d+)")
class Reply2Txt(_handler.Base):
    def get(self, id):
        link = "/"
        reply = Reply.mc_get(id)
        if reply:
            link = "/wall/txt/%s"%reply.rid
        
        self.redirect(link,True)

@urlmap("/wall/txt/(\d+)")
@urlmap("/wall/txt/(\d+)/(\d+)")
class Txt(_handler.Base):
    def get(self, id, page=1):
        zsite = self.zsite
        zsite_id = zsite.id
        zsite_link = zsite.link


        wall = Wall.mc_get(id)

        zsite_id_list = wall.zsite_id_list()

        page, limit, offset = page_limit_offset(
            "%s/wall/txt/%s/%%s"%(zsite_link,id),
            zsite.reply_total,
            page,
            PAGE_LIMIT
        )
        
        reply_list = wall.reply_list_reversed(limit, offset)

        self.render(
            wall = wall,
            zsite_id_list = zsite_id_list,
            reply_list = reply_list,
            page = page
        )

    def post(self):
        pass
