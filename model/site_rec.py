#coding:utf-8

from _db import cursor_by_table, McModel, McLimitA, McCache, McNum, Model, McCacheM, McCacheA
from model.zsite import Zsite
from kv import Kv
from model.zsite import  Zsite
from model.cid import CID_SITE
from model.zsite_fav import zsite_fav_new

SiteRec = Kv('site_rec', 0)

class SiteRecHistory(Model):
    pass

def site_rec(user_id):
    zsite_id = SiteRec.get(user_id)
    if zsite_id:
        return Zsite.mc_get(zsite_id)


SITE_REC_STATE_REJECT = 0
SITE_REC_STATE_PASS = 1
SITE_REC_STATE_FAV = 2
SITE_REC_STATE = (0,1,2)


def site_rec_feeckback(user_id, zsite_id, state):
    site = Zsite.mc_get(zsite_id)
    state = int(state)

    if not (site and site.cid == CID_SITE):
        return

    if state not in SITE_REC_STATE:
        return


    if state == SITE_REC_STATE_FAV:
        zsite_fav_new(site, user_id)


    SiteRecHistory(
        user_id=user_id, zsite_id=zsite_id, state=state
    ).save()

    SiteRec.set(user_id, 0)

