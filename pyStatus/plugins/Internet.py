#! /usr/bin/env python3
import requests
from ..BarItem import BarItem
import socket


def ping(dest_addr, timeout=2):
    """
    Returns either the delay (in seconds) or none on timeout.
    """
    icmp = socket.getprotobyname("icmp")
    try:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
    except (socket.error, error):
        (errno, msg) = error
        if errno == 1:
            # Operation not permitted
            msg = msg + (
                " - Note that ICMP messages can only be sent from processes"
                " running as root."
            )
            raise socket.error(msg)
        raise # raise the original error

    my_ID = int(time.time() * 100000) & 0xFFFF

    send_one_ping(my_socket, dest_addr, my_ID)
    delay = receive_one_ping(my_socket, my_ID, timeout)

    my_socket.close()
    return delay


class Internet(BarItem):

    def __init__(self, address="http://www.google.com"):
        BarItem.__init__(self, "Internet")
        self.output['name'] = "Internet"
        self.address = address
        self.update()

    def update(self):
        self.output['full_text'] = "Internet"
        try:
            with Timeout(2):
                status = requests.get(self.address).status_code
        except:
            status = 0

        if status == 200:
            self.output["color"] = "#00FF00"
        else:
            self.output["color"] = "#FF0000"
