import webapp2
import jinja2
import os
import random

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

from google.appengine.ext import ndb

class postMessage(ndb.Model):
	vent = ndb.StringProperty()
	noun1 = ndb.StringProperty()


class MainPageHandler(webapp2.RequestHandler):
	def get(self):
		
		template = jinja_environment.get_template('homepage.html')
		self.response.write(template.render())
		

class UventAppHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('uvent_in.html')
		self.response.write(template.render())

	def post(self):
		vent = self.request.get('vent')
		n1 = self.request.get('noun1')


		msg = postMessage(vent= vent, noun1= n1)
		msg.put()
		
		template = jinja_environment.get_template('uvent_out.html')
		self.response.write(template.render({
			'vent': vent,
			'noun1' : n1,
	
		
		'msg': msg

		}))


class UpostHandler(webapp2.RequestHandler):
	def get(self):
		vent = postMessage.query().fetch()
		template = jinja_environment.get_template('uvent_list.html')
		self.response.write(template.render(
			{
				'vent': vent,
			}))


app = webapp2.WSGIApplication([
	('/', MainPageHandler),
	('/UventAppHandler', UventAppHandler),
	('/upost', UpostHandler)
], debug=True)