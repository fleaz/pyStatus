#!/usr/bin/env python3


class BarItem(object):
    def __init__(self, name):
        assert(len(name) > 0)
        self.name = name
        self.output = {'name': name.lower()}

    def update(self):
        pass

    def get(self):
        return self.output
