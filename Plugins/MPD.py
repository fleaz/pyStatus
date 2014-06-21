#! /usr/bin/env python3
from BarItem import BarItem
from musicpd import MPDClient


class MPD(BarItem):
    output = {}

    def __init__(self, server="localhost",port=6600):
        self.mpc = MPDClient()
        self.server = server
        self.port = port
        BarItem.__init__(self, "MPD")
        self.output['name'] = "NowPlaying"
        self.update()

    def update(self):
        try:
            self.mpc.connect(self.server, self.port)
            status = self.mpc.status()
            if (status['state'] == "play"):
                song = self.mpc.currentsong()
                self.output['full_text'] = '► ' + song['artist'] + ' - ' + song['album'] + ' - ' + song['title']
            elif (status['state'] == "pause"):
                song = self.mpc.currentsong()
                self.output['full_text'] = '" ' + song['artist'] + ' - ' + song['album'] + ' - ' + song['title']
            else:
                self.output['full_text'] = status['state']
            self.mpc.disconnect()
        except:
            self.output['full_text'] = "MPD disconnected"

    def get_json(self):
        return self.output
