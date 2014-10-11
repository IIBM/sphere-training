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
        print "Queue set."
        logger.info( "Queue set" )
    
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
        self.currentGUI.commitInitialData()
        pass
    
    def dummy_fn(self):
        print "Dummy Function"
        logger.info ( "Dummy function." )
        pass
    
    def setNameSpaceMessage(self, arg1, arg2=0):
        print "setNameSpaceMessage"
        self.jobList.put( (arg1, arg2) )
        self.jobList.join()
        #self.jobList.put_nowait((arg1, arg2))
        print "done."
    
    
    def overrideaction_drop(self):
        logger.info ( "Default API: Drop" )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(1,0)
        #logger.info ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_reward(self):
        logger.info ( "Default API: Reward" )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(2,0)
        #logger.info ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_open(self):
        logger.info ( "Default API: Open" )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(3)
        #logger.info ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_close(self):
        logger.info ( "Default API: Close" )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(4)
        #logger.info ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_startTraining(self):
        logger.info ( "Default API: Start Training" )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(5)
        #logger.info ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_stopTraining(self):
        logger.info ( "Default API: Stop Training" )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(6)
        #logger.info ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_pauseTraining(self):
        logger.info ( "Default API: Pause / Resume Training" )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(7)
        #logger.info ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_resumeTraining(self):
        logger.info ( "Default API: Pause / Resume Training" )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(8)
        #logger.info ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_applyC(self):
        logger.info ( "Default API: Apply Comment" )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage(16, self.comment)
        #logger.info ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_applyP(self):
        logger.info ( "Default API: Apply Parameters" )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        #this actually is composed of a list of messages sent to thread.
        #we will wait till every message has been send to finish the function.
        self.setNameSpaceMessage(17, self.currentGUI.frequencyTone1 )
        #logger.info ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        
        
        self.setNameSpaceMessage(18, self.currentGUI.frequencyTone2 )
        #logger.info ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        
        
        self.setNameSpaceMessage(19, self.currentGUI.movementAmount )
        #logger.info ( "ns: " + ns.__str__() )
        
        self.setNameSpaceMessage(20, self.currentGUI.movementMethod )
        #logger.info ( "ns: " + ns.__str__() )
        
        self.setNameSpaceMessage(21, self.currentGUI.movementTime )
        #logger.info ( "ns: " + ns.__str__() )
        
        self.setNameSpaceMessage(22, self.currentGUI.idleTime )
        #logger.info ( "ns: " + ns.__str__() )
    
    
    
    def overrideaction_applyTE(self):
        logger.info ( "Default API: Apply Trial Events" )
        self.setNameSpaceMessage(23, self.currentGUI.toneStart )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        
        self.setNameSpaceMessage(24, self.currentGUI.toneEnd )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        
        
        self.setNameSpaceMessage(25, self.currentGUI.movementWindowStart )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        
        
        self.setNameSpaceMessage(26, self.currentGUI.movementWindowEnd )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        
        
        self.setNameSpaceMessage(27, self.currentGUI.interTrialStart )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        
        
        
        self.setNameSpaceMessage(28, self.currentGUI.interTrialEnd )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        
        
        self.setNameSpaceMessage(29, self.currentGUI.probabilityToneOne )
        #print "API Namespace:", ns
        #logger.info ( "ns: " + ns.__str__() )
        logger.info ( "Default API: done." )
        
        
        
    
    def overrideaction_testT1(self):
        logger.info( "Default API: Test T1" )
        #logger.info( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        self.frequencyTone1 = self.currentGUI.frequencyTone1
        self.setNameSpaceMessage(10, self.frequencyTone1 )
        #logger.info( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.info( "Default API: done." )
    
    def overrideaction_testT2(self):
        logger.info( "Default API: Test T2" )
        #logger.info( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        self.frequencyTone2 = self.currentGUI.frequencyTone2
        self.setNameSpaceMessage(11, self.frequencyTone2 )
        #logger.info( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        logger.info( "Default API: done." )
    
    def overrideaction_showfeedback(self):
        logger.info( "Default API: Show Feedback" )
        self.setNameSpaceMessage(12)
        logger.info( "Default API: done." )
    
    def overrideaction_hidefeedback(self):
        logger.info( "Default API: Hide Feedback" )
        self.setNameSpaceMessage(13)
        logger.info( "Default API: done." )
    
    def overrideaction_showtracking(self):
        logger.info( "Default API: Show Tracking" )
        self.setNameSpaceMessage(14)
        logger.info( "Default API: done." )
    
    def overrideaction_hidetracking(self):
        logger.info( "Default API: Hide Tracking" )
        self.setNameSpaceMessage(15)
        logger.info( "Default API: done." )
    
    def overrideaction_recalibratec(self):
        logger.info( "Default API: Recalibrate Camera" )
        self.setNameSpaceMessage(30)
        logger.info( "Default API: done." )
        pass
    
    def action_drop(self):
        logger.info( "API: Drop" )
        try:
            self.overrideaction_drop()
        except:
            logger.info( "API Drop: OverrideAction Error" )
    
    def action_reward(self):
        logger.info( "API: Reward" )
        try:
            self.overrideaction_reward()
        except:
            logger.info( "API Reward: OverrideAction Error" )
        
    def action_open(self):
        logger.info( "API: Open" )
        try:
            self.overrideaction_open()
        except:
            logger.info( "API Open: OverrideAction Error" )
        
    def action_close(self):
        logger.info( "API: Close" )
        try:
            self.overrideaction_close()
        except:
            logger.info( "API Close: OverrideAction Error" )
    
    def action_startTraining(self):
        logger.info( "API: Start Training" )
        try:
            self.overrideaction_startTraining()
        except:
            logger.info( "API Start Training: OverrideAction Error" )
    
    def action_stopTraining(self):
        logger.info( "API: Stop Training" )
        try:
            self.overrideaction_stopTraining()
        except:
            logger.info( "API Stop Training: OverrideAction Error" )
    
    def action_pauseTraining(self):
        logger.info( "API: Pause Training" )
        try:
            self.overrideaction_pauseTraining()
        except:
            logger.info( "API Pause Training: OverrideAction Error" )
    
    def action_resumeTraining(self):
        logger.info( "API: Resume Training" )
        try:
            self.overrideaction_resumeTraining()
        except:
            logger.info( "API Resume Training: OverrideAction Error" )
    
    def action_applyC(self):
        try:
            tempstr = str(self.currentGUI.comment).decode(encoding='UTF-8',errors='ignore')
        except:
            print "API: Apply Comment error - Couldn't code to UTF8. Will send an empty string instead."
            logger.info( "API: Apply Comment error - Couldn't code to UTF8. Will send an empty string instead." )
            tempstr = ""
        self.comment = tempstr
        logger.info( "API: Apply Comments: " + tempstr )
        try:
            self.overrideaction_applyC()
        except:
            logger.info( "API ApplyC: OverrideAction Error" )
    
    def action_applyP(self):
        self.frequencyTone1 = self.currentGUI.frequencyTone1
        self.frequencyTone2 = self.currentGUI.frequencyTone2
        self.movementAmount = self.currentGUI.movementAmount
        self.movementMethod = self.currentGUI.movementMethod
        self.movementTime = self.currentGUI.movementTime
        self.idleTime = self.currentGUI.idleTime
        logger.info( "API: Apply Parameters:" )
        try:
            self.overrideaction_applyP()
        except:
            logger.info( "API ApplyP: OverrideAction Error" )
    
    def action_applyTE(self):
        self.toneStart = self.currentGUI.toneStart
        self.toneEnd = self.currentGUI.toneEnd
        self.movementWindowStart = self.currentGUI.movementWindowStart
        self.movementWindowEnd = self.currentGUI.movementWindowEnd
        self.interTrialStart = self.currentGUI.interTrialStart
        self.interTrialEnd = self.currentGUI.interTrialEnd
        self.probabilityToneOne = self.currentGUI.probabilityToneOne
        logger.info( "API: Apply Trial Events:" )
        try:
            self.overrideaction_applyTE()
        except:
            logger.info( "API ApplyTE: OverrideAction Error" )
    
    def action_testT1(self):
        logger.info( "API: Test Tone 1" )
        try:
            self.overrideaction_testT1()
        except:
            logger.info( "API Test Tone 1: OverrideAction Error" )
    
    def action_testT2(self):
        logger.info( "API: Test Tone 2" )
        try:
            self.overrideaction_testT2()
        except:
            logger.info( "API Test Tone 2: OverrideAction Error" )
    
    def action_showfeedback(self):
        logger.info( "API: Show Feedback" )
        try:
            self.overrideaction_showfeedback()
        except:
            logger.info( "API Show Feedback: OverrideAction Error" )
    
    def action_hidefeedback(self):
        logger.info( "API: Hide Feedback" )
        try:
            self.overrideaction_hidefeedback()
        except:
            logger.info( "API Hide Feedback: OverrideAction Error" )
    
    def action_showtracking(self):
        logger.info( "API: Show Tracking" )
        try:
            self.overrideaction_showtracking()
        except:
            logger.info( "API Show Tracking: OverrideAction Error" )
    
    def action_hidetracking(self):
        logger.info( "API: Hide Tracking" )
        try:
            self.overrideaction_hidetracking()
        except:
            logger.info( "API Hide Tracking: OverrideAction Error" )
    
    def action_recalibratec(self):
        logger.info( "API: Recalibrate Camera" )
        try:
            self.overrideaction_recalibratec()
        except:
            logger.info( "API Recalibrate Camera: OverrideAction Error" )
    
    def action_exit(self):
        logger.info( "Default API: Exiting GUI from API." )
        #logger.info( "ns: ", str(ns) )
        #print "API Namespace:", ns
        self.setNameSpaceMessage(9)
        #print "API Namespace:", ns
        #logger.info( "ns: ", str(ns) )
        logger.info( "Default API: done." )
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
        self.currentGUI.overrideaction_exit = self.action_exit
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
        logger.info( "message variables: "+ self.ns.__str__() )
        logger.info( str(self) +  "  Glade Interface Started" )
        print "Glade interface started."
        self.setInitialValues()
        while True:
            time.sleep(1.0)
        pass
    
    
    def launch_tkinter(self):
        import userInterface_tk
        self.currentGUI = userInterface_tk.GUIGTK_Class()
        #print "Overriding functions:"
        time.sleep(0.5)
        time.sleep(0.5)
        logger.info( str(self) +  "Launching Tkinter Interface" )
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
        self.currentGUI.overrideaction_exit = self.action_exit
        logger.info( "message variables: "+ self.ns.__str__() )
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
