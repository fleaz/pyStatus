#! /usr/bin/env python3
from BarItem import BarItem
import psutil


class CPU(BarItem):

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

        sum = sum / count

        if sum < 80:
            self.output['color'] = "#00FF00"
        elif 80 <= sum < 95:
            self.output['color'] = "#FFFF00"
        else:
            self.output['color'] = "#FF0000"

        sum = '%.0f' % sum
        self.output['full_text'] = "CPU: " + str(sum) + "%"
