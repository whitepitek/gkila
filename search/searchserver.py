#!/usr/bin/env python3

import tornado.ioloop
import tornado.web
import json

import search

#IP = '127.0.0.1'
PORT = 10002
PREFIX = '/home/gkila/gkila'


class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        response = dict()
        try:
            keywords = [k.decode() for k in self.request.arguments['keywords']]
        except:
            self.set_status(400)
            response['error'] = 'no keywords'
            self.finish(json.dumps(response))
            return

        try:
            results = search.get_results(keywords)
            response['response'] = results
            self.write(json.dumps(response))
        except Exception as e:
            self.set_status(500)
            response['error'] = 'error loading search results'
            self.finish(json.dumps(response))
            return


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(PREFIX + '/search/search.html')


class ResultsHandler(tornado.web.RequestHandler):
    def get(self):
        response = dict()
        try:
            keywords = [k.decode() for k in self.request.arguments['keywords']]
        except:
            self.set_status(400)
            response['error'] = 'no keywords'
            self.finish(json.dumps(response))
            return

        try:
            results = search.get_results(keywords)
        except Exception as e:
            self.set_status(500)
            response['error'] = 'error loading search results'
            self.finish(json.dumps(response))
            return

        self.render(PREFIX + '/search/results.html', results=results)


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/search', SearchHandler),
        (r'/results', ResultsHandler),
    ])


def main():
    app = make_app()
    app.listen(PORT) #, address=IP) FIXME let it look outside for now
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
