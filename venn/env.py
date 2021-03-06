#
# Venn
#
# Copyright (c) 2019 Payson Wallach
#
# Released under the terms of the Hippocratic License
# (https://firstdonoharm.dev/version/1/1/license.html)
#
# This file incorporates work covered by the following copyright and permission
# notice:
#
#   The MIT License (MIT)
#
#   Copyright (c) 2014, Jeremy Singer-Vine
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#   THE SOFTWARE.
#

import os
import re
import subprocess


def execute(pf, args):
    env = os.environ.copy()
    paths = env["PATH"].split(":")
    bin_paths = pf.get_binpaths()
    new_paths = paths[:1] + bin_paths + paths[1:]
    env["PATH"] = ":".join(new_paths)
    sp = subprocess.Popen(args, env=env)
    out, err = sp.communicate()

    return out


class Env(object):
    @classmethod
    def from_line(cls, line):
        pause_pattern = r"^(?P<pause># *)"
        path = re.sub(pause_pattern, "", line)
        split = path.split("/")
        name = split[4]
        paused = bool(re.match(pause_pattern, line))

        return cls(name, path, paused)

    def __init__(self, name, path, paused=False):
        self.name = name
        self.path = path
        self.paused = paused

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def to_string(self):
        return (self.paused * "# ") + self.path
