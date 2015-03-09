import tornado.ioloop
import os
import tornado.web
from markov import Markov

markov_gen = Markov(open('data/pretty_data.txt'))

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(markov_gen.generate_markov_text())

application = tornado.web.Application([
    (r"/generate_card", MainHandler),
])


if __name__ == "__main__":
    application.listen(os.environ.get("PORT", 5000))
    tornado.ioloop.IOLoop.instance().start()
