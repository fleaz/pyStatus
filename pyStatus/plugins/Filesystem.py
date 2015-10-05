#! /usr/bin/env python3

import os
from collections import namedtuple

from ..BarItem import BarItem

_Diskusage = namedtuple('usage', 'total used free')


class Filesystem(BarItem):

    def __init__(self, path="/", style="used", show_path=True):
        BarItem.__init__(self, "Filesystem")
        self.output['name'] = "Filesystem"
        self.path = path
        self.style = style
        self.show_path = show_path
        self.update()

    def disk_usage(self, path):
        """Return disk usage statistics about the given path.

        Returned valus is a named tuple with attributes 'total', 'used' and
        'free', which are the amount of total, used and free space, in bytes.
        """
        st = os.statvfs(path)
        free = st.f_bavail * st.f_frsize
        total = st.f_blocks * st.f_frsize
        used = (st.f_blocks - st.f_bfree) * st.f_frsize
        return _Diskusage(total, used, free)

    def sizeof_fmt(self, num):
        for x in ('bytes', 'KB', 'MB', 'GB'):
            if num < 1024.0:
                return "%3.1f%s" % (num, x)
            num /= 1024.0
        return "%3.1f%s" % (num, 'TB')

    def update(self):
        root = self.disk_usage(self.path)

        used = self.sizeof_fmt(root.used)
        free = self.sizeof_fmt(root.free)
        total = self.sizeof_fmt(root.total)

        self.output['instance'] = '--'.join((self.style, self.path))

        if root.total - root.free < root.total * 0.9:
            self.output['color'] = "#FFFFFF"
        else:
            self.output['color'] = "#FF0000"

        if self.show_path:
            path = " {path}".format(path=self.path)
        else:
            path = ""

        if self.style == "used":
            self.output['full_text'] = "HDD{path}: {0}/{1}".format(used, total, path=path)
        else:
            self.output['full_text'] = "HDD{path}: {0} free".format(free, path=path)
