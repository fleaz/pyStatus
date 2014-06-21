#! /usr/bin/env python3

from Bar import Bar
from Plugins import Time, Battery, CPU, Memory, MPD, Traffic, Ip


my_bar = Bar(delay=3)
time = Time.Time("%H:%M")
bat = Battery.Battery()
mpd = MPD.MPD()
cpu = CPU.CPU()
mem = Memory.Memory()
traffic = Traffic.Traffic(interface="wlp3s0")
ip = Ip.IP(interface="wlp3s0", type="wifi",protocol=4)

my_bar.register_item(ip)
my_bar.register_item(traffic)
my_bar.register_item(mem)
my_bar.register_item(cpu)
my_bar.register_item(bat)
my_bar.register_item(time)
my_bar.register_item(mpd)

my_bar.loop()
