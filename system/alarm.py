import signal
import time
import os

def ping_host():
    hostname = "google.com" #example
    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
       print(hostname, 'is up!')
    else:
        print(hostname, 'is down!')
        
def alarm_handler(signum, frame):
    print('Alarm at:', time.ctime())
    ping_host()
    
# Register the alarm signal with our handler
signal.signal(signal.SIGALRM, alarm_handler)

signal.alarm(3) # Set the alarm for 3 seconds

print('Current time:', time.ctime())

time.sleep(6) # Sleep for 3 seconds

