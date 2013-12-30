# -*- coding: utf-8 -*-

######################################################
#Training 2:
"""
    Automatic Training.
    This training creates a movement detection object, and waits for a 1 second sustained movement.
    If detected, it will be given a reward (drop of water). Else, it will keep waiting until there is
    a  significant movement.<>
"""
######################################################><
import os, sys
lib_path = os.path.abspath('../modules/')
sys.path.append(lib_path)
import time
import timeit
import logging



class gVariables():
    trainingName = "training_2"
    #relevant Training variables
    eventTime1_sound = 1.0 #in seconds. Instant of time when the soundGen ends.
    eventTime2_movement = 3.0 #in seconds. Instant of time when movement ceases to be considered for reward
    eventTime3_trialEnd = 10.0 #in seconds. Instant of time when the trial ends.
    minIdleIntertrialTime = 1.0 #no-movement time in seconds before the start of next trial. If not reached this time with no movement, trial doesn't start
    
    interTrialRandom1Time = 4.0 #intertrial time is random between this value and the random2 value
    interTrialRandom2Time = 7.0 #intertrial time is random between previous value and this value.
    
    maxMovementThreshold = 200
    maxMovementTime = 11 #max amount of movement time (10 means 1000 ms) to give reward. SHould be less than the opportunity duration
    movementTime = 5 # time for a continuous time that should be reached to give reward.
    #ex.: movementTime = 5 means that there should be movement detected over 500 ms at least
    
    soundGenDuration = 1.0
    soundGenFrequency1 = 1000.0 #in Hz
    soundGenFrequency2 = 2000.0 #in Hz
    
    trialCount = 0 #total number of trials
    successTrialCount=0 #total number of succesful trials
    successRate = 0 #success rate = (success trials / total trial count) %
    dropReleased = 0 #0: no drop of water released this trial, 1: drop of water released
    trialExecuting = False #if true, the trial is online and working. Else, it has been stopped or never started
    
    countMovement = 0 #if it reaches 10, there has been detected a sustained movement for 1000 ms => give reward
    countIdleTime = 0 #if it reaches 10, there has NOT been detected a sustained movement for 1000 ms => reset counters
    
    #video Detection:
    videoDet=0 # video Detection object. initialized in the main.
    
    start_time = timeit.default_timer() #time when training with tone started.
    current_trial_start_time = timeit.default_timer() #current trial in execution, absolute time it started
    current_trial_time = timeit.default_timer() #second of the current trial (between 0 and the maximum length of a trial)
    current_trial_paused_time = 0 #to handle pause and resume correctly..
    
    current_trial_number = 0 #0: tone, 1: movement detection, 2: inter-trial, 3: instant before changing to 0



def printInstructions():
    print 'Options:'
    print 'o: Open Valve'
    print 'c: Close Valve'
    print 'd: Water Drop'
    print '1: %d Hz tone' % gVariables.soundGenFrequency1
    print '2: %d Hz tone' % gVariables.soundGenFrequency2
    print 't/T: increase/decrease threshold (10 - %d)' % gVariables.maxMovementThreshold
    print 'e/E: increase/decrease Movement Time needed for reward (100 ms - %d ms)' % (gVariables.maxMovementTime * 100)
    print 'l/L: recalibrate video input with/without noise filtering.'
    print 'q or ESC: quit'


def initDisplay():
    import trainingDisplay #display for showing different variables of interest
    gVariables.display = trainingDisplay.trainingDisplay()
    gVariables.display.addImportantInfo(("Rewards:", gVariables.successTrialCount))
    gVariables.display.addImportantInfo(("Time", 0))
    gVariables.display.renderAgain()

def updateDisplayInfo():
    now = timeit.default_timer()
    b = getFormattedTime(int(now - gVariables.start_time) )
    gVariables.display.updateInfo("Time", b )
    gVariables.display.updateInfo("Rewards:", gVariables.successTrialCount )
    gVariables.display.renderAgain()

def loopFunction():
    print gVariables.trainingName
    import sphereVideoDetection
    gVariables.videoDet = sphereVideoDetection.sphereVideoDetection(VIDEOSOURCE, CAM_WIDTH, CAM_HEIGHT)
    #Display initialization.
    initDisplay()
    try:
        while(True):
                time.sleep(0.05)
                #####################
                updateDisplayInfo()
                #gVariables.logger.debug('Movement Vector: %s',gVariables.movementVector)
                #####################
                if (gVariables.videoDet.getMovementStatus() == True and 
                    gVariables.videoDet.getMovementTime() >= (gVariables.movementTime / 10.0) ):
                    giveReward()
                    gVariables.videoDet.resetMovementTime()
                    gVariables.videoDet.resetX()
                    gVariables.videoDet.resetY()
                #print "Continuous total time: %r"%gVariables.videoDet.getMovementTime()
    finally:
        return

def giveReward():
            #print "Release drop of water."
            gVariables.valve1.drop()
            gVariables.logger.debug("Release drop of water.")
            gVariables.successTrialCount+=1


def getFormattedTime(a):
    try:
        hours = int (int(a) / 3600)  #hours
        minutes = int((int(a) - hours*3600) / 60) #minutes
        seconds = int(int(a) - hours*3600 - minutes*60 )
        if hours >0:
            hours = str(hours) + " h   "
        else:
            hours = ""
        if (int(minutes) > 0 or int(hours) > 0):
            minutes = str(minutes) + " m   "
        else:
            minutes = ''  
        
        seconds  = str(int(seconds) ) + " s   " 
        return str(hours+ minutes + seconds)
    except:
        return str(a) + ' s   '

def trainingInit():
    #logging
    formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    dateformat = '%Y/%m/%d %I:%M:%S %p'
    import logging
    logging.basicConfig(filename='logs/%s_%s.log' % (gVariables.trainingName,time.strftime("%Y-%m-%d")), filemode='a',
    level=logging.DEBUG, format=formatter, datefmt = dateformat)
    gVariables.logger = logging.getLogger('main')
    gVariables.logger.info('===============================================')
    gVariables.logger.info('Start %s' % gVariables.trainingName)
    #valve:
    import valve
    gVariables.valve1 = valve.Valve()
    #soundGen
    import soundGen
    gVariables.s1 = soundGen.soundGen(gVariables.soundGenFrequency1, gVariables.soundGenDuration)
    gVariables.s2 = soundGen.soundGen(gVariables.soundGenFrequency2, gVariables.soundGenDuration)
    gVariables.trialExecuting = False #boolean, if a 8 second with tone trial is wanted, this shoulb de set to 1
    # Create thread for executing detection tasks without interrupting user input.
    import threading
    fred1 = threading.Thread(target=loopFunction)
    fred1.start()
    time.sleep(1.3) #to print Instructions after calibration printings.
    printInstructions()

if __name__ == '__main__':
    ######
    #Input
    ######
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
    ####################
    #Video configuration
    ####################
    try:
        from configvideo import *
    except ImportError:
        print "File configvideo.py not found."
    except:
        print "Error importing configvideo" 
    ###############
    trainingInit()
    ###############
    try:
        while(True):
            try:
                key = sys.stdin.read(1)#cv2.waitKey(100) #in miliseconds
                if (key == 'o'): #escape pressed
                    gVariables.logger.info('valve open')
                    gVariables.valve1.open()
                elif (key == 'c'):
                    gVariables.logger.info('valve close')
                    gVariables.valve1.close()
                elif (key == 'd'):
                    gVariables.logger.info('valve drop')
                    gVariables.valve1.drop()
                elif (key == '1'):
                    gVariables.logger.info('tone 1: %d Hz' % gVariables.soundGenFrequency1)
                    gVariables.s1.play()
                elif (key == '2'):
                    gVariables.logger.info('tone 2: %d Hz'% gVariables.soundGenFrequency2)
                    gVariables.s2.play()
                elif (key == 't'):
                    gVariables.videoDet.setMovementThreshold(gVariables.videoDet.getMovementThreshold() + 10)
                    if gVariables.videoDet.getMovementThreshold() > gVariables.maxMovementThreshold:
                        gVariables.videoDet.setMovementThreshold(gVariables.maxMovementThreshold)
                    print "Movement Threshold changed to : " + str(gVariables.videoDet.getMovementThreshold())
                    printInstructions()
                elif (key == 'T'):
                    gVariables.videoDet.setMovementThreshold(gVariables.videoDet.getMovementThreshold() - 10)
                    if gVariables.videoDet.getMovementThreshold() < 10:
                        gVariables.videoDet.setMovementThreshold(10)
                    print "Movement Threshold changed to : " + str(gVariables.videoDet.getMovementThreshold())
                    printInstructions()
                elif (key == 'e'):
                    gVariables.movementTime += 1
                    if gVariables.movementTime > gVariables.maxMovementTime:
                        gVariables.movementTime = gVariables.maxMovementTime
                    print "Movement Time changed to : " + str(gVariables.movementTime * 100) + " ms"
                    printInstructions()
                elif (key == 'E'):
                    gVariables.movementTime -= 1
                    if gVariables.movementTime < 1:
                        gVariables.movementTime = 1
                    print "Movement Time changed to : " + str(gVariables.movementTime * 100) + " ms"
                    printInstructions()
                elif (key == 'l'):
                    gVariables.videoDet.calibrate()
                    gVariables.videoDet.setNoiseFiltering(True)
                    print "Calibrated. Noise Filtering is ON."
                elif (key == 'L'):
                    gVariables.videoDet.calibrate()
                    gVariables.videoDet.setNoiseFiltering(False)
                    print "Calibrated. Noise Filtering is OFF."
                elif (key=='\x1b' or key=='q'):
                    print "Exiting."
                    gVariables.logger.info('Exit signal key = %s',key)
                    import signal
                    os.kill(os.getpid(), signal.SIGINT)
                    sys.exit()
                else :
                    print "Key not supported: %r" %key
            except IOError: pass
            time.sleep(0.08)
    except:
        print "Closing %s." % gVariables.trainingName
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        gVariables.logger.info('End %s'% gVariables.trainingName)
        import os
        os._exit(0)