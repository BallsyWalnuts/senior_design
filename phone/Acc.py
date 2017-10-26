#! /usr/bin/env python
# Robert Seaton
# 25 September 2017
# Southern Illinois University Edwardsville

import android
import time
import socket

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
    delta = [(new[0] - old[0]) * 360 / 20 // 1, (new[1] - old[1]) * 360 / 20 // 1, (new[2] - old[2]) * 360 / 20 // 1, i]
    print (delta)
    old = new
    timeSensed += 10
droid.stopSensing()

UDP_IP = "120.0.0.1"
UDP_PORT = 8001
MESSAGE = "Hello World"

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.sendto(data=MESSAGE, flags=(UDP_IP, UDP_PORT))
