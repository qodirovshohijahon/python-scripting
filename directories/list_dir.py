import os
import sys
directories = sorted(os.listdir(sys.argv[1]))
# print(type(directories))
# print(directories[1])

for x in directories:
    if x == 'Zoom':
        print("zoom is here")
    else:
        print("zoom is not here")
        # print(x)