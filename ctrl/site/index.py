# -*- coding: utf-8 -*-

from _handler import Base, LoginBase
from ctrl._urlmap.site import urlmap
from zkit.jsdict import JsDict
from urlparse import parse_qs, urlparse
from zkit.page import page_limit_offset
from model.oauth import linkify
from model.zsite_link import SITE_LINK_NAME,SITE_LINK_ZSITE_DICT
from model.zsite_link import OAUTH2NAME_DICT, link_list_save, link_id_name_by_zsite_id, link_id_cid, link_by_id, OAUTH_LINK_DEFAULT
from zkit.errtip import Errtip
from model.zsite_url import url_by_id, url_new, url_valid, RE_URL
from zkit.pic import picopen
from model.ico import site_ico_new, site_ico_bind
from model.zsite_site import site_new
from model.motto import motto_set
from model.txt import txt_new

PAGE_LIMIT = 25

class SiteListBase(object):
    def get(self):
        return self.render("/ctrl/site/index/index.htm")



@urlmap('/')
class Index(SiteListBase, Base):
    pass

@urlmap("/my")
class My( SiteListBase, LoginBase):
    pass


@urlmap('/new')
class New(LoginBase):
    def get(self):
        link_cid = []
        for cid, name in SITE_LINK_NAME:
            link_cid.append(
                (
                    cid,
                    name, 
                    ''
                )
            )
        return self.render(
            errtip=JsDict(),
            link_cid=link_cid,
            link_list=[]
        )

    def post(self):
        arguments = self.request.arguments

        current_user =  self.current_user
        current_user_id = current_user.id

        link_cid = []
        link_kv = []
        errtip = Errtip()

        name = self.get_argument('name',None)
        motto = self.get_argument('motto', None)
        url = self.get_argument('url', None)
        txt = self.get_argument('txt', None)
        sitetype = int(self.get_argument('sitetype'))


        for cid, link in zip(arguments.get('cid',[]), arguments.get('link',[])):
            cid = int(cid)
            link_name = SITE_LINK_ZSITE_DICT[cid]
            link_cid.append(
                (cid, link_name, linkify(link, cid))
            )

            

        for id, key, value in zip(
            arguments.get('id',[]),
            arguments.get('key',[]),
            arguments.get('value',[])
        ):
            id = int(id)
            link = linkify(value)

            link_kv.append(
                (id, key.strip() or urlparse(link).netloc, link)
            )


        files = self.request.files
        pic_id = None
 
        if 'pic' in files:
            pic = files['pic'][0]['body']
            pic = picopen(pic)
            if pic:
                pic_id = site_ico_new(current_user_id, pic)
            else:
                errtip.pic = '图片格式有误'
        else:
            pic_id = self.get_argument('pic_id',None)
            if not pic_id:
                errtip.pic = "请上传图片"




        if not name:
            errtip.name = "请输入名称"
        
        if not motto:
            errtip.motto = "请编写签名"
        
        if url:
            errtip.url = url_valid(url)


        if errtip:
            for cid, link_name in SITE_LINK_NAME:
                if cid not in set(i[0] for i in link_cid):
                    link_cid.append(
                        (
                            cid,
                            link_name, 
                            ''
                        )
                    )


        if not errtip:
            site = site_new(name, current_user_id, sitetype)                 
            site_id = site.id 
            link_list_save(site_id, link_cid, link_kv)
            site_ico_bind(current_user_id, pic_id, site_id)
            motto_set(site_id, motto)
            txt_new(site_id, txt)
            if url:
                url_new(site_id, url)
            return self.redirect(site.link)

        return self.render(
            errtip=errtip,
            link_cid=link_cid,
            link_list=link_kv,
            name=name,
            motto=motto,
            url=url,
            sitetype=sitetype,
            txt=txt,
            pic_id=pic_id
        )



