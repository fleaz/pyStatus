#! /usr/bin/env

from BarItem import BarItem
import basiciw

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

        if (len(ssid) > 0):
            self.output['full_text'] = ssid + " (" + str(quality) + "%)"
        else:
            self.output['full_text'] = "-"