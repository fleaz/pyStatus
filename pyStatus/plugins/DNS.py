#! /usr/bin/env python3
from socket import gethostbyname
from ..BarItem import BarItem
import signal


class Timeout():
    """Timeout class using ALARM signal."""
    class Timeout(Exception):
        pass

    def __init__(self, sec):
        self.sec = sec

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)

    def __exit__(self, *args):
        signal.alarm(0)    # disable alarm

    def raise_timeout(self, *args):
        raise Timeout.Timeout()


class DNS(BarItem):

    def __init__(self, address="www.google.com"):
        BarItem.__init__(self, "DNS")
        self.output['name'] = "DNS"
        self.address = address
        self.update()

    def update(self):
        self.output['full_text'] = "DNS"
        try:
            with Timeout(2):
                gethostbyname(self.address)
                self.output['color'] = "#00FF00"
        except:
            self.output['color'] = "#FF0000"
