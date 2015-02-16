import os
import sys
import time
import logging
logger = logging.getLogger('userInterfaceAPI')
import track_bola_utils

class userInterface_API:
    usingTK = 0 #0: using GTk;   1: using TK
    jobList = 0 # message Job Queue between processes.
    ns = 0
    subj_list = [""]
    subj_name = ""
    type_pavlov = 0
    type_skinner = 0;
    type_ocond = 0;
    type_discr = 0;
    requireStillnessVar = 0;
    
    
    
    def getSubjName(self):
        
        
        if (self.usingTK == 0):
            logger.debug("GTK GUI Subject List started.")
            import autoCompleteEntry_gtk
            app = autoCompleteEntry_gtk.autoCompleteDialog(self.subj_list);
            app.initAll()
            self.subj_name = app.getSubjectName()
            app.exit()
            del app
            logger.debug("GUI Job ended.")
            logger.debug("GTK GUI Subject List ended.")
            pass
        elif (self.usingTK == 1):
            logger.debug("TK GUI Subject List started.")
            import autoCompleteEntry_tk
            app3 =  autoCompleteEntry_tk.autoCompleteEntry_tk(self.subj_list)
            app3.initAll()
            self.subj_name = app3.getSubjectName()
            app3.exit()
            del app3 #.
            logger.debug("TK GUI Subject List ended.")
        #print "API subj_name %s" % self.subj_name
        logger.debug( "subject name: %s" % self.subj_name )
        return self.subj_name
    
    def __init__(self, toStart = False):
        logger.info( "initializing userInterfaceAPI" )
        #Variables: setting up to 0 before assigning any values.
        self.toneStart = 0
        self.toneEnd = 0
        self.movementWindowStart = 0
        self.movementWindowEnd = 0
        self.interTrialStart = 0
        self.interTrialEnd = 0
        self.probabilityToneOne = 0
        self.frequencyTone1 = 0
        self.frequencyTone2 = 0
        self.movementAmount = 0
        self.movementMethod = 0
        self.movementTime = 0
        self.idleTime = 0
        self.comment = ""
        self.training_started = False
        if (toStart == True):
            self.launch_GUI()
        logger.info( "userInterfaceAPI started." )
    
    def setQueue(self, nuevoqueue):
        #Set the namespace of this class, to interoperate with the master process.
        self.jobList = nuevoqueue
        #logger.info( "Queue set" )
        pass
    
    def setInitialValues(self):
        #print "User Interface API: sending variables to GUI, with the purpose of setting up initial values."
        logger.info( "User Interface API: sending variables to GUI, with the purpose of setting up initial values." )
        
        self.currentGUI.toneStart = self.toneStart
        self.currentGUI.toneEnd = self.toneEnd
        self.currentGUI.movementWindowStart = self.movementWindowStart
        self.currentGUI.movementWindowEnd = self.movementWindowEnd
        self.currentGUI.interTrialStart = self.interTrialStart
        self.currentGUI.interTrialEnd = self.interTrialEnd
        self.currentGUI.probabilityToneOne = self.probabilityToneOne
        self.currentGUI.frequencyTone1 = self.frequencyTone1
        self.currentGUI.frequencyTone2 = self.frequencyTone2
        self.currentGUI.movementAmount = self.movementAmount
        self.currentGUI.movementMethod = self.movementMethod
        self.currentGUI.movementTime = self.movementTime
        self.currentGUI.idleTime = self.idleTime
        self.currentGUI.comment = self.comment
        self.currentGUI.type_pavlov = self.type_pavlov
        self.currentGUI.type_skinner = self.type_skinner
        self.currentGUI.type_ocond = self.type_ocond
        self.currentGUI.type_discr = self.type_discr
        self.currentGUI.requireStillnessVar = self.requireStillnessVar;
        print "..................-"
        #print self.requireStillnessVar
        self.currentGUI.commitInitialData()
        
        
        pass
    
    def dummy_fn(self):
        print "Dummy Function"
        logger.info ( "Dummy function." )
        pass
    
    def setNameSpaceMessage(self, arg1, arg2=0):
        #print "setNameSpaceMessage"
        self.jobList.put( (arg1, arg2) )
        self.jobList.join()
        #self.jobList.put_nowait((arg1, arg2))
        #print "done."
        pass
    
    
    def overrideaction_drop(self):
        logger.debug ( "Default API: Drop" )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(1,0)
        #logger.debug ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.debug ( "Default API: done." )
    
    def overrideaction_reward(self):
        logger.debug ( "Default API: Reward" )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(2,0)
        #logger.debug ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.debug ( "Default API: done." )
    
    def overrideaction_open(self):
        logger.debug ( "Default API: Open" )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(3)
        #logger.debug ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.debug ( "Default API: done." )
    
    def overrideaction_close(self):
        logger.debug ( "Default API: Close" )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(4)
        #logger.debug ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.debug ( "Default API: done." )
    
    def overrideaction_startTraining(self):
        logger.debug ( "Default API: Start Training" )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(5)
        #logger.debug ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.debug ( "Default API: done." )
    
    def overrideaction_stopTraining(self):
        logger.debug ( "Default API: Stop Training" )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(6)
        #logger.debug ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.debug ( "Default API: done." )
    
    def overrideaction_pauseTraining(self):
        logger.debug ( "Default API: Pause / Resume Training" )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(7)
        #logger.debug ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.debug ( "Default API: done." )
    
    def overrideaction_resumeTraining(self):
        logger.debug ( "Default API: Pause / Resume Training" )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(8)
        #logger.debug ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.debug ( "Default API: done." )
    
    def overrideaction_applyC(self):
        logger.debug ( "Default API: Apply Comment" )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(16, self.comment)
        #logger.debug ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.debug ( "Default API: done." )
    
    def overrideaction_applyP(self):
        logger.debug ( "Default API: Apply Parameters" )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        #this actually is composed of a list of messages sent to thread.
        #we will wait till every message has been send to finish the function.
        self.setNameSpaceMessage(17, self.currentGUI.frequencyTone1 )
        #logger.debug ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        
        
        self.setNameSpaceMessage(18, self.currentGUI.frequencyTone2 )
        #logger.debug ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        
        
        self.setNameSpaceMessage(19, self.currentGUI.movementAmount )
        #logger.debug ( "ns: " + ns.__str__() )
        
        self.setNameSpaceMessage(20, self.currentGUI.movementMethod )
        #logger.debug ( "ns: " + ns.__str__() )
        
        self.setNameSpaceMessage(21, self.currentGUI.movementTime )
        #logger.debug ( "ns: " + ns.__str__() )
        
        self.setNameSpaceMessage(22, self.currentGUI.idleTime )
        #logger.debug ( "ns: " + ns.__str__() )
    
    
    
    def overrideaction_applyTE(self):
        print "TE_AP"
        logger.debug ( "Default API: Apply Trial Events" )
        self.setNameSpaceMessage(23, self.currentGUI.toneStart )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        
        self.setNameSpaceMessage(24, self.currentGUI.toneEnd )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        
        
        self.setNameSpaceMessage(25, self.currentGUI.movementWindowStart )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        
        
        self.setNameSpaceMessage(26, self.currentGUI.movementWindowEnd )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        
        
        self.setNameSpaceMessage(27, self.currentGUI.interTrialStart )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        
        
        
        self.setNameSpaceMessage(28, self.currentGUI.interTrialEnd )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        
        
        self.setNameSpaceMessage(29, self.currentGUI.probabilityToneOne )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        
        self.setNameSpaceMessage(32, self.currentGUI.requireStillnessVar )
        
        self.setNameSpaceMessage(33, self.currentGUI.current_type )
        logger.debug ( "Default API: done." )
        
    
    def overrideaction_savestate(self):
        logger.debug ( "Default API: SaveState" )
        #print "API Namespace:", ns
        #logger.debug ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(31,0)
        #logger.debug ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.debug ( "Default API: done." )
    
    def overrideaction_testT1(self):
        logger.debug( "Default API: Test T1" )
        #logger.debug( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        self.frequencyTone1 = self.currentGUI.frequencyTone1
        self.setNameSpaceMessage(10, self.frequencyTone1 )
        #logger.debug( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.debug( "Default API: done." )
    
    def overrideaction_testT2(self):
        logger.debug( "Default API: Test T2" )
        #logger.debug( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        self.frequencyTone2 = self.currentGUI.frequencyTone2
        self.setNameSpaceMessage(11, self.frequencyTone2 )
        #logger.debug( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.debug( "Default API: done." )
    
    def overrideaction_showfeedback(self):
        logger.debug( "Default API: Show Feedback" )
        self.setNameSpaceMessage(12)
        logger.debug( "Default API: done." )
    
    def overrideaction_hidefeedback(self):
        logger.debug( "Default API: Hide Feedback" )
        self.setNameSpaceMessage(13)
        logger.debug( "Default API: done." )
    
    def overrideaction_showtracking(self):
        logger.debug( "Default API: Show Tracking" )
        self.setNameSpaceMessage(14)
        logger.debug( "Default API: done." )
    
    def overrideaction_hidetracking(self):
        logger.debug( "Default API: Hide Tracking" )
        self.setNameSpaceMessage(15)
        logger.debug( "Default API: done." )
    
    def overrideaction_recalibratec(self):
        logger.debug( "Default API: Recalibrate Camera" )
        self.setNameSpaceMessage(30)
        logger.debug( "Default API: done." )
        pass
    
    def action_drop(self):
        logger.debug( "API: Drop" )
        try:
            self.overrideaction_drop()
        except:
            logger.warning( "API Drop: OverrideAction Error" )
    
    def action_savestate(self):
        logger.debug( "API: SaveState" )
        try:
            self.overrideaction_savestate()
        except:
            logger.warning( "API SaveState: OverrideAction Error" )
    
    def action_reward(self):
        logger.debug( "API: Reward" )
        try:
            self.overrideaction_reward()
        except:
            logger.warning( "API Reward: OverrideAction Error" )
        
    def action_open(self):
        logger.debug( "API: Open" )
        try:
            self.overrideaction_open()
        except:
            logger.warning( "API Open: OverrideAction Error" )
        
    def action_close(self):
        logger.debug( "API: Close" )
        try:
            self.overrideaction_close()
        except:
            logger.warning( "API Close: OverrideAction Error" )
    
    def action_startTraining(self):
        logger.debug( "API: Start Training" )
        try:
            self.overrideaction_startTraining()
        except:
            logger.warning( "API Start Training: OverrideAction Error" )
    
    def action_stopTraining(self):
        logger.debug( "API: Stop Training" )
        try:
            self.overrideaction_stopTraining()
        except:
            logger.warning( "API Stop Training: OverrideAction Error" )
    
    def action_pauseTraining(self):
        logger.debug( "API: Pause Training" )
        try:
            self.overrideaction_pauseTraining()
        except:
            logger.warning( "API Pause Training: OverrideAction Error" )
    
    def action_resumeTraining(self):
        logger.debug( "API: Resume Training" )
        try:
            self.overrideaction_resumeTraining()
        except:
            logger.warning( "API Resume Training: OverrideAction Error" )
    
    def action_applyC(self):
        try:
            tempstr = str(self.currentGUI.comment).decode(encoding='UTF-8',errors='ignore')
        except:
            print "API: Apply Comment error - Couldn't code to UTF8. Will send an empty string instead."
            logger.warning( "API: Apply Comment error - Couldn't code to UTF8. Will send an empty string instead." )
            tempstr = ""
        self.comment = tempstr
        logger.debug( "API: Apply Comments: " + tempstr )
        try:
            self.overrideaction_applyC()
        except:
            logger.warning( "API ApplyC: OverrideAction Error" )
    
    def action_applyP(self):
        self.frequencyTone1 = self.currentGUI.frequencyTone1
        self.frequencyTone2 = self.currentGUI.frequencyTone2
        self.movementAmount = self.currentGUI.movementAmount
        self.movementMethod = self.currentGUI.movementMethod
        self.movementTime = self.currentGUI.movementTime
        self.idleTime = self.currentGUI.idleTime
        logger.debug( "API: Apply Parameters:" )
        try:
            self.overrideaction_applyP()
        except:
            logger.warning( "API ApplyP: OverrideAction Error" )
    
    def action_applyTE(self):
        self.toneStart = self.currentGUI.toneStart
        self.toneEnd = self.currentGUI.toneEnd
        self.movementWindowStart = self.currentGUI.movementWindowStart
        self.movementWindowEnd = self.currentGUI.movementWindowEnd
        self.interTrialStart = self.currentGUI.interTrialStart
        self.interTrialEnd = self.currentGUI.interTrialEnd
        self.probabilityToneOne = self.currentGUI.probabilityToneOne
        self.requireStillnessVar = self.currentGUI.requireStillnessVar;
        logger.debug( "API: Apply Trial Events:" )
        try:
            self.overrideaction_applyTE()
        except:
            logger.warning( "API ApplyTE: OverrideAction Error" )
    
    def action_testT1(self):
        logger.debug( "API: Test Tone 1" )
        try:
            self.overrideaction_testT1()
        except:
            logger.warning( "API Test Tone 1: OverrideAction Error" )
    
    def action_testT2(self):
        logger.debug( "API: Test Tone 2" )
        try:
            self.overrideaction_testT2()
        except:
            logger.warning( "API Test Tone 2: OverrideAction Error" )
    
    def action_showfeedback(self):
        logger.debug( "API: Show Feedback" )
        try:
            self.overrideaction_showfeedback()
        except:
            logger.warning( "API Show Feedback: OverrideAction Error" )
    
    def action_hidefeedback(self):
        logger.debug( "API: Hide Feedback" )
        try:
            self.overrideaction_hidefeedback()
        except:
            logger.warning( "API Hide Feedback: OverrideAction Error" )
    
    def action_showtracking(self):
        logger.debug( "API: Show Tracking" )
        try:
            self.overrideaction_showtracking()
        except:
            logger.warning( "API Show Tracking: OverrideAction Error" )
    
    def action_hidetracking(self):
        logger.debug( "API: Hide Tracking" )
        try:
            self.overrideaction_hidetracking()
        except:
            logger.warning( "API Hide Tracking: OverrideAction Error" )
    
    def action_recalibratec(self):
        logger.debug( "API: Recalibrate Camera" )
        try:
            self.overrideaction_recalibratec()
        except:
            logger.warning( "API Recalibrate Camera: OverrideAction Error" )
    
    def action_exit(self):
        logger.debug( "Default API: Exiting GUI from API." )
        #logger.debug( "ns: ", str(ns) )
        #print "API Namespace:", ns
        self.setNameSpaceMessage(9)
        #print "API Namespace:", ns
        #logger.debug( "ns: ", str(ns) )
        logger.debug( "Default API: done." )
        try:
            os._exit(0)
        except:
            pass
    
    
    
    def launch_GUI(self):
        if (self.usingTK == 0):
            self.launch_glade()
        elif (self.usingTK == 1):
            self.launch_tkinter()
        pass
    
    
    def launch_glade(self):
        import userInterface_glade
        logger.info( str(self) +  "  Glade Interface : launching" )
        self.currentGUI = userInterface_glade.GUIGTK_Class()
        self.currentGUI.initAll()
        time.sleep(1)
        self.currentGUI.overrideaction_exit = self.action_exit
        self.currentGUI.overrideaction_savestate = self.action_savestate
        self.currentGUI.overrideaction_drop = self.action_drop
        self.currentGUI.overrideaction_reward = self.action_reward
        self.currentGUI.overrideaction_open = self.action_open
        self.currentGUI.overrideaction_close = self.action_close
        self.currentGUI.overrideaction_startTraining = self.action_startTraining
        self.currentGUI.overrideaction_stopTraining = self.action_stopTraining
        self.currentGUI.overrideaction_pauseTraining = self.action_pauseTraining
        self.currentGUI.overrideaction_resumeTraining = self.action_resumeTraining
        self.currentGUI.overrideaction_applyC = self.action_applyC
        self.currentGUI.overrideaction_applyP = self.action_applyP
        self.currentGUI.overrideaction_applyTE = self.action_applyTE
        self.currentGUI.overrideaction_testT1 = self.action_testT1
        self.currentGUI.overrideaction_testT2 = self.action_testT2
        self.currentGUI.overrideaction_showfeedback = self.action_showfeedback
        self.currentGUI.overrideaction_showtracking = self.action_showtracking
        self.currentGUI.overrideaction_hidefeedback = self.action_hidefeedback
        self.currentGUI.overrideaction_hidetracking = self.action_hidetracking
        self.currentGUI.overrideaction_recalibratec = self.action_recalibratec
        #self.comment = ""
        #self.thread_function(
        #thread1 = threading.Thread(target=self.thread_function, name="glade_GUI")
        #thread1.start()
        logger.debug( "message variables: "+ self.ns.__str__() )
        logger.info( str(self) +  "  Glade Interface Started" )
        print "Glade interface started."
        self.setInitialValues() #loops in this function infinitely
        #while True:
        #    time.sleep(1.0)
        pass
    
    
    def launch_tkinter(self):
        import userInterface_tk
        self.currentGUI = userInterface_tk.GUIGTK_Class()
        self.currentGUI.initAll();
        #print "Overriding functions:"
        time.sleep(0.5)
        time.sleep(0.5)
        logger.info( str(self) +  "Launching Tkinter Interface" )
        self.currentGUI.overrideaction_drop = self.action_drop
        self.currentGUI.overrideaction_savestate = self.action_savestate
        self.currentGUI.overrideaction_reward = self.action_reward
        self.currentGUI.overrideaction_open = self.action_open
        self.currentGUI.overrideaction_close = self.action_close
        self.currentGUI.overrideaction_startTraining = self.action_startTraining
        self.currentGUI.overrideaction_stopTraining = self.action_stopTraining
        self.currentGUI.overrideaction_pauseTraining = self.action_pauseTraining
        self.currentGUI.overrideaction_resumeTraining = self.action_resumeTraining
        self.currentGUI.overrideaction_applyC = self.action_applyC
        self.currentGUI.overrideaction_applyP = self.action_applyP
        self.currentGUI.overrideaction_applyTE = self.action_applyTE
        self.currentGUI.overrideaction_testT1 = self.action_testT1
        self.currentGUI.overrideaction_testT2 = self.action_testT2
        self.currentGUI.overrideaction_showfeedback = self.action_showfeedback
        self.currentGUI.overrideaction_showtracking = self.action_showtracking
        self.currentGUI.overrideaction_hidefeedback = self.action_hidefeedback
        self.currentGUI.overrideaction_hidetracking = self.action_hidetracking
        self.currentGUI.overrideaction_recalibratec = self.action_recalibratec
        self.currentGUI.overrideaction_exit = self.action_exit
        logger.debug( "message variables: "+ self.ns.__str__() )
        logger.info( str(self) +  "  Tkinter Interface Started" )
        print "Tkinter Interface Started"
        self.setInitialValues()
        while True:
            time.sleep(1.0)
        pass

if __name__ == '__main__':
    # create a logging format
    dateformat = '%Y/%m/%d %H:%M:%S'
    formatter_str = '%(asctime)s.%(msecs)d - %(name)s - %(levelname)s - %(message)s'
    filename_to_log='logs/userInterfaceAPI.log'
    
    
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
    
    logger.info('Start userInterfaceAPI Test')
    import multiprocessing
    import time
    print "init.."
    p = multiprocessing.Process(target=userInterface_API(True))
    p.start()
    logger.info('End userInterfaceAPI Test')
