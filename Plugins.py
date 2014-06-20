#! /usr/bin/env python3
from BarItem import BarItem
from time import gmtime, strftime


class Time(BarItem):
    output_format = ""

    def __init__(self, output_format="%H:%M"):
        BarItem.__init__(self, "Time")
        self.output_format = output_format

    def get_json(self):
        time = strftime(self.output_format, gmtime())
        return {'full_text': time}
