#!/usr/bin/python

import tornado.ioloop
import tornado.web
import tornado.options

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, World!')

class StoryHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.db = db

    def get(self, story_id):
        self.write('This story identity is: %s' % story_id)

def make_app():
    return tornado.web.Application([
        tornado.web.url(r'/', MainHandler),
	tornado.web.url(r'/story/([0-9]+)', StoryHandler, dict(db='db'), name='story')
        ])

if __name__ == '__main__':
    tornado.options.parse_command_line()
    application = make_app()
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()
