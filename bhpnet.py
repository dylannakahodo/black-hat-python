#!/usb/bin/env python3
"""
Skeleton code for netcat: Chapter 2
"""

import sys
import socket
import getopt
import threading
import subprocess

# Global Variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    """Prints out program usage."""
    # TODO: Probably worth rewriting this section using argparse

    print("BHP Netcat Replacement")
    print()
    print("Usage: bhpnet.py -t target_host -p port")
    print("-l --listen                  - listen on [host]:[port] for incoming connections")
    print("-e --execute=file_to_run     - execute the given file upon receiving a connection")
    print("-c --command                 - initialize a command shell")
    print("-u --upload=destination      - upon receiving a connection upload a file and write to [destination]")
    print()
    print()
    print("Examples: ")
    print("bhnet.py -t 192.168.0.1 -p 5555 -l -c")
    print("bhnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
    print("bhnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
    print("echo 'ABCDEFGHI' | ./bhnet.py -t 192.168.11.12 -p 135")
    sys.exit(0)
    
def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target
    
    # TODO: Rewrite this section with argparse
    if not len(sys.argv[1:]):
        usage()

    # read the command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",["help", "listen", "execute", "target", "port", "command", "upload"])
    
        for o, a in opts:
            if o in ("-h", "--help"):
                usage()
            elif o in ("-l", "--listen"):
                listen = True
            elif o in ("-e", "--execute"):
                execute = a
            elif o in ("-c", "--commandshell"):
                command = True
            elif o in ("-u", "--upload"):
                upload_destination = a
            elif o in ("-t", "--target"):
                target = a
            elif o in ("-p", "--port"):
                port = int(a)
            else:
                assert False, "Unhandled Option"
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    # Are we going to listen or just send data from STDIN?
    if not listen and len(target) and port > 0:
        
        # Read in the buffer from the commandline
        # This will block, so send CTRL-D if not sending input
        # to STDIN
        buffer = sys.stdin.read()

        # send data
        client_sender(buffer)

    # We are going to listen and potentially
    # upload things, execute commands, and drop a shell
    # depending on our command line options above
    if listen:
        server_loop()

if __name__ == "__main__":
    main()
