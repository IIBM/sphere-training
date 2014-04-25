#!/usr/bin/env python
# -*- coding: utf-8 -*-


import gtk
import gtk.glade
from argparse import Action
import logging
logger = logging.getLogger('userInterface_glade')

class GUIGTK_Class:
        def __init__(self):
                handlers = {
                            "onDeleteWindow": self.action_exit,
                            "destroy": self.action_exit,
                            "clicked_drop": self.action_drop,
                            "clicked_reward": self.action_reward,
                            "clicked_open": self.action_open,
                            "clicked_close": self.action_close,
                            "clicked_start": self.action_startTr,
                            "clicked_pause": self.action_pauseTr,
                            "clicked_exit": self.action_exit,
                            "clicked_comment": self.action_commentFr,
                            "clicked_trialevents": self.action_trialEventsFr,
                            "clicked_parameters": self.action_parametersFr,
                            "clicked_applyTE": self.action_applyTE,
                            "clicked_applyP": self.action_applyP,
                            "clicked_shfeedback": self.action_shfeedback,
                            "clicked_shtracking": self.action_shtracking,
                            "clicked_testT1": self.action_testT1,
                            "clicked_testT2": self.action_testT2,
                            "clicked_applyC": self.action_applyC,
                            "mainwindow_destroy": self.action_exitX,
                            "trialeventswindow_destroy": self.action_hideTE,
                            "parameterswindow_destroy": self.action_hideP,
                            "commentswindow_destroy": self.action_hideC,
                            "mainwindow_keypress": self.action_keypress, 
                            
                        }
                
                self.prepare_variables()
                self.gladefile = "userInputv2.glade"
                import sys
                #sys.path.insert(0, "/home/aimc/workspace/track-bola_eclipse/sphere-training/modules")
                #sys.path.append("../modules/")
                #sys.path.append( "/home/aimc/workspace/track-bola_eclipse/sphere-training/modules")
                #print sys.path[0]
                tempstr = sys.path[0]
                tempstr = tempstr.replace("/training", "/modules")
                #print tempstr
                
                self.gladefile = tempstr + "/userInputv2.glade"
                logging.info( self.gladefile )
                
                self.glade = gtk.Builder()
                
                self.glade.add_from_file(self.gladefile)
                self.glade.connect_signals(handlers)
                self.glade.get_object("mainWindow").show_all()

        def on_mainWindow_delete_event(self, widget, event):
                gtk.main_quit()
        
        def overrideaction_drop(self):
            logging.info( "Default: Drop" )
            return 0
        
        def overrideaction_reward(self):
            logging.info( "Default: Reward" )
            return 0
        
        def overrideaction_open(self):
            logging.info( "Default: Open" )
            return 0
        
        def overrideaction_close(self):
            logging.info( "Default: Close" )
            return 0
        
        def overrideaction_startTraining(self):
                #print "Start / Stop training"
                logging.info( "Default: Start Training" )
                return 0
        
        def overrideaction_stopTraining(self):
                #print "Start / Stop training"
                logging.info( "Default: Stop Training" )
                return 0
        
        def overrideaction_pauseTraining(self):
                #print "Pause / Resume training"
                logging.info( "Default: Pause Training" )
                return 0
        
        def overrideaction_resumeTraining(self):
                #print "Pause / Resume training"
                logging.info( "Default: Resume Training" )
                return 0
        
        def overrideaction_applyTE(self):
            logging.info( "Default: Apply Trials Events" )
            return 0
        
        def overrideaction_applyP(self):
            logging.info( "Default: Parameters" )
            return 0
        
        def overrideaction_applyC(self):
            logging.info( "Default: Comments" )
            return 0
        
        def overrideaction_showfeedback(self):
            logging.info( "Default: Show Feedback" )
            return 0
        
        def overrideaction_hidefeedback(self):
            logging.info( "Default: Hide Feedback" )
            return 0
        
        def overrideaction_showtracking(self):
            logging.info( "Default: Show Tracking" )
            return 0
        
        def overrideaction_hidetracking(self):
            logging.info( "Default: Hide Tracking" )
            return 0
        
        def overrideaction_testT1(self):
            logging.info( "Default: Test T1" )
            return 0
        
        def overrideaction_testT2(self):
            logging.info( "Default: Test T2" )
            return 0
        
        def prepare_variables(self):
                self.start = 0 #initially stopped.
                self.pause = 0 #initially "not paused"
                self.feedback = 0 #initially showing feedback graphics.
                self.tracking = 0 #initially showing tracking lines
        
        def action_keypress(self, widget, event):
            #print "keypress"
            keyname = gtk.gdk.keyval_name(event.keyval)
            logging.info( str( keyname ) )
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
                logging.info( "Dummy fn" )

        def action_drop(self, button):
                #print "Drop"
                try:
                    self.overrideaction_drop()
                except:
                    logging.info( "Drop: An error ocurred." )
        
        def action_reward(self, button):
                try:
                    self.overrideaction_reward()
                except:
                    logging.info( "Reward: An error ocurred." )
        
        def action_open(self, button):
                try:
                    self.overrideaction_open()
                except:
                    logging.info( "Open: An error ocurred." )
        
        def action_close(self, button):
            try:
                self.overrideaction_close()
            except:
                logging.info( "Close: An error ocurred." )
        
        def action_startTr(self, button):
                if ( self.start == 0):
                    #print "Default: Start Training"
                    try:
                        self.overrideaction_startTraining()
                    except:
                        logging.info( "StartTr: An error ocurred." )
                    self.start = 1
                else:
                    #print "Default: Stop Training"
                    try:
                        self.overrideaction_stopTraining()
                    except:
                        logging.info( "StartTr: An error ocurred." )
                    self.start = 0
        
        def action_pauseTr(self, button):
            if ( self.pause == 0):
                    #print "Default: Pause Training"
                    try:
                        self.overrideaction_pauseTraining()
                    except:
                        logging.info( "PauseTr: An error ocurred." )
                    self.pause = 1
            else:
                    #print "Default: Resume Training"
                    try:
                        self.overrideaction_resumeTraining()
                    except:
                        logging.info( "PauseTr: An error ocurred." )
                    self.pause = 0
            return 0
        
        def action_exit(self, button):
                #triggered from "Exit" button
                try:
                    self.overrideaction_exit()
                except:
                    logging.info( "Exit: No override for exit." )
                    self.__exitAll()
                #self.__exitAll()
        
        def __exitAll(self):
                print "Exit Training"
                logging.info( "Exit Training" )
                try:
                    import os
                    os._exit(0)
                    gtk.main_quit()
                except:
                    pass
        
        def action_exitX(self, button, event):
                #triggered from the "x" window button
                self.action_exit(button)
                logging.info( "Pressed X Close button; exiting." )
                #self.__exitAll()
        
        def action_commentFr(self, button):
                logging.info( "Comment about this training" )
                self.glade.get_object("commentWin").show_all()
        
        def action_trialEventsFr(self, button):
                logging.info( "Trial Events frame" )
                self.glade.get_object("trialEventsWin").show_all()
        
        def action_parametersFr(self, button):
                logging.info( "Parameters frame" )
                self.glade.get_object("parametersWin").show_all()
        
        def action_applyTE(self, button):
                logging.info( "Applying Trial Events variables" )
                self.toneStart = self.glade.get_object("entryToneStart").get_text()
                self.toneEnd = self.glade.get_object("entryToneEnd").get_text()
                self.movementWindowStart = self.glade.get_object("entryMvmntWinStart").get_text()
                self.movementWindowEnd = self.glade.get_object("entryMvmntWinEnd").get_text()
                self.interTrialStart = self.glade.get_object("entryITStart").get_text()
                self.interTrialEnd = self.glade.get_object("entryITEnd").get_text()
                self.probabilityToneOne = self.glade.get_object("entryProbab1").get_text()
                logging.info( self.toneStart )
                logging.info( self.toneEnd )
                logging.info( self.movementWindowStart )
                logging.info( self.movementWindowEnd )
                logging.info( self.interTrialStart )
                logging.info( self.interTrialEnd )
                logging.info( self.probabilityToneOne )
                try:
                    self.overrideaction_applyTE()
                except:
                    logging.info( "ApplyTE: An error ocurred." )
                
        
        def action_applyP(self, button):
                logging.info( "Applying Parameters variables" )
                self.frequencyTone1 = self.glade.get_object("entreTone1").get_text()
                self.frequencyTone2 = self.glade.get_object("entryTone2").get_text()
                self.movementAmount = self.glade.get_object("entryMovementAmount").get_text()
                self.movementMethod = self.glade.get_object("entryMethod").get_text()
                self.movementTime = self.glade.get_object("entryMovementTime").get_text()
                self.idleTime = self.glade.get_object("entryIdleTime").get_text()
                logging.info( self.frequencyTone1 )
                logging.info( self.frequencyTone2 )
                logging.info( self.movementAmount )
                logging.info( self.movementMethod )
                logging.info( self.movementTime )
                logging.info( self.idleTime )
                try:
                    self.overrideaction_applyP()
                except:
                    logging.info( "ApplyP: An error ocurred." )
        
        def action_applyC(self, button):
                logging.info( "Applying Comment" )
                #print self.glade.get_object("entryCommentTr").get_text()
                #print self.glade.get_object("entryCommentTr").set_text("test")
                #self.comment = self.glade.get_object("entryCommentTr").get_text()
                self.comment = unicode(self.glade.get_object("entryCommentTr").get_text() , "utf-8")
                logging.info( self.comment )
                try:
                    self.overrideaction_applyC()
                except:
                    logging.info( "ApplyC: An error ocurred." )
        
        
        
        def action_shfeedback(self, button):
                #print "Show / Hide Feedback"
                if ( self.feedback == 0):
                    #print "Hide Feedback"
                    try:
                        self.overrideaction_hidefeedback()
                    except:
                        logging.info( "shfeedback: An error ocurred." )
                    self.feedback = 1
                else:
                    #print "Show Feedback"
                    try:
                        self.overrideaction_showfeedback()
                    except:
                        logging.info( "shfeedback: An error ocurred." )
                    self.feedback = 0
        
        
        def action_shtracking(self, button):
                #print "Show / Hide Feedback"
                if ( self.tracking == 0):
                    #print "Hide Tracking"
                    try:
                        self.overrideaction_hidetracking()
                    except:
                        logging.info( "shtracking: An error ocurred." )
                    self.tracking = 1
                else:
                    #print "Show Tracking"
                    try:
                        self.overrideaction_showtracking()
                    except:
                        logging.info( "shtracking: An error ocurred." )
                    self.tracking = 0
        
        def action_testT1(self, button):
                #print "Test T1"
                self.frequencyTone1 = self.glade.get_object("entreTone1").get_text()
                self.frequencyTone2 = self.glade.get_object("entryTone2").get_text()
                try:
                    self.overrideaction_testT1()
                except:
                    logging.info( "TestT1: An error ocurred." )
        
        def action_testT2(self, button):
                #print "Test T2"
                self.frequencyTone1 = self.glade.get_object("entreTone1").get_text()
                self.frequencyTone2 = self.glade.get_object("entryTone2").get_text()
                try:
                    self.overrideaction_testT2()
                except:
                    logging.info( "TestT2: An error ocurred." )
        
        def action_hideTE(self, button, event):
            self.glade.get_object("trialEventsWin").hide()
            return True;
        
        def action_hideP(self, button, event):
            self.glade.get_object("parametersWin").hide()
            return True;
        
        def action_hideC(self, button, event):
            self.glade.get_object("commentWin").hide()
            return True;
        
        


if __name__ == "__main__":
        # create a logging format
        formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        dateformat = '%Y/%m/%d %I:%M:%S %p'
    
        logging.basicConfig(filename='logs/userInterface_glade.log', filemode='w',
            level=logging.DEBUG, format=formatter, datefmt = dateformat)
        logging.info('Start userInterface_glade Test')
        try:
                a = GUIGTK_Class()
                gtk.main()
        except KeyboardInterrupt:
                pass
        logging.info('End userInterface_glade Test')
