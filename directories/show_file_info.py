#!/usr/bin/env python

from shutil import *
import os
import time
import sys
import pprint
 
def show_file_info(filename):
    stat_info = os.stat(filename)
    print('\tMode    :', stat_info.st_mode)
    print('\tCreated :', time.ctime(stat_info.st_ctime))
    print('\tAccessed:', time.ctime(stat_info.st_atime))
    print('\tModified:', time.ctime(stat_info.st_mtime))
 
show_file_info('/home/mustofa/Documents/test/ds.txt')

# print(os.stat('/home/mustofa/Documents/test/ds.txt'))
