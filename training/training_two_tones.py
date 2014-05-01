# -*- coding: utf-8 -*-

######################################################
# Training two tones:
"""
    This training creates two tone of different frequency.
    Each tone has one second of duration. After the tone, there is a two second
    interval where the subject must move (first tone) or stand still (second
    tone).
    If the subject succed in the task, gets a reward.
    There 50 % propabilty of ocurrance for each tone. If one tone appears three
    time in a row, the other tone is fixed in the next trial. 
    The inter trial delay is random between 3 to 6 seconds.><
    
"""
######################################################><
import os
import sys
import modulespath
import time
import timeit
import logging


class gVariables():
    
    @staticmethod
    def dummy_fn():
        print "testing"
    
    @staticmethod
    def fn_giveDrop():
            #print "_dando drop"
            gVariables.logger.info('valve drop')
            gVariables.valve1.drop()
            if (gVariables.trialExecuting == True):
                gVariables.logger.info('Drop given manually.')
                gVariables.dropsAmountGivenManually += 1
    
    @staticmethod
    def fn_giveReward():
            giveReward();
            if (gVariables.trialExecuting == True):
                            gVariables.logger.info('Reward given manually.')
                            gVariables.dropsAmountGivenManually += 1
    
    @staticmethod
    def fn_closeValve():
            gVariables.logger.info('valve close')
            gVariables.valve1.close()
    
    @staticmethod
    def fn_openValve():
        gVariables.logger.info('valve open')
        gVariables.valve1.open()
    
    @staticmethod
    def fn_tone1Test(newfreq):
        #Tests the tone n°1
        #the argument is the new frequency (if it changed). FIrst updates freq then plays.
        beforefreq = gVariables.soundGenFrequency1
        gVariables.fn_setFrequencyT1(newfreq)
        gVariables.logger.info('Changed Tone 1 Frequency to: %d Hz  (before was %d Hz)' % (gVariables.soundGenFrequency1, beforefreq ) )
        gVariables.s1.play()
    
    @staticmethod
    def fn_tone2Test(newfreq):
        #Tests the tone n°2
        #the argument is the new frequency (if it changed). FIrst updates freq then plays.
        beforefreq = gVariables.soundGenFrequency2
        gVariables.fn_setFrequencyT2(newfreq)
        gVariables.logger.info('Changed Tone 2 Frequency to: %d Hz  (before was %d Hz)' % (gVariables.soundGenFrequency2, beforefreq ) )
        gVariables.s2.play()
    
    @staticmethod
    def fn_setMovementMethod(value_given):
        gVariables.videoDet.setMovementMethod(value_given)
        print "Movement method set: ", value_given
        gVariables.logger.info( "Movement method set: " + str(value_given) )
    
    @staticmethod
    def fn_movementThresholdSet(value_given):
        #aumentar threshold
        gVariables.videoDet.setMovementThreshold(int(value_given) )
        print "Movement Threshold changed to : " + str(gVariables.videoDet.getMovementThreshold())
        gVariables.logger.info( "Movement Threshold changed to : " + str(gVariables.videoDet.getMovementThreshold()) )
    
    @staticmethod
    def fn_toneOneProbabilitySet(value_given):
        #set Probability of the tone nr1 to value
        if (isinstance( value_given, float ) == False ):
            return;
        gVariables.toneOneProbability = value_given
        print "Tone One Probabilty changed to : " + str(gVariables.toneOneProbability * 100) + " %"
        gVariables.logger.info( "Tone One Probabilty changed to : " + str(gVariables.toneOneProbability * 100) + " %" )
    
    @staticmethod
    def fn_setITRandom1(value_given):
        gVariables.interTrialRandom1Time = value_given
        print "Intertrial random 1 time set to : ", value_given
        gVariables.logger.info( "Intertrial random 1 time set to : " + str(value_given) )
    
    @staticmethod
    def fn_setITRandom2(value_given):
        gVariables.interTrialRandom2Time = value_given
        gVariables.logger.info( "Intertrial random 2 time set to : " + str(value_given) )
    
    
    @staticmethod
    def fn_setMovementWindowStart(value_given):
        gVariables.eventTime1_movement_start = value_given
        print "Movement window Start set to value: ", value_given
        gVariables.logger.info( "Movement window Start set to value: " + str(value_given) )
    
    @staticmethod
    def fn_setMovementWindowEnd(value_given):
        gVariables.eventTime2_movement = value_given
        print "Movement window End set to value: ", value_given
        gVariables.logger.info( "Movement window End set to value: " + str(value_given) )
    
    @staticmethod
    def fn_setTone1Duration(value_given):
        if (value_given != gVariables.soundGenDuration1):
            gVariables.soundGenDuration1 = value_given
            gVariables.fn_recreateTone1()
            
            print "Tone 1 Duration set to value: ", value_given
            gVariables.logger.info( "Tone 1 Duration set to value: " + str(value_given) )
        else:
            print "Tone 1 Duration is already at value: ", value_given
            gVariables.logger.info( "Tone 1 Duration is already at value: " + str(value_given) )
    
    @staticmethod
    def fn_setTone2Duration(value_given):
        if (value_given != gVariables.soundGenDuration2):
            gVariables.soundGenDuration2 = value_given
            gVariables.fn_recreateTone2()
            
            print "Tone 2 Duration set to value: ", value_given
            gVariables.logger.info( "Tone 2 Duration set to value: " + str(value_given) )
        else:
            print "Tone 2 Duration is already at value: ", value_given
            gVariables.logger.info( "Tone 2 Duration is already at value: " + str(value_given) )
    
    @staticmethod
    def fn_setFrequencyT1(freq):
        if ( int(freq) != gVariables.soundGenFrequency1):
            import soundGen
            a = "setting frequency T1: " + str(freq)
            print a
            gVariables.logger.info(a)
            gVariables.soundGenFrequency1 = int(freq)
            gVariables.s1 = soundGen.soundGen(gVariables.soundGenFrequency1, gVariables.soundGenDuration1)
        else:
            print "frequency for Tone 1 already set at ", freq
            gVariables.logger.info("frequency for Tone 1 already set at " + str(freq) )
    
    @staticmethod
    def fn_setFrequencyT2(freq):
        if ( int(freq) != gVariables.soundGenFrequency2):
            import soundGen
            a = "setting frequency T2: " + str(freq)
            print a
            gVariables.logger.info(a)
            gVariables.soundGenFrequency2 = int(freq)
            gVariables.s2 = soundGen.soundGen(gVariables.soundGenFrequency2, gVariables.soundGenDuration2)
        else:
            print "frequency for Tone 2 already set at ", freq
            gVariables.logger.info("frequency for Tone 2 already set at " + str(freq) )
    
    @staticmethod
    def fn_recreateTone1():
        import soundGen
        gVariables.s1 = soundGen.soundGen(gVariables.soundGenFrequency1, gVariables.soundGenDuration1)
        pass
    
    @staticmethod
    def fn_recreateTone2():
        import soundGen
        gVariables.s2 = soundGen.soundGen(gVariables.soundGenFrequency2, gVariables.soundGenDuration2)
        pass
    
    @staticmethod
    def fn_movementTimeSet(nwmvnt):
        #set movement time
        movement_time = float(nwmvnt)
        gVariables.movementTime = movement_time
        gVariables.videoDet.setMovementTimeWindow(gVariables.movementTime)
        a = "Movement Time changed to : " + str(gVariables.movementTime * 1000) + " ms"
        print a
        gVariables.logger.info( a )
    
    @staticmethod
    def fn_idleTimeSet(nwmvnt):
        #set idle time.
        idle_time = float(nwmvnt)
        gVariables.idleTime = idle_time
        a = "Idle Time changed to : " + str(gVariables.idleTime * 1000) + " ms"
        print a
        gVariables.logger.info( a )
    
    @staticmethod
    def fn_calibrateNoiseFilteringOn():
        gVariables.videoDet.setNoiseFiltering(True)
        gVariables.videoDet.calibrate()
        print "Calibrated. Noise Filtering is ON."
        gVariables.logger.info( "Calibrated. Noise Filtering is ON." )
    
    @staticmethod
    def fn_calibrateNoiseFilteringOff():
        gVariables.videoDet.setNoiseFiltering(False)
        gVariables.videoDet.calibrate()
        print "Calibrated. Noise Filtering is OFF."
        gVariables.logger.info( "Calibrated. Noise Filtering is OFF." )
    
    @staticmethod
    def fn_startStopTraining(flag):
        #the flag comes from the API/GUICheck system.
        #However, it is best to check if the training has started probing our own variables
        #and override the flag information:
        if (gVariables.trialStarted == False):
            #the trial is "startable"
            flg = 1
        else:
            #the trial has started, is stoppable.
            flg = 2
        
        if (flg == 1):
            restartTraining()
        if (flg == 2):
            stopTraining()
    
    @staticmethod
    def fn_pauseResumeTraining(flag):
        #the flag comes from the API/GUICheck system.
        #However, it is best to check if the training is resumable or pausable probing our own variables
        #and override the flag information:
        if (gVariables.trialStarted == True):
            if (gVariables.trialExecuting == True):
                #trial started and executing, is pausable
                pauseTraining()
            else:
                #trial started and NOT executing, is resumable
                resumeTraining()
        else:
            print "fn_pauseResumeTraining: \n   Trial has not been started and cannot be paused or resumed."
            gVariables.logger.info( "fn_pauseResumeTraining: \n   Trial has not been started and cannot be paused or resumed." )
    
    @staticmethod
    def fn_showTrackingFeedback():
        gVariables.videoDet.setTrackingFeedback(True)
        pass
    
    @staticmethod
    def fn_hideTrackingFeedback():
        gVariables.videoDet.setTrackingFeedback(False)
        pass
    
    @staticmethod
    def fn_showUserFeedback():
        gVariables.videoDet.setUserFeedback(True)
        
        pass
    
    @staticmethod
    def fn_hideUserFeedback():
        gVariables.videoDet.setUserFeedback(False)
        pass
    
    def __checkModules():
            import os
            
            try:
                import configvideo
            except ImportError:
                print "File configvideo.py not found. Generating a new copy..."
                a = (os.getcwd().split("/training") [0]) + "/modules/"
                import shutil
                shutil.copyfile(a+"configvideo.py.example", a+"configvideo.py")
                import configvideo
                print "configvideo.py copied and imported successfully."
            except:
                print "Error importing configvideo."
                os._exit(1)
            
            
            try:
                import configSphereVideoDetection
            except ImportError:
                print "File configSphereVideoDetection.py not found. Generating a new copy..."
                a = (os.getcwd().split("/training") [0]) + "/modules/"
                import shutil
                shutil.copyfile(a+"configSphereVideoDetection.py.example", a+"configSphereVideoDetection.py")
                import configvideo
                print "configSphereVideoDetection.py copied and imported successfully."
            except:
                print "Error importing configSphereVideoDetection."
                os._exit(1)
            
            try:
                import configCamera
            except ImportError:
                print "File configCamera.py not found. Generating a new copy..."
                a = (os.getcwd().split("/training") [0]) + "/modules/"
                import shutil
                shutil.copyfile(a+"configCamera.py.example", a+"configCamera.py")
                import configvideo
                print "configCamera.py copied and imported successfully."
            except:
                print "Error importing configCamera."
                os._exit(1)
            
            try:
                import config_training_two_tones as cfgtwotones
            except ImportError:
                print "File config_training_two_tones.py not found. Generating a new copy..."
                a = os.getcwd() + "/"
                print a
                import shutil
                shutil.copyfile(a+"config_training_two_tones.py.example", a+"config_training_two_tones.py")
                import config_training_two_tones as cfgtwotones
                print "config_training_two_tones.py copied and imported successfully."
            except:
                print "Error importing config_training_two_tones."
                os._exit(1)
            ####
            # End of checking existance of config files.
            
            pass
            ####
            #training init: check for modules and dependencies. Copy from '*.py.example' if needed
            ####
    
    pass
    __checkModules()
    
    import config_training_two_tones as cfgtwotones
    trainingName = cfgtwotones.trainingName
    # relevant Training variables
    eventTime1_sound = cfgtwotones.eventTime1_sound  # in seconds. Instant of time when the soundGen ends.
    eventTime1_movement_start = cfgtwotones.eventTime1_movement_start  # in seconds. Instant of time when the movement starts to be considered
    eventTime2_movement = cfgtwotones.eventTime2_movement  # in seconds. Instant of time when movement ceases to be considered for reward
    eventTime3_trialEnd = cfgtwotones.eventTime3_trialEnd  # in seconds. Instant of time when the trial ends.
    minIdleIntertrialTime = cfgtwotones.minIdleIntertrialTime  # no-movement time in seconds before the start of next trial. If not reached this time with no movement, trial doesn't start
    
    interTrialRandom1Time = cfgtwotones.interTrialRandom1Time  # intertrial time is random between this value and the random2 value
    interTrialRandom2Time = cfgtwotones.interTrialRandom2Time  # intertrial time is random between previous value and this value. This
    # is also the max duration of a trial.
    
    maxMovementThreshold = cfgtwotones.maxMovementThreshold
    maxMovementTime = cfgtwotones.maxMovementTime  # max amount of movement time (10 means 1000 ms) to give reward. SHould be less than the opportunity duration
    maxIdleTime = cfgtwotones.maxIdleTime
    movementTime = cfgtwotones.movementTime  # continuous moving time that should be reached to give reward. 0.5 = 500 ms
    # ex.: movementTime = 0.5 means that there should be movement detected over 500 ms at least
    idleTime = cfgtwotones.idleTime  # continuous idle time that should be reached to give reward. 10= 1000 ms
    
    soundGenDuration1 = cfgtwotones.soundGenDuration1
    soundGenDuration2 = cfgtwotones.soundGenDuration2
    soundGenFrequency1 = cfgtwotones.soundGenFrequency1  # in Hz
    soundGenFrequency2 = cfgtwotones.soundGenFrequency2  # in Hz
    
    trialCount = 0  # total number of trials
    movementTrialCount = 0  # total number of trials which requires the subject to move
    idleTrialCount = 0  # total number of trials which requires the subject to stay idle.
    successTrialCount = 0  # total number of succesful trials
    successMovementTrialCount = 0  # total number of succesful trials regarding movement state
    successIdleTrialCount = 0  # total number of succesful trials regarding idle state
    successRate = 0  # success rate = (success trials / total trial count) %
    dropReleased = 0  # 0: no drop of water released this trial, 1: drop of water released
    dropsAmountGivenManually = 0  # number of drops given manually.
    trialExecuting = False  # if true, the trial is online and working. Else, it has been stopped or never started
    
    trialStarted = False  # if true, the trial has been started (and as a consequence is pausable)
    
    trialSuccessful = False  # true: this trial was successful , false it was not.
    
    countMovement = 0  # if it reaches 10, there has been detected a sustained movement for 1000 ms => give reward
    countIdleTime = 0  # if it reaches 10, there has NOT been detected a sustained movement for 1000 ms => reset counters
    
    LOOP_FUNCTION_SLEEP_TIME = 0.05  # sleep time for the trial loop function (how frequently it asks videodet)
    
    # video Detection:
    videoDet = 0  # video Detection object. initialized in the main.
    
    videoMovementMethod = -1 #movement method to be used for movement analysis.
    
    start_time = timeit.default_timer()  # time when training with tone started.
    current_trial_start_time = timeit.default_timer()  # current trial in execution, absolute time it started
    current_trial_time = timeit.default_timer()  # second of the current trial (between 0 and the maximum length of a trial)
    current_trial_paused_time = 0  # to handle pause and resume correctly..
    
    current_trial_stage = 0  # 0: tone, 1: movement detection, 2: inter-trial, 3: instant before changing to 0

    toneOneProbability = cfgtwotones.toneOneProbability
    history_trial = [1, 2, 1, 2, 1, 2]
    current_trial_type = 0  # 1: for tone one, reward after movement 2: for tone two, reward after standing still
    current_trial_type_str = ""  # same as type but with string format.
    
    trial_comment = "" #comment about this training session.
    ns = 0
    #fin gVariables.
    pass

def initDisplay():
    import trainingDisplay  # display for showing different variables of interest
    gVariables.display = trainingDisplay.trainingDisplay()
    gVariables.display.addImportantInfo(("Trials", 0))
    gVariables.display.addImportantInfo(("Successful Trials", 0))
    gVariables.display.addImportantInfo(("Successful Trials mvnt", 0))
    gVariables.display.addImportantInfo(("Successful Trials idle", 0))
    gVariables.display.addImportantInfo(("Time", 0))
    gVariables.display.addSecondaryInfo(("% s/t", 0.0))
    gVariables.display.addSecondaryInfo(("Trial Time", "0 - 10"))
    gVariables.display.addSecondaryInfo(("Trial status", ""))
    gVariables.display.renderAgain()

def updateDisplayInfo():
    if (gVariables.trialExecuting == True):
                    now = timeit.default_timer()
                    b = getFormattedTime(int(now - gVariables.start_time))
                    gVariables.display.updateInfo("Time", b)
                    if (gVariables.current_trial_type == 1):
                        sttrial = "move"
                    elif (gVariables.current_trial_type == 2):
                        sttrial = "still"
                    else:
                        sttrial = ""
                    gVariables.current_trial_type_str = sttrial
                    if (gVariables.current_trial_time < gVariables.eventTime2_movement):
                        gVariables.display.updateInfo("Trial status", sttrial + " - " + "running")
                    else:
                        if gVariables.dropReleased == 1:
                             gVariables.display.updateInfo("Trial status", sttrial + " - " + "SUCCESS")
                        else:
                            gVariables.display.updateInfo("Trial status", sttrial + " - " + "FAIL")
    gVariables.display.updateInfo("Trials", gVariables.trialCount)
    gVariables.display.updateInfo("Successful Trials", gVariables.successTrialCount)
    
    # stmvnt = str(gVariables.successMovementTrialCount) + " / " + str(gVariables.movementTrialCount )
    # stidle = str(gVariables.successIdleTrialCount) + " / " + str(gVariables.idleTrialCount )
    
    
    if (gVariables.trialCount > 0):
                    if (gVariables.movementTrialCount > 0):
                        temp1 = (1.0 * gVariables.successMovementTrialCount / gVariables.movementTrialCount)
                        tempH1 = temp1 * 100.0
                        tempString1 = str(tempH1)
                        if (len(tempString1) > 3):
                                            tempS1 = str(tempH1)[:4]
                        else:
                                            tempS1 = str(tempH1)[:3]
                        gVariables.display.updateInfo("Successful Trials mvnt", tempS1)
                    
                    if (gVariables.idleTrialCount > 0):
                        temp2 = (1.0 * gVariables.successIdleTrialCount / gVariables.idleTrialCount)
                        tempH2 = temp2 * 100.0
                        tempString2 = str(tempH2)
                        if (len(tempString2) > 3):
                                            tempS2 = str(tempH2)[:4]
                        else:
                                            tempS2 = str(tempH2)[:3]
                        gVariables.display.updateInfo("Successful Trials idle", tempS2)
                    ########
                    temp = (1.0 * gVariables.successTrialCount / gVariables.trialCount)
                    tempH = temp * 100.0
                    tempString = str(tempH)
                    if (len(tempString) > 3):
                        tempS = str(tempH)[:4]
                    else:
                        tempS = str(tempH)[:3]
                    gVariables.successRate = tempS
                    gVariables.display.updateInfo("% s/t", gVariables.successRate)
                    a = str(gVariables.current_trial_time)[:4] + " - " + str(gVariables.eventTime3_trialEnd)
                    gVariables.display.updateInfo("Trial Time", a)
    gVariables.display.renderAgain()

def mainLoopFunction():
    while(True):
                time.sleep(gVariables.LOOP_FUNCTION_SLEEP_TIME)
                GUICheck() #check if any GUI input was received
                trialLoop()  #
                updateDisplayInfo()

def trialLoop():
            # This function controls all events that defines a trial: Tone at a given time, reward opportunity, etc.
            
            #===================================================================
            # Check / update current trial stage and time
            #===================================================================
            if (gVariables.trialExecuting == True):
                # Update Trial Time. Important since this is where events happen at certain moments in this line.
                gVariables.current_trial_start_time += gVariables.current_trial_paused_time
                gVariables.start_time += gVariables.current_trial_paused_time  # we consider that training time has not passed in the pause state.
                gVariables.current_trial_paused_time = 0
                gVariables.current_trial_time = (timeit.default_timer() - gVariables.current_trial_start_time)
                if ((gVariables.current_trial_stage == 3 and 
                            gVariables.videoDet.getIdleTime() >= gVariables.minIdleIntertrialTime and
                                    gVariables.videoDet.getMovementStatus() == False) or (gVariables.trialCount == 0)):
                    gVariables.logger.info('Starting trial:%d' % gVariables.trialCount)
                    gVariables.trialCount += 1
                    gVariables.dropReleased = 0
                    gVariables.current_trial_start_time = timeit.default_timer()
                    gVariables.logger.debug(gVariables.history_trial)
                    gVariables.logger.debug(gVariables.toneOneProbability)
                    gVariables.logger.debug(gVariables.current_trial_type)
                    if (gVariables.toneOneProbability < 0.75) and (gVariables.toneOneProbability > 0.25) and (gVariables.history_trial[-1] == gVariables.history_trial[-2]) and (gVariables.history_trial[-2] == gVariables.history_trial[-3]) :
                        # 3 equal trial have past. forced changing trial
                        gVariables.logger.info('fixed tone')
                        if (gVariables.history_trial[-1]) == 2:
                            gVariables.current_trial_type = 1
                        else :
                            gVariables.current_trial_type = 2
                    else :
                        from random import random
                        if (random() < gVariables.toneOneProbability) :
                            gVariables.current_trial_type = 1
                        else :
                            gVariables.current_trial_type = 2
                            
                    if (gVariables.current_trial_type == 1) :
                            gVariables.logger.info('tone 1: 1 kHz')
                            gVariables.s1.play()
                            gVariables.movementTrialCount += 1
                            # a new "time window" should be set for 
                            # some movement analysis methods to work.
                            gVariables.videoDet.setMovementTimeWindow(gVariables.movementTime)
                    else :
                            gVariables.logger.info('tone 2: 8 kHz')
                            gVariables.s2.play()
                            gVariables.idleTrialCount += 1
                            # a new "time window" should be set for 
                            # some movement analysis methods to work.
                            gVariables.videoDet.setMovementTimeWindow(gVariables.idleTime)

                    gVariables.history_trial[0:-1] = gVariables.history_trial[1:]
                    gVariables.history_trial[-1] = gVariables.current_trial_type

                    gVariables.current_trial_stage = 0
                    gVariables.current_trial_paused_time = 0
                    
                    # add random factor to the intertrial time in the next one:
                    from random import randint
                    i = randint(0, 10)
                    scaleF = (gVariables.interTrialRandom2Time - gVariables.interTrialRandom1Time) / 10
                    gVariables.eventTime3_trialEnd = gVariables.interTrialRandom1Time + (i * scaleF)
                
                #there is a space of time between gVariables.eventTime1_sound and  gVariables.eventTime1_movement_start
                #which is not used. It could be used in the future. see docs.
                
                #the tone end is not necessarily tied to the start of movement detection. see docs.
                
                if (int(gVariables.current_trial_time) >= gVariables.eventTime1_movement_start and 
                     int(gVariables.current_trial_time) <= gVariables.eventTime2_movement 
                     and gVariables.current_trial_stage == 0):
                    gVariables.logger.info('Start trial movement detection')
                    gVariables.trialSuccessful = False
                    if (gVariables.current_trial_type == 1) :
                        gVariables.videoDet.resetMovementTime()
                    else:
                        gVariables.videoDet.resetIdleTime()
                    gVariables.current_trial_stage = 1
                elif (int(gVariables.current_trial_time) >= gVariables.eventTime2_movement and 
                      gVariables.current_trial_stage == 1):
                    gVariables.logger.info('End trial movement detection')
                    if (gVariables.trialSuccessful == True):
                        giveReward()
                        gVariables.logger.info('Reward given because trial was successful')
                    else:
                        gVariables.logger.info('Reward not given because trial was not successful')
                    gVariables.logger.info('Start inter-trial delay')
                    gVariables.current_trial_stage = 2
                elif (int(gVariables.current_trial_time) >= gVariables.eventTime3_trialEnd and
                      gVariables.current_trial_stage == 2):
                    gVariables.logger.info('End trial:%d' % (gVariables.trialCount - 1 ) )
                    gVariables.logger.info('Trial type: ' + str(gVariables.current_trial_type_str))
                    # #
                    gVariables.videoDet.setMovementTimeWindow(gVariables.minIdleIntertrialTime)
                    if(gVariables.dropReleased == 1):
                        gVariables.logger.info('Trial successful')
                    else:
                        gVariables.logger.info('Trial not successful')
                    gVariables.logger.info('Success rate:%r' % (gVariables.successRate))
                    gVariables.current_trial_stage = 3
            # gVariables.logger.debug('Movement Vector: %s',gVariables.movementVector)
            
            #===============================================================
            # Check if should give reward
            #===============================================================
            
            if (gVariables.trialExecuting == True and gVariables.current_trial_stage == 1):
                # print gVariables.videoDet.getTrackingStatus()
                if (gVariables.current_trial_type == 1):
                  if (gVariables.videoDet.getMovementStatus() == True and 
                    ((gVariables.videoDet.getMovementTime() >= (gVariables.movementTime))
                       ) ):
                    # giveReward() #the reward is given at the end of the mvnt window
                    gVariables.trialSuccessful = True
                    # print "Continuous total time: %r"%gVariables.videoDet.getMovementTime()
                elif (gVariables.current_trial_type == 2):
                  if (gVariables.videoDet.getMovementStatus() == False and 
                    gVariables.videoDet.getIdleTime() >= (gVariables.idleTime)):  #
                    # giveReward() #the reward is given at the end of the mvnt window
                    gVariables.trialSuccessful = True
                    # print "Continuous total time: %r"%gVariables.videoDet.getMovementTime()
                    pass
            else:
                #trial not executing or tr.stage not 1, so it is unnecessary to check if should give reward..
                pass

def GUICheck():
        #GUICheck: this function is called once in every thread loop, and checks if
        #    the shared variables between training_ and GUI Process contain new info.
        #    If it does, checks which message type was sent, and it's argument (if any)
        #    and executes the corresponding routine for that type of message.
        if (gVariables.ns.message1 != 0 ):
            print "GUICheck: Got a Message:", gVariables.ns.message1
            gVariables.logger.info( str("GUICheck: Got a Message:" + str(gVariables.ns.message1)) )
            print "GUICheck: Message's argument:", gVariables.ns.message2
            gVariables.logger.info( str("GUICheck: Message's argument:" + str(gVariables.ns.message2) ) )
            index = gVariables.ns.message1
            if (index == 1):
                print "GUICheck: 'Drop' message."
                gVariables.logger.info( "GUICheck: 'Drop' message." )
                gVariables.fn_giveDrop()
            elif (index == 2):
                print "GUICheck: 'Reward' message"
                gVariables.logger.info( "GUICheck: 'Reward' message" )
                gVariables.fn_giveReward()
            elif (index == 3):
                print "GUICheck: 'Open' message"
                gVariables.logger.info( "GUICheck: 'Open' message" )
                gVariables.fn_openValve()
            elif (index == 4):
                print "GUICheck: 'Close' message"
                gVariables.logger.info( "GUICheck: 'Close' message" )
                gVariables.fn_closeValve()
            elif (index == 5):
                print "GUICheck: 'Start Training' message"
                gVariables.logger.info( "GUICheck: 'Start Training' message" )
                gVariables.fn_startStopTraining(1)
            elif (index == 6):
                print "GUICheck: 'Stop Training' message"
                gVariables.logger.info( "GUICheck: 'Stop Training' message" )
                gVariables.fn_startStopTraining(2)
            elif (index == 7):
                print "GUICheck: 'Pause Training' message"
                gVariables.logger.info( "GUICheck: 'Pause Training' message" )
                gVariables.fn_pauseResumeTraining(2) ########
            elif (index == 8):
                print "GUICheck: 'Resume Training' message"
                gVariables.logger.info( "GUICheck: 'Resume Training' message" )
                gVariables.fn_pauseResumeTraining(1) ########
            elif (index == 9):
                print "GUICheck: 'Exit Training' message"
                gVariables.logger.info( "GUICheck: 'Exit Training' message" )
                exitTraining()
            elif (index == 10):
                print "GUICheck: 'Tone 1 Test' message"
                gVariables.logger.info( "GUICheck: 'Tone 1 Test' message" )
                gVariables.fn_tone1Test(gVariables.ns.message2)
            elif (index == 11):
                print "GUICheck: 'Tone 2 Test' message"
                gVariables.logger.info( "GUICheck: 'Tone 2 Test' message" )
                gVariables.fn_tone2Test(gVariables.ns.message2)
            elif (index == 12):
                print "GUICheck: 'Show Feedback' message"
                gVariables.logger.info( "GUICheck: 'Show Feedback' message" )
                gVariables.fn_showUserFeedback()
            elif (index == 13):
                print "GUICheck: 'Hide Feedback' message"
                gVariables.logger.info( "GUICheck: 'Hide Feedback' message" )
                gVariables.fn_hideUserFeedback()
            elif (index == 14):
                print "GUICheck: 'Show Tracking' message"
                gVariables.logger.info( "GUICheck: 'Show Tracking' message" )
                gVariables.fn_showTrackingFeedback()
            elif (index == 15):
                print "GUICheck: 'Hide Tracking' message"
                gVariables.logger.info( "GUICheck: 'Hide Tracking' message" )
                gVariables.fn_hideTrackingFeedback()
            elif (index == 16):
                print "GUICheck: 'Set Comment' message"
                gVariables.logger.info( "GUICheck: 'Set Comment' message" )
                gVariables.trial_comment = gVariables.ns.message2
                print "GUICheck: comment read from ns: ", gVariables.trial_comment
                gVariables.logger.info( str( "GUICheck: comment read from ns: "+ str(gVariables.trial_comment )) )
            elif (index == 17):
                print "GUICheck: 'Variable to change: Tone1 Frequency' message"
                gVariables.logger.info( "GUICheck: 'Variable to change: Tone1 Frequency' message" )
                gVariables.fn_setFrequencyT1( gVariables.ns.message2 )
                print "GUICheck: Argument value read from ns: ", gVariables.ns.message2
                gVariables.logger.info( str( "GUICheck: Argument value read from ns: " + str(gVariables.ns.message2) ) )
            elif (index == 18):
                print "GUICheck: 'Variable to change: Tone2 Frequency' message"
                gVariables.logger.info( "GUICheck: 'Variable to change: Tone2 Frequency' message" )
                gVariables.fn_setFrequencyT2( gVariables.ns.message2 )
                print "GUICheck: Argument value read from ns: ", gVariables.ns.message2
                gVariables.logger.info( str( "GUICheck: Argument value read from ns: " + str(gVariables.ns.message2) ) )
            elif (index == 19):
                print "GUICheck: 'Variable to change: Movement Amount' message"
                gVariables.logger.info( "GUICheck: 'Variable to change: Movement Amount' message" )
                gVariables.fn_movementThresholdSet(gVariables.ns.message2)
                print "GUICheck: Argument value read from ns: ", gVariables.ns.message2
                gVariables.logger.info( str( "GUICheck: Argument value read from ns: " + str(gVariables.ns.message2) ) )
            elif (index == 20):
                print "GUICheck: 'Variable to change: Method Type to be used' message"
                gVariables.logger.info( "GUICheck: 'Variable to change: Method Type to be used' message" )
                gVariables.fn_setMovementMethod(gVariables.ns.message2)
                print "GUICheck: Argument value read from ns: ", gVariables.ns.message2
                gVariables.logger.info( str( "GUICheck: Argument value read from ns: " + str(gVariables.ns.message2) ) )
            elif (index == 21):
                print "GUICheck: 'Variable to change: Movement Time' message"
                gVariables.logger.info( "GUICheck: 'Variable to change: Movement Time' message" )
                gVariables.fn_movementTimeSet(gVariables.ns.message2)
                print "GUICheck: Argument value read from ns: ", gVariables.ns.message2
                gVariables.logger.info( str("GUICheck: Argument value read from ns: " + gVariables.ns.message2) )
            elif (index == 22):
                print "GUICheck: 'Variable to change: Idle Time' message"
                gVariables.logger.info( "GUICheck: 'Variable to change: Idle Time' message" )
                gVariables.fn_idleTimeSet(gVariables.ns.message2)
                print "GUICheck: Argument value read from ns: ", gVariables.ns.message2
                gVariables.logger.info( str("GUICheck: Argument value read from ns: " + gVariables.ns.message2) )
            elif (index == 23):
                print "GUICheck: 'Variable to change: Tone Start' message"
                gVariables.logger.info( "GUICheck: 'Variable to change: Tone Start' message" )
                print "Tone Start variable is not meant to change. Add intertrial delay instead."
                gVariables.logger.info( "Tone Start variable is not meant to change. Add intertrial delay instead." )
                print "GUICheck: Argument value read from ns: ", gVariables.ns.message2
                gVariables.logger.info( str( "GUICheck: Argument value read from ns: " + str(gVariables.ns.message2) ) )
            elif (index == 24):
                print "GUICheck: 'Variable to change: Tone End' message"
                gVariables.logger.info( "GUICheck: 'Variable to change: Tone End' message" )
                gVariables.fn_setTone1Duration(float(gVariables.ns.message2))
                gVariables.fn_setTone2Duration(float(gVariables.ns.message2))
                print "GUICheck: Argument value read from ns: ", gVariables.ns.message2
                gVariables.logger.info( str( "GUICheck: Argument value read from ns: " + str(gVariables.ns.message2) ) )
            elif (index == 25):
                print "GUICheck: 'Variable to change: Movement Window Start' message"
                gVariables.logger.info( "GUICheck: 'Variable to change: Movement Window Start' message" )
                gVariables.fn_setMovementWindowStart( float(gVariables.ns.message2) )
                print "GUICheck: Argument value read from ns: ", gVariables.ns.message2
                gVariables.logger.info( str( "GUICheck: Argument value read from ns: " + str(gVariables.ns.message2) ) )
            elif (index == 26):
                print "GUICheck: 'Variable to change: Movement Window End' message"
                gVariables.logger.info( "GUICheck: 'Variable to change: Movement Window End' message" )
                gVariables.fn_setMovementWindowEnd( float(gVariables.ns.message2) )
                print "GUICheck: Argument value read from ns: ", gVariables.ns.message2
                gVariables.logger.info( str( "GUICheck: Argument value read from ns: " + str(gVariables.ns.message2) ) )
            elif (index == 27):
                print "GUICheck: 'Variable to change: Inter Trial Start' message"
                gVariables.logger.info( "GUICheck: 'Variable to change: Inter Trial Start' message" )
                gVariables.fn_setITRandom1( float(gVariables.ns.message2) )
                print "GUICheck: Argument value read from ns: ", gVariables.ns.message2
                gVariables.logger.info( str( "GUICheck: Argument value read from ns: " + str(gVariables.ns.message2) ) )
            elif (index == 28):
                print "GUICheck: 'Variable to change: Inter Trial End' message"
                gVariables.logger.info( "GUICheck: 'Variable to change: Inter Trial End' message" )
                gVariables.fn_setITRandom2( float(gVariables.ns.message2) )
                print "GUICheck: Argument value read from ns: ", gVariables.ns.message2
                gVariables.logger.info( str( "GUICheck: Argument value read from ns: " + str(gVariables.ns.message2) ) )
            elif (index == 29):
                print "GUICheck: 'Variable to change: Probability Tone One' message"
                gVariables.logger.info( "GUICheck: 'Variable to change: Probability Tone One' message" )
                gVariables.fn_toneOneProbabilitySet( float(gVariables.ns.message2) )
                print "GUICheck: Argument value read from ns: ", gVariables.ns.message2
                gVariables.logger.info( str( "GUICheck: Argument value read from ns: " + str(gVariables.ns.message2) ) )
            
            print "GUICheck: Reestablishing previous namespace: ", gVariables.ns
            gVariables.logger.info( str("GUICheck: Reestablishing previous namespace: "+ str(gVariables.ns)) )
            gVariables.ns.message1 = 0
            gVariables.ns.message2 = 0
            print "GUICheck: Namespace set: ", gVariables.ns
            gVariables.logger.info( str( "GUICheck: Namespace set: "+ str(gVariables.ns) ) )
            print "GUICheck: done."
            gVariables.logger.info( "GUICheck: done." )

def restartTraining():
        # Starts or restarts training.
        try:
            gVariables.start_time = timeit.default_timer()
            gVariables.current_trial_start_time = timeit.default_timer()
        except:
            gVariables.logger.info( 'Error generating "timeit" variables' )
            pass
        gVariables.current_trial_stage = 3
        gVariables.trialCount = 0
        gVariables.successTrialCount = 0
        gVariables.dropsAmountGivenManually = 0
        gVariables.logger.info('Variables set. Starting %s' % gVariables.trainingName)
        gVariables.trialStarted = True
        gVariables.trialExecuting = True
        print "Tone Training started."
        gVariables.logger.info( "Tone Training started." )
        a = "  %d seconds: tone" % gVariables.soundGenDuration1
        b = "  %d seconds: detection of movement" % (gVariables.eventTime2_movement - 
                                                                       gVariables.eventTime1_movement_start)
        c = "  (%r - %r) seconds: inter trial delay time" % (gVariables.interTrialRandom1Time ,
                                                                               gVariables.interTrialRandom2Time)
        print a
        print b
        print c
        gVariables.logger.info( a )
        gVariables.logger.info( b )
        gVariables.logger.info( c )
    
def stopTraining():
    #Stop
        gVariables.logger.info('%s stopped.' % gVariables.trainingName)
        gVariables.logger.info('Success rate: %s' % gVariables.successRate)
        gVariables.logger.info('Movement trials: %d / %d' % (gVariables.successMovementTrialCount, gVariables.movementTrialCount))
        gVariables.logger.info('Idle trials: %d / %d' % (gVariables.successIdleTrialCount, gVariables.idleTrialCount))
        gVariables.logger.info('Drops given manually: %r' % gVariables.dropsAmountGivenManually)
        gVariables.trialStarted = False
        gVariables.trialExecuting = False
        print "Tone Training stopped."
        gVariables.logger.info( "Tone Training stopped." )

def pauseTraining():
    gVariables.trialExecuting = False
    gVariables.current_trial_paused_time = timeit.default_timer()
    gVariables.logger.info('%s paused.' % gVariables.trainingName)
    print "Training paused."

def resumeTraining():
    gVariables.trialExecuting = True
    gVariables.current_trial_paused_time = (timeit.default_timer() - gVariables.current_trial_paused_time)
    print "Resuming training. Time that has been in pause: ", gVariables.current_trial_paused_time
    gVariables.logger.info('%s resumed.' % gVariables.trainingName)

def giveReward():
    if (gVariables.dropReleased == 0 and gVariables.trialExecuting == True):
            # print "Release drop of water."
            gVariables.valve1.drop()
            gVariables.logger.debug("Drop of water released.")
            gVariables.successTrialCount += 1
            gVariables.dropReleased = 1
            if (gVariables.current_trial_type == 1) :
                            gVariables.successMovementTrialCount += 1
            else:
                gVariables.successIdleTrialCount += 1

def getFormattedTime(a):
    #returns h m s correctly given the time in seconds, as argument
    try:
        hours = int (int(a) / 3600)  # hours
        minutes = int((int(a) - hours * 3600) / 60)  # minutes
        seconds = int(int(a) - hours * 3600 - minutes * 60)
        if hours > 0:
            hours = str(hours) + " h   "
            minutes = str(minutes) + " m   "
        else:
            hours = ""
            if (int(minutes) > 0):
                
                minutes = str(minutes) + " m   "
            else:
                minutes = ''  
        
        seconds = str(int(seconds)) + " s   " 
        return ( str(hours) + str(minutes) + str(seconds) )
    except:
        return str(a) + ' s   '

def userInputGUI(ns):
    #initialize user input GUI and associated variables.
    #this function uses trainingAPI to handle graphical user interfaces
    #ns = is the NameSpace associated with multiprocessing , contains the shared variables (message1 and 2)
    import userInterfaceAPI
    currentGUI = userInterfaceAPI.userInterface_API(False)
    currentGUI.setNamespace(ns)
    import config_training_two_tones as configs
    
    currentGUI.toneStart = 0.0
    currentGUI.toneEnd = configs.eventTime1_sound
    currentGUI.movementWindowStart = configs.eventTime1_movement_start
    currentGUI.movementWindowEnd = configs.eventTime2_movement
    currentGUI.interTrialStart = configs.interTrialRandom1Time
    currentGUI.interTrialEnd = configs.interTrialRandom2Time
    currentGUI.probabilityToneOne = configs.toneOneProbability
    currentGUI.frequencyTone1 = configs.soundGenFrequency1
    currentGUI.frequencyTone2 = configs.soundGenFrequency2
    
    currentGUI.movementAmount = configs.MOVEMENT_THRESHOLD_INITIAL_VALUE #sphereVideoDetection but readed from training config file
    currentGUI.movementMethod = configs.MOVEMENT_METHOD_INITIAL_VALUE #same as above
    currentGUI.movementTime = configs.movementTime
    currentGUI.idleTime = configs.idleTime
    currentGUI.comment = configs.initialComment
    
    currentGUI.usingTK = configs.usingTK
    
    time.sleep(1.0)
    
    currentGUI.launch_GUI()
    
def exitTraining():
    # Finalize this training and exits.
    print "Exiting."
    gVariables.logger.info('Exit signal.')
    gVariables.logger.info('Comment about this training: %s', gVariables.trial_comment)
    gVariables.GUIProcess.terminate()
    gVariables.display.exitDisplay()
    gVariables.videoDet.exit()
    sys.exit(0)

def trainingInit():
    print gVariables.trainingName
    # logging:
    formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    dateformat = '%Y/%m/%d %I:%M:%S %p'
    logging.basicConfig(filename='logs/%s_%s.log' % (gVariables.trainingName, time.strftime("%Y-%m-%d")),
                         filemode='a', level=logging.DEBUG, format=formatter, datefmt=dateformat)
    gVariables.logger = logging.getLogger('main')
    gVariables.logger.info('===============================================')
    gVariables.logger.info('Start %s' % gVariables.trainingName)
    # valve:
    import valve
    gVariables.valve1 = valve.Valve()
    gVariables.logger.info('Valve created.')
    # soundGen:
    import soundGen
    gVariables.s1 = soundGen.soundGen(gVariables.soundGenFrequency1, gVariables.soundGenDuration1)
    gVariables.s2 = soundGen.soundGen(gVariables.soundGenFrequency2, gVariables.soundGenDuration2)
    gVariables.trialExecuting = False  # boolean, if a 8 second with tone trial is wanted, this shoulb de set to 1
    gVariables.logger.info('Soundgen init started..')
    #GUI:
    import multiprocessing
    manager = multiprocessing.Manager()
    gVariables.ns = manager.Namespace()
    gVariables.ns.message1 = 0
    gVariables.ns.message2 = 0
    gVariables.GUIProcess = multiprocessing.Process(target=userInputGUI, args=(gVariables.ns,))
    gVariables.GUIProcess.start()
    gVariables.logger.info('GUI Process started.')
    #Sphere Video Detection:
    import sphereVideoDetection
    gVariables.videoDet = sphereVideoDetection.sphereVideoDetection(VIDEOSOURCE, CAM_WIDTH, CAM_HEIGHT)
    gVariables.videoDet.setMovementTimeWindow(gVariables.movementTime)  # seconds that should be moving.
    gVariables.videoMovementMethod =  gVariables.videoDet.getMovementMethod()
    gVariables.logger.info('sphereVideoDetection started.')
    #Display:
    initDisplay()
    #main Program Loop
    import threading
    gVariables.fred1 = threading.Thread(target=mainLoopFunction)
    gVariables.fred1.start()
    gVariables.logger.info('Training loop function started..')


if __name__ == '__main__':
    from configvideo import *
    ###############
    trainingInit()
    