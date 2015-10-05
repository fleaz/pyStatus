#! /usr/bin/env python3
import psutil
from ..BarItem import BarItem


class MemoryPercent(BarItem):

    def __init__(self):
        BarItem.__init__(self, "Memory")
        self.output['name'] = "MemoryPercent"
        self.update()

    def update(self):
        mem = psutil.virtual_memory()

        self.output['full_text'] = "RAM: {}%".format(mem.percent)

        if mem_percent < 80:
            self.output['color'] = "#FFFFFF"
        elif 80 <= mem_percent < 90:
            self.output['color'] = "#FFFF00"
        else:
            self.output['color'] = "#FF0000"
