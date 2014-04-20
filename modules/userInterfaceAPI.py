import os, sys
import time


class userInterface_API:
    usingTK = 0 #0: using GTk;   1: using TK
    ns = 0 # message variable , that will be shared among processes.
    def __init__(self, toStart):
        print "initializing userInterfaceAPI"
        #put initialization variables here.
        #self.launch_glade() # by design, won't initialize the gtk main loop from the init but from outside.
        if (toStart == True):
            self.launch_glade()
        print "userInterfaceAPI created."
    
    def setNamespace(self, nuevons):
        global ns
        ns = nuevons
        print "Namespace set"
        self.launch_glade()
    
    def dummy_fn(self):
        
        print "Dummy function."
        print "."
        return 0
    
    def overrideaction_drop(self):
        print "Default API: Drop"
        print "ns: ", ns
        print ns.message1
        ns.message1 = 1
        print ns.message1
        print "Default API: done."
    
    def overrideaction_reward(self):
        print "Default API: Reward"
        print "ns: ", ns
        print ns.message1
        ns.message1 = 2
        print ns.message1
        print "Default API: done."
    
    def overrideaction_open(self):
        print "Default API: Open"
        print "ns: ", ns
        print ns.message1
        ns.message1 = 3
        print ns.message1
        print "Default API: done."
    
    def overrideaction_close(self):
        print "Default API: Close"
        print "ns: ", ns
        print ns.message1
        ns.message1 = 4
        print ns.message1
        print "Default API: done."
    
    def overrideaction_startTraining(self):
        print "Default API: Start Training"
        print "ns: ", ns
        print ns.message1
        ns.message1 = 5
        print ns.message1
        print "Default API: done."
    
    def overrideaction_stopTraining(self):
        print "Default API: Stop Training"
        print "ns: ", ns
        print ns.message1
        ns.message1 = 6
        print ns.message1
        print "Default API: done."
    
    def overrideaction_pauseTraining(self):
        print "Default API: Pause Training"
        print "ns: ", ns
        print ns.message1
        ns.message1 = 7
        print ns.message1
        print "Default API: done."
    
    def overrideaction_resumeTraining(self):
        print "Default API: Resume Training"
        print "ns: ", ns
        print ns.message1
        ns.message1 = 8
        print ns.message1
        print "Default API: done."
    
    def overrideaction_applyC(self):
        print "Default API: Apply Comment"
        ns.message2 = self.comment
        ns.message1 = 16
        print ns
        print "Default API: done."
    
    def overrideaction_applyP(self):
        print "Default API: Apply Parameters"
        #this actually is composed of a list of messages sent to thread.
        #we will wait till every message has been send to finish the function.
        ns.message2 = self.currentGUI.frequencyTone1
        ns.message1 = 17
        print ns
        while True:
            if (ns.message1 == 0):
                #carry on doing things.
                ns.message2 = self.currentGUI.frequencyTone2
                ns.message1 = 18
                print ns
                #return; #it is better to keep on nesting while true if code to exhaust all variables.
                while True:
                    if (ns.message1 == 0):
                        ns.message2 = self.currentGUI.movementAmount
                        ns.message1 = 19
                        print ns
                        while True:
                            if (ns.message1 == 0):
                                ns.message2 = self.currentGUI.movementMethod
                                ns.message1 = 20
                                print ns
                                while True:
                                    if (ns.message1 == 0):
                                        ns.message2 = self.currentGUI.movementTime
                                        ns.message1 = 21
                                        print ns
                                        while True:
                                            if (ns.message1 == 0):
                                                ns.message2 = self.currentGUI.idleTime
                                                ns.message1 = 22
                                                print ns
                                                print "Default API: done."
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
        print "Default API: Apply Trial Events"
        ns.message2 = self.currentGUI.toneStart
        ns.message1 = 23
        print ns
        while True:
            if (ns.message1 == 0):
                #carry on doing things.
                ns.message2 = self.currentGUI.toneEnd
                ns.message1 = 24
                print ns
                #return; #it is better to keep on nesting while true if code to exhaust all variables.
                while True:
                    if (ns.message1 == 0):
                        ns.message2 = self.currentGUI.movementWindowStart
                        ns.message1 = 25
                        print ns
                        while True:
                            if (ns.message1 == 0):
                                ns.message2 = self.currentGUI.movementWindowEnd
                                ns.message1 = 26
                                print ns
                                while True:
                                    if (ns.message1 == 0):
                                        ns.message2 = self.currentGUI.interTrialStart
                                        ns.message1 = 27
                                        print ns
                                        while True:
                                            if (ns.message1 == 0):
                                                ns.message2 = self.currentGUI.interTrialEnd
                                                ns.message1 = 28
                                                print ns
                                                while True:
                                                    if (ns.message1 == 0):
                                                        ns.message2 = self.currentGUI.probabilityToneOne
                                                        ns.message1 = 29
                                                        print ns
                                                        print "Default API: done."
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
        print "Default API: Test T1"
        print "ns: ", ns
        print ns.message1
        ns.message1 = 10
        print ns.message1
        print "Default API: done."
    
    def overrideaction_testT2(self):
        print "Default API: Test T2"
        print "ns: ", ns
        print ns.message1
        ns.message1 = 11
        print ns.message1
        print "Default API: done."
    
    def overrideaction_showfeedback(self):
        print "Default API: Show Feedback"
        print "ns: ", ns
        print ns.message1
        ns.message1 = 12
        print ns.message1
        print "Default API: done."
    
    def overrideaction_hidefeedback(self):
        print "Default API: Hide Feedback"
        print "ns: ", ns
        print ns.message1
        ns.message1 = 13
        print ns.message1
        print "Default API: done."
    
    def overrideaction_showtracking(self):
        print "Default API: Show Tracking"
        print "ns: ", ns
        print ns.message1
        ns.message1 = 14
        print ns.message1
        print "Default API: done."
    
    def overrideaction_hidetracking(self):
        print "Default API: Hide Tracking"
        print "ns: ", ns
        print ns.message1
        ns.message1 = 15
        print ns.message1
        print "Default API: done."
    
    def action_drop(self):
        print "API: Drop"
        try:
            self.overrideaction_drop()
        except:
            print "API Error: Drop"
    
    def action_reward(self):
                print "API: Reward"
                try:
                    self.overrideaction_reward()
                except:
                    print "API Error: Reward"
        
    def action_open(self):
                print "API: Open"
                try:
                    self.overrideaction_open()
                except:
                    print "API Error: Open"
        
    def action_close(self):
                print "API: Close"
                try:
                    self.overrideaction_close()
                except:
                    print "API Error: Close"
    
    def action_startTraining(self):
                print "API: Start Training"
                try:
                    self.overrideaction_startTraining()
                except:
                    print "API Error: Start Training"
    
    def action_stopTraining(self):
                print "API: Stop Training"
                try:
                    self.overrideaction_stopTraining()
                except:
                    print "API Error: Stop Training"
    
    def action_pauseTraining(self):
                print "API: Pause Training"
                try:
                    self.overrideaction_pauseTraining()
                except:
                    print "API Error: Pause Training"
    
    def action_resumeTraining(self):
                print "API: Resume Training"
                try:
                    self.overrideaction_resumeTraining()
                except:
                    print "API Error: Resume Training"
    
    def action_applyC(self):
        self.comment = self.currentGUI.comment
        print "API: Apply Comments: ", self.comment
        try:
            self.overrideaction_applyC()
        except:
            print "API Error: applyC"
    
    def action_applyP(self):
        self.frequencyTone1 = self.currentGUI.frequencyTone1
        self.frequencyTone2 = self.currentGUI.frequencyTone2
        self.movementAmount = self.currentGUI.movementAmount
        self.movementMethod = self.currentGUI.movementMethod
        self.movementTime = self.currentGUI.movementTime
        self.idleTime = self.currentGUI.idleTime
        print "API: Apply Parameters:"
        print self.frequencyTone1, "--",self.frequencyTone2, "--",
        print self.movementAmount , "--", self.movementMethod,  "--", self.movementTime,  "--", self.idleTime
        try:
            self.overrideaction_applyP()
        except:
            print "API Error: applyP"
    
    def action_applyTE(self):
        self.toneStart = self.currentGUI.toneStart
        self.toneEnd = self.currentGUI.toneEnd
        self.movementWindowStart = self.currentGUI.movementWindowStart
        self.movementWindowEnd = self.currentGUI.movementWindowEnd
        self.interTrialStart = self.currentGUI.interTrialStart
        self.interTrialEnd = self.currentGUI.interTrialEnd
        self.probabilityToneOne = self.currentGUI.probabilityToneOne
        
        print "API: Apply Trial Events:"
        print self.toneStart, "--",self.toneEnd, "--",
        print self.movementWindowStart , "--", self.movementWindowEnd, "--"
        print self.interTrialStart,  "--", self.interTrialEnd, "--", self.probabilityToneOne
        try:
            self.overrideaction_applyTE()
        except:
            print "API Error: applyTE"
    
    def action_testT1(self):
        print "API: Test Tone 1"
        try:
            self.overrideaction_testT1()
        except:
            print "API Error: testT1"
    
    def action_testT2(self):
        print "API: Test Tone 2"
        try:
            self.overrideaction_testT2()
        except:
            print "API Error: testT2"
    
    def action_showfeedback(self):
        print "API: Show Feedback"
        try:
            self.overrideaction_showfeedback()
        except:
            print "API Error: Show Feedback"
    
    def action_hidefeedback(self):
        print "API: Hide Feedback"
        try:
            self.overrideaction_hidefeedback()
        except:
            print "API Error: Hide Feedback"
    
    def action_showtracking(self):
        print "API: Show Tracking"
        try:
            self.overrideaction_showtracking()
        except:
            print "API Error: Show Tracking"
    
    def action_hidetracking(self):
        print "API: Hide Tracking"
        try:
            self.overrideaction_hidetracking()
        except:
            print "API Error: Hide Tracking"
    
    def action_exit(self):
        print "Default API: Exiting GUI from API."
        print "ns: ", ns
        print ns.message1
        ns.message1 = 9
        print ns.message1
        print "Default API: done."
        try:
                    import os
                    os._exit(0)
                    gtk.main_quit()
        except:
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
        #thread2 = threading.Thread(target=self.thread_test)
        #thread2.start()
        #thread3 = threading.Thread(target=self.thread_test2)
        #thread3.start()
        print "message variables: ", self.ns
        print self, "Glade Interface Started"
        self.thread_function()
        
        
    def thread_function(self):
        import userInterface_glade
        import time
        #userInterface_glade.gtk.gdk.threads_init()
        #time.sleep(3)
        userInterface_glade.gtk.main()
        print "finish glade."
        #while (True):
            #userInterface_glade.gtk.threads_enter()
            #userInterface_glade.gtk.main()
            #userInterface_glade.gtk.main_iteration_do()
            #time.sleep(0.001)
            #print "bucle .."
            #userInterface_glade.gtk.threads_leave()
    
    def thread_test(self):
        import time
        while (True):
            print self.ns
            time.sleep(5)
    
    def thread_test2(self):
        import sphereVideoDetection
        videoDet = sphereVideoDetection.sphereVideoDetection(0, 320, 240)

if __name__ == '__main__':
    import multiprocessing
    import time
    print "init.."
    p = multiprocessing.Process(target=userInterface_API(True))
    p.start()
    print "finish glade."
    while(True):
        time.sleep(1)
        print "sleeping"
        print p
    #a.dummy_fn()
    #a.launch_glade()
