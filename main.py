import os
import json
import webapp2
import jinja2
from urllib import urlencode
from google.appengine.api import urlfetch

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/main.html')
        self.response.write(template.render())

class SearchHandler(webapp2.RequestHandler):
    def post(self):
        base_url = 'http://ghibli.herokuapp.com/'
        params = { 'q': query }
        response = urlfetch.fetch(base_url + urlencode(params)).content
        results = json.loads(response)
        template = jinja_env.get_template('templates/results.html')
        self.response.write(template.render({
            'results': results
        }))

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/search', SearchHandler)
], debug=True)
