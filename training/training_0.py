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
TIMEVALVEOPEN = 1.0


import spherevideotracker
try:
    from configvideo import *
except ImportError:
    print "No existe el archivo configvideo.py"
except:
    print "otro error"

sp1 = spherevideotracker.spherevideotracker(VIDEOSOURCE,CAM_WIDTH,CAM_HEIGHT)
#sp1.calibrate()
#time.sleep(2)

import threading
import time

def detectmove():
    while True:
        a = sp1.getCumState()
        xm = a[0]
        ym = a[1]
        print "x = " + str(xm) + " y = " + str(ym)

        if ( (xm**2+ym**2) >= THRESHOLD):
            print "Detectado movimiento"
    #        v1.open()
    #        time.sleep(TIMEVALVEOPEN)       
    #    else :
    #        v1.close()
        time.sleep(0.25)
              


th1 = threading.Thread(target=sp1.startcapture)
th2 = threading.Thread(target=detectmove)

th1.start()
th2.start()

import termios, fcntl, sys, os
fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

time.sleep(2)

try:
    import valve
    import signal
    v1 = valve.Valve()
    while True:
        try:
            key = sys.stdin.read(1)#cv2.waitKey(100) #in miliseconds
            if (key == 'a'): #escape pressed
                v1.open()
                print "valve open"
            elif (key == 'c'):
                v1.close()
                print "valve close"
            elif (key=='\x1b'):
                os.kill(os.getpid(), signal.SIGINT)
                sys.exit()
            else :
                a.append(key)
        except IOError: pass
        time.sleep(.05)
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
