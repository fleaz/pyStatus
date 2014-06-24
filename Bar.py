#!/usr/bin/env python3
from BarItem import BarItem
from time import sleep
import sys
import json


class Bar():
    def __init__(self, delay=1.5):
        self.items = []
        self.delay = delay

    def register(self, item):
        """
        Register a new BarItem with the Bar
        :param item: A BarItem instance
        """
        assert(isinstance(item, BarItem))
        self.items.append(item)

    def get(self):
        """
        Collect the data from each registered BarItem
        :return: json str
        """
        output = []
        for item in self.items:
            item.update()
            output.append(item.get())
        return json.dumps(output)

    def loop(self):
        """
        Main Loop
        """
        print("{\"version\": 1}")
        print("[")
        print("[],")
        while(1):
            print("%s," % self.get())
            sys.stdout.flush()
            sleep(self.delay)