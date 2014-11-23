#! /usr/bin/env python3
from subprocess import Popen, PIPE
from ..BarItem import BarItem


class Updates(BarItem):

    def __init__(self):
        BarItem.__init__(self, "Updates")
        self.output['name'] = "Updates"
        self.update()

    def update(self):

        p = Popen("pacman -Qqu".split(" "), stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=-1)
        output, error = p.communicate()

        num = len(output.splitlines())

        if num == 0:
            self.output['full_text'] = "No Updates"
        else:
            if num < 10:
                self.output['color'] = "#FFFFFF"
            elif 10 <= num < 50:
                self.output['color'] = "#FFFF00"
            else:
                self.output['color'] = "#FF0000"

            self.output['full_text'] = "Updates: {}".format(str(num))
