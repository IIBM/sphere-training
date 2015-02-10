#!/usr/bin/env python
# -*- coding: utf-8 -*-


import gtk
import gtk.glade
from argparse import Action
import logging
logger = logging.getLogger('userInterface_glade')
import track_bola_utils


class GUIGTK_Class():
        type_pavlov = 0;
        type_skinner = 0
        type_ocond = 0
        type_discr = 0
        requireStillnessVar = 0;
        
        current_type = ""
        
        orig_toneend = 0;
        orig_mvntwinend = 0;
        
        class Empty_cl():
            #Used to save our variables' previous states.
            def __init__(self):
                pass
        
        def __init__(self, startEv = False):
                self.startEv = startEv
        
        def initAll(self):
                handlers = {
                            "onDeleteWindow": self.action_exit,
                            "destroy": self.action_exit,
                            "clicked_drop": self.action_drop,
                            "clicked_savestate": self.action_savestate,
                            "clicked_reward": self.action_reward,
                            "clicked_open": self.action_open,
                            "clicked_close": self.action_close,
                            "clicked_start": self.action_startTr,
                            "clicked_pause": self.action_pauseTr,
                            "clicked_exit": self.action_exit,
                            "clicked_help": self.action_help,
                            "clicked_comment": self.action_commentFr,
                            "clicked_trialevents": self.action_trialEventsFr,
                            "clicked_parameters": self.action_parametersFr,
                            "clicked_applyTE": self.action_applyTE,
                            "clicked_applyP": self.action_applyP,
                            "clicked_shfeedback": self.action_shfeedback,
                            "clicked_shtracking": self.action_shtracking,
                            "clicked_recalibratec": self.action_recalibratec,
                            "clicked_testT1": self.action_testT1,
                            "clicked_testT2": self.action_testT2,
                            "clicked_applyC": self.action_applyC,
                            "mainwindow_destroy": self.action_exitX,
                            "trialeventswindow_destroy": self.action_hideTE,
                            "parameterswindow_destroy": self.action_hideP,
                            "commentswindow_destroy": self.action_hideC,
                            "helpWindow_destroy": self.action_hideHelp,
                            "mainwindow_keypress": self.action_keypress, 
                            
                        }
                logger.info( "Starting userInterface_glade variables and .glade file:")
                
                self.customVariablesInit()
                self.gladefile = "userInputv2.glade"
                import sys
                #repair inconsistent path:
                self.gladefile = "../modules/userInputv2.glade"
                
                logger.info( self.gladefile )
                
                self.glade = gtk.Builder()
                
                self.glade.add_from_file(self.gladefile)
                #para solucionar problema viewport: http://www.daa.com.au/pipermail/pygtk/2009-June/017189.html
                self.glade.connect_signals(handlers)
                self.glade.get_object("mainWindow").show_all()
                #self.glade.get_object("helpWindow").set_size_request(600,600)
                
                #gray color on one entry:
                #clr = gtk.gdk.Color(red = 200, green = 200, blue = 200);
                clr = gtk.gdk.Color('#ddd') #gray color, so users know that it isn't editable
                #self.glade.get_object("entryToneStart").modify_text(0, clr);
                self.glade.get_object("entryToneStart").modify_base(0, clr);
                
                
                
                if (self.startEv == True):
                    gtk.main()

        def on_mainWindow_delete_event(self, widget, event):
                gtk.main_quit()
        
        def overrideaction_drop(self):
            logger.info( "Default: Drop" )
            return 0
        
        def overrideaction_savestate(self):
            logger.info( "Default: Save State" )
            return 0
        
        def overrideaction_reward(self):
            logger.info( "Default: Reward" )
            return 0
        
        def overrideaction_open(self):
            logger.info( "Default: Open" )
            return 0
        
        def overrideaction_close(self):
            logger.info( "Default: Close" )
            return 0
        
        def overrideaction_startTraining(self):
                #print "Start / Stop training"
                logger.info( "Default: Start Training" )
                return 0
        
        def overrideaction_stopTraining(self):
                #print "Start / Stop training"
                logger.info( "Default: Stop Training" )
                return 0
        
        def overrideaction_pauseTraining(self):
                #print "Pause / Resume training"
                logger.info( "Default: Pause Training" )
                return 0
        
        def overrideaction_resumeTraining(self):
                #print "Pause / Resume training"
                logger.info( "Default: Resume Training"  )
                return 0
        
        def overrideaction_applyTE(self):
            logger.info( "Default: Apply Trials Events" )
            return 0
        
        def overrideaction_applyP(self):
            logger.info( "Default: Parameters" )
            return 0
        
        def overrideaction_applyC(self):
            logger.info( "Default: Comments" )
            return 0
        
        def overrideaction_showfeedback(self):
            logger.info( "Default: Show Feedback" )
            return 0
        
        def overrideaction_hidefeedback(self):
            logger.info( "Default: Hide Feedback" )
            return 0
        
        def overrideaction_showtracking(self):
            logger.info( "Default: Show Tracking" )
            return 0
        
        def overrideaction_hidetracking(self):
            logger.info( "Default: Hide Tracking" )
            return 0
        
        def overrideaction_recalibratec(self):
            logger.info( "Default: recalibrate camera" )
            pass
        
        def overrideaction_testT1(self):
            logger.info( "Default: Test T1" )
            return 0
        
        def overrideaction_testT2(self):
            logger.info( "Default: Test T2" )
            return 0
        
        def customVariablesInit(self):
                self.previousVars = self.Empty_cl()
                self.start = 0 #initially stopped.
                self.pause = 0 #initially "not paused"
                self.feedback = 0 #initially showing feedback graphics.
                self.tracking = 0 #initially showing tracking lines
                self.comment = ""
                self.frequencyTone1 = 0
                self.frequencyTone2 = 0
                self.movementAmount = 0
                self.movementMethod = 0
                self.movementTime = 0
                self.idleTime = 0
                self.toneStart = 0
                self.toneEnd = 0
                self.movementWindowStart = 0
                self.movementWindowEnd = 0
                self.interTrialStart = 0
                self.interTrialEnd = 0
                self.probabilityToneOne = 0
                self.type_pavlov = 0
                self.type_skinner = 0
                self.type_ocond = 0
                self.type_discr = 0
        
        def commitInitialData(self):
            #Set graphic elements' data with the variables that has been passed from the upper class that is executing this module.
            logger.info( "Setting userInterface_glade initial data.")
            logger.info( str( self.toneStart ) )
            logger.info( str( self.toneEnd ) )
            logger.info( str( self.movementWindowStart ) )
            logger.info( str( self.movementWindowEnd ) )
            logger.info( str( self.interTrialStart ) )
            logger.info( str( self.interTrialEnd ) )
            logger.info( str( self.probabilityToneOne ) )
            logger.info( str( self.frequencyTone1 ) )
            logger.info( str( self.frequencyTone2 ) )
            logger.info( str( self.movementAmount ) )
            logger.info( str( self.movementMethod ) )
            logger.info( str( self.movementTime ) )
            logger.info( str( self.idleTime ) )
            logger.info( str( self.comment ) )
            self.glade.get_object("entryToneStart").set_text( str(self.toneStart) )
            self.glade.get_object("entryToneEnd").set_text( str(self.toneEnd) )
            self.glade.get_object("entryMvmntWinStart").set_text( str(self.movementWindowStart) )
            self.glade.get_object("entryMvmntWinEnd").set_text( str(self.movementWindowEnd) )
            self.glade.get_object("entryITStart").set_text( str(self.interTrialStart) )
            self.glade.get_object("entryITEnd").set_text( str(self.interTrialEnd) )
            self.glade.get_object("entryProbab1").set_text( str(self.probabilityToneOne) )
            self.glade.get_object("entryTone1").set_text( str(self.frequencyTone1) )
            self.glade.get_object("entryTone2").set_text( str(self.frequencyTone2) )
            self.glade.get_object("entryMovementAmount").set_text( str(self.movementAmount) )
            self.glade.get_object("entryMethod").set_text( str(self.movementMethod) )
            self.glade.get_object("entryMovementTime").set_text( str(self.movementTime) )
            self.glade.get_object("entryIdleTime").set_text( str(self.idleTime) )
            self.glade.get_object("entryCommentTr").set_text( str(self.comment) )
            
            self.orig_mvntwinend = self.movementWindowEnd
            self.orig_toneend = self.toneEnd
            
            self.resetGUIElements();
            self.setPavlovVars();
            self.setSkinnerVars();
            self.setOCVars();
            self.setDiscrVars();
            
            self.glade.get_object("checkbuttonRequireS").set_active(True);
            if self.requireStillnessVar == 1: #pending: get this var from config file
                 self.glade.get_object("checkbuttonRequireS").set_active(True);
                 print "stillness 1"
            else:
                self.glade.get_object("checkbuttonRequireS").set_active(False);
                print "stillness 0"
            
            logger.info( "   Done: Setting userInterface_glade initial data.")
            gtk.main() #probably not launched before. Launching gtk.main
            pass
        
        def setPavlovVars(self):
            if (self.type_pavlov == 1):
                clr = gtk.gdk.Color('#ddd') #gray color, so users know that it isn't editable
                #self.glade.get_object("entryToneStart").modify_text(0, clr);
                self.glade.get_object("entryMvmntWinStart").modify_base(0, clr);
                self.glade.get_object("entryMvmntWinEnd").modify_base(0, clr);
                self.glade.get_object("entryMvmntWinStart").set_editable(False)
                self.glade.get_object("entryMvmntWinEnd").set_editable(False)
            else:
                clr = gtk.gdk.Color('#fff') #gray color, so users know that it isn't editable
                #self.glade.get_object("entryToneStart").modify_text(0, clr);
                self.glade.get_object("entryMvmntWinStart").modify_base(0, clr);
                self.glade.get_object("entryMvmntWinStart").set_editable(True)
                self.glade.get_object("entryMvmntWinEnd").modify_base(0, clr);
                self.glade.get_object("entryMvmntWinEnd").set_editable(True)
        
        def setSkinnerVars(self):
            print "skinner vars."
            if (self.type_skinner == 1):
                clr = gtk.gdk.Color('#ddd') #gray color, so users know that it isn't editable
                #self.glade.get_object("entryToneStart").modify_text(0, clr);
                self.glade.get_object("entryTone1").modify_base(0, clr);
                self.glade.get_object("entryTone1").set_editable(False)
                self.glade.get_object("entryTone2").modify_base(0, clr);
                self.glade.get_object("entryTone2").set_editable(False)
            else:
                clr = gtk.gdk.Color('#fff') #gray color, so users know that it isn't editable
                #self.glade.get_object("entryToneStart").modify_text(0, clr);
                self.glade.get_object("entryTone1").modify_base(0, clr);
                self.glade.get_object("entryTone1").set_editable(True)
                self.glade.get_object("entryTone2").modify_base(0, clr);
                self.glade.get_object("entryTone2").set_editable(True)
        
        def action_keypress(self, widget, event):
            #print "keypress"
            keyname = gtk.gdk.keyval_name(event.keyval)
            logger.info( str( keyname ) )
            #print keyname
            if (keyname == 'd' or keyname == 'D'):
                self.action_drop(0)
            elif (keyname == 'r' or keyname == 'R'):
                self.action_reward(0)
            elif (keyname == 'o' or keyname == 'O'):
                self.action_open(0)
            elif (keyname == 'c' or keyname == 'C'):
                self.action_close(0)
            elif (keyname == 'k' or keyname == 'K'):
                self.action_startTr(0)
            elif (keyname == 'p' or keyname == 'P'):
                self.action_pauseTr(0)
        
        def action_dummy(button, args):
                print "Dummy fn."
                logger.info( "Dummy fn." )

        def action_drop(self, button):
                #print "Drop"
                try:
                    self.overrideaction_drop()
                except:
                    logger.info( "Drop: An error ocurred." )
        
        def action_savestate(self, button):
                #print "SS"
                try:
                    self.overrideaction_savestate()
                except:
                    logger.info( "Save State: An error ocurred." )
        
        def action_reward(self, button):
                try:
                    self.overrideaction_reward()
                except:
                    logger.info( "Reward: An error ocurred." )
        
        def action_open(self, button):
                try:
                    self.overrideaction_open()
                except:
                    logger.info( "Open: An error ocurred." )
        
        def action_close(self, button):
            try:
                self.overrideaction_close()
            except:
                logger.info( "Close: An error ocurred." )
        
        def action_startTr(self, button):
                if ( self.start == 0):
                    #print "Default: Start Training"
                    try:
                        self.overrideaction_startTraining()
                    except:
                        logger.info( "StartTr: An error ocurred." )
                    self.start = 1
                else:
                    #print "Default: Stop Training"
                    try:
                        self.overrideaction_stopTraining()
                    except:
                        logger.info( "StartTr: An error ocurred." )
                    self.start = 0
        
        def action_pauseTr(self, button):
            if ( self.pause == 0):
                    #print "Default: Pause Training"
                    try:
                        self.overrideaction_pauseTraining()
                    except:
                        logger.info( "PauseTr: An error ocurred." )
                    self.pause = 1
            else:
                    #print "Default: Resume Training"
                    try:
                        self.overrideaction_resumeTraining()
                    except:
                        logger.info( "PauseTr: An error ocurred." )
                    self.pause = 0
            return 0
        
        def action_exit(self, button):
                #triggered from "Exit" button
                try:
                    self.overrideaction_exit()
                except:
                    logger.info( "Exit: No override for exit." )
                    self.__exitAll()
        
        def action_help(self, button):
                #triggered from "Exit" button
                self.glade.get_object("helpWindow").show_all()
                print "Help button."
        
        def __exitAll(self):
                print "Exit Training"
                logger.info( "Exit Training" )
                try:
                    import os
                    os._exit(0)
                    gtk.main_quit()
                except:
                    pass
        
        def saveTrialEventsPreviousState(self):
            self.__rawTEInput()
            self.previousVars.toneStart = self.toneStart
            self.previousVars.toneEnd = self.toneEnd
            self.previousVars.movementWindowStart = self.movementWindowStart
            self.previousVars.movementWindowEnd = self.movementWindowEnd
            self.previousVars.interTrialStart = self.interTrialStart
            self.previousVars.interTrialEnd = self.interTrialEnd
            self.previousVars.probabilityToneOne = self.probabilityToneOne
            print "Trial Events: Previous states saved."
            pass
        
        def resetGUIElements(self):
            self.current_type = ""
            clr = gtk.gdk.Color('#fff') #white color, editable mode for all.
            self.glade.get_object("entryTone1").set_editable(True);
            self.glade.get_object("entryTone1").modify_base(0, clr);
            
            self.glade.get_object("entryTone2").set_editable(True);
            self.glade.get_object("entryTone2").modify_base(0, clr);
            
            self.glade.get_object("entryMovementAmount").set_editable(True);
            self.glade.get_object("entryMovementAmount").modify_base(0, clr);
            
            self.glade.get_object("entryMethod").set_editable(True);
            self.glade.get_object("entryMethod").modify_base(0, clr);
            
            self.glade.get_object("entryMovementTime").set_editable(True);
            self.glade.get_object("entryMovementTime").modify_base(0, clr);
            
            self.glade.get_object("entryIdleTime").set_editable(True);
            self.glade.get_object("entryIdleTime").modify_base(0, clr);
            
            self.glade.get_object("entryToneEnd").set_editable(True);
            self.glade.get_object("entryToneEnd").modify_base(0, clr);
            
            self.glade.get_object("entryMvmntWinStart").set_editable(True);
            self.glade.get_object("entryMvmntWinStart").modify_base(0, clr);
            
            self.glade.get_object("entryMvmntWinEnd").set_editable(True);
            self.glade.get_object("entryMvmntWinEnd").modify_base(0, clr);
            self.glade.get_object("entryMvmntWinEnd").set_text( str( self.orig_mvntwinend ) )
            
            self.glade.get_object("entryToneEnd").set_editable(True);
            self.glade.get_object("entryToneEnd").modify_base(0, clr);
            self.glade.get_object("entryToneEnd").set_text( str( self.orig_toneend ) )
            
            self.glade.get_object("entryProbab1").set_editable(True);
            self.glade.get_object("entryProbab1").modify_base(0, clr);
            
            if (self.type_pavlov == 1):
                self.glade.get_object("checkbuttonPavlov").set_active(True);
            else:
                self.glade.get_object("checkbuttonPavlov").set_active(False);
            
            if (self.type_skinner == 1):
                self.glade.get_object("checkbuttonSkinner").set_active(True);
            else:
                self.glade.get_object("checkbuttonSkinner").set_active(False);
            
            if (self.type_ocond == 1):
                self.glade.get_object("checkbuttonOC").set_active(True);
            else:
                self.glade.get_object("checkbuttonOC").set_active(False);
            
            if (self.type_discr == 1):
                self.glade.get_object("checkbuttonDiscr").set_active(True);
            else:
                self.glade.get_object("checkbuttonDiscr").set_active(False);
            
            pass
        
        def setPavlovVars(self):
            if (self.type_pavlov == 0):
                return;
            clr = gtk.gdk.Color('#ddd')
            
            self.glade.get_object("entryMvmntWinEnd").set_editable(True);
            self.glade.get_object("entryMvmntWinEnd").set_text( str( self.glade.get_object("entryMvmntWinStart").get_text() ) )
            self.glade.get_object("entryMvmntWinEnd").set_editable(False);
            self.glade.get_object("entryMvmntWinEnd").modify_base(0, clr);
            
            self.glade.get_object("entryMvmntWinStart").set_editable(False);
            self.glade.get_object("entryMvmntWinStart").modify_base(0, clr);
            
            self.glade.get_object("entryTone2").set_editable(False);
            self.glade.get_object("entryTone2").modify_base(0, clr);
            
            self.glade.get_object("entryMovementAmount").set_editable(False);
            self.glade.get_object("entryMovementAmount").modify_base(0, clr);
            
            self.glade.get_object("entryMethod").set_editable(False);
            self.glade.get_object("entryMethod").modify_base(0, clr);
            
            self.glade.get_object("entryMovementTime").set_editable(False);
            self.glade.get_object("entryMovementTime").modify_base(0, clr);
            
            self.glade.get_object("entryIdleTime").set_editable(False);
            self.glade.get_object("entryIdleTime").modify_base(0, clr);
            
            self.glade.get_object("entryProbab1").set_editable(False);
            self.glade.get_object("entryProbab1").modify_base(0, clr);
            
            self.current_type = "pavlov"
            pass
        
        def setSkinnerVars(self):
            if (self.type_skinner == 0):
                return;
            clr = gtk.gdk.Color('#ddd')
            
            
            self.glade.get_object("entryTone1").set_editable(False);
            self.glade.get_object("entryTone1").modify_base(0, clr);
            
            self.glade.get_object("entryTone2").set_editable(False);
            self.glade.get_object("entryTone2").modify_base(0, clr);
            
            self.glade.get_object("entryToneEnd").set_editable(True);
            self.glade.get_object("entryToneEnd").set_text( str( 0.0 ) )
            self.glade.get_object("entryToneEnd").set_editable(False);
            self.glade.get_object("entryToneEnd").modify_base(0, clr);
            
            self.glade.get_object("entryIdleTime").set_editable(False);
            self.glade.get_object("entryIdleTime").modify_base(0, clr);
            
            self.glade.get_object("entryProbab1").set_editable(False);
            self.glade.get_object("entryProbab1").modify_base(0, clr);
            
            self.current_type = "skinner"
            pass
        
        def setOCVars(self):
            if (self.type_ocond == 0):
                return;
            clr = gtk.gdk.Color('#ddd')
            
            self.glade.get_object("entryTone2").set_editable(False);
            self.glade.get_object("entryTone2").modify_base(0, clr);
            
            self.glade.get_object("entryIdleTime").set_editable(False);
            self.glade.get_object("entryIdleTime").modify_base(0, clr);
            
            self.glade.get_object("entryProbab1").set_editable(False);
            self.glade.get_object("entryProbab1").modify_base(0, clr);
            
            self.current_type = "oc"
            pass
        
        def setDiscrVars(self):
            if (self.type_discr == 0):
                return;
            self.current_type = "discr"
            pass
        
        def saveParametersPreviousState(self):
            self.__rawPInput()
            self.previousVars.frequencyTone1 = self.frequencyTone1
            self.previousVars.frequencyTone2 = self.frequencyTone2
            self.previousVars.movementAmount = self.movementAmount
            self.previousVars.movementMethod = self.movementMethod
            self.previousVars.movementTime = self.movementTime
            self.previousVars.idleTime = self.idleTime
            print "Parameters: Previous states saved."
            pass
        
        def checkTrialEventsVarsConsistency(self):
            
            
            try:
                a = float(self.toneStart)
            except:
                #incorrect input. Returning to previous state.
                self.toneStart = self.previousVars.toneStart
                self.glade.get_object("entryToneStart").set_text( str( self.previousVars.toneStart ) )
                print "Bad input: toneStart to previous var."
            try:
                a = float(self.toneEnd)
            except:
                #incorrect input. Returning to previous state.
                self.toneEnd = self.previousVars.toneEnd
                self.glade.get_object("entryToneEnd").set_text( str( self.previousVars.toneEnd ) )
                print "Bad input: toneEnd to previous var."
            try:
                a = float(self.movementWindowStart)
            except:
                #incorrect input. Returning to previous state.
                self.movementWindowStart = self.previousVars.movementWindowStart
                self.glade.get_object("entryMvmntWinStart").set_text( str( self.previousVars.movementWindowStart ) )
                print "Bad input: movementWindowStart to previous var."
            try:
                a = float(self.movementWindowEnd)
            except:
                #incorrect input. Returning to previous state.
                self.movementWindowEnd = self.previousVars.movementWindowEnd
                self.glade.get_object("entryMvmntWinEnd").set_text( str( self.previousVars.movementWindowEnd ) )
                print "Bad input: movementWindowEnd to previous var."
            try:
                a = float(self.interTrialStart)
            except:
                #incorrect input. Returning to previous state.
                self.interTrialStart = self.previousVars.interTrialStart
                self.glade.get_object("entryITStart").set_text( str( self.previousVars.interTrialStart ) )
                print "Bad input: interTrialStart to previous var."
            try:
                a = float(self.interTrialEnd)
            except:
                #incorrect input. Returning to previous state.
                self.interTrialEnd = self.previousVars.interTrialEnd
                self.glade.get_object("entryITEnd").set_text( str( self.previousVars.interTrialEnd ) )
                print "Bad input: interTrialEnd to previous var."
            try:
                a = float(self.probabilityToneOne)
            except:
                #incorrect input. Returning to previous state.
                self.probabilityToneOne = self.previousVars.probabilityToneOne
                self.glade.get_object("entryProbab1").set_text( str( self.previousVars.probabilityToneOne ) )
                print "Bad input: probabilityToneOne to previous var."
            pass
        
        def __rawPInput(self):
                self.frequencyTone1 = self.glade.get_object("entryTone1").get_text()
                self.frequencyTone2 = self.glade.get_object("entryTone2").get_text()
                self.movementAmount = self.glade.get_object("entryMovementAmount").get_text()
                self.movementMethod = self.glade.get_object("entryMethod").get_text()
                self.movementTime = self.glade.get_object("entryMovementTime").get_text()
                self.idleTime = self.glade.get_object("entryIdleTime").get_text()
                print "Raw P Input done."
                pass
        
        def __TE_modes(self):
                
                self.modeHasChanged = 0;
                temppavlov = self.glade.get_object("checkbuttonPavlov").get_active()
                
                if (temppavlov == False):
                    if (self.type_pavlov == 1):
                        self.modeHasChanged = 1;
                    self.type_pavlov = 0;
                else:
                    if (self.type_pavlov == 0):
                        self.modeHasChanged = 1;
                    self.type_pavlov = 1;
                
                tempskinner = self.glade.get_object("checkbuttonSkinner").get_active()
                
                if (tempskinner == False):
                    if (self.type_skinner == 1):
                        self.modeHasChanged = 1;
                    self.type_skinner = 0;
                else:
                    if (self.type_skinner == 0):
                        self.modeHasChanged = 1;
                    self.type_skinner = 1;
                
                tempocond = self.glade.get_object("checkbuttonOC").get_active()
                
                if (tempocond == False):
                    if (self.type_ocond == 1):
                        self.modeHasChanged = 1;
                    self.type_ocond = 0;
                else:
                    if (self.type_ocond == 0):
                        self.modeHasChanged = 1;
                    self.type_ocond = 1;
                
                tempdiscr = self.glade.get_object("checkbuttonDiscr").get_active()
                
                if (tempdiscr == False):
                    if (self.type_discr == 1):
                        self.modeHasChanged = 1;
                    self.type_discr = 0;
                else:
                    if (self.type_discr == 0):
                        self.modeHasChanged = 1;
                    self.type_discr = 1;
                
                
                if (self.type_pavlov == 1):
                    self.type_skinner = 0;
                    self.type_ocond = 0;
                    self.type_discr = 0;
                
                if (self.type_skinner == 1):
                    self.type_pavlov = 0;
                    self.type_ocond = 0;
                    self.type_discr = 0;
                
                if (self.type_ocond == 1):
                    self.type_pavlov = 0;
                    self.type_skinner = 0;
                    self.type_discr = 0;
                
                if (self.type_discr == 1):
                    self.type_pavlov = 0;
                    self.type_ocond = 0;
                    self.type_skinner = 0;
                
                #print "mode has changed: %d" % self.modeHasChanged
                #print self.type_pavlov
                #print self.type_skinner
                #print self.type_ocond
                #print self.type_discr
                
                if (self.modeHasChanged == 1):
                    self.resetGUIElements()
                    self.setPavlovVars()
                    self.setSkinnerVars()
                    self.setOCVars()
                    self.setDiscrVars()
                
                
        
        def __rawTEInput(self):
                self.__TE_modes();
                
                self.toneStart = self.glade.get_object("entryToneStart").get_text()
                self.toneEnd = self.glade.get_object("entryToneEnd").get_text()
                self.movementWindowStart = self.glade.get_object("entryMvmntWinStart").get_text()
                self.movementWindowEnd = self.glade.get_object("entryMvmntWinEnd").get_text()
                self.interTrialStart = self.glade.get_object("entryITStart").get_text()
                self.interTrialEnd = self.glade.get_object("entryITEnd").get_text()
                self.probabilityToneOne = self.glade.get_object("entryProbab1").get_text()
                
                tempreq = self.glade.get_object("checkbuttonRequireS").get_active()
                    
                if (tempreq == False):
                    self.requireStillnessVar = 0
                else:
                    self.requireStillnessVar = 1 
                
                print "Raw TE Input done."
                pass
        
        def checkParametersVarsConsistency(self):
            try:
                a = float(self.frequencyTone1)
            except:
                #incorrect input. Returning to previous state.
                self.frequencyTone1 = self.previousVars.frequencyTone1
                self.glade.get_object("entryTone1").set_text( str( self.previousVars.frequencyTone1 ) )
                print "Bad input: frequencyTone1 to previous var."
            try:
                a = float(self.frequencyTone2)
            except:
                #incorrect input. Returning to previous state.
                self.frequencyTone2 = self.previousVars.frequencyTone2
                self.glade.get_object("entryTone2").set_text( str( self.previousVars.frequencyTone2 ) )
                print "Bad input: frequencyTone2 to previous var."
            try:
                a = float(self.movementAmount)
            except:
                #incorrect input. Returning to previous state.
                self.movementAmount = self.previousVars.movementAmount
                self.glade.get_object("entryMovementAmount").set_text( str( self.previousVars.movementAmount ) )
                print "Bad input: movementAmount to previous var."
            try:
                a = float(self.movementMethod)
            except:
                #incorrect input. Returning to previous state.
                self.movementMethod = self.previousVars.movementMethod
                self.glade.get_object("entryMethod").set_text( str( self.previousVars.movementMethod ) )
                print "Bad input: movementMethod to previous var."
            try:
                a = float(self.movementTime)
            except:
                #incorrect input. Returning to previous state.
                self.movementTime = self.previousVars.movementTime
                self.glade.get_object("entryMovementTime").set_text( str( self.previousVars.movementTime ) )
                print "Bad input: movementTime to previous var."
            try:
                a = float(self.idleTime)
            except:
                #incorrect input. Returning to previous state.
                self.idleTime = self.previousVars.idleTime
                self.glade.get_object("entryIdleTime").set_text( str( self.previousVars.idleTime ) )
                print "Bad input: idleTime to previous var."
            
            pass
        
        def action_exitX(self, button, event):
                #triggered from the "x" window button
                self.action_exit(button)
                logger.info( "Pressed X Close button; exiting." )
                #self.__exitAll()
        
        def action_commentFr(self, button):
                logger.info( "Comment about this training" )
                self.glade.get_object("commentWin").show_all()
        
        def action_trialEventsFr(self, button):
                logger.info( "Trial Events frame" )
                self.saveTrialEventsPreviousState()
                self.glade.get_object("trialEventsWin").show_all()
        
        def action_parametersFr(self, button):
                logger.info( "Parameters frame" )
                self.saveParametersPreviousState()
                self.glade.get_object("parametersWin").show_all()
        
        def action_applyTE(self, button):
                logger.info( "Applying Trial Events variables" )
                
                self.__rawTEInput()
                
                self.checkTrialEventsVarsConsistency() #if bad input, return to previous state...
                
                logger.info( self.toneStart )
                logger.info( self.toneEnd )
                logger.info( self.movementWindowStart )
                logger.info( self.movementWindowEnd )
                logger.info( self.interTrialStart )
                logger.info( self.interTrialEnd )
                logger.info( self.probabilityToneOne )
                
                self.saveTrialEventsPreviousState()
                try:
                    self.overrideaction_applyTE()
                except:
                    logger.info( "ApplyTE: An error ocurred." )
        
        def action_applyP(self, button):
                logger.info( "Applying Parameters variables" )
                
                self.__rawPInput()
                
                self.checkParametersVarsConsistency()
                
                logger.info( self.frequencyTone1 )
                logger.info( self.frequencyTone2 )
                logger.info( self.movementAmount )
                logger.info( self.movementMethod )
                logger.info( self.movementTime )
                logger.info( self.idleTime )
                
                self.saveParametersPreviousState()
                try:
                    self.overrideaction_applyP()
                except:
                    logger.info( "ApplyP: An error ocurred." )
        
        def action_applyC(self, button):
                logger.info( "Applying Comment" )
                #print self.glade.get_object("entryCommentTr").get_text()
                #print self.glade.get_object("entryCommentTr").set_text("test")
                #self.comment = self.glade.get_object("entryCommentTr").get_text()
                self.comment = unicode(self.glade.get_object("entryCommentTr").get_text() , "utf-8")
                logger.info( self.comment )
                try:
                    self.overrideaction_applyC()
                except:
                    logger.info( "ApplyC: An error ocurred." )
        
        def action_shfeedback(self, button):
                #print "Show / Hide Feedback"
                if ( self.feedback == 0):
                    #print "Hide Feedback"
                    try:
                        self.overrideaction_hidefeedback()
                    except:
                        logger.info( "shfeedback: An error ocurred." )
                    self.feedback = 1
                else:
                    #print "Show Feedback"
                    try:
                        self.overrideaction_showfeedback()
                    except:
                        logger.info( "shfeedback: An error ocurred." )
                    self.feedback = 0
        
        def action_shtracking(self, button):
                #print "Show / Hide Feedback"
                if ( self.tracking == 0):
                    #print "Hide Tracking"
                    try:
                        self.overrideaction_hidetracking()
                    except:
                        logger.info( "shtracking: An error ocurred." )
                    self.tracking = 1
                else:
                    #print "Show Tracking"
                    try:
                        self.overrideaction_showtracking()
                    except:
                        logger.info( "shtracking: An error ocurred." )
                    self.tracking = 0
        
        def action_recalibratec(self, button):
                try:
                    self.overrideaction_recalibratec()
                except:
                    logger.info( "Recalibrate Camera: An error ocurred." )
        
        def action_testT1(self, button):
                #print "Test T1"
                self.frequencyTone1 = self.glade.get_object("entryTone1").get_text()
                self.frequencyTone2 = self.glade.get_object("entryTone2").get_text()
                self.checkParametersVarsConsistency()
                self.saveParametersPreviousState()
                try:
                    self.overrideaction_testT1()
                except:
                    logger.info( "TestT1: An error ocurred." )
        
        def action_testT2(self, button):
                #print "Test T2"
                self.frequencyTone1 = self.glade.get_object("entryTone1").get_text()
                self.frequencyTone2 = self.glade.get_object("entryTone2").get_text()
                self.checkParametersVarsConsistency()
                self.saveParametersPreviousState()
                try:
                    self.overrideaction_testT2()
                except:
                    logger.info( "TestT2: An error ocurred." )
        
        def action_hideTE(self, button, event):
            self.glade.get_object("trialEventsWin").hide()
            return True;
        
        def action_hideP(self, button, event):
            self.glade.get_object("parametersWin").hide()
            return True;
        
        def action_hideC(self, button, event):
            self.glade.get_object("commentWin").hide()
            return True;
        
        def action_hideHelp(self, button, event):
            print "hidehelp"
            self.glade.get_object("helpWindow").hide()
            return True;


if __name__ == "__main__":
        # create a logging format
        dateformat = '%Y/%m/%d %H:%M:%S'
        formatter_str = '%(asctime)s.%(msecs)d - %(name)s - %(levelname)s - %(message)s'
        filename_to_log='logs/userInterface_glade.log'
        
        
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
        logger.addHandler(console)
        #===========================================================================
        
        logger.info('Start userInterface_glade Test')
        try:
                a = GUIGTK_Class(True)
                a.initAll()
        except KeyboardInterrupt:
                pass
        logger.info('End userInterface_glade Test')
