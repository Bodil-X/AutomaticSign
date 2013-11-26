#-*- coding: UTF-8 -*-
import urllib, urllib2, httplib, cookielib
import re, json
import Cookie
import time
import string
from datetime import datetime

from google.appengine.api import urlfetch

__author__ = 'Bodil'


def get_cookie(acct, password):
    url_str = 'http://www.smzdm.com//wp-login.php?log=' + acct + '&pwd=' + password
    cookie = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)
    request = urllib2.Request(url_str)
    opener.open(request)
    #b = urlfetch.fetch(url=url_str, method=urlfetch.GET)
    #cookie = Cookie.SimpleCookie(b.headers.get('set-cookie'))
    print(cookie)
    return cookie


def attendance(cookie):
    #headers = {'www.smzdm.com': cookie}
    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    #urllib2.install_opener(opener)
    url = 'http://www.smzdm.com//wp-content//plugins//daily_attendance//add_daily_attendance.php'
    attend_reqst = urllib2.Request(url)
    json_str = urllib2.urlopen(attend_reqst).read()
    #json_str = opener.open(attend_reqst).read()
    json_dict = json.loads(json_str)
    print(json_dict)
    return json_dict