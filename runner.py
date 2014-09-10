#! /usr/bin/env python3

from pyStatus.Bar import Bar
from pyStatus.plugins import Time, Battery, CPU, Memory, MPD, Traffic, Ip, MemPercent, ESSID


my_bar = Bar(delay=3)
time = Time.Time("%H:%M")
bat = Battery.Battery()
mpd = MPD.MPD()
cpu = CPU.CPU()
mem = Memory.Memory()
memPercent = MemPercent.MemoryPercent()
traffic = Traffic.Traffic(interface="wlp3s0")
ip = Ip.IP(interface="wlp3s0", type="wifi",protocol=4)
ip2 = Ip.IP(interface="enp0s25", type="lan",protocol=4)
essid = ESSID.ESSID(interface="wlp3s0")

my_bar.register(essid)
my_bar.register(ip)
my_bar.register(ip2)
my_bar.register(traffic)
my_bar.register(memPercent)
my_bar.register(cpu)
my_bar.register(bat)
my_bar.register(time)

my_bar.loop()
