#!/usr/bin/env python
# -*- coding: utf-8 -*-
from _handler import Base, LoginBase, XsrfGetBase, ZsiteBase
from zweb._urlmap import urlmap
from model.po import po_rm, po_word_new, Po
from model.po_pos import po_pos_get, po_pos_set
from model import reply
from model.zsite import Zsite
from model.zsite_tag import zsite_tag_list_by_zsite_id_with_init, tag_id_by_po_id

@urlmap('/note/(\d+)', template='note')
@urlmap('/word/(\d+)', template='word')
@urlmap('/question/(\d+)', template='question')
@urlmap('/answer/(\d+)', template='answer')
class Index(ZsiteBase):
    def initialize(self, template):
        self.template = 'ctrl/zsite/po/%s.htm' % template

    def get(self, id):
        po = Po.mc_get(id)
        current_user_id = self.current_user_id
        if not po:
            return self.redirect('/')

        if po.user_id != self.zsite_id:
            link = po.link
            return self.redirect(link)

        current_user_id = self.current_user_id
        can_admin = po.can_admin(current_user_id)
        can_view = po.can_view(current_user_id)
        if can_view and current_user_id:
            po_pos_set(current_user_id, po)
        return self.render(
            po=po,
            can_admin=can_admin,
            can_view=can_view
        )


@urlmap('/po/reply/rm/(\d+)')
class ReplyRm(LoginBase):
    def post(self, id):
        current_user_id = self.current_user_id
        r = reply.Reply.mc_get(id)
        can_rm = r.can_rm(current_user_id)

        if r:
            po = Po.mc_get(r.rid)
            if po:
                if can_rm is False and po.can_admin(current_user_id):
                    can_rm = True

        if can_rm:
            r.rm()

        self.finish({'success' : can_rm})


@urlmap('/po/reply/(\d+)')
class Reply(LoginBase):
    def post(self, id):
        po = Po.mc_get(id)
        if po:
            current_user_id = self.current_user_id
            can_view = po.can_view(current_user_id)
            link = po.link
            if can_view:
                txt = self.get_argument('txt', '')
                m = po.reply_new(current_user_id, txt, po.state)
                if m:
                    link = '%s#reply%s' % (link, m)
        else:
            link = '/'
        self.redirect(link)


    def get(self, id):
        po = Po.mc_get(id)
        if po:
            link = po.link
        else:
            link = '/'
        self.redirect(link)


@urlmap('/po/rm/(\d+)')
class Rm(XsrfGetBase):
    def get(self, id):
        current_user = self.current_user
        current_user_id = self.current_user_id
        po_rm(current_user_id, id)
        self.redirect(current_user.link)

    post = get


@urlmap('/po/tag/(\d+)')
class Tag(LoginBase):
    def get(self, id):
        current_user = self.current_user
        current_user_id = self.current_user_id
        po = Po.mc_get(id)
        if not (po and po.can_admin(current_user_id)):
            return self.redirect('/')
        tag_list = zsite_tag_list_by_zsite_id_with_init(current_user_id)
        po_id = po.id
        tag_id = tag_id_by_po_id(current_user_id, po_id)
        self.render(tag_list=tag_list, po=po, tag_id=tag_id)

    def post(self, id):
        pass


