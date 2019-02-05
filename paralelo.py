#!/usr/bin/env python3
#
# This is the solution code for the *echo server*.
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Ola mundo')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
