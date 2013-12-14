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
    #relevant Training variables
    duration1_Sound = 1.0 #in seconds. Amount of time that the soundGen is executed.
    duration2_Movement = 2.0 #in seconds. Amount of time during which movement is considered
    duration3_interTrial = 4.0 #in seconds. Amount of delay time between two trials.
    ##
    timeWindowDivider = 10.0
    maxPointMovement = 2000 #above this amount of movement detected, it will be trimmed to this value.
    initialMovementThreshold = 4000
    initialWindowThreshold = 1
    maxMovementThreshold = 14000
    maxWindowThreshold = 5
    
    soundGenDuration = duration1_Sound
    soundGenFrequency1 = 1000.0
    soundGenFrequency2 = 2000.0
    totalTimeDuration = duration1_Sound + duration2_Movement + duration3_interTrial #in seconds
    timeThreshold_01 = 20
    timeThreshold_02 = 64
    timeThreshold_03 = 150
    
    trialCount = 0
    successTrialCount=0
    dropReleased = 0
    
    countMovement = 0 #if it reaches 10, there has been detected a sustained movement for 1000 ms => give reward
    countIdleTime = 0 #if it reaches 10, there has NOT been detected a sustained movement for 1000 ms => reset counters
    
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
    print 't/T: increase/decrease threshold (500 - %d)' % gVariables.maxMovementThreshold
    print 'w/W: increase/decrease movement window (1 - %d sec)' % gVariables.maxWindowThreshold
    print 'k: set 8 second trial training'
    print 'q or ESC: quit'

def loopFunction():
    def renderAgain():
        #render things in pygame again.
        # draw the white background onto the surface
        windowSurface.fill((55,55,55))
        #
        text1 = basicFont.render('Trials: %d' % gVariables.trialCount, True, (255,255,255))
        textRect1 = text1.get_rect()
        textRect1.centerx = windowSurface.get_rect().centerx
        textRect1.centery = windowSurface.get_rect().centery
        
        text2 = basicFont.render('Successful Trials: %d' % gVariables.successTrialCount, True, (255,255,255))
        textRect2 = text2.get_rect()
        textRect2.centerx = windowSurface.get_rect().centerx
        textRect2.centery = windowSurface.get_rect().centery+30
        # draw the text onto the surface
        windowSurface.blit(text1, textRect1)
        windowSurface.blit(text2, textRect2)
        # draw the window onto the screen
        pygame.display.update()
    
    print gVariables.trainingName
    import sphereVideoDetection
    videoDet = sphereVideoDetection.sphereVideoDetection(VIDEOSOURCE, CAM_WIDTH, CAM_HEIGHT)
    import time
    
    movementVector = [0,0,0,0,0,0,0,0,0,0] #has the history of previous movements, separated by 0.1 seconds
    #pygame for displaying variables
    import pygame, sys
    pygame.init()
    windowSurface = pygame.display.set_mode((350, 100), 0, 32)
    pygame.display.set_caption('Variables')
    basicFont = pygame.font.SysFont(None, 48)
    renderAgain()
    try:
        while(True):
                videoDet.resetX()
                videoDet.resetY()
                time.sleep(movementWindow / gVariables.timeWindowDivider)
                renderAgain()
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
                if (movementVector[9]>= gVariables.maxPointMovement):
                    movementVector[9] = gVariables.maxPointMovement - 1 
                vectorSum = 0
                for i in range(0,len(movementVector)):
                    vectorSum+= movementVector[i]
                if (vectorSum  > movementThreshold):
                    gVariables.countMovement += 1
                else:
                    gVariables.countIdleTime += 1
                #print movementVector
                logger.debug('Movement Vector: %s',movementVector)
                #print "vector sum: " + str(vectorSum) + "       movement count: "+ str(countMovement)        
                logger.debug('%s',"vector sum: " + str(vectorSum) + "       movement count: "+ str(gVariables.countMovement))
                if (gVariables.countIdleTime >9):
                    #durante 1000 ms no se estuvo moviendo. Resetear contadores
                    gVariables.countMovement = 0
                    gVariables.countIdleTime = 0
                if (gVariables.countMovement > 9):
                    #se estuvo moviendo durante 1000 ms. Dar recompensa.
                    gVariables.countMovement = 0
                    for i in range(0,len(movementVector)):
                        movementVector[i] = 0
                    #print "Release drop of water."
                    if (trialTime > gVariables.timeThreshold_01 and trialTime < gVariables.timeThreshold_02 and gVariables.dropReleased == 0):
                        val1.drop()
                        logger.debug("Release drop of water.")
                        gVariables.successTrialCount+=1
			gVariables.dropReleased = 1
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
    
    try:
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
    
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    except:
        print "Error capturing input."

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
                    if movementThreshold > gVariables.maxMovementThreshold:
                        movementThreshold = gVariables.maxMovementThreshold
                    print "Movement Threshold changed to : " + str(movementThreshold)
                    printInstructions()
                elif (key == 'T'):
                    movementThreshold -= 500
                    if movementThreshold < 500:
                        movementThreshold = 500
                    print "Movement Threshold changed to : " + str(movementThreshold)
                    printInstructions()
                elif (key == 'w'):
                    movementWindow +=1
                    if movementWindow > gVariables.maxWindowThreshold:
                        movementWindow = gVariables.maxWindowThreshold
                    print "Movement Window changed to : " + str(movementWindow) + "seconds"
                    printInstructions()
                elif (key == 'W'):
                    movementWindow -=1
                    if movementWindow < 1:
                        movementWindow = 1
                    print "Movement Window changed to : " + str(movementWindow) + "seconds"
                    printInstructions()
                elif (key == 'k'):
                    if isTrial == 0:
                        isTrial = 1
                        trialTime = 0
                        print "8 second trial activated:"
                        print "  %d second: tone" %gVariables.soundGenDuration
                        print "  2 second: detection of movement"
                        print "  4 second: inter trial delay time"
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
                if (trialTime == 1 ):
                    logger.info('Starting new trial')
                    gVariables.trialCount+=1
		    gVariables.dropReleased = 0
                    logger.info('tone 1: 1 kHz')
                    s1.play()
                if (trialTime == gVariables.timeThreshold_01):
                    logger.info('Start trial movement detection')
                elif (trialTime == gVariables.timeThreshold_02):
                    logger.info('End trial movement detection')
                    logger.info('Start inter-trial delay')
                elif trialTime> gVariables.timeThreshold_03:
                    trialTime = 0
                    logger.info('End inter-trial delay')
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
