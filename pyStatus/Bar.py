#!/usr/bin/env python3
import sys
import json
from time import sleep
from .BarItem import BarItem


class Bar():
    def __init__(self, delay=1.5, separator=True, separator_width=9):
        self.items = []
        self.delay = delay
        self.separator = separator
        self.separator_width = separator_width

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
            plugin_text = item.get()
            plugin_text["separator"] = self.separator
            plugin_text["separator_block_width"] = self.separator_width

            output.append(plugin_text)
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
