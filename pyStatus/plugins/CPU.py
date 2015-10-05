#! /usr/bin/env python3
import psutil
from ..BarItem import BarItem


class CPU(BarItem):

    def __init__(self):
        BarItem.__init__(self, "CPU")
        self.output['name'] = "CPU"
        self.update()

    def update(self):
        load = sum(psutil.cpu_percent(interval=1, percpu=True)) / psutil.cpu_count()

        if load < 80:
            self.output['color'] = "#FFFFFF"
        elif 80 <= load < 95:
            self.output['color'] = "#FFFF00"
        else:
            self.output['color'] = "#FF0000"

        self.output['full_text'] = "CPU: {0:.0f}%".format(load)
