#! /usr/bin/env python3
from ..BarItem import BarItem
import os


class Load(BarItem):

    def __init__(self, warning, critical):
        BarItem.__init__(self, "Load")
        self.output['name'] = "Load"
        self.warning = warning
        self.critical = critical
        self.update()

    def update(self):
        load_1, *_ = os.getloadavg()

        if load_1 < self.warning:
            self.output['color'] = "#FFFFFF"
        elif self.warning <= load_1 < self.critical:
            self.output['color'] = "#FFFF00"
        else:
            self.output['color'] = "#FF0000"

        self.output['full_text'] = "Load: {}".format(load_1)
