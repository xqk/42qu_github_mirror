#!/usr/bin/env python
# -*- coding: utf-8 -*-
from _handler import Base
from _urlmap import urlmap

@urlmap('/')
class Index(Base):
    def get(self):
        self.render()

@urlmap('/chart')
class Chart(Base):
    def get(self):
        self.render()
