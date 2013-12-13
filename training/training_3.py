# -*- coding: utf-8 -*-

######################################################
#Training 3:
"""
    This training creates a gives a 1 sec tone , then has an 2 second interval where the subject can
    generate movement or not, and a reward in case there has been detected movement. Then follows a 5 second delay
    for the next trial.<>
"""
######################################################><
import os, sys
lib_path = os.path.abspath('../modules/')
sys.path.append(lib_path)

import logging

class gVariables():
    trainingName = "Training 3"
    timeWindowDivider = 10.0
    maxPointMovement = 2000
    initialMovementThreshold = 6000
    initialWindowThreshold = 1
    soundGenDuration = 1.0
    soundGenFrequency1 = 1000.0
    soundGenFrequency2 = 2000.0
    totalTimeDuration = 8.0 #in seconds
    timeThreshold_01 = 21
    timeThreshold_02 = 63
    timeThreshold_03 = 170
    def recalculateTimeIntervals(self):
        print "recalculating time intervals."
        #Should recalculate timeThreshold_0x according to total Time DUration.
        #This should be executed by the program only once, at the beginning of the run.
    
def printInstructions():
    print 'Options:'
    print 'o: Open Valve'
    print 'c: Close Valve'
    print 'd: Water Drop'
    print '1: %d Hz tone' % gVariables.soundGenFrequency1
    print '2: %d Hz tone' % gVariables.soundGenFrequency2
    print 't: set threshold (500 - 10000)'
    print 'w: set movement window (1 - 5 sec)'
    print 'k: set 8 second trial training'
    print 'q or ESC: quit'

def loopFunction():
    print gVariables.trainingName
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
                time.sleep(movementWindow / gVariables.timeWindowDivider)
                movementVector[0] = movementVector[1]
                movementVector[1] = movementVector[2]
                movementVector[2] = movementVector[3]
                movementVector[3] = movementVector[4]
                movementVector[4] = movementVector[5]
                movementVector[5] = movementVector[6]
                movementVector[6] = movementVector[7]
                movementVector[7] = movementVector[8]
                movementVector[8] = movementVector[9]
                if ((trialTime > gVariables.timeThreshold_01 and trialTime < gVariables.timeThreshold_02) or (isTrial == False) ):
                    movementVector[9] = (abs(videoDet.getAccumX() * videoDet.getAccumX())  + abs( videoDet.getAccumY()*videoDet.getAccumY() ))
                if (movementVector[9]>= gVariables.maxPointMovement):
                    movementVector[9] = gVariables.maxPointMovement - 1 
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

    logging.basicConfig(filename='logs/training3.log', filemode='a',
    level=logging.DEBUG, format=formatter, datefmt = dateformat)

    logger = logging.getLogger('main')
    logger.info('===============================================')
    logger.info('Start Training 3')
    #end logging
    #valve:
    import valve
    val1 = valve.Valve()
    #soundGen
    import soundGen
    s1 = soundGen.soundGen(gVariables.soundGenFrequency1, gVariables.soundGenDuration)
    s2 = soundGen.soundGen(gVariables.soundGenFrequency2, gVariables.soundGenDuration)
    #variables to be used as calibration
    movementThreshold = gVariables.initialMovementThreshold
    movementWindow = gVariables.initialWindowThreshold
    trialTime = 0
    isTrial = 0 #boolean, if a 8 second with tone trial is wanted, this shoulb de set to 1
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
                    logger.info('tone 1: %d Hz' % gVariables.soundGenFrequency1)
                    s1.play()
                elif (key == '2'):
                    logger.info('tone 2: %d Hz'% gVariables.soundGenFrequency2)
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
                elif (key == 'k'):
                    if isTrial == 0:
                        isTrial = 1
                        trialTime = 0
                        print "8 second trial activated:"
                        print "  1 second: tone"
                        print "  2 second: detection of movement"
                        print "  5 second: inter trial delay time"
                    else:
                        isTrial = 0
                        print "8 second trial deactivated."
                elif (key=='\x1b' or key=='q'):
                    print "Exiting."
                    logger.info('Exit signal key = %s',key)
                    import signal
                    os.kill(os.getpid(), signal.SIGINT)
                    sys.exit()
                else :
                    print "another key pressed"
            except IOError: pass
            if (isTrial == 1):
                trialTime +=1
                if trialTime> gVariables.timeThreshold_03:
                    trialTime = 0
                    logger.info('End inter-trial delay')
                if (trialTime == 1):
                    logger.info('Starting new trial')
                    logger.info('tone 1: 1 kHz')
                    s1.play()
                if (trialTime == gVariables.timeThreshold_01 - 1):
                    logger.info('Start trial movement detection')
                if (trialTime == gVariables.timeThreshold_02 + 1):
                    logger.info('End trial movement detection')
                    logger.info('Start inter-trial delay')
            #print trialTime
            time.sleep(.05)
    except:
        print "Closing Training 3."
    finally:
        print "."
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        logger.info('End Training 3')
        print "-"
        import os
        os._exit(0)