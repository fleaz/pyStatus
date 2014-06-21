#! /usr/bin/env

from BarItem import BarItem
import psutil
from time import time

class Traffic(BarItem):
    output = {}

    def __init__(self, interface="eth0"):
        BarItem.__init__(self, "Traffic")
        self.output['name'] = "Traffic"
        self.interface = interface
        self.old_sent = 1
        self.old_recv = 1
        self.old_timestamp = 1
        self.update()

    def update(self):
        interface_info = psutil.net_io_counters(pernic=True)[self.interface]
        new_sent = interface_info[0]
        new_recv = interface_info[1]
        new_timestamp = int(time())

        if ((new_timestamp - self.old_timestamp) > 0):
            speed_sent = (new_sent - self.old_sent) / (new_timestamp - self.old_timestamp)
            speed_recv = (new_recv - self.old_recv) / (new_timestamp - self.old_timestamp)
        else:
            speed_sent = 0
            speed_recv = 0

        speed_sent = "%.2f" % ((speed_sent * 8) / 1000000) # Convert 'byte per sec' to 'mbit per sec'
        speed_recv = "%.2f" % ((speed_recv * 8) / 1000000)

        self.old_recv = new_recv
        self.old_sent = new_sent
        self.old_timestamp = new_timestamp

        self.output['full_text'] = self.interface + ": " + speed_recv + " MBps down " + "," + speed_sent + " MBps up"

    def get_json(self):
        return self.output
