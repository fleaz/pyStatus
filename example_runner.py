#! /usr/bin/env python3

from pyStatus.Bar import Bar
from pyStatus.plugins import Time, Battery, CPU, Memory, Ip, Traffic, Filesystem, ESSID, Updates, DNS, Internet, Load, Temp, Text


my_bar = Bar(delay=1, separator=False, separator_width = 15)
my_bar.register(Updates.Updates())
my_bar.register(Temp.Temp(warn=50, crit=70))
my_bar.register(Filesystem.Filesystem(path='/', style="free", show_path=False))
my_bar.register(ESSID.ESSID(interface="wlp3s0"))
my_bar.register(Load.Load(2.0, 4.0))
my_bar.register(Battery.Battery())
my_bar.register(Time.Time("%H:%M"))
my_bar.register(Text.Text(text="Foo", color="#FF0000"))

my_bar.loop()

