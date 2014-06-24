#! /usr/bin/env python3
from BarItem import BarItem
import psutil


class Memory(BarItem):

    def __init__(self):
        BarItem.__init__(self, "Memory")
        self.output['name'] = "Memory"
        self.update()

    def update(self):
        mem = psutil.virtual_memory()
        mem_total = mem[0]
        mem_used = mem[3]
        mem_buffer = mem[7]
        mem_cached = mem[8]

        mem_used = mem_used - mem_buffer - mem_cached

        mem_total = '%.0f' % (mem_total / 1048578)
        mem_used = '%.0f' % (mem_used / 1048578)

        self.output['full_text'] = "RAM: " + mem_used + " MB/" + mem_total + " MB"
