import ntplib
from time import ctime

client = ntplib.NTPClient()
response = client.request("europe.pool.ntp.org", version=3)
print(response.offest)

response.version = 3
print(ctime(response.tx_time))
