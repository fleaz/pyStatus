#!/usr/bin/env python3


class BarItem(object):
    valid_options = set(['full_text', 'short_text', 'color', 'min_width',
                         'align', 'name', 'instance', 'urgent', 'separator',
                         'separator_block_width'])
    COLOR_DEFAULT = '#FFFFFF'

    def __init__(self, name):
        assert(len(name) > 0)
        self.name = name
        self.output = {'name': name.lower()}

    def update(self):
        pass

    def get(self):
        return self.output

    def set(self, option, value):
        assert option in self.valid_options
        self.output[option] = value
