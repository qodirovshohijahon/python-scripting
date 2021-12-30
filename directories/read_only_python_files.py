#!/usr/bin/env python

import os
import sys

print(os.get_terminal_size())
print(os.listdir())

files = os.listdir()
for x in files:
    if x.endswith("py"):
        f = open(x, "r")
        print(f.read())
    else:
        print("Python files don't found")