#!/usr/bin/env python

import sys
import paramiko
import time
import os

from paramiko.client import MissingHostKeyPolicy
# print enviroment variables
# print enviroment hostname
IP_ADDRESS = os.environ['VULTR_SERVER'] # It can be loaded from environment variable like this
REMOTE_USER = os.environ['VULTR_USER']
KEY_FILE = os.environ['VULT_KEY_FILE']

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(MissingHostKeyPolicy())
ssh_client.connect(
    hostname = IP_ADDRESS, 
    username = REMOTE_USER, 
    key_filename = KEY_FILE
)
print("Successful connection", IP_ADDRESS)

ssh_client.invoke_shell()
remote_connection = ssh_client.exec_command('ping -c 3 google.com')
ssh_client.close()