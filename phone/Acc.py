#! /usr/bin/env python
# Robert Seaton, Grant Steiner
# 25 September 2017
# Southern Illinois University Edwardsville

import android
import time
import socket

UDP_IP = "120.0.0.1"  # IP address of the Raspberry Pi
UDP_PORT = 8001  # Port that the Pi is listening on
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Initialize the socket


def sock_send(data=None):
    sock.sendto(data=data, flags=(UDP_IP, UDP_PORT))


if __name__ == '__main__':
    new = [0, 0, 0]
    old = new
    droid = android.Android()
    endTime = 1000
    timeSensed = 0
    i = 0
    droid.startSensingTimed(2, 10)
    while timeSensed <= endTime:
        time.sleep(.01)
        i += 1
        new = droid.sensorsReadAccelerometer().result
        delta = [(new[0] - old[0]) * 360 / 20 // 1,
                 (new[1] - old[1]) * 360 / 20 // 1]
        sock_send(data=delta)  # send the data to the Pi
        # print (delta)
        old = new
        timeSensed += 10
    droid.stopSensing()
