#! /usr/bin/env python3
import time
from ..BarItem import BarItem


class Text(BarItem):
    output_format = ""

    def __init__(self, text="Lorem ipsum", color="#000000"):
        BarItem.__init__(self, "Text")
        self.output['name'] = "Text"
        self.text = text
        self.color = color
        self.update()

    def update(self):
        self.output['full_text'] = self.text
        self.output['color'] = self.color
