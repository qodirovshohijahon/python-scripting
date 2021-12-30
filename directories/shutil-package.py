#!/usr/bin/env python

import shutil
import os
import time
import pprint

print(shutil.which("ping"))

# shutil.rmtree('Latracal')
 
print('\nAFTER:')
pprint.pprint(os.listdir('.'))

