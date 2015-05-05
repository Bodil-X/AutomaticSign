#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'bodil'

try:
    import cPickle as pickle
except ImportError:
    import pickle
from cookielib import CookieJar


class StringCookieJar(CookieJar):
    def __init__(self, string=None, policy=None):
        CookieJar.__init__(self, policy)
        if string:
            self._cookies = pickle.loads(string)

    def dumps(self):
        return pickle.dumps(self._cookies)