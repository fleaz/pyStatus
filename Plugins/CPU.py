#! /usr/bin/env python3
from BarItem import BarItem
import psutil


class CPU(BarItem):
    output = {}

    def __init__(self):
        BarItem.__init__(self, "CPU")
        self.output['name'] = "CPU"
        self.update()

    def update(self):
        all_load = psutil.cpu_percent(interval=1, percpu=True)
        count = psutil.cpu_count()
        sum = 0
        for i in range(count):
            sum = sum + all_load[i]
        sum = '%.0f' % (sum / count)

        self.output['full_text'] = "CPU: " + str(sum) + "%"

    def get_json(self):
        return self.output
