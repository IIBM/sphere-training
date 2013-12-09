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

logger = logging.getLogger('main')
logger.info('===============================================')
logger.info('Start Manual Training')

try:
    import valve
    import signal

    print 'Options:'
    print 'o: Open Valve'
    print 'c: Close Valve'
    print 'd: Water Drop'
    print '1: 1 kHz tone'
    print '2: 2 kHz tone'
    print 'q or ESC: quit'
    
    v1 = valve.Valve()
    s1 = soundGen.soundGen(1000.0, 1.0)
    s2 = soundGen.soundGen(2000.0, 1.0)
    while True:
        try:
            key = sys.stdin.read(1)#cv2.waitKey(100) #in miliseconds
            if (key == 'o'): #escape pressed
                logger.info('valve open')
                v1.open()
            elif (key == 'c'):
                logger.info('valve close')
                v1.close()
            elif (key == 'd'):
                logger.info('valve drop')
                v1.drop()
            elif (key == '1'):
                logger.info('tone 1: 1 kHz')
                s1.play()
            elif (key == '2'):
                logger.info('tone 2: 2 kHz')
                s2.play()
            elif (key=='\x1b' or key=='q'):
                logger.info('Exit signal key = %s',key)
                os.kill(os.getpid(), signal.SIGINT)
                sys.exit()
            else :
                logger.debug('key pressesed = %s',key)
        except IOError: pass
        time.sleep(.05)
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
    logger.info('End Manual Training')
