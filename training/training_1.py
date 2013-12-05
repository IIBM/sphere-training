# -*- coding: utf-8 -*-

######################################################
####################
#track-bola v0.1 Modificado para uso de Serial Port:
####################
#Se toma como entrada un flujo de video (webcam o archivo de video), se procesan y detectan círculos negros para
#mover un entorno virtual (Laberinto tipo T).
# Se enciende válvula de agua si se detecta movimiento en la bola.
######################################################><


#import pygame
#from pygame.locals import *
import os, sys
lib_path = os.path.abspath('../modules/')
sys.path.append(lib_path)

THRESHOLD = 200
dropTime = 1.0


import spherevideotracker
try:
    from configvideo import *
except ImportError:
    print "No existe el archivo configvideo.py"
except:
    print "otro error"

sp1 = spherevideotracker.spherevideotracker(VIDEOSOURCE,CAM_WIDTH,CAM_HEIGHT)

import threading
import time

th1 = threading.Thread(target=sp1.startcapture)

th1.start()

time.sleep(2)

import valve
v1 = valve.Valve()
while True:
    a = sp1.getCumState()
    xm = a[0]
    ym = a[1]
    print "x = " + str(xm) + " y = " + str(ym)

    if ( (xm**2+ym**2) >= THRESHOLD):
        print "Detectado movimiento"
        v1.open()
        time.sleep(dropTime)
        v1.close()
        a = sp1.getCumState()
    time.sleep(0.25)
