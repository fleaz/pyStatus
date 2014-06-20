#! /usr/bin/env python3

from Bar import Bar
from Plugins import Time
from time import sleep

my_bar = Bar()
time = Time("%H:%M")
my_bar.register_item(time)

my_bar.loop()
