#! /usr/bin/env python3
import os
import subprocess

from BarItem import BarItem


class Battery(BarItem):

    def __init__(self, number=0):
        BarItem.__init__(self, "Battery")
        self.output['name'] = "Battery"
        self.number = number
        self._battery_path = "/sys/class/power_supply/"

    def update(self):
        for element in os.listdir(self._battery_path):
            if element.startswith('BAT'):
                device = element
                break
        else:
            self.output['full_text'] = "No Battery"
            return

        args = ("cat", "/sys/class/power_supply/{0}/energy_full_design".format(device)) #to get a realistic value
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        bat_full = popen.stdout.read().decode("utf-8").strip()

        args = ("cat", "/sys/class/power_supply/{0}/energy_now".format(device))
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        bat_now = popen.stdout.read().decode("utf-8").strip()

        args = ("cat", "/sys/class/power_supply/{0}/status".format(device))
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        status = popen.stdout.read().decode("utf-8").strip()

        percentage = (int(bat_now) / int(bat_full)) * 100
        self.output['full_text'] = "Battery: " + '%.1f' % percentage + "%"

        if(status == "Charging"):
            self.output['color'] = "#0676cb"
        else:
            if(25 < percentage):
                self.output['color'] = "#FFFFFF"
            elif(10 < percentage <= 25):
                self.output['color'] = "#FFFF00"
            else:
                self.output['color'] = "#FF0000"


