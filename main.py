#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.api import users
import webapp2
from attend import get_cookie, attendance
import accounts


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.redirect('Accounts')
        else:
            self.redirect(users.create_login_url(self.request.uri))


class AttendHandler(webapp2.RequestHandler):
    def get(self):
        cookie = get_cookie('xxc3303', '62570303')
        attend_dict = attendance(cookie)
        self.response.write(attend_dict)


app = webapp2.WSGIApplication([('/', MainHandler), ('/Attend', AttendHandler), ('/Accounts', accounts.MainPage),
                               ('/Accounts/Create', accounts.CreatePage)], debug=True)
