#! /usr/bin/env python3
from socket import gethostbyname
from ..BarItem import BarItem


class DNS(BarItem):

    def __init__(self, address="www.google.com"):
        BarItem.__init__(self, "DNS")
        self.output['name'] = "DNS"
        self.address = address
        self.update()

    def update(self):
        self.output['full_text'] = "DNS"
        try:
            gethostbyname(self.address)
            self.output['color'] = "#00FF00"
        except:
            self.output['color'] = "#FF0000"