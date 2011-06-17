# -*- coding: utf-8 -*-
from _handler import Base, LoginBase, XsrfGetBase
from ctrl._urlmap.main import urlmap

@urlmap('/')
class Index(Base):
    def get(self):
        current_user = self.current_user
        if current_user:
            self.redirect(
                "%s/live"%current_user.link
            )
        else:
            self.redirect("/auth/reg")
