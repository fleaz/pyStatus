#! /usr/bin/env python3

from json import loads, dumps
from time import sleep

class Bar(object):
    bar_items = []

    def __init__(self):
        pass

    def register_item(self, item):
        self.bar_items.append(item)

    def get_json(self):
        output = []
        for item in self.bar_items:
            output.append(item.get_json())
        return dumps(output)

    def loop(self, delay=3):
        print("{\"version\":1}")
        print("[")
        print("[],")
        while(1):
            print (self.get_json() + ",")
            sleep(delay)