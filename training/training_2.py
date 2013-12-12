# -*- coding: utf-8 -*-

######################################################
#Training 2:
"""
    This training creates a movement detection object, and waits for a 1 second sustained movement.
    If detected, it will be given a reward (drop of water). Else, it will keep waiting until there is
    a  significant movement.<>
"""
######################################################><
import os, sys
lib_path = os.path.abspath('../modules/')
sys.path.append(lib_path)

import logging

def printInstructions():
    print 'Options:'
    print 'o: Open Valve'
    print 'c: Close Valve'
    print 'd: Water Drop'
    print '1: 1 kHz tone'
    print '2: 2 kHz tone'
    print 't: set threshold (500 - 10000)'
    print 'w: set movement window (1 - 5 sec)'
    print 'q or ESC: quit'

def loopFunction():
    print "Training 2."

    import sphereVideoDetection
    videoDet = sphereVideoDetection.sphereVideoDetection(VIDEOSOURCE, CAM_WIDTH, CAM_HEIGHT)
    import time
    

    movementVector = [0,0,0,0,0,0,0,0,0,0] #has the history of previous movements, separated by 0.1 seconds
    countMovement = 0 #if it reaches 10, there has been detected a sustained movement for 1000 ms => give reward
    countIdleTime = 0 #if it reaches 10, there has NOT been detected a sustained movement for 1000 ms => reset counters
    try:
        while(True):
                videoDet.resetX()
                videoDet.resetY()
                time.sleep(movementWindow / 10.0)
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
                if (vectorSum  > movementThreshold):
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
        return

if __name__ == '__main__':
    import time
    import threading
    try:
        from configvideo import *
    except ImportError:
        print "File configvideo.py not found."
    except:
        print "Error importing configvideo"
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

    logging.basicConfig(filename='logs/training2.log', filemode='a',
    level=logging.DEBUG, format=formatter, datefmt = dateformat)

    logger = logging.getLogger('main')
    logger.info('===============================================')
    logger.info('Start Training 2')
    #end logging
    #valve:
    import valve
    val1 = valve.Valve()
    #soundGen
    import soundGen
    s1 = soundGen.soundGen(1000.0, 1.0)
    s2 = soundGen.soundGen(2000.0, 1.0)
    #variables to be used as calibration
    movementThreshold = 6000
    movementWindow = 1
    # Create thread for executing detection tasks without interrupting user input.
    fred1 = threading.Thread(target=loopFunction)
    fred1.start()
    time.sleep(4)
    printInstructions()
    try:
        while(True):
            try:
                key = sys.stdin.read(1)#cv2.waitKey(100) #in miliseconds
                if (key == 'o'): #escape pressed
                    logger.info('valve open')
                    val1.open()
                elif (key == 'c'):
                    logger.info('valve close')
                    val1.close()
                elif (key == 'd'):
                    logger.info('valve drop')
                    val1.drop()
                elif (key == '1'):
                    logger.info('tone 1: 1 kHz')
                    s1.play()
                elif (key == '2'):
                    logger.info('tone 2: 2 kHz')
                    s2.play()
                elif (key == 't'):
                    movementThreshold += 500
                    if movementThreshold > 10000:
                        movementThreshold = 500
                    print "Movement Threshold changed to : " + str(movementThreshold)
                    printInstructions()
                elif (key == 'w'):
                    movementWindow +=1
                    if movementWindow > 5:
                        movementWindow = 1
                    print "Movement Window changed to : " + str(movementWindow) + "seconds"
                    printInstructions()
                elif (key=='\x1b' or key=='q'):
                    print "Exiting."
                    logger.info('Exit signal key = %s',key)
                    import signal
                    os.kill(os.getpid(), signal.SIGINT)
                    sys.exit()
                else :
                    print "another key pressed"
            except IOError: pass
            time.sleep(.05)
    except:
        print "Closing Training 2."
    finally:
        print "."
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        logger.info('End Training 2')
        print "-"
        import os
        os._exit(0)