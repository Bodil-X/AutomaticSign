import os
from google.appengine.api import users

import jinja2
import webapp2
from model import Account

__author__ = 'Bodil'

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        accounts_query = Account.query(Account.author == user)
        accounts = accounts_query.fetch(10)
        template_values = {
            'accounts': accounts
        }

        template = JINJA_ENVIRONMENT.get_template('templates/accounts.html')
        self.response.write(template.render(template_values))


class CreatePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/account_create.html')
        self.response.write(template.render())

    def post(self):
        author = users.get_current_user()
        acct = self.request.get('acct')
        psw = self.request.get('psw')
        acctType = self.request.get('acctType')
        account = Account(author=author, acct=acct, psw=psw, acctType=acctType)
        account.put()

        self.redirect('/Accounts')


class EditPage(webapp2.RequestHandler):
    def get(self):
        self.response.write()
