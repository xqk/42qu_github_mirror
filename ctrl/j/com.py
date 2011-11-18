#coding:utf-8
from ctrl._urlmap.j import urlmap
from _handler import JLoginBase
from model.zsite_member import zsite_member_can_admin, zsite_member_rm
from model.zsite_url import zsite_by_domain, url_by_digit_domain
from model.cid import CID_COM

class AdminBase(JLoginBase):
    def prepare(self):
        super(AdminBase, self).prepare()

        request = self.request
        host = request.host
        zsite = zsite_by_domain(host)
        if zsite is None:
            self.zsite_id = 0
        else:
            self.zsite_id = zsite.id
        self.zsite = zsite

        zsite = self.zsite
        if not zsite.cid == CID_COM or not zsite_member_can_admin(self.zsite_id, self.current_user_id):
            self.finish('{}')

@urlmap('/j/member/invite/rm/(\d+)')
class MemberInviteRm(AdminBase):
    def get(self, id):
        zsite_id = self.zsite_id
        current_user_id = self.current_user_id
        id = int(id)
        if id != current_user_id:
            zsite_member_rm(zsite_id, id)
        self.finish('{}')