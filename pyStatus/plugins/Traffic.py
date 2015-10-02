#! /usr/bin/env python3

from time import time
from collections import namedtuple

from ..BarItem import BarItem

import psutil


_DataSnapshot = namedtuple('DataSnapshot', ['timestamp', 'sent', 'received'])


class Traffic(BarItem):

    def __init__(self, interface="eth0"):
        BarItem.__init__(self, "Traffic")
        self.output['name'] = "Traffic"
        self.interface = interface
        self.old = _DataSnapshot(time(), 1, 1)
        self.update()

    def update(self):
        try:
            interface_info = psutil.net_io_counters(pernic=True)[self.interface]
        except KeyError:
            self.output['color'] = '#FF0000'
            self.output['full_text'] = "Failed to find interface {!r}".format(self.interface)
            return

        new_sent, new_recv, *_ = interface_info
        new_timestamp = time()

        time_difference = new_timestamp - self.old.timestamp

        if time_difference > 0:
            speed_sent = (new_sent - self.old.sent) / time_difference
            speed_recv = (new_recv - self.old.received) / time_difference
        else:
            speed_sent = 0
            speed_recv = 0

        self.old = _DataSnapshot(new_timestamp, new_sent, new_recv)

        speed_sent = "%.2f" % ((speed_sent * 8) / 1000000) # Convert 'byte per sec' to 'mbit per sec'
        speed_recv = "%.2f" % ((speed_recv * 8) / 1000000)
        self.output['color'] = self.COLOR_DEFAULT
        self.output['full_text'] = "▲ {} MBps ▼ {} MBps".format(speed_sent, speed_recv)
