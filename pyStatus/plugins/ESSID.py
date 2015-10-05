#! /usr/bin/env python3
import basiciw
from ..BarItem import BarItem


class ESSID(BarItem):

    def __init__(self, interface="wlp3s0"):
        BarItem.__init__(self, "SSID")
        self.output['name'] = "SSID"
        self.interface = interface
        self.update()

    def update(self):
        iwi = basiciw.iwinfo(self.interface)
        ssid = iwi["essid"]
        quality = iwi["quality"]["quality"]

        if ssid:
            self.output['full_text'] = "{0} ({1}%)".format(ssid, quality)
        else:
            self.output['full_text'] = "-"
