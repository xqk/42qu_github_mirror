#!/usr/bin/env python
# -*- coding: utf-8 -*-
from _handler import Base, LoginBase, XsrfGetBase
from zweb._urlmap import urlmap
from config import SITE_HTTP
from model.cid import CID_TRADE_CHARDE, CID_TRADE_WITHDRAW
from model.money import pay_account_new, pay_account_get, withdraw_new, TRADE_STATE_FINISH
from model.money_alipay import alipay_payurl
from model.user_auth import user_password_verify

@urlmap('/money')
class Money(LoginBase):
    def get(self):
        self.render()

@urlmap('/money/charge')
@urlmap('/money/charge/(\d{1,8}(?:\.\d{1,2})?)')
class Charge(LoginBase):
    def get(self, price='42'):
        self.render(price=price)

    def post(self, price=None):
        price = self.get_argument('price', None)
        error = None
        try:
            price = float(price)
        except ValueError:
            error = '金额输入错误'
        else:
            charge_min = 0.42
            charge_max = 100000000
            if price < charge_min:
                error = '单笔充值最少为%s' % charge_min
            elif price > charge_max:
                error = '单笔充值最多为%s' % charge_max
            else:
                return_url = '%s/rpc/money/alipay_sync' % SITE_HTTP
                notify_url = '%s/rpc/money/alipay_async' % SITE_HTTP
                return self.redirect(
                    alipay_payurl(
                        self.current_user_id,
                        price,
                        return_url,
                        notify_url,
                        '%s 充值' % self.current_user.name,
                    )
                )

@urlmap('/money/charged/(\d+)/(\d+)')
class Charged(Base):
    def get(self, tid, uid):
        uid = int(uid)
        t = Trade.get(tid)
        if t and t.cid == CID_TRADE_CHARDE and t.state == TRADE_STATE_FINISH and t.to_id == uid:
            self.render(trade=t)
        else:
            self.redirect('/money')

@urlmap('/money/draw')
class Draw(LoginBase):
    def get(self):
        user_id = self.current_user_id
        account, name = pay_account_get(user_id)
        self.render(
            account=account,
            name=name,
        )

    def post(self):
        user_id = self.current_user_id
        password = self.get_argument('password', '')
        account = self.get_argument('account', '')
        name = self.get_argument('name', '')
        price = self.get_argument('price', '')

        if user_password_verify(user_id, password):
            pass

@urlmap('/money/drawed/(\d+)')
class Drawed(LoginBase):
    def get(self, tid):
        t = Trade.get(tid)
        if t and t.from_id == self.current_user_id:
            self.render(trade=t)
        else:
            self.redirect('/money')


