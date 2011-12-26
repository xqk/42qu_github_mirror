#coding:utf-8

from model.cid import CID_BUZZ_SYS,  CID_BUZZ_FOLLOW, CID_BUZZ_WALL, CID_BUZZ_WALL_REPLY, CID_BUZZ_PO_REPLY, CID_BUZZ_ANSWER, CID_BUZZ_JOIN, CID_BUZZ_EVENT_JOIN_APPLY, CID_BUZZ_EVENT_FEEDBACK_JOINER, CID_BUZZ_EVENT_FEEDBACK_OWNER, CID_USER, CID_BUZZ_SITE_NEW , CID_BUZZ_SITE_FAV, CID_BUZZ_WORD

CID_EVENT_LIST = (
    CID_BUZZ_EVENT_JOIN_APPLY,
)

CID_FOLLOW_LIST = (
    CID_BUZZ_FOLLOW,
    CID_BUZZ_SITE_NEW,
    CID_BUZZ_SITE_FAV,
    CID_BUZZ_JOIN,
)

CID_REPLY_LIST = (
    CID_BUZZ_PO_REPLY,
    CID_BUZZ_ANSWER,
    CID_BUZZ_EVENT_FEEDBACK_JOINER,
    CID_BUZZ_EVENT_FEEDBACK_OWNER,
    CID_BUZZ_WALL
)

CID_BUZZ_BLOCK_EVENT = 1
CID_BUZZ_BLOCK_FOLLOW = 2
CID_BUZZ_BLOCK_REPLY = 3
CID_BUZZ_BLOCK_AT = 4

BUZZ_CID2LIST = {
    CID_BUZZ_BLOCK_EVENT  : CID_EVENT_LIST,
    CID_BUZZ_BLOCK_FOLLOW : CID_FOLLOW_LIST,
    CID_BUZZ_BLOCK_REPLY  : CID_REPLY_LIST,
}