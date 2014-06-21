#! /usr/bin/env python3

from Bar import Bar
from Plugins import Time, Battery


my_bar = Bar()
time = Time("%H:%M:%S")
bat = Battery()

my_bar.register_item(bat)
my_bar.register_item(time)


my_bar.loop()
