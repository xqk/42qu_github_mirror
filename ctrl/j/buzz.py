#!/usr/bin/env python
# -*- coding: utf-8 

from ctrl._urlmap.j import urlmap
from _handler import JLoginBase, Base
from model.buzz import Buzz, buzz_set_read, clear_buzz_by_po_id, clear_buzz_by_user_id_cid
from model.po import Po, PO_SHARE_FAV_CID
from json import dumps
from model.buzz_reply import buzz_reply_hide_or_rm

@urlmap('/j/buzz/reply/x')
class BuzzX(JLoginBase):
    def post(self):
        current_user_id = self.current_user_id
        clear_buzz_by_po_id(current_user_id, id)
        self.finish('{}')


@urlmap("/j/buzz/reply/x/(\d+)")
class BuzzReplyX(JLoginBase):
    def post(self, id):
        current_user_id = self.current_user_id
        buzz_reply_hide_or_rm(id, current_user_id)
        self.finish('{}')