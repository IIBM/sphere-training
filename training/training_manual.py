# -*- coding: utf-8 -*-

######################################################
# Se enciende válvula de agua de forma maual:
######################################################><


import modulespath

import threading
import time
import soundGen

import logging

import termios, fcntl, sys, os
fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

time.sleep(2)

formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
dateformat = '%Y/%m/%d %I:%M:%S %p'

logging.basicConfig(filename='logs/tmanual.log', filemode='a',
    level=logging.DEBUG, format=formatter, datefmt = dateformat)
logging.info('===============================================')
logging.info('Start Manual Training')

try:
    import valve
    import signal
    v1 = valve.Valve()
    s1 = soundGen.soundGen()
    s1.tone(1.0, 1000)
    s2 = soundGen.soundGen()
    s2.tone(1.0, 2000)
    while True:
        try:
            key = sys.stdin.read(1)#cv2.waitKey(100) #in miliseconds
            if (key == 'o'): #escape pressed
                logging.info('valve open')
                v1.open()
            elif (key == 'c'):
                logging.info('valve close')
                v1.close()
            elif (key == 'd'):
                logging.info('valve drop')
                v1.drop()
            elif (key == '1'):
                logging.info('tone 1: 1 kHz')
                s1.play()
            elif (key == '2'):
                logging.info('tone 2: 2 kHz')
                s2.play()
            elif (key=='\x1b' or key=='q'):
                logging.info('Exit signal key = %s',key)
                os.kill(os.getpid(), signal.SIGINT)
                sys.exit()
            else :
                logging.debug('key pressesed = %s',key)
        except IOError: pass
        time.sleep(.05)
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
    logging.info('End Manual Training')
