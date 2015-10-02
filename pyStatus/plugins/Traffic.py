#! /usr/bin/env python3
import psutil
from time import time
from ..BarItem import BarItem

class Traffic(BarItem):

    def __init__(self, interface="eth0"):
        BarItem.__init__(self, "Traffic")
        self.output['name'] = "Traffic"
        self.interface = interface
        self.old_sent = 1
        self.old_recv = 1
        self.old_timestamp = 1
        self.update()

    def update(self):
        try:
            interface_info = psutil.net_io_counters(pernic=True)[self.interface]
        except KeyError:
            self.output['color'] = '#FF0000'
            self.output['full_text'] = "Failed to find interface {!r}".format(self.interface)
            return

        new_sent = interface_info[0]
        new_recv = interface_info[1]
        new_timestamp = int(time())

        if (new_timestamp - self.old_timestamp) > 0:
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

        self.output['full_text'] = "▲ {} MBps ▼ {} MBps".format(speed_sent, speed_recv)
