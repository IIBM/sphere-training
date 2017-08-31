# -*- coding: utf-8 -*-

######################################################
# Training:
"""
    This training system creates two tones of different frequency.
    Each tone has one second of duration (adjustable). After the tone ends, there is a two second
    interval (also adjustable) where the subject must either move (first tone) or stand still (second
    tone).
    If the subject succeds in the task, gets a reward (drop of water).
    There is a certain probabilty of ocurrence for each tone. If one tone appears three
    time in a row, the other tone is fixed in the next trial. 
    The inter trial delay is random between 3 to 6 seconds (can be modified.) ><
    
"""
######################################################><

import os
import sys
import modulespath
import time
import timeit
import logging
import threading
import importlib
import track_bola_utils




def __checkConfigFiles():
                #checks if the config files needed for training exist. If not, it generates them.
                try:
                    import config_training as cfgtraining
                except ImportError:
                    print "File config_training.py not found. Generating a new copy..."
                    a = os.getcwd() + "/"
                    import shutil
                    shutil.copyfile(a+"config_training.py.example", a+"config_training.py")
                    import config_training as cfgtraining
                    print "config_training.py copied and imported successfully."
                    print ""
                    print "Note: To create a custom configuration file for a given subject, copy 'config_training.py' into SUBJNAME_config_training.py"
                    print ""
                except:
                    print "Error importing config_training."
                    os._exit(1)
                
                if 'config_training' in sys.modules:  
                    del(sys.modules["config_training"]) 
                pass
        
def __checkModules():
            def __checkOneModule(arg):
                #checks if the given module exists in the system.
                import imp
                try:
                    imp.find_module( str(arg) )
                    found = True
                except ImportError:
                    found = False
                if (found == False):
                    print "Module %r not found" % (str(arg))
                return found
            
            print "Checking modules."
            if (__checkOneModule("cv2")  == False):
                print "Exiting because of missing import: "+ "cv2"
                sys.exit(1)
                pass
            if (__checkOneModule("timeit")  == False):
                print "Exiting because of missing import: "+ "timeit"
                sys.exit(1)
                pass
            if (__checkOneModule("numpy")  == False):
                print "Exiting because of missing import: "+ "numpy"
                sys.exit(1)
                pass
            if (__checkOneModule("pygame")  == False):
                print "Exiting because of missing import: "+ "pygame"
                sys.exit(1)
                pass
            if (__checkOneModule("parallel")  == False):
                print "Warning: missing module: " + "parallel"
                pass
            if (__checkOneModule("Tkinter")  == False):
                print "Warning: missing module: " + "Tkinter"
                pass
            if (__checkOneModule("gtk")  == False):
                print "Warning: missing module: " + "gtk"
                print ""
                print ""
                print "If you are using default configurations, install gtk for python or change configuration variable usingTk to the value 1"
                print ""
                print ""
                pass
            pass
        
__checkModules()
__checkConfigFiles()

class Training():
    def __init__(self):
        self.trainingInit()
        pass
    
    class gVariables():
        #Global variables to be used within the Training class.
        #Contains global variables AND some training functions (internal to the Training class).
        
        @staticmethod
        def dummy_fn():
            #does nothing, used before as a testing function.
            print "testing"
        
        @staticmethod
        def fn_giveDrop():
                #print "giving drop"
                Training.gVariables.logger.debug('valve drop')
                Training.gVariables.valve1.drop()
                if (Training.gVariables.trialExecuting == True):
                    Training.gVariables.logger.info('Drop given manually - training started.')
                    Training.gVariables.dropsAmountGivenManually += 1
                else:
                    Training.gVariables.logger.info('Drop given manually - training not started.')
        
        @staticmethod
        def fn_savestate():
                #print "giving drop"
                Training.gVariables.logger.debug('save state')
                print "Saving all variables state."
                Training.gVariables.fn_internalSaveFileWithVars("configs/config_Pavlov.py", 1)
                Training.gVariables.fn_internalSaveFileWithVars("configs/config_Skinner.py", 2)
                Training.gVariables.fn_internalSaveFileWithVars("configs/config_Ocond.py", 3)
                Training.gVariables.fn_internalSaveFileWithVars("configs/config_Discr.py", 4)
                print "Done saving."
                pass
        
        @staticmethod
        def fn_internalSaveFileWithVars(nombr, num):
            
            if (num == 1):
                targetObj = Training.gVariables.pavlovVars
            if (num == 2):
                targetObj = Training.gVariables.skinnerVars
            if (num == 3):
                targetObj = Training.gVariables.ocondVars
            if (num == 4):
                targetObj = Training.gVariables.discrVars
            fileToSave = open(nombr, "w+");
            fileToSave.write("#%s\n" % time.asctime( time.localtime(time.time()) ) ) ;
            fileToSave.write("eventTime1_sound = %r\n" % targetObj.eventTime1_sound);
            fileToSave.write("eventTime1_movement_start = %r\n" % targetObj.eventTime1_movement_start);
            fileToSave.write("eventTime2_movement = %r\n" % targetObj.eventTime2_movement);
            fileToSave.write("eventTime3_trialEnd = %r\n" % targetObj.eventTime3_trialEnd);
            fileToSave.write("requireStillness = %r\n" % targetObj.requireStillness);
            fileToSave.write("interTrialRandom1Time = %r\n" % targetObj.interTrialRandom1Time);
            fileToSave.write("interTrialRandom2Time = %r\n" % targetObj.interTrialRandom2Time);
            fileToSave.write("movementTime = %r\n" % targetObj.movementTime);
            fileToSave.write("idleTime = %r\n" % targetObj.idleTime);
            fileToSave.write("soundGenDuration1 = %r\n" % targetObj.soundGenDuration1);
            fileToSave.write("soundGenDuration2 = %r\n" % targetObj.soundGenDuration2);
            fileToSave.write("soundGenFrequency1 = %r\n" % targetObj.soundGenFrequency1);
            fileToSave.write("soundGenFrequency2 = %r\n" % targetObj.soundGenFrequency2);
            fileToSave.write("toneOneProbability = %r\n" % targetObj.toneOneProbability);
        
        @staticmethod
        def fn_giveReward():
                #gives a drop of water and counts the trial as successful.
                Training.giveReward();
                if (Training.gVariables.trialExecuting == True):
                    Training.gVariables.logger.info('Reward given manually.')
                    Training.gVariables.dropsAmountGivenManually += 1
                else:
                    Training.gVariables.logger.info('Reward not given because training is not in execution.')
        
        @staticmethod
        def fn_closeValve():
                #Calls the valve object to close if opened.
                Training.gVariables.logger.info('valve closed manually')
                Training.gVariables.valve1.close()
        
        @staticmethod
        def fn_openValve():
            #Calls the valve object to open if closed.
            Training.gVariables.logger.info('valve opened manually')
            Training.gVariables.valve1.open()
        
        @staticmethod
        def fn_tone1Test(newfreq):
            #Tests the tone n°1
            #the argument is the new frequency (if it changed). FIrst updates freq variable then plays.
            beforefreq = Training.gVariables.soundGenFrequency1
            Training.gVariables.fn_setFrequencyT1(newfreq)
            Training.gVariables.logger.info('Changed Tone 1 Frequency to: %d Hz  (before was %d Hz)' % (Training.gVariables.soundGenFrequency1, beforefreq ) )
            Training.gVariables.s1.play()
        
        @staticmethod
        def fn_tone2Test(newfreq):
            #Tests the tone n°2
            #the argument is the new frequency (if it changed). FIrst updates freq then plays.
            beforefreq = Training.gVariables.soundGenFrequency2
            Training.gVariables.fn_setFrequencyT2(newfreq)
            Training.gVariables.logger.info('Changed Tone 2 Frequency to: %d Hz  (before was %d Hz)' % (Training.gVariables.soundGenFrequency2, beforefreq ) )
            Training.gVariables.s2.play()
        
        @staticmethod
        def fn_setMovementMethod(value_given):
            Training.gVariables.videoDet.setMovementMethod(value_given)
            print "Movement method set: ", value_given
            Training.gVariables.logger.info( "Movement method set: " + str(value_given) )
        
        @staticmethod
        def fn_movementThresholdSet(value_given):
            #aumentar threshold
            Training.gVariables.videoDet.setMovementThreshold(int(value_given) )
            print "Movement Threshold changed to : " + str(Training.gVariables.videoDet.getMovementThreshold())
            Training.gVariables.logger.info( "Movement Threshold changed to : " + str(Training.gVariables.videoDet.getMovementThreshold()) )
        
        @staticmethod
        def fn_toneOneProbabilitySet(value_given):
            #set Probability of the tone nr1 to value
            if (isinstance( value_given, float ) == False ):
                return;
            Training.gVariables.toneOneProbability = value_given
            print "Tone One Probabilty changed to : " + str(Training.gVariables.toneOneProbability * 100) + " %"
            Training.gVariables.logger.info( "Tone One Probabilty changed to : " + str(Training.gVariables.toneOneProbability * 100) + " %" )
        
        @staticmethod
        def fn_setITRandom1(value_given):
            Training.gVariables.interTrialRandom1Time = value_given
            print "Intertrial random 1 time set to : ", value_given
            Training.gVariables.logger.info( "Intertrial random 1 time set to : " + str(value_given) )
        
        @staticmethod
        def fn_setITRandom2(value_given):
            Training.gVariables.interTrialRandom2Time = value_given
            Training.gVariables.logger.info( "Intertrial random 2 time set to : " + str(value_given) )
        
        
        @staticmethod
        def fn_setMovementWindowStart(value_given):
            Training.gVariables.eventTime1_movement_start = value_given
            print "Movement window Start set to value: ", value_given
            Training.gVariables.logger.info( "Movement window Start set to value: " + str(value_given) )
        
        @staticmethod
        def fn_setMovementWindowEnd(value_given):
            Training.gVariables.eventTime2_movement = value_given
            print "Movement window End set to value: ", value_given
            Training.gVariables.logger.info( "Movement window End set to value: " + str(value_given) )
        
        @staticmethod
        def fn_setTone1Duration(value_given):
            if (value_given != Training.gVariables.soundGenDuration1):
                Training.gVariables.soundGenDuration1 = value_given
                Training.gVariables.fn_recreateTone1()
                
                print "Tone 1 Duration set to value: ", value_given
                Training.gVariables.logger.info( "Tone 1 Duration set to value: " + str(value_given) )
            else:
                print "Tone 1 Duration is already at value: ", value_given
                Training.gVariables.logger.info( "Tone 1 Duration is already at value: " + str(value_given) )
        
        @staticmethod
        def fn_setTone2Duration(value_given):
            if (value_given != Training.gVariables.soundGenDuration2):
                Training.gVariables.soundGenDuration2 = value_given
                Training.gVariables.fn_recreateTone2()
                
                print "Tone 2 Duration set to value: ", value_given
                Training.gVariables.logger.info( "Tone 2 Duration set to value: " + str(value_given) )
            else:
                print "Tone 2 Duration is already at value: ", value_given
                Training.gVariables.logger.info( "Tone 2 Duration is already at value: " + str(value_given) )
        
        @staticmethod
        def fn_setFrequencyT1(freq):
            if ( int(freq) != Training.gVariables.soundGenFrequency1):
                a = "setting frequency T1: " + str(freq)
                print a
                Training.gVariables.logger.info(a)
                Training.gVariables.soundGenFrequency1 = int(freq)
                Training.gVariables.s1.tone(Training.gVariables.soundGenDuration1, Training.gVariables.soundGenFrequency1)
                #Training.gVariables.s1 = soundGen.soundGen(Training.gVariables.soundGenFrequency1, Training.gVariables.soundGenDuration1)
            else:
                print "frequency for Tone 1 already set at ", freq
                Training.gVariables.logger.info("frequency for Tone 1 already set at " + str(freq) )
        
        @staticmethod
        def fn_setFrequencyT2(freq):
            if ( int(freq) != Training.gVariables.soundGenFrequency2):
                a = "setting frequency T2: " + str(freq)
                print a
                Training.gVariables.logger.info(a)
                Training.gVariables.soundGenFrequency2 = int(freq)
                Training.gVariables.s2.tone(Training.gVariables.soundGenDuration2, Training.gVariables.soundGenFrequency2)
                #Training.gVariables.s2 = soundGen.soundGen(Training.gVariables.soundGenFrequency2, Training.gVariables.soundGenDuration2)
            else:
                print "frequency for Tone 2 already set at ", freq
                Training.gVariables.logger.info("frequency for Tone 2 already set at " + str(freq) )
        
        @staticmethod
        def fn_recreateTone1():
            #Training.gVariables.s1 = soundGen.soundGen(Training.gVariables.soundGenFrequency1, Training.gVariables.soundGenDuration1)
            #recreating tone is too unstable. Better to configure tone
            Training.gVariables.s1.tone(Training.gVariables.soundGenDuration1, Training.gVariables.soundGenFrequency1)
            pass
        
        @staticmethod
        def fn_recreateTone2():
            #Training.gVariables.s2 = soundGen.soundGen(Training.gVariables.soundGenFrequency2, Training.gVariables.soundGenDuration2)
            #recreating tone is too unstable. Better to configure tone
            Training.gVariables.s2.tone(Training.gVariables.soundGenDuration2, Training.gVariables.soundGenFrequency2)
            pass
        
        @staticmethod
        def fn_movementTimeSet(nwmvnt):
            #set movement time
            movement_time = float(nwmvnt)
            Training.gVariables.movementTime = movement_time
            Training.gVariables.videoDet.setMovementTimeWindow(Training.gVariables.movementTime)
            a = "Movement Time changed to : " + str(Training.gVariables.movementTime * 1000) + " ms"
            print a
            Training.gVariables.logger.info( a )
        
        @staticmethod
        def fn_idleTimeSet(nwmvnt):
            #set idle time.
            idle_time = float(nwmvnt)
            Training.gVariables.idleTime = idle_time
            a = "Idle Time changed to : " + str(Training.gVariables.idleTime * 1000) + " ms"
            print a
            Training.gVariables.logger.info( a )
        
        @staticmethod
        def fn_calibrateNoiseFilteringOn():
            Training.gVariables.videoDet.setNoiseFiltering(True)
            Training.gVariables.videoDet.calibrateCircle()
            print "Calibrated. Noise Filtering is ON."
            Training.gVariables.logger.info( "Calibrated. Noise Filtering is ON." )
        
        @staticmethod
        def fn_calibrateNoiseFilteringOff():
            Training.gVariables.videoDet.setNoiseFiltering(False)
            Training.gVariables.videoDet.calibrateCircle()
            print "Calibrated. Noise Filtering is OFF."
            Training.gVariables.logger.info( "Calibrated. Noise Filtering is OFF." )
        
        @staticmethod
        def fn_startStopTraining(flag):
            #the flag comes from the API/GUICheck system.
            #However, it is best to check if the training has started probing our own variables
            #and override the flag information:
            if (Training.gVariables.trialStarted == False):
                #the trial is "startable"
                flg = 1
            else:
                #the trial has started, is stoppable.
                flg = 2
            
            if (flg == 1):
                Training.restartTraining()
            if (flg == 2):
                Training.stopTraining()
        
        @staticmethod
        def fn_pauseResumeTraining(flag):
            #the flag comes from the API/GUICheck system.
            #However, it is best to check if the training is resumable or pausable probing our own variables
            #and override the flag information:
            if (Training.gVariables.trialStarted == True):
                if (Training.gVariables.trialExecuting == True):
                    #trial started and executing, is pausable
                    Training.pauseTraining()
                else:
                    #trial started and NOT executing, is resumable
                    Training.resumeTraining()
            else:
                print "fn_pauseResumeTraining: \n   Trial has not been started and cannot be paused or resumed."
                Training.gVariables.logger.info( "fn_pauseResumeTraining: \n   Trial has not been started and cannot be paused or resumed." )
        
        @staticmethod
        def fn_showTrackingFeedback():
            Training.gVariables.videoDet.setTrackingFeedback(True)
            pass
        
        @staticmethod
        def fn_hideTrackingFeedback():
            Training.gVariables.videoDet.setTrackingFeedback(False)
            pass
        
        @staticmethod
        def fn_showUserFeedback():
            Training.gVariables.videoDet.setUserFeedback(True)
            
            pass
        
        @staticmethod
        def fn_hideUserFeedback():
            Training.gVariables.videoDet.setUserFeedback(False)
            pass
        
        @staticmethod
        def getFormattedTime(a):
            #returns h m s correctly, given the time in seconds as the argument
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
        
        class saveVariables():
            #each instance of this class will allocate variables associated with a type of training.
            #the instances are loaded on init, and when a user chooses a certain type of training,
            # it will load by default these variables associated with that type. To override, press save button.
            type_pavlov = 0;
            type_skinner = 0;
            type_ocond = 0;
            type_discr = 0;
            nothingToLoad = 0; #if 1, there is nothing to load from here (probably there isn't a config file)
            def __init__(self, numtype):
                try:
                    numParsed = int(numtype)
                except:
                    return 1;
                self.type_pavlov = 0;
                self.type_skinner = 0;
                self.type_ocond = 0;
                self.type_discr = 0;
                self.nothingToLoad = 0;
                import os, sys, inspect
                # use this if you want to include modules from a subfolder
                cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"configs")))
                if cmd_subfolder not in sys.path:
                            sys.path.insert(0, cmd_subfolder)
                            
                if (numParsed == 1):
                    #type pavlov.
                    type_pavlov = 1;
                    try:
                        #a = open("configs/config_Pavlov.cfg")
                        #print a.readlines()
                        
                        print "about to import."
                        
                        
                        import config_Pavlov as cfg
                        self.eventTime1_sound = cfg.eventTime1_sound
                        self.eventTime1_movement_start = cfg.eventTime1_movement_start
                        self.eventTime2_movement = cfg.eventTime2_movement
                        self.eventTime3_trialEnd = cfg.eventTime3_trialEnd
                        self.requireStillness = cfg.requireStillness
                        self.interTrialRandom1Time = cfg.interTrialRandom1Time
                        self.interTrialRandom2Time = cfg.interTrialRandom2Time
                        self.movementTime = cfg.movementTime
                        self.idleTime = cfg.idleTime
                        self.soundGenDuration1 = cfg.soundGenDuration1
                        self.soundGenDuration2 = cfg.soundGenDuration2
                        self.soundGenFrequency1 = cfg.soundGenFrequency1
                        self.soundGenFrequency2 = cfg.soundGenFrequency2
                        self.toneOneProbability = cfg.toneOneProbability
                        
                        print "done."
                        nothingToLoad = 0
                    except:
                        nothingToLoad = 1;
                        pass
                if (numParsed == 2):
                    #type skinner.
                    type_skinner = 1;
                    try:
                        #a = open("configs/config_Pavlov.cfg")
                        #print a.readlines()
                        
                        print "about to import."
                        
                        
                        import config_Skinner as cfg
                        
                        self.eventTime1_sound = cfg.eventTime1_sound
                        self.eventTime1_movement_start = cfg.eventTime1_movement_start
                        self.eventTime2_movement = cfg.eventTime2_movement
                        self.eventTime3_trialEnd = cfg.eventTime3_trialEnd
                        self.requireStillness = cfg.requireStillness
                        self.interTrialRandom1Time = cfg.interTrialRandom1Time
                        self.interTrialRandom2Time = cfg.interTrialRandom2Time
                        self.movementTime = cfg.movementTime
                        self.idleTime = cfg.idleTime
                        self.soundGenDuration1 = cfg.soundGenDuration1
                        self.soundGenDuration2 = cfg.soundGenDuration2
                        self.soundGenFrequency1 = cfg.soundGenFrequency1
                        self.soundGenFrequency2 = cfg.soundGenFrequency2
                        self.toneOneProbability = cfg.toneOneProbability
                        
                        print "done."
                        nothingToLoad = 0
                    except:
                        nothingToLoad = 1;
                        pass
                if (numParsed == 3):
                    #type ocond.
                    type_ocond = 1;
                    try:
                        #a = open("configs/config_Pavlov.cfg")
                        #print a.readlines()
                        
                        print "about to import."
                        
                        
                        import config_Ocond as cfg
                        
                        self.eventTime1_sound = cfg.eventTime1_sound
                        self.eventTime1_movement_start = cfg.eventTime1_movement_start
                        self.eventTime2_movement = cfg.eventTime2_movement
                        self.eventTime3_trialEnd = cfg.eventTime3_trialEnd
                        self.requireStillness = cfg.requireStillness
                        self.interTrialRandom1Time = cfg.interTrialRandom1Time
                        self.interTrialRandom2Time = cfg.interTrialRandom2Time
                        self.movementTime = cfg.movementTime
                        self.idleTime = cfg.idleTime
                        self.soundGenDuration1 = cfg.soundGenDuration1
                        self.soundGenDuration2 = cfg.soundGenDuration2
                        self.soundGenFrequency1 = cfg.soundGenFrequency1
                        self.soundGenFrequency2 = cfg.soundGenFrequency2
                        self.toneOneProbability = cfg.toneOneProbability
                        
                        print "done."
                        nothingToLoad = 0
                    except:
                        nothingToLoad = 1;
                        pass
                if (numParsed == 4):
                    #type discr.
                    type_discr = 1;
                    try:
                        #a = open("configs/config_Pavlov.cfg")
                        #print a.readlines()
                        
                        print "about to import."
                        
                        
                        import config_Discr as cfg
                        
                        self.eventTime1_sound = cfg.eventTime1_sound
                        self.eventTime1_movement_start = cfg.eventTime1_movement_start
                        self.eventTime2_movement = cfg.eventTime2_movement
                        self.eventTime3_trialEnd = cfg.eventTime3_trialEnd
                        self.requireStillness = cfg.requireStillness
                        self.interTrialRandom1Time = cfg.interTrialRandom1Time
                        self.interTrialRandom2Time = cfg.interTrialRandom2Time
                        self.movementTime = cfg.movementTime
                        self.idleTime = cfg.idleTime
                        self.soundGenDuration1 = cfg.soundGenDuration1
                        self.soundGenDuration2 = cfg.soundGenDuration2
                        self.soundGenFrequency1 = cfg.soundGenFrequency1
                        self.soundGenFrequency2 = cfg.soundGenFrequency2
                        self.toneOneProbability = cfg.toneOneProbability
                        
                        print "done."
                        nothingToLoad = 0
                    except:
                        nothingToLoad = 1;
                        pass
                
                if (nothingToLoad == 1):
                    import config_training as cfgtraining
                    #nothing to load. but as this hasn't loaded anything, its vars will be set to default vars
                    self.eventTime1_sound = cfgtraining.eventTime1_sound
                    self.eventTime1_movement_start = cfgtraining.eventTime1_movement_start
                    self.eventTime2_movement = cfgtraining.eventTime2_movement
                    self.eventTime3_trialEnd = cfgtraining.eventTime3_trialEnd
                    self.requireStillness = cfgtraining.requireStillness
                    self.interTrialRandom1Time = cfgtraining.interTrialRandom1Time
                    self.interTrialRandom2Time = cfgtraining.interTrialRandom2Time
                    self.movementTime = cfgtraining.movementTime
                    self.idleTime = cfgtraining.idleTime
                    self.soundGenDuration1 = cfgtraining.soundGenDuration1
                    self.soundGenDuration2 = cfgtraining.soundGenDuration2
                    self.soundGenFrequency1 = cfgtraining.soundGenFrequency1
                    self.soundGenFrequency2 = cfgtraining.soundGenFrequency2
                    self.toneOneProbability = cfgtraining.toneOneProbability
                    print "Couldn't read config file for this type. Setting default variables."
                pass
            
            @staticmethod
            def savePavlovVars():
                    print "savePavlovVars"
                    
                    Training.gVariables.pavlovVars.eventTime1_sound = Training.gVariables.eventTime1_sound
                    Training.gVariables.pavlovVars.eventTime1_movement_start = Training.gVariables.eventTime1_movement_start
                    Training.gVariables.pavlovVars.eventTime2_movement = Training.gVariables.eventTime2_movement
                    Training.gVariables.pavlovVars.eventTime3_trialEnd = Training.gVariables.eventTime3_trialEnd
                    Training.gVariables.pavlovVars.requireStillness = Training.gVariables.requireStillness
                    Training.gVariables.pavlovVars.interTrialRandom1Time = Training.gVariables.interTrialRandom1Time
                    Training.gVariables.pavlovVars.interTrialRandom2Time = Training.gVariables.interTrialRandom2Time
                    Training.gVariables.pavlovVars.movementTime = Training.gVariables.movementTime
                    Training.gVariables.pavlovVars.idleTime = Training.gVariables.idleTime
                    Training.gVariables.pavlovVars.soundGenDuration1 = Training.gVariables.soundGenDuration1
                    Training.gVariables.pavlovVars.soundGenDuration2 = Training.gVariables.soundGenDuration2
                    Training.gVariables.pavlovVars.soundGenFrequency1 = Training.gVariables.soundGenFrequency1
                    Training.gVariables.pavlovVars.soundGenFrequency2 = Training.gVariables.soundGenFrequency2
                    Training.gVariables.pavlovVars.toneOneProbability = Training.gVariables.toneOneProbability
                    
                    pass
            @staticmethod
            def saveSkinnerVars():
                    print "saveSkinnerVars"
                    
                    Training.gVariables.skinnerVars.eventTime1_sound = Training.gVariables.eventTime1_sound
                    Training.gVariables.skinnerVars.eventTime1_movement_start = Training.gVariables.eventTime1_movement_start
                    Training.gVariables.skinnerVars.eventTime2_movement = Training.gVariables.eventTime2_movement
                    Training.gVariables.skinnerVars.eventTime3_trialEnd = Training.gVariables.eventTime3_trialEnd
                    Training.gVariables.skinnerVars.requireStillness = Training.gVariables.requireStillness
                    Training.gVariables.skinnerVars.interTrialRandom1Time = Training.gVariables.interTrialRandom1Time
                    Training.gVariables.skinnerVars.interTrialRandom2Time = Training.gVariables.interTrialRandom2Time
                    Training.gVariables.skinnerVars.movementTime = Training.gVariables.movementTime
                    Training.gVariables.skinnerVars.idleTime = Training.gVariables.idleTime
                    Training.gVariables.skinnerVars.soundGenDuration1 = Training.gVariables.soundGenDuration1
                    Training.gVariables.skinnerVars.soundGenDuration2 = Training.gVariables.soundGenDuration2
                    Training.gVariables.skinnerVars.soundGenFrequency1 = Training.gVariables.soundGenFrequency1
                    Training.gVariables.skinnerVars.soundGenFrequency2 = Training.gVariables.soundGenFrequency2
                    Training.gVariables.skinnerVars.toneOneProbability = Training.gVariables.toneOneProbability
                    
                    pass
            
            @staticmethod
            def saveOcondVars():
                    print "saveOcondVars"
                    
                    Training.gVariables.ocondVars.eventTime1_sound = Training.gVariables.eventTime1_sound
                    Training.gVariables.ocondVars.eventTime1_movement_start = Training.gVariables.eventTime1_movement_start
                    Training.gVariables.ocondVars.eventTime2_movement = Training.gVariables.eventTime2_movement
                    Training.gVariables.ocondVars.eventTime3_trialEnd = Training.gVariables.eventTime3_trialEnd
                    Training.gVariables.ocondVars.requireStillness = Training.gVariables.requireStillness
                    Training.gVariables.ocondVars.interTrialRandom1Time = Training.gVariables.interTrialRandom1Time
                    Training.gVariables.ocondVars.interTrialRandom2Time = Training.gVariables.interTrialRandom2Time
                    Training.gVariables.ocondVars.movementTime = Training.gVariables.movementTime
                    Training.gVariables.ocondVars.idleTime = Training.gVariables.idleTime
                    Training.gVariables.ocondVars.soundGenDuration1 = Training.gVariables.soundGenDuration1
                    Training.gVariables.ocondVars.soundGenDuration2 = Training.gVariables.soundGenDuration2
                    Training.gVariables.ocondVars.soundGenFrequency1 = Training.gVariables.soundGenFrequency1
                    Training.gVariables.ocondVars.soundGenFrequency2 = Training.gVariables.soundGenFrequency2
                    Training.gVariables.ocondVars.toneOneProbability = Training.gVariables.toneOneProbability
                    
                    pass
            
            @staticmethod
            def saveDiscrVars():
                    print "saveDiscrVars"
                    
                    Training.gVariables.discrVars.eventTime1_sound = Training.gVariables.eventTime1_sound
                    Training.gVariables.discrVars.eventTime1_movement_start = Training.gVariables.eventTime1_movement_start
                    Training.gVariables.discrVars.eventTime2_movement = Training.gVariables.eventTime2_movement
                    Training.gVariables.discrVars.eventTime3_trialEnd = Training.gVariables.eventTime3_trialEnd
                    Training.gVariables.discrVars.requireStillness = Training.gVariables.requireStillness
                    Training.gVariables.discrVars.interTrialRandom1Time = Training.gVariables.interTrialRandom1Time
                    Training.gVariables.discrVars.interTrialRandom2Time = Training.gVariables.interTrialRandom2Time
                    Training.gVariables.discrVars.movementTime = Training.gVariables.movementTime
                    Training.gVariables.discrVars.idleTime = Training.gVariables.idleTime
                    Training.gVariables.discrVars.soundGenDuration1 = Training.gVariables.soundGenDuration1
                    Training.gVariables.discrVars.soundGenDuration2 = Training.gVariables.soundGenDuration2
                    Training.gVariables.discrVars.soundGenFrequency1 = Training.gVariables.soundGenFrequency1
                    Training.gVariables.discrVars.soundGenFrequency2 = Training.gVariables.soundGenFrequency2
                    Training.gVariables.discrVars.toneOneProbability = Training.gVariables.toneOneProbability
                    
                    pass
            
                        
            @staticmethod
            def loadPavlovVars():
                    print "loadPavlovVars"
                    
                    Training.gVariables.eventTime1_sound = Training.gVariables.pavlovVars.eventTime1_sound
                    Training.gVariables.eventTime1_movement_start = Training.gVariables.pavlovVars.eventTime1_movement_start
                    Training.gVariables.eventTime2_movement = Training.gVariables.pavlovVars.eventTime2_movement
                    Training.gVariables.eventTime3_trialEnd = Training.gVariables.pavlovVars.eventTime3_trialEnd
                    Training.gVariables.requireStillness = Training.gVariables.pavlovVars.requireStillness
                    Training.gVariables.interTrialRandom1Time = Training.gVariables.pavlovVars.interTrialRandom1Time
                    Training.gVariables.interTrialRandom2Time = Training.gVariables.pavlovVars.interTrialRandom2Time
                    Training.gVariables.movementTime = Training.gVariables.pavlovVars.movementTime
                    Training.gVariables.idleTime = Training.gVariables.pavlovVars.idleTime
                    #Training.gVariables.soundGenDuration1 = Training.gVariables.pavlovVars.soundGenDuration1
                    #fn_setTone1Duration
                    Training.gVariables.fn_setTone1Duration(Training.gVariables.pavlovVars.soundGenDuration1)
                    #fn_setTone2Duration
                    #Training.gVariables.soundGenDuration2 = Training.gVariables.pavlovVars.soundGenDuration2
                    Training.gVariables.fn_setTone2Duration(Training.gVariables.pavlovVars.soundGenDuration2)
                    ##
                    Training.gVariables.fn_setFrequencyT1(Training.gVariables.pavlovVars.soundGenFrequency1)
                    #Training.gVariables.soundGenFrequency1 = Training.gVariables.pavlovVars.soundGenFrequency1
                    Training.gVariables.fn_setFrequencyT2(Training.gVariables.pavlovVars.soundGenFrequency2)
                    #Training.gVariables.soundGenFrequency2 = Training.gVariables.pavlovVars.soundGenFrequency2
                    Training.gVariables.toneOneProbability = Training.gVariables.pavlovVars.toneOneProbability
                    
                    
                    
                    
                    pass
            @staticmethod
            def loadSkinnerVars():
                    print "loadSkinnerVars"
                    
                    Training.gVariables.eventTime1_sound = Training.gVariables.skinnerVars.eventTime1_sound
                    Training.gVariables.eventTime1_movement_start = Training.gVariables.skinnerVars.eventTime1_movement_start
                    Training.gVariables.eventTime2_movement = Training.gVariables.skinnerVars.eventTime2_movement
                    Training.gVariables.eventTime3_trialEnd = Training.gVariables.skinnerVars.eventTime3_trialEnd
                    Training.gVariables.requireStillness = Training.gVariables.skinnerVars.requireStillness
                    Training.gVariables.interTrialRandom1Time = Training.gVariables.skinnerVars.interTrialRandom1Time
                    Training.gVariables.interTrialRandom2Time = Training.gVariables.skinnerVars.interTrialRandom2Time
                    Training.gVariables.movementTime = Training.gVariables.skinnerVars.movementTime
                    Training.gVariables.idleTime = Training.gVariables.skinnerVars.idleTime
                    #Training.gVariables.soundGenDuration1 = Training.gVariables.skinnerVars.soundGenDuration1
                    #fn_setTone1Duration
                    Training.gVariables.fn_setTone1Duration(Training.gVariables.skinnerVars.soundGenDuration1)
                    #fn_setTone2Duration
                    #Training.gVariables.soundGenDuration2 = Training.gVariables.skinnerVars.soundGenDuration2
                    Training.gVariables.fn_setTone2Duration(Training.gVariables.skinnerVars.soundGenDuration2)
                    ##
                    Training.gVariables.fn_setFrequencyT1(Training.gVariables.skinnerVars.soundGenFrequency1)
                    #Training.gVariables.soundGenFrequency1 = Training.gVariables.skinnerVars.soundGenFrequency1
                    Training.gVariables.fn_setFrequencyT2(Training.gVariables.skinnerVars.soundGenFrequency2)
                    #Training.gVariables.soundGenFrequency2 = Training.gVariables.skinnerVars.soundGenFrequency2
                    Training.gVariables.toneOneProbability = Training.gVariables.skinnerVars.toneOneProbability
                    
                    pass
            
            @staticmethod
            def loadOcondVars():
                    print "loadOcondVars"
                    
                    Training.gVariables.eventTime1_sound = Training.gVariables.ocondVars.eventTime1_sound
                    Training.gVariables.eventTime1_movement_start = Training.gVariables.ocondVars.eventTime1_movement_start
                    Training.gVariables.eventTime2_movement = Training.gVariables.ocondVars.eventTime2_movement
                    Training.gVariables.eventTime3_trialEnd = Training.gVariables.ocondVars.eventTime3_trialEnd
                    Training.gVariables.requireStillness = Training.gVariables.ocondVars.requireStillness
                    Training.gVariables.interTrialRandom1Time = Training.gVariables.ocondVars.interTrialRandom1Time
                    Training.gVariables.interTrialRandom2Time = Training.gVariables.ocondVars.interTrialRandom2Time
                    Training.gVariables.movementTime = Training.gVariables.ocondVars.movementTime
                    Training.gVariables.idleTime = Training.gVariables.ocondVars.idleTime
                    #Training.gVariables.soundGenDuration1 = Training.gVariables.ocondVars.soundGenDuration1
                    #fn_setTone1Duration
                    Training.gVariables.fn_setTone1Duration(Training.gVariables.ocondVars.soundGenDuration1)
                    #fn_setTone2Duration
                    #Training.gVariables.soundGenDuration2 = Training.gVariables.ocondVars.soundGenDuration2
                    Training.gVariables.fn_setTone2Duration(Training.gVariables.ocondVars.soundGenDuration2)
                    ##
                    Training.gVariables.fn_setFrequencyT1(Training.gVariables.ocondVars.soundGenFrequency1)
                    #Training.gVariables.soundGenFrequency1 = Training.gVariables.ocondVars.soundGenFrequency1
                    Training.gVariables.fn_setFrequencyT2(Training.gVariables.ocondVars.soundGenFrequency2)
                    #Training.gVariables.soundGenFrequency2 = Training.gVariables.ocondVars.soundGenFrequency2
                    Training.gVariables.toneOneProbability = Training.gVariables.ocondVars.toneOneProbability
                    
                    pass
            
            @staticmethod
            def loadDiscrVars():
                    print "loadDiscrVars"
                    
                    Training.gVariables.eventTime1_sound = Training.gVariables.discrVars.eventTime1_sound
                    Training.gVariables.eventTime1_movement_start = Training.gVariables.discrVars.eventTime1_movement_start
                    Training.gVariables.eventTime2_movement = Training.gVariables.discrVars.eventTime2_movement
                    Training.gVariables.eventTime3_trialEnd = Training.gVariables.discrVars.eventTime3_trialEnd
                    Training.gVariables.requireStillness = Training.gVariables.discrVars.requireStillness
                    Training.gVariables.interTrialRandom1Time = Training.gVariables.discrVars.interTrialRandom1Time
                    Training.gVariables.interTrialRandom2Time = Training.gVariables.discrVars.interTrialRandom2Time
                    Training.gVariables.movementTime = Training.gVariables.discrVars.movementTime
                    Training.gVariables.idleTime = Training.gVariables.discrVars.idleTime
                    #Training.gVariables.soundGenDuration1 = Training.gVariables.discrVars.soundGenDuration1
                    #fn_setTone1Duration
                    Training.gVariables.fn_setTone1Duration(Training.gVariables.discrVars.soundGenDuration1)
                    #fn_setTone2Duration
                    #Training.gVariables.soundGenDuration2 = Training.gVariables.discrVars.soundGenDuration2
                    Training.gVariables.fn_setTone2Duration(Training.gVariables.discrVars.soundGenDuration2)
                    ##
                    Training.gVariables.fn_setFrequencyT1(Training.gVariables.discrVars.soundGenFrequency1)
                    #Training.gVariables.soundGenFrequency1 = Training.gVariables.discrVars.soundGenFrequency1
                    Training.gVariables.fn_setFrequencyT2(Training.gVariables.discrVars.soundGenFrequency2)
                    #Training.gVariables.soundGenFrequency2 = Training.gVariables.discrVars.soundGenFrequency2
                    Training.gVariables.toneOneProbability = Training.gVariables.discrVars.toneOneProbability
                    
                    pass
            
            
            
            
            @staticmethod
            def loadIntoAPIPavlovVars():
                    print "loadIntoAPIPavlovVars"
                    objc = Training.gVariables.currentGUI.pavlovVars
                    objc.toneStart = 0;
                    objc.toneEnd = Training.gVariables.pavlovVars.eventTime1_sound;
                    objc.movementWindowStart = Training.gVariables.pavlovVars.eventTime1_movement_start;
                    objc.movementWindowEnd = Training.gVariables.pavlovVars.eventTime2_movement;
                    objc.interTrialStart = Training.gVariables.pavlovVars.interTrialRandom1Time;
                    objc.interTrialEnd = Training.gVariables.pavlovVars.interTrialRandom2Time;
                    objc.probabilityToneOne = Training.gVariables.pavlovVars.toneOneProbability;
                    objc.frequencyTone1 = Training.gVariables.pavlovVars.soundGenFrequency1;
                    objc.frequencyTone2 = Training.gVariables.pavlovVars.soundGenFrequency2;
                    
                    #objc.movementAmount = Training.gVariables.pavlovVars.?¡??????
                    #objc.movementMethod = Training.gVariables.pavlovVars.??????????????????????????'
                    objc.movementTime = Training.gVariables.pavlovVars.movementTime;
                    objc.idleTime = Training.gVariables.pavlovVars.idleTime;
                    objc.requireStillnessVar = Training.gVariables.pavlovVars.requireStillness;
                    
                    
                    
                    pass
            @staticmethod
            def loadIntoAPISkinnerVars():
                    print "loadIntoAPISkinnerVars"
                    objc = Training.gVariables.currentGUI.skinnerVars
                    objc.toneStart = 0;
                    objc.toneEnd = Training.gVariables.skinnerVars.eventTime1_sound;
                    objc.movementWindowStart = Training.gVariables.skinnerVars.eventTime1_movement_start;
                    objc.movementWindowEnd = Training.gVariables.skinnerVars.eventTime2_movement;
                    objc.interTrialStart = Training.gVariables.skinnerVars.interTrialRandom1Time;
                    objc.interTrialEnd = Training.gVariables.skinnerVars.interTrialRandom2Time;
                    objc.probabilityToneOne = Training.gVariables.skinnerVars.toneOneProbability;
                    objc.frequencyTone1 = Training.gVariables.skinnerVars.soundGenFrequency1;
                    objc.frequencyTone2 = Training.gVariables.skinnerVars.soundGenFrequency2;
                    
                    #objc.movementAmount = Training.gVariables.skinnerVars.?¡??????
                    #objc.movementMethod = Training.gVariables.skinnerVars.??????????????????????????'
                    objc.movementTime = Training.gVariables.skinnerVars.movementTime;
                    objc.idleTime = Training.gVariables.skinnerVars.idleTime;
                    objc.requireStillnessVar = Training.gVariables.skinnerVars.requireStillness;
                    
                    pass
            
            @staticmethod
            def loadIntoAPIOcondVars():
                    print "loadIntoAPIOcondVars"
                    objc = Training.gVariables.currentGUI.ocondVars
                    objc.toneStart = 0;
                    objc.toneEnd = Training.gVariables.ocondVars.eventTime1_sound;
                    objc.movementWindowStart = Training.gVariables.ocondVars.eventTime1_movement_start;
                    objc.movementWindowEnd = Training.gVariables.ocondVars.eventTime2_movement;
                    objc.interTrialStart = Training.gVariables.ocondVars.interTrialRandom1Time;
                    objc.interTrialEnd = Training.gVariables.ocondVars.interTrialRandom2Time;
                    objc.probabilityToneOne = Training.gVariables.ocondVars.toneOneProbability;
                    objc.frequencyTone1 = Training.gVariables.ocondVars.soundGenFrequency1;
                    objc.frequencyTone2 = Training.gVariables.ocondVars.soundGenFrequency2;
                    
                    #objc.movementAmount = Training.gVariables.ocondVars.?¡??????
                    #objc.movementMethod = Training.gVariables.ocondVars.??????????????????????????'
                    objc.movementTime = Training.gVariables.ocondVars.movementTime;
                    objc.idleTime = Training.gVariables.ocondVars.idleTime;
                    objc.requireStillnessVar = Training.gVariables.ocondVars.requireStillness;
                    
                    pass
            
            @staticmethod
            def loadIntoAPIDiscrVars():
                    print "loadIntoAPIDiscrVars"
                    objc = Training.gVariables.currentGUI.discrVars
                    objc.toneStart = 0;
                    objc.toneEnd = Training.gVariables.discrVars.eventTime1_sound;
                    objc.movementWindowStart = Training.gVariables.discrVars.eventTime1_movement_start;
                    objc.movementWindowEnd = Training.gVariables.discrVars.eventTime2_movement;
                    objc.interTrialStart = Training.gVariables.discrVars.interTrialRandom1Time;
                    objc.interTrialEnd = Training.gVariables.discrVars.interTrialRandom2Time;
                    objc.probabilityToneOne = Training.gVariables.discrVars.toneOneProbability;
                    objc.frequencyTone1 = Training.gVariables.discrVars.soundGenFrequency1;
                    objc.frequencyTone2 = Training.gVariables.discrVars.soundGenFrequency2;
                    
                    #objc.movementAmount = Training.gVariables.discrVars.?¡??????
                    #objc.movementMethod = Training.gVariables.discrVars.??????????????????????????'
                    objc.movementTime = Training.gVariables.discrVars.movementTime;
                    objc.idleTime = Training.gVariables.discrVars.idleTime;
                    objc.requireStillnessVar = Training.gVariables.discrVars.requireStillness;
                    
                    pass
            
            
            
        pass
        
        
        import config_training as cfgtraining
        trainingName = cfgtraining.trainingName
        # relevant Training variables
        eventTime1_sound = cfgtraining.eventTime1_sound  # in seconds. Instant of time when the soundGen ends.
        eventTime1_movement_start = cfgtraining.eventTime1_movement_start  # in seconds. Instant of time when the movement starts to be considered
        eventTime2_movement = cfgtraining.eventTime2_movement  # in seconds. Instant of time when movement ceases to be considered for reward
        eventTime3_trialEnd = cfgtraining.eventTime3_trialEnd  # in seconds. Instant of time when the trial ends.
        minIdleIntertrialTime = cfgtraining.minIdleIntertrialTime  # no-movement time in seconds before the start of next trial. If not reached this time with no movement, trial doesn't start
        
        requireStillness = cfgtraining.requireStillness # require to stay idle to end trial and start next one.
        numberOfRewardDrops = cfgtraining.numberOfRewardDrops #number of drops to give as reward when trial successful
        numberOfRewardDropsIdle = cfgtraining.numberOfRewardDropsIdle #number of drops to give as reward when trial successful
        
        interTrialRandom1Time = cfgtraining.interTrialRandom1Time  # intertrial time is random between this value and the random2 value
        interTrialRandom2Time = cfgtraining.interTrialRandom2Time  # intertrial time is random between previous value and this value. This
        # is also the max duration of a trial.
        
        #maxMovementTime = cfgtraining.maxMovementTime  # max amount of movement time (10 means 1000 ms) to give reward. SHould be less than the opportunity duration
        movementTime = cfgtraining.movementTime  # continuous moving time that should be reached to give reward. 0.5 = 500 ms
        # ex.: movementTime = 0.5 means that there should be movement detected over 500 ms at least
        idleTime = cfgtraining.idleTime  # continuous idle time that should be reached to give reward. 10= 1000 ms
        
        soundGenDuration1 = cfgtraining.soundGenDuration1
        soundGenDuration2 = cfgtraining.soundGenDuration2
        soundGenFrequency1 = cfgtraining.soundGenFrequency1  # in Hz
        soundGenFrequency2 = cfgtraining.soundGenFrequency2  # in Hz
        
        trialCount = 0  # total number of trials
        movementTrialCount = 0  # total number of trials of the type "Move" (which requires the subject to move)
        idleTrialCount = 0  # total number of trials of the type "Idle" (which requires the subject to stay idle.)
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
        
        #GUI Type:
        GUIType = cfgtraining.usingTK
        multiProcSubjectNameQuery = cfgtraining.multiProcSubjectNameQuery
        currentGUI = None #user Interface API object.
        current_mode=""
        
        # video Detection:
        videoDet = 0  # video Detection object. initialized in the main.
        videoSecond = -1 # second camera object
        
        videoMovementMethod = -1 #movement method to be used for movement analysis.
        
        absolute_start_time = timeit.default_timer()  # time when training started.
        start_time = timeit.default_timer()  # time when training with tone started.
        current_trial_start_time = timeit.default_timer()  # current trial in execution, absolute time it started
        current_trial_time = timeit.default_timer()  # second of the current trial (between 0 and the maximum length of a trial)
        current_trial_paused_time = 0  # to handle pause and resume correctly..
        
        current_trial_stage = 0  # 0: tone, 1: movement detection, 2: inter-trial, 3: instant before changing to 0
        
        toneOneProbability = cfgtraining.toneOneProbability
        history_trial = [1, 2, 1, 2, 1, 2]
        current_trial_type = 0  # 1: for tone one, reward after movement 2: for tone two, reward after standing still
        current_trial_type_str = ""  # same as type but with string format.
        
        trial_comment = "" #comment about this training session.
        
        override_training_types = 0; #if 1, all training types configs will be ommited.
        type_pavlov = cfgtraining.type_pavlov;
        type_skinner = cfgtraining.type_skinner;
        type_ocond = cfgtraining.type_ocond;
        type_discr = cfgtraining.type_discr;
        
        if (type_pavlov == 1 and type_skinner == 1):
            print "Warning! Both Pavlov and Skinner mode are enabled. This training instance will use Pavlov mode only."
            type_skinner = 0;
        
        pavlovVars = saveVariables(1)
        
        skinnerVars = saveVariables(2)
        
        ocondVars = saveVariables(3)
        
        discrVars = saveVariables(4)
        
        subject_name = "" #subject name, set at training init, used in logging filename.
        programRunning = 1;
        #print soundGenFrequency1
        #print pavlovVars.soundGenFrequency1
        
        if type_pavlov == 1:
            #get training variables from pavlovVars object.
            if pavlovVars.nothingToLoad == 0:
                #grabbing vars from object
                eventTime1_sound = pavlovVars.eventTime1_sound
                eventTime1_movement_start = pavlovVars.eventTime1_movement_start
                eventTime2_movement = pavlovVars.eventTime2_movement
                eventTime3_trialEnd = pavlovVars.eventTime3_trialEnd
                requireStillness = pavlovVars.requireStillness
                interTrialRandom1Time = pavlovVars.interTrialRandom1Time
                interTrialRandom2Time = pavlovVars.interTrialRandom2Time
                movementTime = pavlovVars.movementTime
                idleTime = pavlovVars.idleTime
                soundGenDuration1 = pavlovVars.soundGenDuration1
                soundGenDuration2 = pavlovVars.soundGenDuration2
                soundGenFrequency1 = pavlovVars.soundGenFrequency1
                soundGenFrequency2 = pavlovVars.soundGenFrequency2
                toneOneProbability = pavlovVars.toneOneProbability
                current_mode = "pavlov"
                print "grabbed from pavlovVars."
                pass
            pass
        elif type_skinner == 1:
            #get training variables ffrom skinnerVars object..
            if skinnerVars.nothingToLoad == 0:
                #grabbing vars from object
                eventTime1_sound = skinnerVars.eventTime1_sound
                eventTime1_movement_start = skinnerVars.eventTime1_movement_start
                eventTime2_movement = skinnerVars.eventTime2_movement
                eventTime3_trialEnd = skinnerVars.eventTime3_trialEnd
                requireStillness = skinnerVars.requireStillness
                interTrialRandom1Time = skinnerVars.interTrialRandom1Time
                interTrialRandom2Time = skinnerVars.interTrialRandom2Time
                movementTime = skinnerVars.movementTime
                idleTime = skinnerVars.idleTime
                soundGenDuration1 = skinnerVars.soundGenDuration1
                soundGenDuration2 = skinnerVars.soundGenDuration2
                soundGenFrequency1 = skinnerVars.soundGenFrequency1
                soundGenFrequency2 = skinnerVars.soundGenFrequency2
                toneOneProbability = skinnerVars.toneOneProbability
                current_mode = "skinner"
                print "grabbed from skinnerVars."
                pass
                pass
            pass
        elif type_ocond == 1:
            if ocondVars.nothingToLoad == 0:
                #grabbing vars from object
                eventTime1_sound = ocondVars.eventTime1_sound
                eventTime1_movement_start = ocondVars.eventTime1_movement_start
                eventTime2_movement = ocondVars.eventTime2_movement
                eventTime3_trialEnd = ocondVars.eventTime3_trialEnd
                requireStillness = ocondVars.requireStillness
                interTrialRandom1Time = ocondVars.interTrialRandom1Time
                interTrialRandom2Time = ocondVars.interTrialRandom2Time
                movementTime = ocondVars.movementTime
                idleTime = ocondVars.idleTime
                soundGenDuration1 = ocondVars.soundGenDuration1
                soundGenDuration2 = ocondVars.soundGenDuration2
                soundGenFrequency1 = ocondVars.soundGenFrequency1
                soundGenFrequency2 = ocondVars.soundGenFrequency2
                toneOneProbability = ocondVars.toneOneProbability
                current_mode = "oc"
                print "grabbed from ocondVars."
                pass
            pass
        elif type_discr == 1:
            if discrVars.nothingToLoad == 0:
                #grabbing vars from object
                eventTime1_sound = discrVars.eventTime1_sound
                eventTime1_movement_start = discrVars.eventTime1_movement_start
                eventTime2_movement = discrVars.eventTime2_movement
                eventTime3_trialEnd = discrVars.eventTime3_trialEnd
                requireStillness = discrVars.requireStillness
                interTrialRandom1Time = discrVars.interTrialRandom1Time
                interTrialRandom2Time = discrVars.interTrialRandom2Time
                movementTime = discrVars.movementTime
                idleTime = discrVars.idleTime
                soundGenDuration1 = discrVars.soundGenDuration1
                soundGenDuration2 = discrVars.soundGenDuration2
                soundGenFrequency1 = discrVars.soundGenFrequency1
                soundGenFrequency2 = discrVars.soundGenFrequency2
                toneOneProbability = discrVars.toneOneProbability
                current_mode = "discr"
                print "grabbed from discrVars."
                pass
            pass
        #fin Training.gVariables.
        pass

    def initDisplay(self):
        import trainingDisplay  # display for showing different variables of interest
        Training.gVariables.display = trainingDisplay.trainingDisplay("Training variables for: " + self.gVariables.subject_name)
        Training.gVariables.display.addImportantInfo(("Trials", 0))
        Training.gVariables.display.addImportantInfo(("Successful Trials", 0))
        Training.gVariables.display.addImportantInfo(("Successful Trials mvnt", 0))
        Training.gVariables.display.addImportantInfo(("Successful Trials idle", 0))
        Training.gVariables.display.addImportantInfo(("Time", 0))
        Training.gVariables.display.addSecondaryInfo(("% s/t", 0.0))
        Training.gVariables.display.addSecondaryInfo(("Trial Time", "0 - 10"))
        Training.gVariables.display.addSecondaryInfo(("Trial status", ""))
        time.sleep(0.5)
        Training.gVariables.display.renderAgain()
    
    @staticmethod
    def internal_updateDisplayInfoWithSleep(argument1, argument2):
        Training.gVariables.display.updateInfo(argument1, argument2)
        pass
    
    @staticmethod
    def updateDisplayInfo():
        if (Training.gVariables.trialExecuting == True):
                UpdList = []
                now = timeit.default_timer()
                b = Training.gVariables.getFormattedTime(int(now - Training.gVariables.start_time))
                #Training.gVariables.display.updateInfo("Time", b)
                UpdList.append(("Time", b))
                if (Training.gVariables.current_trial_type == 1):
                    sttrial = "move"
                elif (Training.gVariables.current_trial_type == 2):
                    sttrial = "still"
                else:
                    sttrial = ""
                Training.gVariables.current_trial_type_str = sttrial
                if (Training.gVariables.current_trial_time < Training.gVariables.eventTime2_movement):
                    #Training.gVariables.display.updateInfo("Trial status", sttrial + " - " + "running")
                    UpdList.append( ("Trial status", sttrial + " - " + "running") )
                else:
                    if Training.gVariables.dropReleased == 1:
                        #Training.gVariables.display.updateInfo("Trial status", sttrial + " - " + "SUCCESS")
                        UpdList.append( ("Trial status", sttrial + " - " + "SUCCESS") )
                    else:
                        #Training.gVariables.display.updateInfo("Trial status", sttrial + " - " + "FAIL")
                        UpdList.append( ("Trial status", sttrial + " - " + "FAIL") )
                #Training.gVariables.display.updateInfo("Trials", Training.gVariables.trialCount)
                UpdList.append( ("Trials", Training.gVariables.trialCount) )
                #Training.gVariables.display.updateInfo("Successful Trials", Training.gVariables.successTrialCount)
                UpdList.append( ("Successful Trials", Training.gVariables.successTrialCount) )
                # stmvnt = str(Training.gVariables.successMovementTrialCount) + " / " + str(Training.gVariables.movementTrialCount )
                # stidle = str(Training.gVariables.successIdleTrialCount) + " / " + str(Training.gVariables.idleTrialCount )
                
                
                if (Training.gVariables.trialCount > 0):
                                if (Training.gVariables.movementTrialCount > 0):
                                    temp1 = (1.0 * Training.gVariables.successMovementTrialCount / Training.gVariables.movementTrialCount)
                                    tempH1 = temp1 * 100.0
                                    tempString1 = str(tempH1)
                                    if (len(tempString1) > 3):
                                        tempS1 = str(tempH1)[:4]
                                    else:
                                        tempS1 = str(tempH1)[:3]
                                    #Training.gVariables.display.updateInfo("Successful Trials mvnt", tempS1)
                                    UpdList.append( ("Successful Trials mvnt", tempS1) )
                                else:
                                    #Training.gVariables.display.updateInfo("Successful Trials mvnt", "0.0")
                                    UpdList.append( ("Successful Trials mvnt", "0.0") )
                                
                                if (Training.gVariables.idleTrialCount > 0):
                                    temp2 = (1.0 * Training.gVariables.successIdleTrialCount / Training.gVariables.idleTrialCount)
                                    tempH2 = temp2 * 100.0
                                    tempString2 = str(tempH2)
                                    if (len(tempString2) > 3):
                                         tempS2 = str(tempH2)[:4]
                                    else:
                                         tempS2 = str(tempH2)[:3]
                                    #Training.gVariables.display.updateInfo("Successful Trials idle", tempS2)
                                    UpdList.append( ("Successful Trials idle", tempS2) )
                                else:
                                    #Training.gVariables.display.updateInfo("Successful Trials idle", "0.0")
                                    UpdList.append( ("Successful Trials idle", "0.0") )
                                ########
                                temp = (1.0 * Training.gVariables.successTrialCount / Training.gVariables.trialCount)
                                tempH = temp * 100.0
                                tempString = str(tempH)
                                if (len(tempString) > 3):
                                    tempS = str(tempH)[:4]
                                else:
                                    tempS = str(tempH)[:3]
                                Training.gVariables.successRate = tempS
                                #Training.gVariables.display.updateInfo("% s/t", Training.gVariables.successRate)
                                UpdList.append( ("% s/t", Training.gVariables.successRate) )
                                a = str(Training.gVariables.current_trial_time)[:4] + " - " + str(Training.gVariables.eventTime3_trialEnd)
                                #Training.gVariables.display.updateInfo("Trial Time", a)
                                UpdList.append( ("Trial Time", a) )
                                Training.gVariables.display.updateMultipleInfo( UpdList )
                pass
                #Training.gVariables.display.renderAgain() # not necessary since the update info calls renderAgain
                pass
    
    @staticmethod
    def restartTraining():
            # Starts or restarts training.
            try:
                Training.gVariables.start_time = timeit.default_timer()
                Training.gVariables.current_trial_start_time = timeit.default_timer()
            except:
                Training.gVariables.logger.warning( 'Error generating "timeit" variables' )
                pass
            Training.gVariables.current_trial_stage = 3
            Training.gVariables.trialCount = 0
            Training.gVariables.successTrialCount = 0
            Training.gVariables.successIdleTrialCount = 0;
            Training.gVariables.countIdleTime = 0;
            
            Training.gVariables.movementTrialCount = 0  # total number of trials which requires the subject to move
            Training.gVariables.idleTrialCount = 0  # total number of trials which requires the subject to stay idle.
            Training.gVariables.successTrialCount = 0  # total number of succesful trials
            Training.gVariables.successMovementTrialCount = 0  # total number of succesful trials regarding movement state
            Training.gVariables.successIdleTrialCount = 0  # total number of succesful trials regarding idle state
            Training.gVariables.successRate = 0  # success rate = (success trials / total trial count) %
            Training.gVariables.dropReleased = 0  # 0: no drop of water released this trial, 1: drop of water released
            Training.gVariables.dropsAmountGivenManually = 0  # number of drops given manually.
            
            #######################################################
            Training.gVariables.logger.debug("START: Logging the current state of all variables:")
            #logging the current status of config file first..
            Training.gVariables.logger.debug("START: config_training.py")
            with open("config_training.py", 'r') as configfile:
                Training.gVariables.logger.debug("\n"+configfile.read())
            Training.gVariables.logger.debug("END: config_training.py")
            
            Training.gVariables.logger.debug("trainingName %s" % str(Training.gVariables.trainingName))
            Training.gVariables.logger.debug("eventTime1_sound %s" % str(Training.gVariables.eventTime1_sound))
            Training.gVariables.logger.debug("eventTime1_movement_start %s" % str(Training.gVariables.eventTime1_movement_start))
            Training.gVariables.logger.debug("eventTime2_movement %s" % str(Training.gVariables.eventTime2_movement))
            Training.gVariables.logger.debug("eventTime3_trialEnd %s" % str(Training.gVariables.eventTime3_trialEnd))
            Training.gVariables.logger.debug("minIdleIntertrialTime %s" % str(Training.gVariables.minIdleIntertrialTime))
            Training.gVariables.logger.debug("interTrialRandom1Time %s" % str(Training.gVariables.interTrialRandom1Time))
            Training.gVariables.logger.debug("interTrialRandom2Time %s" % str(Training.gVariables.interTrialRandom2Time))
            #Training.gVariables.logger.debug("maxMovementTime %s" % str(Training.gVariables.maxMovementTime))
            Training.gVariables.logger.debug("movementTime %s" % str(Training.gVariables.movementTime))
            Training.gVariables.logger.debug("idleTime %s" % str(Training.gVariables.idleTime))
            Training.gVariables.logger.debug("soundGenDuration1 %s" % str(Training.gVariables.soundGenDuration1))
            Training.gVariables.logger.debug("soundGenDuration2 %s" % str(Training.gVariables.soundGenDuration2))
            Training.gVariables.logger.debug("soundGenFrequency1 %s" % str(Training.gVariables.soundGenFrequency1))
            Training.gVariables.logger.debug("soundGenFrequency2 %s" % str(Training.gVariables.soundGenFrequency2))
            Training.gVariables.logger.debug("trialCount %s" % str(Training.gVariables.trialCount))
            Training.gVariables.logger.debug("movementTrialCount %s" % str(Training.gVariables.movementTrialCount))
            Training.gVariables.logger.debug("idleTrialCount %s" % str(Training.gVariables.idleTrialCount))
            Training.gVariables.logger.debug("successTrialCount %s" % str(Training.gVariables.successTrialCount))
            Training.gVariables.logger.debug("successMovementTrialCount %s" % str(Training.gVariables.successMovementTrialCount))
            Training.gVariables.logger.debug("successIdleTrialCount %s" % str(Training.gVariables.successIdleTrialCount))
            Training.gVariables.logger.debug("successRate %s" % str(Training.gVariables.successRate))
            Training.gVariables.logger.debug("dropReleased %s" % str(Training.gVariables.dropReleased))
            Training.gVariables.logger.debug("dropsAmountGivenManually %s" % str(Training.gVariables.dropsAmountGivenManually))
            Training.gVariables.logger.debug("trialExecuting %s" % str(Training.gVariables.trialExecuting))
            Training.gVariables.logger.debug("trialStarted %s" % str(Training.gVariables.trialStarted))
            Training.gVariables.logger.debug("trialSuccessful %s" % str(Training.gVariables.trialSuccessful))
            Training.gVariables.logger.debug("countMovement %s" % str(Training.gVariables.countMovement))
            Training.gVariables.logger.debug("countIdleTime %s" % str(Training.gVariables.countIdleTime))
            Training.gVariables.logger.debug("LOOP_FUNCTION_SLEEP_TIME %s" % str(Training.gVariables.LOOP_FUNCTION_SLEEP_TIME))
            Training.gVariables.logger.debug("GUIType %s" % str(Training.gVariables.GUIType))
            Training.gVariables.logger.debug("videoDet %s" % str(Training.gVariables.videoDet))
            Training.gVariables.logger.debug("videoMovementMethod %s" % str(Training.gVariables.videoMovementMethod))
            Training.gVariables.logger.debug("absolute_start_time %s" % str(Training.gVariables.absolute_start_time))
            Training.gVariables.logger.debug("start_time %s" % str(Training.gVariables.start_time))
            Training.gVariables.logger.debug("current_trial_start_time %s" % str(Training.gVariables.current_trial_start_time))
            Training.gVariables.logger.debug("current_trial_time %s" % str(Training.gVariables.current_trial_time))
            Training.gVariables.logger.debug("current_trial_paused_time %s" % str(Training.gVariables.current_trial_paused_time))
            Training.gVariables.logger.debug("current_trial_stage %s" % str(Training.gVariables.current_trial_stage))
            Training.gVariables.logger.debug("toneOneProbability %s" % str(Training.gVariables.toneOneProbability))
            Training.gVariables.logger.debug("history_trial %s" % str(Training.gVariables.history_trial))
            Training.gVariables.logger.debug("current_trial_type %s" % str(Training.gVariables.current_trial_type))
            Training.gVariables.logger.debug("current_trial_type_str %s" % str(Training.gVariables.current_trial_type_str))
            Training.gVariables.logger.debug("trial_comment %s" % str(Training.gVariables.trial_comment))
            Training.gVariables.logger.debug("subject_name %s" % str(Training.gVariables.subject_name))
            
            Training.gVariables.logger.debug("END: Logging the current state of all variables:")
            #######################################################
            Training.gVariables.logger.info('Variables set. Starting %s' % Training.gVariables.trainingName)
            Training.gVariables.trialStarted = True
            Training.gVariables.trialExecuting = True
            Training.gVariables.absolute_start_time = timeit.default_timer()
            print "Tone Training started."
            Training.gVariables.logger.info( "Tone Training started." )
            a = "  %d seconds: tone" % Training.gVariables.soundGenDuration1
            b = "  %d seconds: detection of movement" % (Training.gVariables.eventTime2_movement - 
                                                                           Training.gVariables.eventTime1_movement_start)
            c = "  (%r - %r) seconds: inter trial delay time" % (Training.gVariables.interTrialRandom1Time ,
                                                                                   Training.gVariables.interTrialRandom2Time)
            print a
            print b
            print c
            Training.gVariables.logger.info( a )
            Training.gVariables.logger.info( b )
            Training.gVariables.logger.info( c )
    
    @staticmethod
    def stopTraining():
            #Stop
            if (Training.gVariables.current_trial_stage < 2 ):
                #stage 0: starting trial / playing tone
                #stage 1: detecting movement
                #if trial stage is 0 or 1, the subject hadn't have enough time to complete the trial opportunity window, so this trial cannot count
                #in the analysis. (decreasing trial count.)
                Training.gVariables.trialCount -= 1;
                if (Training.gVariables.current_trial_type == 1):
                    Training.gVariables.movementTrialCount -= 1;
                    #print "Restado mvnt por trial trunco"
                    pass
                elif (Training.gVariables.current_trial_type == 2):
                    Training.gVariables.idleTrialCount -= 1;
                    #print "Restado idle por trial trunco"
                    pass
            
            Training.updateDisplayInfo()
            Training.gVariables.logger.info('%s stopped.' % Training.gVariables.trainingName)
            Training.gVariables.logger.info('Success rate: %s' % Training.gVariables.successRate)
            Training.gVariables.logger.info('Movement trials: %d / %d' % (Training.gVariables.successMovementTrialCount, Training.gVariables.movementTrialCount))
            Training.gVariables.logger.info('Idle trials: %d / %d' % (Training.gVariables.successIdleTrialCount, Training.gVariables.idleTrialCount))
            Training.gVariables.logger.info('Drops given manually: %r' % Training.gVariables.dropsAmountGivenManually)
            Training.gVariables.trialStarted = False
            Training.gVariables.trialExecuting = False
            print "Tone Training stopped."
            Training.gVariables.logger.info( "Tone Training stopped." )
    
    @staticmethod
    def pauseTraining():
        Training.gVariables.trialExecuting = False
        Training.gVariables.current_trial_paused_time = timeit.default_timer()
        Training.gVariables.logger.info('%s paused.' % Training.gVariables.trainingName)
        print "Training paused."
    
    @staticmethod
    def resumeTraining():
        Training.gVariables.trialExecuting = True
        Training.gVariables.current_trial_paused_time = (timeit.default_timer() - Training.gVariables.current_trial_paused_time)
        print "Resuming training. Time that has been in pause: ", Training.gVariables.current_trial_paused_time
        Training.gVariables.logger.info('Resuming training. Time that has been in pause: %s' % Training.gVariables.current_trial_paused_time)
        Training.gVariables.logger.info('%s resumed.' % Training.gVariables.trainingName)
    
    @staticmethod
    def giveReward():
        if (Training.gVariables.dropReleased == 0 and Training.gVariables.trialExecuting == True):
                
                Training.gVariables.successTrialCount += 1
                Training.gVariables.dropReleased = 1
                if (Training.gVariables.current_trial_type == 1) :
                    Training.gVariables.successMovementTrialCount += 1
                    # print "Release drop of water."
                    for i in range(0, Training.gVariables.numberOfRewardDrops):
                        Training.gVariables.valve1.drop()
                        #print "drop"
                        if (Training.gVariables.numberOfRewardDrops > 1):
                             time.sleep(0.45)
                        Training.gVariables.logger.debug("Drop of water released.")
                else:
                    Training.gVariables.successIdleTrialCount += 1
                    # print "Release drop of water."
                    for i in range(0, Training.gVariables.numberOfRewardDropsIdle):
                        Training.gVariables.valve1.drop()
                        #print "drop"
                        if (Training.gVariables.numberOfRewardDropsIdle > 1):
                             time.sleep(0.45)
                        Training.gVariables.logger.debug("Drop of water released.")
    
    def exitTraining(self):
        # Finalize this training and exits.
        self.gVariables.logger.info('Exit signal.')
        self.gVariables.logger.info('Comment about this training: %s', Training.gVariables.trial_comment)
        #self.gVariables.fred1.stop() #this function has not
        self.gVariables.programRunning = 0;
        time.sleep(0.5)
        
        if (self.gVariables.GUIType != 2) :
            #self.gVariables.currentGUI.exit(); #It is auto-executed on uiAPI , so it's not necessary here.
            pass
        else:
            time.sleep(0.2)
            del self.gVariables.fredInput
        self.gVariables.valve1.exit()
        del self.gVariables.valve1
        if (self.gVariables.videoSecond != -1):
            try:
                self.gVariables.videoSecond.exit()
                del self.gVariables.videoSecond
            except:
                pass
        self.gVariables.videoDet.exit()
        time.sleep(0.2)
        del self.gVariables.videoDet
        self.gVariables.audioRec.exit()
        time.sleep(0.2)
        del self.gVariables.audioRec
        #print "videodet exit"
        time.sleep(0.2)
        self.gVariables.display.exitDisplay()
        del self.gVariables.display
        #print "display exit"
        time.sleep(0.2)
        self.gVariables.s1.exit()
        time.sleep(0.6)
        del self.gVariables.s1
        self.gVariables.s2.exit()
        time.sleep(0.6)
        del self.gVariables.s2
        #print "sound exit"
        print "Exiting."
        sys.exit(0)
    
    def getSubjectName(self):
        # getSubjectName : asks user (by showing a list) which name corresponds to this training.
        import userInterfaceAPI
        
        def checkSubjectName( starg ):
            #checks if valid and if it is a new subject
            try:
                subj_name = str(starg )
            except:
                subj_name = ""
            tmp = 0
            newname_found = False
            try:
                f = open(sbjlistfile ,"r+")
            except:
                print "Couldn't open subject list file. Creating new subject list file."
                f = open(sbjlistfile ,"w")
            for i in range(0, len(subj_list) ):
                if subj_name.strip() == subj_list[i]:
                    tmp = 1;
            if tmp == 0:
                #print "nuevo nombre"
                #print subj_name
                if len(subj_name) > 1:
                    newname_found = True
                    subj_list.append(subj_name.strip())
                #f.write(subj_name + "\n")
                pass
            self.gVariables.subject_name = subj_name
            if (newname_found == True):
                print "Adding new name to subject list."
                f.close()
                f = open(sbjlistfile ,"w")
                print subj_list
                for sn in subj_list:
                    f.write(sn + "\n")
                #f.writelines(subj_list)
                pass
            f.close()
            pass
        
        sbjlistfile = "subject_list.txt"
        try:
            f = open(sbjlistfile ,"r+")
        except:
            #self.gVariables.logger.warning( "Error getting subject list." ); #logger does not exist yet.
            print "Error getting subject list. Creating new one."
            f = open(sbjlistfile ,"w+")
        subj_list = f.readlines()
        j = len(subj_list)
        i=0;
        while i < j:
            subj_list[i] = subj_list[i].strip()
            if len(subj_list[i]) <= 1:
                subj_list.remove(subj_list[i])
                j = 0;
                i=0;
            i+=1;
        print "List of subjects: %r " % subj_list
        
        if (self.gVariables.GUIType != 2):
            uiAPI = userInterfaceAPI.userInterface_API(False);
            #uiAPI = userInterfaceAPI.multiproc_userInterface_API(False)
            uiAPI.usingTK = self.gVariables.GUIType
            uiAPI.multiProcSubjectNameQuery = self.gVariables.multiProcSubjectNameQuery
            uiAPI.subj_list = subj_list;
            subj_name =  uiAPI.getSubjName();
            #del uiAPI
            self.gVariables.currentGUI = uiAPI;
        else:
            #non-gui mode: ask for name with CL input
            subj_name = str(raw_input("Please enter subject name: "))
        checkSubjectName(subj_name)
        
        self.gVariables.subject_name = subj_name
        
        pass
    
    def trainingInit(self):
        #trainingInit : Called when the class is instantiated.
        print self.gVariables.trainingName
        #get subject name:
        self.getSubjectName()
        print "Subject's name: %s" % self.gVariables.subject_name
        #counting number of sessions
        session_files_count = 0
        rootDir = '.'
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                if fname.startswith("%s_" % self.gVariables.subject_name):
                    session_files_count += 1;
                    #self.gVariables.logger.debug("Previous subject log found: %s" % str(fname) ) #todavía no existe el logger
                    pass
        print "There are %r session files from this subject" % session_files_count;
        #a SNN (session_files_count+1) string is put in the new filename.
        session_files_count +=1
        # logging:
        self.gVariables.logger = logging.getLogger( self.gVariables.trainingName )
        # create a logging format
        dateformat = '%Y/%m/%d %H:%M:%S'
        formatter_str = '%(asctime)s.%(msecs)d - %(name)s - %(levelname)s - %(message)s'
        filename_to_log='logs/%s_S%s_%s_%s.log' % (self.gVariables.subject_name, str(session_files_count).zfill(3) , self.gVariables.trainingName, time.strftime("%Y-%m-%d") )
        
        
        logging.basicConfig(filename=filename_to_log, filemode='w+',
            level=logging.DEBUG, format=formatter_str,
            datefmt=dateformat)
        
        #===========================================================================
        #the following lines are only to ALSO log to stdout, are not strictly necessary
        #===========================================================================
        console = logging.StreamHandler()
        console.setLevel(logging.WARNING)
        formatter = track_bola_utils.formatterWithMillis(fmt=formatter_str,datefmt=dateformat)
        console.setFormatter(formatter)
        self.gVariables.logger.addHandler(console)
        #===========================================================================
        
        pass
        #setting training configs per subject; if exists, has priority over previous configs. Check docs.
        subj_config_file = Training.gVariables.subject_name + "_config_training"
        try:
            subj_config_file = Training.gVariables.subject_name + "_config_training"
            subjectConfig = importlib.import_module(subj_config_file);
            Training.gVariables.trainingName = subjectConfig.trainingName
            Training.gVariables.eventTime1_sound = subjectConfig.eventTime1_sound
            Training.gVariables.eventTime1_movement_start = subjectConfig.eventTime1_movement_start
            Training.gVariables.eventTime2_movement = subjectConfig.eventTime2_movement
            Training.gVariables.eventTime3_trialEnd = subjectConfig.eventTime3_trialEnd
            Training.gVariables.minIdleIntertrialTime = subjectConfig.minIdleIntertrialTime
            Training.gVariables.requireStillness = subjectConfig.requireStillness
            Training.gVariables.interTrialRandom1Time = subjectConfig.interTrialRandom1Time
            Training.gVariables.interTrialRandom2Time = subjectConfig.interTrialRandom2Time
            Training.gVariables.movementTime = subjectConfig.movementTime
            Training.gVariables.idleTime = subjectConfig.idleTime
            Training.gVariables.soundGenDuration1 = subjectConfig.soundGenDuration1
            Training.gVariables.soundGenDuration2 = subjectConfig.soundGenDuration2
            Training.gVariables.soundGenFrequency1 = subjectConfig.soundGenFrequency1
            Training.gVariables.soundGenFrequency2 = subjectConfig.soundGenFrequency2
            Training.gVariables.toneOneProbability = subjectConfig.toneOneProbability
            Training.gVariables.usingTK = subjectConfig.usingTK
            Training.gVariables.initialComment = subjectConfig.initialComment
            Training.gVariables.type_pavlov = subjectConfig.type_pavlov
            Training.gVariables.type_skinner = subjectConfig.type_skinner
            Training.gVariables.type_ocond = subjectConfig.type_ocond
            Training.gVariables.type_discr = subjectConfig.type_discr
            #movement threshold and method: edit sphereVideoDetection config files (check docs.)
            Training.gVariables.numberOfRewardDrops = subjectConfig.numberOfRewardDrops
            Training.gVariables.numberOfRewardDropsIdle = subjectConfig.numberOfRewardDropsIdle
            Training.gVariables.override_training_types = 1;
            print "Configurations loaded from %s.py" % subj_config_file
            self.gVariables.logger.info("Configurations loaded from %s.py" % subj_config_file)
        except:
            print "File %s.py doesn't exist. Will be using general configuration variables instead." % subj_config_file
            self.gVariables.logger.info("File %s.py doesn't exist. Will be using general configuration variables instead." % subj_config_file)
        #adjusting trial types and modes:
        if (self.gVariables.type_pavlov == 1):
            #movement starts and ceases to be detected just after the tone ends. Basically, there's no movement window when Pavlov mode is enabled.
            self.gVariables.eventTime2_movement = self.gVariables.soundGenDuration1
            self.gVariables.eventTime1_movement_start = self.gVariables.soundGenDuration1
        
        if (self.gVariables.type_skinner == 1):
            #there are no tones, so setting their duration to 0
            Training.gVariables.soundGenDuration1 = 0.0
            Training.gVariables.soundGenDuration2 = 0.0
        
        
        self.gVariables.trialExecuting = False  # boolean, if a 8 second with tone trial is wanted, this shoulb be set to 1
        self.gVariables.logger.info('===============================================')
        self.gVariables.logger.info('Start %s' % self.gVariables.trainingName)
        self.gVariables.logger.info('Subject name: %s' % self.gVariables.subject_name)
        
        # valve:
        import valveDevice as vlv
        self.gVariables.valve1 = vlv.Valve()
        self.gVariables.logger.debug('Valve created.')
        
        
        # soundGen:
        # La configuración es a nivel de módulo, no en el entrenamiento principal.
        import soundGenerator
        self.gVariables.s1 = soundGenerator.soundGen(self.gVariables.soundGenFrequency1, self.gVariables.soundGenDuration1)
        self.gVariables.s2 = soundGenerator.soundGen(self.gVariables.soundGenFrequency2, self.gVariables.soundGenDuration2)
        
        self.gVariables.logger.debug('Soundgen init started..')
        #GUI:
        import multiprocessing
        self.gVariables.jobList = multiprocessing.JoinableQueue()
        #self.gVariables.jobList.put_nowait((0, 0))
        pass
        
        
        if (self.gVariables.GUIType != 2):
            #import userInterfaceAPI
            print ".---------------------------"
            print "import done for API"
            print ".---------------------------"
            #self.gVariables.currentGUI = userInterfaceAPI.userInterface_API(False);
            self.commitToCurrentGUI()
            self.gVariables.currentGUI.launch_GUI()
            #self.gVariables.GUIProcess = multiprocessing.Process(target=self.initUserInputGUI, args=(self.gVariables.jobList,))
            #self.gVariables.GUIProcess.start()
            self.gVariables.logger.info('GUI Process started.')
        else:
            self.gVariables.fredInput = threading.Thread(target=self.noGUIInputLoop)
            self.gVariables.fredInput.start()
            pass
        #Sphere Video Detection:
        import sphereVideoDetection
        self.gVariables.videoDet = sphereVideoDetection.sphereVideoDetection()
        import audioRecorder
        #.mainAudioDetection()
        self.gVariables.audioRec = audioRecorder.audioRecorder()
        filename='logs/%s_S%s_%s_%s' % (self.gVariables.subject_name, str(session_files_count).zfill(3) , self.gVariables.trainingName, time.strftime("%Y-%m-%d") )
        self.gVariables.videoDet.setOutputVideoFile(filename+'.avi')
        self.gVariables.audioRec.setOutputAudioFile(filename+'.wav')
        self.gVariables.videoDet.setMovementTimeWindow(self.gVariables.movementTime)  # seconds that should be moving.
        self.gVariables.videoMovementMethod =  self.gVariables.videoDet.getMovementMethod()
        self.gVariables.videoDet.usingPygameDisplay = False; #to prevent launching pygame visualization tools for vd.
        self.gVariables.videoDet.initAll()
        self.gVariables.fred0 = threading.Thread(target=self.gVariables.audioRec.mainAudioDetection)
        self.gVariables.fred0.start()
        self.gVariables.logger.debug('sphereVideoDetection started.')
        #second cam:
        ####import simpleCam
        ####self.gVariables.videoSecond = simpleCam.simpleCam();
        ####self.gVariables.logger.debug('secondCam started.');
        #Display:
        self.initDisplay()
        #main Program Loop
        self.gVariables.fred1 = threading.Thread(target=self.mainLoopFunction)
        self.gVariables.fred1.start()
        self.gVariables.logger.debug('Training loop function started..')
        
    
    def commitToCurrentGUI(self):
        import config_training as configs
        self.gVariables.currentGUI.toneStart = 0.0
        self.gVariables.currentGUI.toneEnd = self.gVariables.eventTime1_sound
        self.gVariables.currentGUI.movementWindowStart = self.gVariables.eventTime1_movement_start
        self.gVariables.currentGUI.movementWindowEnd = self.gVariables.eventTime2_movement
        self.gVariables.currentGUI.interTrialStart = self.gVariables.interTrialRandom1Time
        self.gVariables.currentGUI.interTrialEnd = self.gVariables.interTrialRandom2Time
        self.gVariables.currentGUI.probabilityToneOne = self.gVariables.toneOneProbability
        self.gVariables.currentGUI.frequencyTone1 = self.gVariables.soundGenFrequency1
        self.gVariables.currentGUI.frequencyTone2 = self.gVariables.soundGenFrequency2
        self.gVariables.currentGUI.movementAmount = configs.MOVEMENT_THRESHOLD_INITIAL_VALUE #sphereVideoDetection but read from training config file
        self.gVariables.currentGUI.movementMethod = configs.MOVEMENT_METHOD_INITIAL_VALUE #same as above
        self.gVariables.currentGUI.movementTime = self.gVariables.movementTime
        self.gVariables.currentGUI.idleTime = self.gVariables.idleTime
        self.gVariables.currentGUI.comment = configs.initialComment
        
        self.gVariables.currentGUI.usingTK = self.gVariables.GUIType
        
        self.gVariables.currentGUI.type_pavlov = self.gVariables.type_pavlov
        self.gVariables.currentGUI.type_skinner = self.gVariables.type_skinner
        self.gVariables.currentGUI.type_ocond = self.gVariables.type_ocond
        self.gVariables.currentGUI.type_discr = self.gVariables.type_discr
        
        
        if (Training.gVariables.override_training_types == 0):
            Training.gVariables.saveVariables.loadIntoAPIPavlovVars()
            Training.gVariables.saveVariables.loadIntoAPISkinnerVars()
            Training.gVariables.saveVariables.loadIntoAPIOcondVars()
            Training.gVariables.saveVariables.loadIntoAPIDiscrVars()
        else:
            #instead, save into pavlov, skinner, etc. Because we are assuming the SUBJ_config_training
            #has been edited to have priority over other configs.
            Training.gVariables.saveVariables.saveDiscrVars()
            Training.gVariables.saveVariables.saveOcondVars()
            Training.gVariables.saveVariables.savePavlovVars()
            Training.gVariables.saveVariables.saveSkinnerVars()
            Training.gVariables.saveVariables.loadIntoAPIPavlovVars()
            Training.gVariables.saveVariables.loadIntoAPISkinnerVars()
            Training.gVariables.saveVariables.loadIntoAPIOcondVars()
            Training.gVariables.saveVariables.loadIntoAPIDiscrVars()
        
        if (self.gVariables.type_pavlov):
            self.gVariables.currentGUI.current_type = "pavlov"
        if (self.gVariables.type_skinner):
            self.gVariables.currentGUI.current_type = "skinner"
        if (self.gVariables.type_ocond):
            self.gVariables.currentGUI.current_type = "ocond"
        if (self.gVariables.type_discr):
            self.gVariables.currentGUI.current_type = "discr"
        
        
        
        self.gVariables.currentGUI.requireStillnessVar = self.gVariables.requireStillness
        #print "--%d" % self.gVariables.requireStillness
        pass
    
    def trialLoop(self):
            # This function controls all events that defines a trial: Tone at a given time, reward opportunity, etc.
            
            #===================================================================
                # Check / update current trial stage and time
                #===================================================================
            if (Training.gVariables.trialExecuting == True):
                # Update Trial Time. Important since this is where events happen at certain moments in this line.
                Training.gVariables.current_trial_start_time += Training.gVariables.current_trial_paused_time
                Training.gVariables.start_time += Training.gVariables.current_trial_paused_time  # we consider that training time has not passed in the pause state.
                Training.gVariables.current_trial_paused_time = 0
                Training.gVariables.current_trial_time = (timeit.default_timer() - Training.gVariables.current_trial_start_time)
                if ( ( Training.gVariables.current_trial_stage == 3 and 
                            ( ( Training.gVariables.videoDet.getIdleTime() >= Training.gVariables.minIdleIntertrialTime and
                                    Training.gVariables.videoDet.getMovementStatus() == False) or (Training.gVariables.requireStillness == 0) ) or (Training.gVariables.trialCount == 0)  ) ) :
                    
                    
                    Training.gVariables.trialCount += 1
                    Training.gVariables.logger.info('Starting trial:%d' % Training.gVariables.trialCount)
                    
                    Training.gVariables.dropReleased = 0
                    Training.gVariables.current_trial_start_time = timeit.default_timer()

                    if (Training.gVariables.toneOneProbability < 0.75) and (Training.gVariables.toneOneProbability > 0.25) and (Training.gVariables.history_trial[-1] == Training.gVariables.history_trial[-2]) and (Training.gVariables.history_trial[-2] == Training.gVariables.history_trial[-3]) :
                        # 3 equal trial have past. forcing change of trial type
                        Training.gVariables.logger.info('fixed tone')
                        if (Training.gVariables.history_trial[-1]) == 2:
                            Training.gVariables.current_trial_type = 1
                        else :
                            Training.gVariables.current_trial_type = 2
                    else :
                        from random import random
                        if (random() < Training.gVariables.toneOneProbability) :
                            Training.gVariables.current_trial_type = 1
                        else :
                            Training.gVariables.current_trial_type = 2
                    
                    if (Training.gVariables.type_ocond == 1 or Training.gVariables.type_skinner == 1 or Training.gVariables.type_pavlov == 1): #force it to "move"
                        Training.gVariables.current_trial_type = 1 #pavlov here is unnecessary, but to keep all except discr in "move" type.
                    
                    if (Training.gVariables.current_trial_type == 1) :
                            Training.gVariables.logger.info('tone 1: %s Hz' % str(Training.gVariables.soundGenFrequency1) )
                            
                            Training.gVariables.s1.play()
                            Training.gVariables.movementTrialCount += 1
                            # a new "time window" should be set for 
                            # some movement analysis methods to work.
                            Training.gVariables.videoDet.setMovementTimeWindow(Training.gVariables.movementTime)
                    else :
                            Training.gVariables.logger.info('tone 2: %s Hz'  % str(Training.gVariables.soundGenFrequency2))
                            Training.gVariables.s2.play()
                            Training.gVariables.idleTrialCount += 1
                            # a new "time window" should be set for 
                            # some movement analysis methods to work.
                            Training.gVariables.videoDet.setMovementTimeWindow(Training.gVariables.idleTime)

                    if (Training.gVariables.current_trial_type == 1):
                            sttrial = "move"
                    elif (Training.gVariables.current_trial_type == 2):
                            sttrial = "still"
                    Training.gVariables.logger.info('Trial type:%s' % sttrial)
                    Training.gVariables.logger.debug(Training.gVariables.history_trial)
                    Training.gVariables.logger.debug(Training.gVariables.toneOneProbability)
                    Training.gVariables.logger.debug(Training.gVariables.current_trial_type)
                    
                    Training.gVariables.history_trial[0:-1] = Training.gVariables.history_trial[1:]
                    Training.gVariables.history_trial[-1] = Training.gVariables.current_trial_type

                    Training.gVariables.current_trial_stage = 0
                    Training.gVariables.current_trial_paused_time = 0
                    
                    # add random factor to the intertrial time in the next one:
                    from random import randint
                    i = randint(0, 10)
                    scaleF = (Training.gVariables.interTrialRandom2Time - Training.gVariables.interTrialRandom1Time) / 10
                    Training.gVariables.eventTime3_trialEnd = Training.gVariables.interTrialRandom1Time + (i * scaleF)
                
                #there is a space of time between Training.gVariables.eventTime1_sound and  Training.gVariables.eventTime1_movement_start
                #which is not used. It could be used in the future. see docs.
                
                #the tone end is not necessarily tied to the start of movement detection. see docs.
                
                if (int(Training.gVariables.current_trial_time) >= Training.gVariables.eventTime1_movement_start and 
                     int(Training.gVariables.current_trial_time) <= Training.gVariables.eventTime2_movement 
                     and Training.gVariables.current_trial_stage == 0):
                    Training.gVariables.logger.info('Start trial movement detection')
                    Training.gVariables.trialSuccessful = False
                    if (Training.gVariables.current_trial_type == 1) :
                        Training.gVariables.videoDet.resetMovementTime()
                    else:
                        Training.gVariables.videoDet.resetIdleTime()
                    Training.gVariables.current_trial_stage = 1
                elif (int(Training.gVariables.current_trial_time) >= Training.gVariables.eventTime2_movement and 
                      Training.gVariables.current_trial_stage == 1):
                    Training.gVariables.logger.info('End trial movement detection')
                    if (Training.gVariables.type_pavlov == 0):
                        if (Training.gVariables.trialSuccessful == True):
                            Training.giveReward()
                            Training.gVariables.logger.info('Reward given because trial was successful')
                        else:
                            Training.gVariables.logger.info('Reward not given because trial was not successful')
                    else:
                        Training.giveReward()
                        Training.gVariables.logger.info('Reward given because pavlov mode is enabled')
                    Training.gVariables.logger.info('Start inter-trial delay')
                    Training.gVariables.current_trial_stage = 2
                elif (int(Training.gVariables.current_trial_time) >= Training.gVariables.eventTime3_trialEnd and
                      Training.gVariables.current_trial_stage == 2):
                    Training.gVariables.logger.info('End trial:%d' % (Training.gVariables.trialCount - 1 ) )
                    Training.gVariables.logger.info('Trial type was: ' + str(Training.gVariables.current_trial_type_str))
                    now = timeit.default_timer()
                    frmtime = Training.gVariables.getFormattedTime(int(now - Training.gVariables.absolute_start_time))
                    Training.gVariables.logger.info('Amount of time passed since start of training: %s' % frmtime)
                    # #
                    Training.gVariables.videoDet.setMovementTimeWindow(Training.gVariables.minIdleIntertrialTime)
                    if(Training.gVariables.dropReleased == 1):
                        Training.gVariables.logger.info('Trial successful')
                    else:
                        Training.gVariables.logger.info('Trial not successful')
                    Training.gVariables.logger.info('Success rate: %r' % (Training.gVariables.successRate))
                    Training.gVariables.current_trial_stage = 3
            # Training.gVariables.logger.debug('Movement Vector: %s',Training.gVariables.movementVector)
            
            #===============================================================
            # Check if should give reward
            #===============================================================
            
            if (Training.gVariables.trialExecuting == True and Training.gVariables.current_trial_stage == 1):
                # print Training.gVariables.videoDet.getTrackingStatus()
                if (Training.gVariables.current_trial_type == 1):
                  if (Training.gVariables.videoDet.getMovementStatus() == True and 
                    ((Training.gVariables.videoDet.getMovementTime() >= (Training.gVariables.movementTime))
                       ) ):
                    # Training.giveReward() #the reward is given at the end of the mvnt window
                    Training.gVariables.trialSuccessful = True
                    Training.gVariables.logger.info('Movement threshold reached. Will give reward at the end of movement window. (mvnt)')
                    # print "Continuous total time: %r"%Training.gVariables.videoDet.getMovementTime()
                elif (Training.gVariables.current_trial_type == 2):
                  if (Training.gVariables.videoDet.getMovementStatus() == False and 
                    Training.gVariables.videoDet.getIdleTime() >= (Training.gVariables.idleTime)):  #
                    # Training.giveReward() #the reward is given at the end of the mvnt window
                    Training.gVariables.trialSuccessful = True
                    Training.gVariables.logger.info('Movement threshold reached. Will give reward at the end of movement window. (idle)')
                    # print "Continuous total time: %r"%Training.gVariables.videoDet.getMovementTime()
                    pass
            else:
                #trial not executing or tr.stage not 1, so it is unnecessary to check if should give reward..
                pass
    
    def saveToInternalVars(self, a):
                    if ("pavlov" in a):
                        print "pavlov mode detected"
                        if (Training.gVariables.type_pavlov == 1):
                            print "Pavlov already set to 1. Saving Pavlov vars."
                            Training.gVariables.saveVariables.savePavlovVars()
                        else:
                            print "Pavlov set. Not saving Pavlov variables. Loading GUI for previously loaded vars"
                            Training.gVariables.saveVariables.loadPavlovVars()
                            
                            
                        Training.gVariables.type_pavlov = 1
                        Training.gVariables.type_skinner = 0
                        Training.gVariables.type_discr = 0
                        Training.gVariables.type_ocond = 0
                        pass
                    if ("skinner") in a:
                        print "skinner detected"
                        if (Training.gVariables.type_skinner == 1):
                            print "Skinner already set to 1. Saving Skinner vars."
                            Training.gVariables.saveVariables.saveSkinnerVars()
                        else:
                            print "Skinner set. Not saving Skinner variables. Loading GUI for previously loaded vars"
                            Training.gVariables.saveVariables.loadSkinnerVars()
                        Training.gVariables.type_pavlov = 0
                        Training.gVariables.type_skinner = 1
                        Training.gVariables.type_discr = 0
                        Training.gVariables.type_ocond = 0
                        pass
                    if ("oc") in a:
                        print "oc detected"
                        if (Training.gVariables.type_ocond == 1):
                            print "O.Cond. already set to 1. Saving O.Cond. vars."
                            Training.gVariables.saveVariables.saveOcondVars()
                        else:
                            print "O.Cond. set. Not saving O.Cond. variables. Loading GUI for previously loaded vars"
                            Training.gVariables.saveVariables.loadOcondVars()
                        Training.gVariables.type_pavlov = 0
                        Training.gVariables.type_skinner = 0
                        Training.gVariables.type_discr = 0
                        Training.gVariables.type_ocond = 1
                        pass
                    if ("discr") in a:
                        print "discr detected"
                        if (Training.gVariables.type_discr == 1):
                            print "..................................................................."
                            print "Discr. already set to 1. Saving Discr. vars."
                            print "..................................................................."
                            Training.gVariables.saveVariables.saveDiscrVars()
                        else:
                            print "..................................................................."
                            print "Discr. set. Not saving Discr. variables. Loading GUI for previously loaded vars"
                            print "..................................................................."
                            Training.gVariables.saveVariables.loadDiscrVars()
                        Training.gVariables.type_pavlov = 0
                        Training.gVariables.type_skinner = 0
                        Training.gVariables.type_discr = 1
                        Training.gVariables.type_ocond = 0
                        pass
    
    def GUICheck(self):
                #GUICheck: this function is called once in every thread loop, and checks if
                #    the shared variables between training_ and GUI Process contain new info.
                #    If it does, checks which message type was sent, and it's argument (if any)            #    and executes the corresponding routine for that type of messag
                index = -1
                argument = -1
                try:
                    if ( int (self.gVariables.currentGUI.last_message) != -1):
                        #print self.gVariables.currentGUI.last_message
                        #print "received."
                        #print self.gVariables.currentGUI.last_argument
                        #print "received."
                        index = self.gVariables.currentGUI.last_message
                        argument = self.gVariables.currentGUI.last_argument
                        self.gVariables.currentGUI.last_message = -1
                        self.gVariables.currentGUI.last_argument = -1
                except:
                    return;
                if (index == -1):
                    return
#             return;
#             
#             if (self.gVariables.jobList.qsize() > 0 or self.gVariables.jobList.empty() == False ):
#                 try:
#                         tempvar = self.gVariables.jobList.get()
#                         self.gVariables.jobList.task_done()
#                 except:
#                         return;
#                 Training.gVariables.logger.debug( str("GUICheck: queue: " + str(tempvar) )  )
#                 index = tempvar[0]
#                 try:
#                     argument = tempvar[1]
#                 except:
#                     argument = ""
#                     pass
#                 pass
                #print "GUICheck: Got a Message:", index
                Training.gVariables.logger.debug( str("GUICheck: Got a Message:" + str(index)) )
                #print "GUICheck: Message's argument:", argument
                try:
                    a = str(argument)
                    Training.gVariables.logger.debug( str("GUICheck: Message's argument:" + a ) )
                except:
                    Training.gVariables.logger.warning( str("GUICheck: Message's received argument cannot be parsed to string" ) )
                    a = "__"
                    pass
                
                if (index == 0):
                    return;
                if (index == 1):
                    print "GUICheck: 'Drop' message."
                    Training.gVariables.logger.debug( "GUICheck: 'Drop' message." )
                    Training.gVariables.fn_giveDrop()
                elif (index == 2):
                    print "GUICheck: 'Reward' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Reward' message" )
                    Training.gVariables.fn_giveReward()
                elif (index == 3):
                    print "GUICheck: 'Open' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Open' message" )
                    Training.gVariables.fn_openValve()
                elif (index == 4):
                    print "GUICheck: 'Close' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Close' message" )
                    Training.gVariables.fn_closeValve()
                elif (index == 5):
                    print "GUICheck: 'Start Training' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Start Training' message" )
                    Training.gVariables.fn_startStopTraining(1)
                elif (index == 6):
                    print "GUICheck: 'Stop Training' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Stop Training' message" )
                    Training.gVariables.fn_startStopTraining(2)
                elif (index == 7):
                    if (Training.gVariables.trialExecuting == True):
                        print "GUICheck: 'Pause Training' message"
                        Training.gVariables.logger.debug( "GUICheck: 'Pause Training' message" )
                        Training.gVariables.fn_pauseResumeTraining(2) ########
                    else:
                        print "GUICheck: 'Resume Training' message"
                        Training.gVariables.logger.debug( "GUICheck: 'Resume Training' message" )
                        Training.gVariables.fn_pauseResumeTraining(1) ########
                elif (index == 8):
                    if (Training.gVariables.trialExecuting == True):
                        print "GUICheck: 'Pause Training' message"
                        Training.gVariables.logger.debug( "GUICheck: 'Pause Training' message" )
                        Training.gVariables.fn_pauseResumeTraining(2) ########
                    else:
                        print "GUICheck: 'Resume Training' message"
                        Training.gVariables.logger.debug( "GUICheck: 'Resume Training' message" )
                        Training.gVariables.fn_pauseResumeTraining(1) ########
                elif (index == 9):
                    print "GUICheck: 'Exit Training' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Exit Training' message" )
                    self.exitTraining()
                elif (index == 10):
                    print "GUICheck: 'Tone 1 Test' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Tone 1 Test' message" )
                    Training.gVariables.fn_tone1Test( argument )
                elif (index == 11):
                    print "GUICheck: 'Tone 2 Test' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Tone 2 Test' message" )
                    Training.gVariables.fn_tone2Test( argument )
                elif (index == 12):
                    print "GUICheck: 'Show Feedback' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Show Feedback' message" )
                    Training.gVariables.fn_showUserFeedback()
                elif (index == 13):
                    print "GUICheck: 'Hide Feedback' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Hide Feedback' message" )
                    Training.gVariables.fn_hideUserFeedback()
                elif (index == 14):
                    print "GUICheck: 'Show Tracking' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Show Tracking' message" )
                    Training.gVariables.fn_showTrackingFeedback()
                elif (index == 15):
                    print "GUICheck: 'Hide Tracking' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Hide Tracking' message" )
                    Training.gVariables.fn_hideTrackingFeedback()
                elif (index == 16):
                    print "GUICheck: 'Set Comment' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Set Comment' message" )
                    try:
                        tempstring = str(argument)
                    except:
                        tempstring = ""
                    Training.gVariables.trial_comment = tempstring
                    print "GUICheck: comment read from Queue: ", tempstring
                    Training.gVariables.logger.debug( str( "GUICheck: comment read from Queue: "+ tempstring ) )
                elif (index == 17):
                    print "GUICheck: 'Variable to change: Tone1 Frequency' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Variable to change: Tone1 Frequency' message" )
                    Training.gVariables.fn_setFrequencyT1( argument )
                    print "GUICheck: Argument value read from Queue: ", argument
                    Training.gVariables.logger.debug( str( "GUICheck: Argument value read from Queue: " + str(argument) ) )
                elif (index == 18):
                    print "GUICheck: 'Variable to change: Tone2 Frequency' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Variable to change: Tone2 Frequency' message" )
                    Training.gVariables.fn_setFrequencyT2( argument )
                    print "GUICheck: Argument value read from Queue: ", argument
                    Training.gVariables.logger.debug( str( "GUICheck: Argument value read from Queue: " + str(argument) ) )
                elif (index == 19):
                    print "GUICheck: 'Variable to change: Movement Amount' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Variable to change: Movement Amount' message" )
                    Training.gVariables.fn_movementThresholdSet(argument)
                    print "GUICheck: Argument value read from Queue: ", argument
                    Training.gVariables.logger.debug( str( "GUICheck: Argument value read from Queue: " + str(argument) ) )
                elif (index == 20):
                    print "GUICheck: 'Variable to change: Method Type to be used' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Variable to change: Method Type to be used' message" )
                    Training.gVariables.fn_setMovementMethod(argument)
                    print "GUICheck: Argument value read from Queue: ", argument
                    Training.gVariables.logger.debug( str( "GUICheck: Argument value read from ns: " + str(argument) ) )
                elif (index == 21):
                    print "GUICheck: 'Variable to change: Movement Time' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Variable to change: Movement Time' message" )
                    Training.gVariables.fn_movementTimeSet(argument)
                    print "GUICheck: Argument value read from Queue: ", argument
                    Training.gVariables.logger.debug( str("GUICheck: Argument value read from Queue: " + str(argument)) )
                elif (index == 22):
                    print "GUICheck: 'Variable to change: Idle Time' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Variable to change: Idle Time' message" )
                    Training.gVariables.fn_idleTimeSet(argument)
                    ############################################################
                    # Saving to internal vars here because of lack of a better place to put them.
                    ############################################################
                    print "Parameters: saving to internal vars."
                    self.saveToInternalVars(Training.gVariables.current_mode)
                    
                    print "GUICheck: Argument value read from Queue: ", argument
                    Training.gVariables.logger.debug( str("GUICheck: Argument value read from Queue: " + str(argument)) )
                elif (index == 23):
                    print "GUICheck: 'Variable to change: Tone Start' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Variable to change: Tone Start' message" )
                    print "Tone Start variable is not meant to change. Add intertrial delay instead."
                    Training.gVariables.logger.debug( "Tone Start variable is not meant to change. Add intertrial delay instead." )
                    print "GUICheck: Argument value read from Queue: ", argument
                    Training.gVariables.logger.debug( str( "GUICheck: Argument value read from Queue: " + str(argument) ) )
                elif (index == 24):
                    print "GUICheck: 'Variable to change: Tone End' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Variable to change: Tone End' message" )
                    Training.gVariables.fn_setTone1Duration(float(argument))
                    Training.gVariables.fn_setTone2Duration(float(argument))
                    print "GUICheck: Argument value read from Queue: ", argument
                    Training.gVariables.logger.debug( str( "GUICheck: Argument value read from Queue: " + str(argument) ) )
                elif (index == 25):
                    print "GUICheck: 'Variable to change: Movement Window Start' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Variable to change: Movement Window Start' message" )
                    Training.gVariables.fn_setMovementWindowStart( float(argument) )
                    print "GUICheck: Argument value read from Queue: ", argument
                    Training.gVariables.logger.debug( str( "GUICheck: Argument value read from Queue: " + str(argument) ) )
                elif (index == 26):
                    print "GUICheck: 'Variable to change: Movement Window End' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Variable to change: Movement Window End' message" )
                    Training.gVariables.fn_setMovementWindowEnd( float(argument) )
                    print "GUICheck: Argument value read from Queue: ", argument
                    Training.gVariables.logger.debug( str( "GUICheck: Argument value read from Queue: " + str(argument) ) )
                elif (index == 27):
                    print "GUICheck: 'Variable to change: Inter Trial Start' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Variable to change: Inter Trial Start' message" )
                    Training.gVariables.fn_setITRandom1( float(argument) )
                    print "GUICheck: Argument value read from Queue: ", argument
                    Training.gVariables.logger.debug( str( "GUICheck: Argument value read from Queue: " + str(argument) ) )
                elif (index == 28):
                    print "GUICheck: 'Variable to change: Inter Trial End' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Variable to change: Inter Trial End' message" )
                    Training.gVariables.fn_setITRandom2( float(argument) )
                    print "GUICheck: Argument value read from Queue: ", argument
                    Training.gVariables.logger.debug( str( "GUICheck: Argument value read from Queue: " + str(argument) ) )
                elif (index == 29):
                    print "GUICheck: 'Variable to change: Probability Tone One' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Variable to change: Probability Tone One' message" )
                    Training.gVariables.fn_toneOneProbabilitySet( float(argument) )
                    print "GUICheck: Argument value read from Queue: ", argument
                    Training.gVariables.logger.debug( str( "GUICheck: Argument value read from Queue: " + str(argument) ) )
                elif (index == 30):
                    print "GUICheck: 'Recalibrate Camera' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Recalibrate Camera' message" )
                    Training.gVariables.videoDet.calibrateCircle()
                    pass
                elif (index == 31):
                    print "GUICheck: 'Save State' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Save State' message" )
                    Training.gVariables.fn_savestate();
                    pass
                elif (index == 32):
                    print "GUICheck: 'Require Stillness' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Require Stillness' message" )
                    Training.gVariables.requireStillness = int(a)
                    print "Arg: %d" % int(a)
                    pass
                elif (index == 33):
                    print "GUICheck: 'current_type' message"
                    Training.gVariables.logger.debug( "GUICheck: 'current_type' message" )
                    Training.gVariables.current_mode = a
                    print "Current type: %s" % a
                    self.saveToInternalVars(a)
                elif (index == 34):
                    print "GUICheck: 'Noise Filtering' message"
                    Training.gVariables.logger.debug( "GUICheck: 'Noise Filtering' message" )
                    a = Training.gVariables.videoDet.getNoiseFiltering()
                    if (a):
                        Training.gVariables.videoDet.setNoiseFiltering(False)
                    else:
                        Training.gVariables.videoDet.setNoiseFiltering(True)
                    pass
                pass
                #print "GUICheck: done."
                Training.gVariables.logger.debug( "GUICheck: done." )
    
    
    
    
    def noGUIInputLoop(self):
        def printInstructions():
            print "--------------------------------------------------------"
            print "Command keys:"
            print "--------------------------------------------------------"
            print "Key d : Drop of water"
            print "Key r : Reward (drop + count trial as successfull)"
            print "Key o : Open Valve"
            print "Key c : Close Valve"
            print "Key k : Start / Stop Training"
            print "Key p : Pause / Resume Training"
            print "Key q : Exit Training"
            print "--------------------------------------------------------"
        #Starts capturing user Input from command-line console.
        time.sleep(1.0)
        print "No GUI mode: Initializing..."
        self.gVariables.logger.info( "No GUI mode: Initializing Command-line interface..." )
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
            self.gVariables.logger.warning( "Error capturing input." )
        time.sleep(1.0)
        printInstructions()
        while self.gVariables.programRunning == 1:
            try:
                key = sys.stdin.read(1)#cv2.waitKey(100) #in miliseconds
                if (key == 'd' or key == 'D'):
                    printInstructions()
                    print "d : Drop"
                    self.gVariables.logger.info( "Command executed by user: Drop" )
                    self.gVariables.fn_giveDrop()
                if (key == 'r' or key == 'R'):
                    printInstructions()
                    print "r : Reward"
                    self.gVariables.logger.info( "Command executed by user: Reward" )
                    self.gVariables.fn_giveReward()
                if (key == 'o' or key == 'O'):
                    printInstructions()
                    print "o : Open"
                    self.gVariables.logger.info( "Command executed by user: Open" )
                    self.gVariables.fn_openValve()
                if (key == 'c' or key == 'C'):
                    printInstructions()
                    print "c : Close"
                    self.gVariables.logger.info( "Command executed by user: Close" )
                    self.gVariables.fn_closeValve()
                if (key == 'k' or key == 'K'):
                    printInstructions()
                    print "k : Start / Stop Training"
                    self.gVariables.logger.info( "Command executed by user: Start / Stop Training" )
                    self.gVariables.fn_startStopTraining(0)
                if (key == 'p' or key == 'P'):
                    printInstructions()
                    print "p : Pause / Resume Training"
                    self.gVariables.logger.info( "Command executed by user: Pause / Resume Training" )
                    self.gVariables.fn_pauseResumeTraining(0)
                if (key == 'q' or key == 'Q'):
                    printInstructions()
                    print "q : Quit Training"
                    self.gVariables.logger.info( "Command executed by user: Quit Training" )
                    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
                    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
                    self.exitTraining()
                    return;
            except:
                pass
    
    def mainLoopFunction(self):
        DISPLAY_INTERVAL = 2
        counter_val = 0
        
        while(self.gVariables.programRunning == 1):
                    if (self.gVariables.programRunning == 0):
                        print "Exiting main loop."
                        return;
                    time.sleep(Training.gVariables.LOOP_FUNCTION_SLEEP_TIME)
                    self.GUICheck() #check if any GUI input was received
                    self.trialLoop()  #
                    if (counter_val == DISPLAY_INTERVAL):
                        self.updateDisplayInfo();
                        counter_val = 0;
                    counter_val+=1;


if __name__ == '__main__':
    a = Training()
    #while (True):
    #    time.sleep(0.3)
    #    print "x: %d        y: %d" % ( a.gVariables.videoDet.getInstantX() , a.gVariables.videoDet.getInstantY() )
    pass
