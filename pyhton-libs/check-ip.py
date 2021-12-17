import ipaddress
import subprocess
# Create the network
ip_net = ipaddress.ip_network(u'192.168.1.0/24')
# Get all hosts on that network
all_hosts = list(ip_net.hosts())
# Conﬁgure subprocess to hide the console window
info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE
# For each IP address in the subnet,
# run the ping command with subprocess.popen interface
for i in range(len(all_hosts)):
    output = subprocess.Popen(['ping', '-n', '1', '-w', '500',
    str(all_hosts[i])], stdout=subprocess.PIPE,
    startupinfo=info).communicate()[0]
    if "Destination host unreachable" in output.decode('utf-8'):
        print(str(all_hosts[i]), "is Oﬄine")
    elif "Request timed out" in output.decode('utf-8'):
            print(str(all_hosts[i]), "is unreachable")
    else:
        print(str(all_hosts[i]), "is reachable")