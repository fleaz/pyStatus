#! /usr/bin/env python3
import psutil
from ..BarItem import BarItem


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

        mem_total = mem_total / 1048578
        mem_used = mem_used / 1048578

        self.output['full_text'] = "RAM: {0:.0f} MB / {1:.0f} MB".format(mem_used, mem_total)


class FreeMemory(BarItem):

    def __init__(self):
        BarItem.__init__(self, "MemoryFree")
        self.output['name'] = "MemoryFree"
        self.update()

    def update(self):
        mem = psutil.virtual_memory()
        mem_total = mem[0]
        mem_used = mem[3]
        mem_buffer = mem[7]
        mem_cached = mem[8]

        mem_used = mem_used - mem_buffer - mem_cached
        total_memory = (mem_total / 1048578)
        free_memory = (total_memory - (mem_used / 1048578))

        self.output['full_text'] = "RAM free: {0:.0f}MB".format(free_memory)

        percent_free = free_memory / total_memory * 100

        if percent_free < 10:
            self.output['color'] = '#FF0000'
        elif percent_free < 25:
            self.output['color'] = '#FFFF00'
        else:
            self.output['color'] = '#FFFFFF'

