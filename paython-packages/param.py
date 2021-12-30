#!/usr/bin/env python

import sys
import paramiko
import time

ip_address = "0.3.21.126"
username = "k8s-user"
password = "Ng}4NW@"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.load_system_host_keys()
ssh_client.connect(
    hostname=ip_address,\
    username=username, 
    password=password,
    key_filename='/home/mustofa/.ssh/id_rsa',
)

print ("Successful connection", ip_address)
ssh_client.invoke_shell()
remote_connection = ssh_client.exec_command('ls -l')
remote_connection = ssh_client.exec_command('uname -s')
#print( remote_connection.read() )
ssh_client.close