import os

import datetime, random
from tornado import ioloop, web, websocket, gen
from tornado.ioloop import IOLoop
import serial

from weight_translator import CoffeeWeightToStatusTranslator

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

cl = []


class MainHandler(web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render("static/templates/coffee_status.html")


@gen.coroutine
def auto_loop():
    translator = CoffeeWeightToStatusTranslator()

    while True:
        s = serial.Serial(port='/dev/tty.usbmodem1411', baudrate=9600)
        weight = float(s.readline()) #random.randrange(100, 200, 1)
        status = int(translator.translate(weight))
        for c in cl:
            c.write_message('Current coffee status: ' + str(status) + '%')

        yield gen.Task(
            IOLoop.current().add_timeout,
            datetime.timedelta(milliseconds=5000))


class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            cl.append(self)

    def on_close(self):
        if self in cl:
            cl.remove(self)


def make_app():
    return web.Application([
        (r"/", MainHandler),
        (r'/ws', SocketHandler),
        (r"/css\)", web.StaticFileHandler, dict(path=settings['static_path'])),
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    auto_loop()
    ioloop.IOLoop.current().start()