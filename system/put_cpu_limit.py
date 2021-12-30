import resource
import sys
import signal
import time
import pprint
import json
# def time_expired(n, stack):
#     print('Expired:', time.ctime())
#     raise SystemExit('time ran out')
# signal.signal(signal.SIGXCPU, time_expired)

# soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
# print('Soft limit starts as :', soft)
# resource.setrlimit(resource.RLIMIT_CPU, (10, hard))
# print('Soft limit changed to : ', soft)
# print()

# print('Starting:', time.ctime())

# for i in range(200000):
#     for i in range(200000):
#         v = i * i
# print('Exiting:', time.ctime())

valid_signals = signal.valid_signals()
 
# print(valid_signals)


"""
    A Signal Handler is a user defined function, where Python signals can be handled.
    If we take the signal SIGINT (Interrupt Signal), the default behavior would be to stop
    the current running program.
    We can, however, assign a signal handler to detect this signal and 
    do our custom processing instead!
"""
def signal_handler(signum, frame):  
    print("Signal Number:", signum, " Frame: ", frame)  
 
def exit_handler(signum, frame):
    print('Exiting....')
    exit(0)
    
# Register our signal handler with `SIGINT`(CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

signal.signal(signal.SIGTSTP, signal_handler)

# Register the exit handler with `SIGTSTP` (Ctrl + Z)
signal.signal(signal.SIGTSTP, exit_handler)
 
# While Loop
while 1:  
    print("Press Ctrl + C") 
    time.sleep(3) 