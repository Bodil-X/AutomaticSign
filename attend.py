# -*- coding: UTF-8 -*-
import urllib, urllib2, httplib, cookielib
import re, json
import Cookie
import time
import string
from datetime import datetime

from google.appengine.api import urlfetch

__author__ = 'Bodil'


def get_cookie(acct, password):
    login_url = 'http://www.smzdm.com/user/login'
    login_headers = {
        'Host': 'www.smzdm.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
        'Referer': 'http://www.smzdm.com/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'Keep-Alive',
        'X-Requested-With': 'XMLHttpRequest'
    }
    login_post = {
        'user_login': acct,
        'user_pass': password,
        'rememberme': 1,
        'is_pop': 1
    }
    request = urllib2.Request(login_url, login_post, login_headers)
    cookie = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)
    opener.open(request)
    # b = urlfetch.fetch(url=url_str, method=urlfetch.GET)
    # cookie = Cookie.SimpleCookie(b.headers.get('set-cookie'))
    print(cookie)
    return cookie


def attendance(cookie):
    # headers = {'www.smzdm.com': cookie}
    # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    #urllib2.install_opener(opener)
    url = 'http://www.smzdm.com/wp-content/plugins/daily_attendance/add_daily_attendance.php'
    attend_reqst = urllib2.Request(url)
    json_str = urllib2.urlopen(attend_reqst).read()
    #json_str = opener.open(attend_reqst).read()
    json_dict = json.loads(json_str)
    print(json_dict)
    return json_dict