from google.appengine.ext import ndb

__author__ = 'Bodil'


def account_key(author_name='Default Author'):
    return ndb.Key('Account', author_name)


class Account(ndb.Model):
    author = ndb.UserProperty()
    acct = ndb.StringProperty()
    psw = ndb.StringProperty()
    acctType = ndb.StringProperty()
    createdTime = ndb.DateTimeProperty(auto_now_add=True)
    lastModifiedTime = ndb.DateTimeProperty(auto_now=True)
