#! /usr/bin/env python3

from BarItem import BarItem
from time import sleep
import sys
import json


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
        return json.dumps(output)

    def loop(self):
        print("{\"version\": 1}")
        print("[")
        print("[],")
        while(1):
            sys.stdout.flush()
            print("%s," % self.get_json())
            sleep(self.delay)

    def get_delay(self):
        return self.delay