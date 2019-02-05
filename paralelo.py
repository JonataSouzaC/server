#!/usr/bin/env python3
#
# This is the solution code for the *echo server*.
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.path[1:].encode())

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
