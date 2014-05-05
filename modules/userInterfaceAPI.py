import os
import sys
import time
import logging
logger = logging.getLogger('userInterfaceAPI')

class userInterface_API:
    usingTK = 0 #0: using GTk;   1: using TK
    ns = 0 # message variable (namespace), that will be shared among processes.
    
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
    
    def setNamespace(self, nuevons):
        #Set the namespace of this class, to interoperate with the master process.
        global ns
        ns = nuevons
        logger.info( "Namespace set" )
    
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
    
    def setNameSpaceMessage1(self, num):
        if ( self.isNameSpaceEnabled()):
            ns.message1 = num
            logger.info( 'Msg1: Handled from here.' )
        else:
            logger.info( 'Msg1: Not ready to send message.' )
        pass
    
    def setNameSpaceMessage2(self,arg):
        #it is preferable to first send message 2 (this) and then msg1. Else this message won't take effect.
        if ( self.isNameSpaceEnabled() ):
            ns.message2 = arg
            
            logger.info( 'Msg2: Handled from here.' )
            ns.message1 = 0
        else:
            logger.info( 'Msg2: Not ready to send message.' )
        pass
    
    def isNameSpaceEnabled(self):
        if (ns.message1 == 0):
            return True
        else:
            return False
    
    def overrideaction_drop(self):
        logger.info ( "Default API: Drop" )
        print "API Namespace:", ns
        logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage1(1)
        logger.info ( "ns: " + ns.__str__() )
        print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_reward(self):
        logger.info ( "Default API: Reward" )
        print "API Namespace:", ns
        logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage1(2)
        logger.info ( "ns: " + ns.__str__() )
        print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_open(self):
        logger.info ( "Default API: Open" )
        print "API Namespace:", ns
        logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage1(3)
        logger.info ( "ns: " + ns.__str__() )
        print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_close(self):
        logger.info ( "Default API: Close" )
        print "API Namespace:", ns
        logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage1(4)
        logger.info ( "ns: " + ns.__str__() )
        print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_startTraining(self):
        logger.info ( "Default API: Start Training" )
        print "API Namespace:", ns
        logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage1(5)
        logger.info ( "ns: " + ns.__str__() )
        print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_stopTraining(self):
        logger.info ( "Default API: Stop Training" )
        print "API Namespace:", ns
        logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage1(6)
        logger.info ( "ns: " + ns.__str__() )
        print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_pauseTraining(self):
        logger.info ( "Default API: Pause / Resume Training" )
        print "API Namespace:", ns
        logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage1(7)
        logger.info ( "ns: " + ns.__str__() )
        print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_resumeTraining(self):
        logger.info ( "Default API: Pause / Resume Training" )
        print "API Namespace:", ns
        logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage1(8)
        logger.info ( "ns: " + ns.__str__() )
        print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_applyC(self):
        logger.info ( "Default API: Apply Comment" )
        print "API Namespace:", ns
        logger.info ( "ns: " + ns.__str__() )
        self.setNameSpaceMessage2(self.comment)
        self.setNameSpaceMessage1(16)
        logger.info ( "ns: " + ns.__str__() )
        print "API Namespace:", ns
        logger.info ( "Default API: done." )
    
    def overrideaction_applyP(self):
        logger.info ( "Default API: Apply Parameters" )
        print "API Namespace:", ns
        logger.info ( "ns: " + ns.__str__() )
        #this actually is composed of a list of messages sent to thread.
        #we will wait till every message has been send to finish the function.
        self.setNameSpaceMessage2(self.currentGUI.frequencyTone1)
        self.setNameSpaceMessage1(17)
        logger.info ( "ns: " + ns.__str__() )
        print "API Namespace:", ns
        while True:
            if ( self.isNameSpaceEnabled() ):
                #carry on doing things.
                self.setNameSpaceMessage2(self.currentGUI.frequencyTone2)
                self.setNameSpaceMessage1(18)
                logger.info ( "ns: " + ns.__str__() )
                print "API Namespace:", ns
                #return; #it is better to keep on nesting while true if code to exhaust all variables.
                while True:
                    if (self.isNameSpaceEnabled()):
                        self.setNameSpaceMessage2(self.currentGUI.movementAmount)
                        self.setNameSpaceMessage1(19)
                        logger.info ( "ns: " + ns.__str__() )
                        print "API Namespace:", ns
                        while True:
                            if (self.isNameSpaceEnabled()):
                                self.setNameSpaceMessage2(self.currentGUI.movementMethod)
                                self.setNameSpaceMessage1(20)
                                logger.info ( "ns: " + ns.__str__() )
                                print "API Namespace:", ns
                                while True:
                                    if (self.isNameSpaceEnabled()):
                                        self.setNameSpaceMessage2(self.currentGUI.movementTime)
                                        self.setNameSpaceMessage1(21)
                                        logger.info ( "ns: " + ns.__str__() )
                                        print "API Namespace:", ns
                                        while True:
                                            if (self.isNameSpaceEnabled()):
                                                self.setNameSpaceMessage2(self.currentGUI.idleTime)
                                                self.setNameSpaceMessage1(22)
                                                logger.info ( "ns: " + ns.__str__() )
                                                print "API Namespace:", ns
                                                logger.info ( "Default API: done." )
                                                return; #last variable was idle Time.
                                            else:
                                                time.sleep(0.01)
                                    else:
                                        time.sleep(0.01)
                            else:
                                time.sleep(0.01)
                    else:
                        time.sleep(0.01)
            else:
                #print "waiting."
                time.sleep(0.01)
    
    def overrideaction_applyTE(self):
        logger.info ( "Default API: Apply Trial Events" )
        self.setNameSpaceMessage2(self.currentGUI.toneStart)
        self.setNameSpaceMessage1(23)
        print "API Namespace:", ns
        logger.info ( "ns: " + ns.__str__() )
        while True:
            if (self.isNameSpaceEnabled()):
                #carry on doing things.
                self.setNameSpaceMessage2(self.currentGUI.toneEnd)
                self.setNameSpaceMessage1(24)
                print "API Namespace:", ns
                logger.info ( "ns: " + ns.__str__() )
                #return; #it is better to keep on nesting while true if code to exhaust all variables.
                while True:
                    if (self.isNameSpaceEnabled()):
                        self.setNameSpaceMessage2(self.currentGUI.movementWindowStart)
                        self.setNameSpaceMessage1(25)
                        print "API Namespace:", ns
                        logger.info ( "ns: " + ns.__str__() )
                        while True:
                            if (self.isNameSpaceEnabled()):
                                self.setNameSpaceMessage2(self.currentGUI.movementWindowEnd)
                                self.setNameSpaceMessage1(26)
                                print "API Namespace:", ns
                                logger.info ( "ns: " + ns.__str__() )
                                while True:
                                    if (self.isNameSpaceEnabled()):
                                        self.setNameSpaceMessage2(self.currentGUI.interTrialStart)
                                        self.setNameSpaceMessage1(27)
                                        print "API Namespace:", ns
                                        logger.info ( "ns: " + ns.__str__() )
                                        while True:
                                            if (self.isNameSpaceEnabled()):
                                                self.setNameSpaceMessage2(self.currentGUI.interTrialEnd)
                                                self.setNameSpaceMessage1(28)
                                                print "API Namespace:", ns
                                                logger.info ( "ns: " + ns.__str__() )
                                                while True:
                                                    if (self.isNameSpaceEnabled()):
                                                        self.setNameSpaceMessage2(self.currentGUI.probabilityToneOne)
                                                        self.setNameSpaceMessage1(29)
                                                        print "API Namespace:", ns
                                                        logger.info ( "ns: " + ns.__str__() )
                                                        logger.info ( "Default API: done." )
                                                        return; #last variable was probabilityToneOne
                                                    else:
                                                        time.sleep(0.01)
                                            else:
                                                time.sleep(0.01)
                                    else:
                                        time.sleep(0.01)
                            else:
                                time.sleep(0.01)
                    else:
                        time.sleep(0.01)
            else:
                #print "waiting."
                time.sleep(0.01)
    
    def overrideaction_testT1(self):
        logger.info( "Default API: Test T1" )
        logger.info( "ns: " + ns.__str__() )
        print "API Namespace:", ns
        self.frequencyTone1 = self.currentGUI.frequencyTone1
        self.setNameSpaceMessage2(self.frequencyTone1)
        self.setNameSpaceMessage1(10)
        logger.info( "ns: " + ns.__str__() )
        print "API Namespace:", ns
        logger.info( "Default API: done." )
    
    def overrideaction_testT2(self):
        logger.info( "Default API: Test T2" )
        logger.info( "ns: " + ns.__str__() )
        print "API Namespace:", ns
        self.frequencyTone2 = self.currentGUI.frequencyTone2
        self.setNameSpaceMessage2(self.frequencyTone2)
        self.setNameSpaceMessage1(11)
        logger.info( "ns: " + ns.__str__() )
        print "API Namespace:", ns
        logger.info( "Default API: done." )
    
    def overrideaction_showfeedback(self):
        logger.info( "Default API: Show Feedback" )
        logger.info( "ns: "+ ns.__str__() )
        print "API Namespace:", ns
        self.setNameSpaceMessage1(12)
        print "API Namespace:", ns
        logger.info( "ns: "+ ns.__str__() )
        logger.info( "Default API: done." )
    
    def overrideaction_hidefeedback(self):
        logger.info( "Default API: Hide Feedback" )
        logger.info( "ns: "+ ns.__str__() )
        print "API Namespace:", ns
        self.setNameSpaceMessage1(13)
        print "API Namespace:", ns
        logger.info( "ns: "+ ns.__str__() )
        logger.info( "Default API: done." )
    
    def overrideaction_showtracking(self):
        logger.info( "Default API: Show Tracking" )
        logger.info( "ns: "+ ns.__str__() )
        print "API Namespace:", ns
        self.setNameSpaceMessage1(14)
        print "API Namespace:", ns
        logger.info( "ns: "+ ns.__str__() )
        logger.info( "Default API: done." )
    
    def overrideaction_hidetracking(self):
        logger.info( "Default API: Hide Tracking" )
        logger.info( "ns: "+ ns.__str__() )
        print "API Namespace:", ns
        self.setNameSpaceMessage1(15)
        print "API Namespace:", ns
        logger.info( "ns: "+ ns.__str__() )
        logger.info( "Default API: done." )
    
    def overrideaction_recalibratec(self):
        logger.info( "Default API: Recalibrate Camera" )
        logger.info( "ns: "+ ns.__str__() )
        print "API Namespace:", ns
        self.setNameSpaceMessage1(30)
        print "API Namespace:", ns
        logger.info( "ns: "+ ns.__str__() )
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
        print "API Namespace:", ns
        self.setNameSpaceMessage1(9)
        print "API Namespace:", ns
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
    formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    dateformat = '%Y/%m/%d %I:%M:%S %p'
    logging.basicConfig(filename='logs/userInterfaceAPI.log', filemode='w',
            level=logging.DEBUG, format=formatter, datefmt = dateformat)
    logger.info('Start userInterfaceAPI Test')
    import multiprocessing
    import time
    print "init.."
    p = multiprocessing.Process(target=userInterface_API(True))
    p.start()
    logger.info('End userInterfaceAPI Test')
