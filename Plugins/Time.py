#! /usr/bin/env python3
from BarItem import BarItem
import time


class Time(BarItem):
    output_format = ""
    output = {}

    def __init__(self, output_format="%H:%M"):
        BarItem.__init__(self, "Time")
        self.output['name'] = "Time"
        self.output_format = output_format
        self.update()

    def update(self):
        time_string = time.strftime(self.output_format)
        self.output['full_text'] = time_string

    def get_json(self):
        return self.output