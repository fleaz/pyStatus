#! /usr/bin/env python3

from pyStatus.Bar import Bar
from pyStatus.plugins import Time, Battery, CPU, Memory, Ip, Traffic, Filesystem, ESSID, MemPercent, MPD, Load


my_bar = Bar(delay=1)
my_bar.register(DNS.DNS(address="www.google.de"))
my_bar.register(Internet.Internet(address="http://www.google.de"))
my_bar.register(Filesystem.Filesystem(path='/', style="free", show_path=True))
my_bar.register(ESSID.ESSID(interface="wlp3s0"))
my_bar.register(Ip.IP(interface="wlp3s0", type="wifi", protocol=4))
my_bar.register(Ip.IP(interface="eth0", type="lan", protocol=4))
my_bar.register(Traffic.Traffic(interface="wlp3s0"))
my_bar.register(Memory.Memory())
my_bar.register(MemPercent.MemoryPercent())
my_bar.register(CPU.CPU())
my_bar.register(Load.Load(0.5, 1.0))
my_bar.register(Battery.Battery())
my_bar.register(Time.Time("%H:%M"))
my_bar.register(MPD.MPD("localhost"))

my_bar.loop()
