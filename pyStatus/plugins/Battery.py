#! /usr/bin/env python3
import os
from ..BarItem import BarItem


class Battery(BarItem):

    TYPE_AND_LOCATION = {
        "bat_full": ["energy_full_design", "charge_full_design"],
        "bat_now": ["energy_now", "charge_now"],
        "status": ["status"]
    }

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

        results = {}

        for (key, locations) in self.TYPE_AND_LOCATION.items():
            for location in locations:
                try:
                    results[key] = self.getValueFromLocation(
                        os.path.join(self._battery_path, device, location)
                    )
                except OSError:
                    pass

        try:
            percentage = (int(results["bat_now"]) / int(results["bat_full"])) * 100
            self.output['full_text'] = "Battery: {0:.1f}%".format(percentage)

            if 25 < percentage:
                self.output['color'] = "#FFFFFF"
            elif 10 < percentage <= 25:
                self.output['color'] = "#FFFF00"
            else:
                self.output['color'] = "#FF0000"
        except KeyError:
            self.output['full_text'] = "Battery: unknown"

        try:
            if results["status"].strip() == "Charging":

                self.output['color'] = "#0676cb"
        except KeyError:
            pass

    @staticmethod
    def getValueFromLocation(path):
        with open(path) as foo:
            return ''.join(foo.readlines())
