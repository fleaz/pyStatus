#! /usr/bin/env python3
import netifaces
from ..BarItem import BarItem


class IP(BarItem):

    def __init__(self,type="lan", interface="eth0", protocol=4):
        BarItem.__init__(self, "IP")
        self.output['name'] = "IP"
        self.type = "cable"
        self.type = type
        self.interface = interface
        self.protocol = protocol
        self.update()

    def update(self):
        try:
            if(self.protocol == 4):
                addr = netifaces.ifaddresses(self.interface)[2][0]['addr']
            elif(self.protocol == 6):
                addr =netifaces.ifaddresses(self.interface)[10][1]['addr']
        except:
            addr = "-"

        if (self.type == "lan"):
            prefix = "E: "
        elif (self.type == "wifi"):
            prefix = "W: "
        else:
            prefix ="Net: "

        self.output['full_text'] = prefix + addr

        if(addr == "-"):
            self.output['color'] = "#FF0000"
        else:
            self.output['color'] = "#FFFFFF"