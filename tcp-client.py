#!/usr/bin/env python3
"""
Simple TCP Client from Chapter 2
"""

import socket

target_host = "0.0.0.0"
target_port = 9999 

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

# Send data
client.send(b"TESTING!")

# receive data
response = client.recv(4096)

print(response)
