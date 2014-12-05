#! /usr/bin/env python3
import requests
from ..BarItem import BarItem


class Internet(BarItem):

    def __init__(self, address="http://www.google.com"):
        BarItem.__init__(self, "Internet")
        self.output['name'] = "Internet"
        self.address = address
        self.update()

    def update(self):
        self.output['full_text'] = "Internet"
        try:
            r = requests.get(self.address, verify=False)
            self.output['color'] = "#00FF00"
        except:
            self.output['color'] = "#FF0000"