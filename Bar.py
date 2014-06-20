#! /usr/bin/env python3

from json import loads, dumps
from BarItem import BarItem
from time import sleep
import sys

class Bar(object):

    def __init__(self, delay=1):
        self.bar_items = []
        self.delay = delay

    def register_item(self, item):
        assert(type(item) == BarItem, True)
        self.bar_items.append(item)

    def get_json(self):
        output = []
        for item in self.bar_items:
            item.update()
            output.append(item.get_json())
        return dumps(output)

    def loop(self):
        print("{\"version\": 1}")
        print("[")
        print("[],")
        while(1):
            sys.stdout.flush()
            print (self.get_json() + ",")
            sleep(self.delay)