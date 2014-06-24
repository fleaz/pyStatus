#! /urs/bin/env python3


class BarItem(object):

    def __init__(self, name):
        self.name = name
        self.output = {}

    def update(self):
        pass

    def get_json(self):
        return self.output
