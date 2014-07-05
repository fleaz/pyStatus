#! /usr/bin/env python3
from BarItem import BarItem
import psutil


class MemoryPercent(BarItem):

    def __init__(self):
        BarItem.__init__(self, "Memory")
        self.output['name'] = "MemoryPercent"
        self.update()

    def update(self):
        mem = psutil.virtual_memory()
        mem_percent = mem[2]


        self.output['full_text'] = "RAM: " + str(mem_percent) + "%"

        if(mem_percent < 80):
            self.output['color'] = "#FFFFFF"
        elif(80 <= mem_percent < 90):
            self.output['color'] = "#FFFF00"
        else:
            self.output['color'] = "#FF0000"
