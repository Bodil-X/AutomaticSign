#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'bodil'

from google.appengine.api import urlfetch
import urllib
import urllib2
import json

from model import Account


class Smzdm(object):
    def __init__(self, account):
        self.login_url = 'http://www.smzdm.com/user/login/jsonp_check'
        self.attend_url = 'http://www.smzdm.com/user/qiandao/jsonp_checkin'
        self.headers = {
            'Host': 'www.smzdm.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0'
        }
        self.login_post = {
            'rememberme': 1,
            'is_pop': 1
        }
        self.__prepare_auth(account)

    def __prepare_auth(self, account):
        if not isinstance(account, Account):
            raise TypeError('argument ''account'' is not Account Type')

        self.login_post['user_login'] = account.acct
        self.login_post['user_pass'] = account.psw
        post_data = urllib.urlencode(self.login_post)

        # self.cookie = StringCookieJar()
        # self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        # self.opener.open(self.login_url, post_data)
        result = urlfetch.fetch(self.login_url, post_data, urlfetch.POST, self.headers)
        if result.status_code == 200:
            self.headers['Cookie'] = result.headers.get('set-cookie')

    def attendance(self):
        # req = urllib2.Request(self.attend_url, headers=self.headers)
        try:
            # result = self.opener.open(req).read()
            result = urlfetch.fetch(self.attend_url, headers=self.headers, follow_redirects=False)
            if result.status_code == 200:
                json_dict_result = json.loads(result.content)
                print json_dict_result
                return json_dict_result
            print result.content
            return result.status_code
        except urllib2.HTTPError, e:
            print e
            return False