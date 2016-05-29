#! /usr/bin/env python3
from subprocess import Popen, PIPE
from ..BarItem import BarItem


class Temp(BarItem):

    def __init__(self, warn=50, crit=70):
        BarItem.__init__(self, "Temp")
        self.output['name'] = "Temp"
        self.warn = warn
        self.crit = crit
        self.update()

    def update(self):

        p = Popen("cat /sys/class/thermal/thermal_zone0/temp".split(" "), stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=-1)
        output, error = p.communicate()

        temp = int(output) / 1000

        if temp < self.warn:
            self.output['color'] = "#FFFFFF"
        elif self.warn <= temp < self.crit:
            self.output['color'] = "#FFFF00"
        else:
            self.output['color'] = "#FF0000"

        self.output['full_text'] = "CPU: {}°C".format(temp)
