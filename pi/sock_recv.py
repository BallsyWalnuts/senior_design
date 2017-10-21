#! /usr/bin/env python
#
# Grant Steiner
# Southern Illinois University Edwardsville
# 10/20/2017
#
# A simple script to daemonize a UDP process
# so a Raspberry Pi can receive accelerometer
# data from the android.
#
# https://wiki.python.org/moin/UdpCommunication
# http://web.archive.org/web/20131017130434/http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/

# NOT OPERATIONAL
TODO: add conditions so that daemon releases the bind on the port when asked to stop

import socket
import time
import sys
import argparse

from daemon import Daemon

START_TIME = time.time()  # for tracking how long the program ran
UDP_IP = "146.163.42.94"  # IP of Pi
UDP_PORT = 5005           # Port the Pi is listening on

# Set up the socket connection
# sock = socket.socket(socket.AF_INET,  # Internet
#                      socket.SOCK_DGRAM)  # UDP
# sock.bind((UDP_IP, UDP_PORT))


class RecvDaemon(Daemon):
    def run(self):
        sock = socket.socket(socket.AF_INET,  # Internet
                             socket.SOCK_DGRAM)  # UDP
        sock.bind((UDP_IP, UDP_PORT))
        while True:
            data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
            print "received message:", data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set up a UDP connection between an RPi and something else")
    parser.add_argument("action",
                        nargs=1,
                        choices=["start", "restart", "stop"],
                        help="What should the daemon do? Options are start, restart, and stop")
    daemon = RecvDaemon('/tmp/daemon_udp_receive.pid')
    args = parser.parse_args()
    if args.action[0] == "start":
        daemon.start()
    elif args.action[0] == "restart":
        daemon.restart()
    else:
        daemon.stop()
