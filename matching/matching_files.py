#!/usr/bin/env python

import glob

print(glob.glob('*.txt'))
file_match = glob.glob('**/*.py', recursive=True)
print(file_match)