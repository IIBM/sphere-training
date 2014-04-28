import os, sys
import time
import logging
logger = logging.getLogger('userInterfaceAPI')

class userInterface_API:
    usingTK = 1 #0: using GTk;   1: using TK
    ns = 0 # message variable (namespace), that will be shared among processes.
    
    
    def __init__(self, toStart = False):

        logger.info( "initializing userInterfaceAPI" )
        #put initialization variables here.
        #self.launch_glade() # by design, won't initialize the gtk main loop from the init but from outside.
        self.training_started = False
        print "initializing userInterfaceAPI"
        if (toStart == True):
            #
            self.launch_GUI()
        logger.info( "userInterfaceAPI started." )
    
    def setNamespace(self, nuevons):
        global ns
        ns = nuevons
        logger.info( "Namespace set" )
        #self.launch_glade()
    
    def setInitialValues(self):
        print "UIAPI: to set initial values."
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
        self.currentGUI.comment = ""
        self.currentGUI.commitInitialData()
        pass
    
    def dummy_fn(self):
        print "Dummy Function"
        logger.info ( "Dummy function." )
        logger.info ( "." ) 
        return 0
    
    def overrideaction_drop(self):
        logger.info ( "Default API: Drop" )
        print ns
        logger.info ( "ns: " + ns.__str__() )
        ns.message1 = 1
        logger.info ( "ns: " + ns.__str__() )
        print ns
        logger.info ( "Default API: done." )
    
    def overrideaction_reward(self):
        logger.info ( "Default API: Reward" )
        print ns
        logger.info ( "ns: " + ns.__str__() )
        ns.message1 = 2
        logger.info ( "ns: " + ns.__str__() )
        print ns
        logger.info ( "Default API: done." )
    
    def overrideaction_open(self):
        logger.info ( "Default API: Open" )
        print ns
        logger.info ( "ns: " + ns.__str__() )
        ns.message1 = 3
        logger.info ( "ns: " + ns.__str__() )
        print ns
        logger.info ( "Default API: done." )
    
    def overrideaction_close(self):
        logger.info ( "Default API: Close" )
        print ns
        logger.info ( "ns: " + ns.__str__() )
        ns.message1 = 4
        logger.info ( "ns: " + ns.__str__() )
        print ns
        logger.info ( "Default API: done." )
    
    def overrideaction_startTraining(self):
        logger.info ( "Default API: Start Training" )
        print ns
        logger.info ( "ns: " + ns.__str__() )
        ns.message1 = 5
        logger.info ( "ns: " + ns.__str__() )
        print ns
        logger.info ( "Default API: done." )
    
    def overrideaction_stopTraining(self):
        logger.info ( "Default API: Stop Training" )
        print ns
        logger.info ( "ns: " + ns.__str__() )
        ns.message1 = 6
        logger.info ( "ns: " + ns.__str__() )
        print ns
        logger.info ( "Default API: done." )
    
    def overrideaction_pauseTraining(self):
        logger.info ( "Default API: Pause / Resume Training" )
        print ns
        logger.info ( "ns: " + ns.__str__() )
        ns.message1 = 7
        logger.info ( "ns: " + ns.__str__() )
        print ns
        logger.info ( "Default API: done." )
    
    def overrideaction_resumeTraining(self):
        logger.info ( "Default API: Pause / Resume Training" )
        print ns
        logger.info ( "ns: " + ns.__str__() )
        ns.message1 = 8
        logger.info ( "ns: " + ns.__str__() )
        print ns
        logger.info ( "Default API: done." )
    
    def overrideaction_applyC(self):
        logger.info ( "Default API: Apply Comment" )
        print ns
        logger.info ( "ns: " + ns.__str__() )
        ns.message2 = self.comment
        ns.message1 = 16
        logger.info ( "ns: " + ns.__str__() )
        print ns
        logger.info ( "Default API: done." )
    
    def overrideaction_applyP(self):
        logger.info ( "Default API: Apply Parameters" )
        print ns
        logger.info ( "ns: " + ns.__str__() )
        #this actually is composed of a list of messages sent to thread.
        #we will wait till every message has been send to finish the function.
        ns.message2 = self.currentGUI.frequencyTone1
        ns.message1 = 17
        logger.info ( "ns: " + ns.__str__() )
        print ns
        while True:
            if (ns.message1 == 0):
                #carry on doing things.
                ns.message2 = self.currentGUI.frequencyTone2
                ns.message1 = 18
                logger.info ( "ns: " + ns.__str__() )
                print ns
                #return; #it is better to keep on nesting while true if code to exhaust all variables.
                while True:
                    if (ns.message1 == 0):
                        ns.message2 = self.currentGUI.movementAmount
                        ns.message1 = 19
                        logger.info ( "ns: " + ns.__str__() )
                        print ns
                        while True:
                            if (ns.message1 == 0):
                                ns.message2 = self.currentGUI.movementMethod
                                ns.message1 = 20
                                logger.info ( "ns: " + ns.__str__() )
                                print ns
                                while True:
                                    if (ns.message1 == 0):
                                        ns.message2 = self.currentGUI.movementTime
                                        ns.message1 = 21
                                        logger.info ( "ns: " + ns.__str__() )
                                        print ns
                                        while True:
                                            if (ns.message1 == 0):
                                                ns.message2 = self.currentGUI.idleTime
                                                ns.message1 = 22
                                                logger.info ( "ns: " + ns.__str__() )
                                                print ns
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
        ns.message2 = self.currentGUI.toneStart
        ns.message1 = 23
        print ns
        logger.info ( "ns: " + ns.__str__() )
        while True:
            if (ns.message1 == 0):
                #carry on doing things.
                ns.message2 = self.currentGUI.toneEnd
                ns.message1 = 24
                print ns
                logger.info ( "ns: " + ns.__str__() )
                #return; #it is better to keep on nesting while true if code to exhaust all variables.
                while True:
                    if (ns.message1 == 0):
                        ns.message2 = self.currentGUI.movementWindowStart
                        ns.message1 = 25
                        print ns
                        logger.info ( "ns: " + ns.__str__() )
                        while True:
                            if (ns.message1 == 0):
                                ns.message2 = self.currentGUI.movementWindowEnd
                                ns.message1 = 26
                                print ns
                                logger.info ( "ns: " + ns.__str__() )
                                while True:
                                    if (ns.message1 == 0):
                                        ns.message2 = self.currentGUI.interTrialStart
                                        ns.message1 = 27
                                        print ns
                                        logger.info ( "ns: " + ns.__str__() )
                                        while True:
                                            if (ns.message1 == 0):
                                                ns.message2 = self.currentGUI.interTrialEnd
                                                ns.message1 = 28
                                                print ns
                                                logger.info ( "ns: " + ns.__str__() )
                                                while True:
                                                    if (ns.message1 == 0):
                                                        ns.message2 = self.currentGUI.probabilityToneOne
                                                        ns.message1 = 29
                                                        print ns
                                                        logger.info ( "ns: " + ns.__str__() )
                                                        logger.info ( "Default API: done." )
                                                        return;
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
        print "Default API: Test T1"
        logger.info( "ns: " + ns.__str__() )
        print "Default API: Test T1 ns:.. "
        print ns
        print "Default API: Assigning variable fqt1.:.. "
        self.frequencyTone1 = self.currentGUI.frequencyTone1
        print "Default API: Test T1 setting message 2.:.. "
        ns.message1 = 10
        ns.message2 = self.frequencyTone1
        print "Default API: msg2 done"
        logger.info( "ns: " + ns.__str__() )
        print ns
        logger.info( "Default API: done." )
    
    def overrideaction_testT2(self):
        logger.info( "Default API: Test T2" )
        logger.info( "ns: " + ns.__str__() )
        print ns
        self.frequencyTone2 = self.currentGUI.frequencyTone2
        ns.message1 = 10
        ns.message2 = self.frequencyTone2
        logger.info( "ns: " + ns.__str__() )
        print ns
        logger.info( "Default API: done." )
    
    def overrideaction_showfeedback(self):
        logger.info( "Default API: Show Feedback" )
        logger.info( "ns: "+ ns.__str__() )
        print ns
        ns.message1 = 12
        print ns
        logger.info( "ns: "+ ns.__str__() )
        logger.info( "Default API: done." )
    
    def overrideaction_hidefeedback(self):
        logger.info( "Default API: Hide Feedback" )
        logger.info( "ns: "+ ns.__str__() )
        print ns
        ns.message1 = 13
        print ns
        logger.info( "ns: "+ ns.__str__() )
        logger.info( "Default API: done." )
    
    def overrideaction_showtracking(self):
        logger.info( "Default API: Show Tracking" )
        logger.info( "ns: "+ ns.__str__() )
        print ns
        ns.message1 = 14
        print ns
        logger.info( "ns: "+ ns.__str__() )
        logger.info( "Default API: done." )
    
    def overrideaction_hidetracking(self):
        logger.info( "Default API: Hide Tracking" )
        logger.info( "ns: "+ ns.__str__() )
        print ns
        ns.message1 = 15
        print ns
        logger.info( "ns: "+ ns.__str__() )
        logger.info( "Default API: done." )
    
    def action_drop(self):
        print "DROP from API"
        logger.info( "API: Drop" )
        try:
            self.overrideaction_drop()
        except:
            logger.info( "API Error: Drop" )
    
    def action_reward(self):
                logger.info( "API: Reward" )
                try:
                    self.overrideaction_reward()
                except:
                    logger.info( "API Error: Reward" )
        
    def action_open(self):
                logger.info( "API: Open" )
                try:
                    self.overrideaction_open()
                except:
                    logger.info( "API Error: Open" )
        
    def action_close(self):
                logger.info( "API: Close" )
                try:
                    self.overrideaction_close()
                except:
                    logger.info( "API Error: Close" )
    
    def action_startTraining(self):
                logger.info( "API: Start Training" )
                try:
                    self.overrideaction_startTraining()
                except:
                    logger.info( "API Error: Start Training" )
    
    def action_stopTraining(self):
                logger.info( "API: Stop Training" )
                try:
                    self.overrideaction_stopTraining()
                except:
                    logger.info( "API Error: Stop Training" )
    
    def action_pauseTraining(self):
                logger.info( "API: Pause Training" )
                try:
                    self.overrideaction_pauseTraining()
                except:
                    logger.info( "API Error: Pause Training" )
    
    def action_resumeTraining(self):
                logger.info( "API: Resume Training" )
                try:
                    self.overrideaction_resumeTraining()
                except:
                    logger.info( "API Error: Resume Training" )
    
    def action_applyC(self):
        self.comment = self.currentGUI.comment
        logger.info( "API: Apply Comments: " + str(self.comment) )
        try:
            self.overrideaction_applyC()
        except:
            logger.info( "API Error: applyC" )
    
    def action_applyP(self):
        self.frequencyTone1 = self.currentGUI.frequencyTone1
        self.frequencyTone2 = self.currentGUI.frequencyTone2
        self.movementAmount = self.currentGUI.movementAmount
        self.movementMethod = self.currentGUI.movementMethod
        self.movementTime = self.currentGUI.movementTime
        self.idleTime = self.currentGUI.idleTime
        logger.info( "API: Apply Parameters:" )
        #print self.frequencyTone1, "--",self.frequencyTone2, "--",
        #print self.movementAmount , "--", self.movementMethod,  "--", self.movementTime,  "--", self.idleTime
        try:
            self.overrideaction_applyP()
        except:
            logger.info( "API Error: applyP" )
    
    def action_applyTE(self):
        self.toneStart = self.currentGUI.toneStart
        self.toneEnd = self.currentGUI.toneEnd
        self.movementWindowStart = self.currentGUI.movementWindowStart
        self.movementWindowEnd = self.currentGUI.movementWindowEnd
        self.interTrialStart = self.currentGUI.interTrialStart
        self.interTrialEnd = self.currentGUI.interTrialEnd
        self.probabilityToneOne = self.currentGUI.probabilityToneOne
        
        logger.info( "API: Apply Trial Events:" )
        #print self.toneStart, "--",self.toneEnd, "--",
        #print self.movementWindowStart , "--", self.movementWindowEnd, "--"
        #print self.interTrialStart,  "--", self.interTrialEnd, "--", self.probabilityToneOne
        try:
            self.overrideaction_applyTE()
        except:
            logger.info( "API Error: applyTE" )
    
    def action_testT1(self):
        logger.info( "API: Test Tone 1" )
        try:
            self.overrideaction_testT1()
        except:
            logger.info( "API Error: testT1" )
    
    def action_testT2(self):
        logger.info( "API: Test Tone 2" )
        try:
            self.overrideaction_testT2()
        except:
            logger.info( "API Error: testT2" )
    
    def action_showfeedback(self):
        logger.info( "API: Show Feedback" )
        try:
            self.overrideaction_showfeedback()
        except:
            logger.info( "API Error: Show Feedback" )
    
    def action_hidefeedback(self):
        logger.info( "API: Hide Feedback" )
        try:
            self.overrideaction_hidefeedback()
        except:
            logger.info( "API Error: Hide Feedback" )
    
    def action_showtracking(self):
        logger.info( "API: Show Tracking" )
        try:
            self.overrideaction_showtracking()
        except:
            logger.info( "API Error: Show Tracking" )
    
    def action_hidetracking(self):
        logger.info( "API: Hide Tracking" )
        try:
            self.overrideaction_hidetracking()
        except:
            logger.info( "API Error: Hide Tracking" )
    
    def action_exit(self):
        logger.info( "Default API: Exiting GUI from API." )
        #logger.info( "ns: ", str(ns) )
        print ns
        ns.message1 = 9
        print ns
        #logger.info( "ns: ", str(ns) )
        logger.info( "Default API: done." )
        try:
                    import os
                    os._exit(0)
                    gtk.main_quit()
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
        print "Launching Glade interface."
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
        #self.comment = ""
        #self.thread_function(
        #thread1 = threading.Thread(target=self.thread_function, name="glade_GUI")
        #thread1.start()
        logger.info( "message variables: "+ self.ns.__str__() )
        logger.info( str(self) +  "  Glade Interface Started" )
        self.setInitialValues()
        self.thread_function()
        
    
    def launch_tkinter(self):
        import userInterface_tk
        self.currentGUI = userInterface_tk.GUIGTK_Class()
        print "Overriding functions:"
        time.sleep(0.5)
        time.sleep(0.5)
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
        self.currentGUI.overrideaction_exit = self.action_exit
        print "   Overriding functions: done."
        logger.info( "message variables: "+ self.ns.__str__() )
        logger.info( str(self) +  "  Tkinter Interface Started" )
        self.setInitialValues()
        while True:
            time.sleep(1.0)
        
    
    def thread_function(self):
        import userInterface_glade
        import time
        #userInterface_glade.gtk.gdk.threads_init()
        #time.sleep(3)
        userInterface_glade.gtk.main()
        logger.info( str(self) +  "  Glade Interface Finished." )
        #while (True):
            #userInterface_glade.gtk.threads_enter()
            #userInterface_glade.gtk.main()
            #userInterface_glade.gtk.main_iteration_do()
            #time.sleep(0.001)
            #print "bucle .."
            #userInterface_glade.gtk.threads_leave()
        pass

if __name__ == '__main__':
    # create a logging format
    formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    dateformat = '%Y/%m/%d %I:%M:%S %p'
    logging.basicConfig(filename='logs/userInterfaceAPI.log', filemode='w',
            level=logging.DEBUG, format=formatter, datefmt = dateformat)
    logging.info('Start userInterfaceAPI Test')
    import multiprocessing
    import time
    print "init.."
    p = multiprocessing.Process(target=userInterface_API(True))
    p.start()
    logging.info('End userInterfaceAPI Test')
