# -*- coding: utf-8 -*-

######################################################
#Training 2:
"""
    Se crea un objeto de detección de video y se espera que durante 1 segundo haya movimiento significativo.
    Si lo hay, se da recompensa (gota de agua), caso contrario, se sigue esperando a que haya un movimiento
    significativo durante 1 segundo sostenido.
"""
######################################################><
import os, sys
lib_path = os.path.abspath('../modules/')
sys.path.append(lib_path)

import logging

if __name__ == '__main__':
    print "Training 2."
    try:
        from configvideo import *
    except ImportError:
        print "No existe el archivo configvideo.py"
    except:
        print "otro error"
    import sphereVideoDetection
    videoDet = sphereVideoDetection.sphereVideoDetection(VIDEOSOURCE, CAM_WIDTH, CAM_HEIGHT)
    import time
    import valve
    #logging
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
    logger.info('Start Training 2')
    #fin logging
    movementVector = [0,0,0,0,0,0,0,0,0,0] #has the history of previous movements, separated by 0.1 seconds
    countMovement = 0 #si llega a 10, es que durante 1000 ms estuvo moviéndose => dar recompensa
    countIdleTime = 0 #si llega a 10, es que durante 1000 ms estuvo NO moviéndose => resetear contadores
    val1 = valve.Valve()
    try:
        while(True):
            videoDet.resetX()
            videoDet.resetY()
            time.sleep(0.1)
            movementVector[0] = movementVector[1]
            movementVector[1] = movementVector[2]
            movementVector[2] = movementVector[3]
            movementVector[3] = movementVector[4]
            movementVector[4] = movementVector[5]
            movementVector[5] = movementVector[6]
            movementVector[6] = movementVector[7]
            movementVector[7] = movementVector[8]
            movementVector[8] = movementVector[9]
            movementVector[9] = (abs(videoDet.getAccumX() * videoDet.getAccumX())  + abs( videoDet.getAccumY()*videoDet.getAccumY() ))
            if (movementVector[9]>= 2000):
                movementVector[9] = 1999
            vectorSum = 0
            for i in range(0,len(movementVector)):
                vectorSum+= movementVector[i]
            if (vectorSum  > 4000):
                countMovement += 1
            else:
                countIdleTime += 1
            #print movementVector
            logger.debug('Movement Vector: %s',movementVector)
            #print "vector sum: " + str(vectorSum) + "       movement count: "+ str(countMovement)        
            logger.debug('%s',"vector sum: " + str(vectorSum) + "       movement count: "+ str(countMovement))
            if (countIdleTime >9):
                #durante 1000 ms no se estuvo moviendo. Resetear contadores
                countMovement = 0
                countIdleTime = 0
            if (countMovement > 9):
                #se estuvo moviendo durante 1000 ms. Dar recompensa.
                countMovement = 0
                for i in range(0,len(movementVector)):
                    movementVector[i] = 0
                logger.debug("Release drop of water.")
                #print "Release drop of water."
                val1.drop()
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        logger.info('End Manual Training')

