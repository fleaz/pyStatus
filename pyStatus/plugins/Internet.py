#! /usr/bin/env python3
import requests
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


class Internet(BarItem):

    def __init__(self, address="http://www.google.com"):
        BarItem.__init__(self, "Internet")
        self.output['name'] = "Internet"
        self.address = address
        self.update()

    def update(self):
        self.output['full_text'] = "Internet"
        try:
            with Timeout(2):
                status = requests.get(self.address).status_code
        except:
            status = 0

        if status == 200:
            self.output["color"] = "#00FF00"
        else:
            self.output["color"] = "#FF0000"
