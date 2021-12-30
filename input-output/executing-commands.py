#!/usr/bin/env python

import sys
import paramiko
import time
import os
import subprocess

# subprocess.call(['ls', '-l'])

res = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
print('return', res.returncode)
print(' {} bytes in stdput:\n{}'
    .format(
        len(res.stdout), 
        res.stdout.decode('utf-8')
    )
)