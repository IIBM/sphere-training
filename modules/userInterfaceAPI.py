import os
import sys
import time
import logging
logger = logging.getLogger('userInterfaceAPI')
import track_bola_utils


class userInterface_API:
    #----------------------------------------------
    #API that handles the user interface.
    #it currently has two types: tkinter and GTK.
    #This class receives multiprocessing messages from the currentGUI object
    #   (in that strict order: the messages are from currentGUI to API)
    #----------------------------------------------
    pass
    last_message = -1; #to be accessed by training.py when it needs the var
    last_argument = -1; #to be accessed by training.py when it needs the var
    stopAll = False
    subj_list = [""]
    multiProcSubjectNameQuery = 1 #if 0, use non-multiprocessing autocompleteentry. if 1, use multiprocessing. def 1
    subj_name = ""
    usingTK = 0
    toneStart = 0
    toneEnd = 0
    movementWindowStart = 0
    movementWindowEnd = 0
    interTrialStart = 0
    interTrialEnd = 0
    probabilityToneOne = 0
    frequencyTone1 = 0
    frequencyTone2 = 0
    volumeTone1 = 0
    volumeTone2 = 0
    movementAmount = 0
    movementMethod = 0
    movementTime = 0
    idleTime = 0
    comment = ""
    
    current_type = 0
    
    type_pavlov = 0
    type_skinner = 0;
    type_ocond = 0;
    type_discr = 0;
    requireStillnessVar = 0;
    
    pavlovVars = track_bola_utils.dummyClass()
    skinnerVars = track_bola_utils.dummyClass()
    ocondVars = track_bola_utils.dummyClass()
    discrVars = track_bola_utils.dummyClass()
    
    
    pavlovVars.toneStart = 1
    pavlovVars.toneEnd = 1
    pavlovVars.movementWindowStart = 1
    pavlovVars.movementWindowEnd = 1
    pavlovVars.interTrialStart = 1
    pavlovVars.interTrialEnd = 1
    pavlovVars.probabilityToneOne = 1
    pavlovVars.frequencyTone1 = 1
    pavlovVars.frequencyTone2 = 1
    pavlovVars.volumeTone1 = 1
    pavlovVars.volumeTone2 = 1
    #pavlovVars.movementAmount = 1
    #pavlovVars.movementMethod = 1
    pavlovVars.movementTime = 1
    pavlovVars.idleTime = 1
    pavlovVars.requireStillnessVar = 0;
    
    
    
    skinnerVars.toneStart = 1
    skinnerVars.toneEnd = 1
    skinnerVars.movementWindowStart = 1
    skinnerVars.movementWindowEnd = 1
    skinnerVars.interTrialStart = 1
    skinnerVars.interTrialEnd = 1
    skinnerVars.probabilityToneOne = 1
    skinnerVars.frequencyTone1 = 1
    skinnerVars.frequencyTone2 = 1
    skinnerVars.volumeTone1 = 1
    skinnerVars.volumeTone2 = 1
    #skinnerVars.movementAmount = 1
    #skinnerVars.movementMethod = 1
    skinnerVars.movementTime = 1
    skinnerVars.idleTime = 1
    skinnerVars.requireStillnessVar = 0;
    
    ocondVars.toneStart = 1
    ocondVars.toneEnd = 1
    ocondVars.movementWindowStart = 1
    ocondVars.movementWindowEnd = 1
    ocondVars.interTrialStart = 1
    ocondVars.interTrialEnd = 1
    ocondVars.probabilityToneOne = 1
    ocondVars.frequencyTone1 = 1
    ocondVars.frequencyTone2 = 1
    ocondVars.volumeTone1 = 1
    ocondVars.volumeTone2 = 1
    #ocondVars.movementAmount = 1
    #ocondVars.movementMethod = 1
    ocondVars.movementTime = 1
    ocondVars.idleTime = 1
    ocondVars.requireStillnessVar = 0;
    
    discrVars.toneStart = 1
    discrVars.toneEnd = 1
    discrVars.movementWindowStart = 1
    discrVars.movementWindowEnd = 1
    discrVars.interTrialStart = 1
    discrVars.interTrialEnd = 1
    discrVars.probabilityToneOne = 1
    discrVars.frequencyTone1 = 1
    discrVars.frequencyTone2 = 1
    discrVars.volumeTone1 = 1
    discrVars.volumeTone2 = 1
    #discrVars.movementAmount = 1
    #discrVars.movementMethod = 1
    discrVars.movementTime = 1
    discrVars.idleTime = 1
    discrVars.requireStillnessVar = 0;
    
    def launch_multiproc(self, jobl, toStart):
        multipUI = multiproc_userInterface_API(jobl,  False)
        time.sleep(0.5)
        #checkK = threading.Thread(target=self.checkOutJobContinuously, args=(a,) )
        #checkK.start()
        #acA corresponde setear todas las configs del proceso
        multipUI.usingTK = self.usingTK
        multipUI.toneStart = self.toneStart
        multipUI.toneEnd = self.toneEnd
        multipUI.movementWindowStart = self.movementWindowStart
        multipUI.movementWindowEnd = self.movementWindowEnd
        multipUI.interTrialStart = self.interTrialStart
        multipUI.interTrialEnd = self.interTrialEnd
        multipUI.probabilityToneOne = self.probabilityToneOne
        multipUI.frequencyTone1 = self.frequencyTone1
        multipUI.frequencyTone2 = self.frequencyTone2
        multipUI.volumeTone1 = self.volumeTone1
        multipUI.volumeTone2 = self.volumeTone2
        
        multipUI.movementAmount = self.movementAmount
        multipUI.movementMethod = self.movementMethod
        multipUI.movementTime = self.movementTime
        multipUI.idleTime = self.idleTime
        multipUI.comment = self.comment
        
        
        multipUI.type_pavlov = self.type_pavlov
        multipUI.type_skinner = self.type_skinner
        multipUI.type_ocond = self.type_ocond
        multipUI.type_discr = self.type_discr
        
        multipUI.requireStillnessVar = self.requireStillnessVar
        
        multipUI.current_type = self.current_type
        
        
        
        
        multipUI.pavlovVars.toneStart = self.pavlovVars.toneStart
        multipUI.pavlovVars.toneEnd = self.pavlovVars.toneEnd
        multipUI.pavlovVars.movementWindowStart = self.pavlovVars.movementWindowStart
        multipUI.pavlovVars.movementWindowEnd = self.pavlovVars.movementWindowEnd
        multipUI.pavlovVars.interTrialStart = self.pavlovVars.interTrialStart
        multipUI.pavlovVars.interTrialEnd = self.pavlovVars.interTrialEnd
        multipUI.pavlovVars.probabilityToneOne = self.pavlovVars.probabilityToneOne
        multipUI.pavlovVars.frequencyTone1 = self.pavlovVars.frequencyTone1
        multipUI.pavlovVars.frequencyTone2 = self.pavlovVars.frequencyTone2
        multipUI.pavlovVars.volumeTone1 = self.pavlovVars.volumeTone1
        multipUI.pavlovVars.volumeTone2 = self.pavlovVars.volumeTone2
        
        #multipUI.pavlovVars.movementAmount = self.pavlovVars.movementAmount
        #multipUI.pavlovVars.movementMethod = self.pavlovVars.movementMethod
        multipUI.pavlovVars.movementTime = self.pavlovVars.movementTime
        multipUI.pavlovVars.idleTime = self.pavlovVars.idleTime
        
        multipUI.pavlovVars.requireStillnessVar = self.pavlovVars.requireStillnessVar
        
        if (self.current_type == "pavlov"):
            #overwrite "default" vars
            multipUI.toneStart = self.pavlovVars.toneStart
            multipUI.toneEnd = self.pavlovVars.toneEnd
            multipUI.movementWindowStart = self.pavlovVars.movementWindowStart
            multipUI.movementWindowEnd = self.pavlovVars.movementWindowEnd
            multipUI.interTrialStart = self.pavlovVars.interTrialStart
            multipUI.interTrialEnd = self.pavlovVars.interTrialEnd
            multipUI.probabilityToneOne = self.pavlovVars.probabilityToneOne
            multipUI.frequencyTone1 = self.pavlovVars.frequencyTone1
            multipUI.frequencyTone2 = self.pavlovVars.frequencyTone2
            multipUI.volumeTone1 = self.pavlovVars.volumeTone1
            multipUI.volumeTone2 = self.pavlovVars.volumeTone2
            
            #multipUI.movementAmount = self.pavlovVars.movementAmount
            #multipUI.movementMethod = self.pavlovVars.movementMethod
            multipUI.movementTime = self.pavlovVars.movementTime
            multipUI.idleTime = self.pavlovVars.idleTime
            
            multipUI.requireStillnessVar = self.pavlovVars.requireStillnessVar
        
        #############################
        
        multipUI.skinnerVars.toneStart = self.skinnerVars.toneStart
        multipUI.skinnerVars.toneEnd = self.skinnerVars.toneEnd
        multipUI.skinnerVars.movementWindowStart = self.skinnerVars.movementWindowStart
        multipUI.skinnerVars.movementWindowEnd = self.skinnerVars.movementWindowEnd
        multipUI.skinnerVars.interTrialStart = self.skinnerVars.interTrialStart
        multipUI.skinnerVars.interTrialEnd = self.skinnerVars.interTrialEnd
        multipUI.skinnerVars.probabilityToneOne = self.skinnerVars.probabilityToneOne
        multipUI.skinnerVars.frequencyTone1 = self.skinnerVars.frequencyTone1
        multipUI.skinnerVars.frequencyTone2 = self.skinnerVars.frequencyTone2
        multipUI.skinnerVars.volumeTone1 = self.skinnerVars.volumeTone1
        multipUI.skinnerVars.volumeTone2 = self.skinnerVars.volumeTone2
        
        #multipUI.skinnerVars.movementAmount = self.skinnerVars.movementAmount
        #multipUI.skinnerVars.movementMethod = self.skinnerVars.movementMethod
        multipUI.skinnerVars.movementTime = self.skinnerVars.movementTime
        multipUI.skinnerVars.idleTime = self.skinnerVars.idleTime
        
        multipUI.skinnerVars.requireStillnessVar = self.skinnerVars.requireStillnessVar
        
        if (self.current_type == "skinner"):
            #overwrite "default" vars
            multipUI.toneStart = self.skinnerVars.toneStart
            multipUI.toneEnd = self.skinnerVars.toneEnd
            multipUI.movementWindowStart = self.skinnerVars.movementWindowStart
            multipUI.movementWindowEnd = self.skinnerVars.movementWindowEnd
            multipUI.interTrialStart = self.skinnerVars.interTrialStart
            multipUI.interTrialEnd = self.skinnerVars.interTrialEnd
            multipUI.probabilityToneOne = self.skinnerVars.probabilityToneOne
            multipUI.frequencyTone1 = self.skinnerVars.frequencyTone1
            multipUI.frequencyTone2 = self.skinnerVars.frequencyTone2
            multipUI.volumeTone1 = self.skinnerVars.volumeTone1
            multipUI.volumeTone2 = self.skinnerVars.volumeTone2
            
            #multipUI.movementAmount = self.skinnerVars.movementAmount
            #multipUI.movementMethod = self.skinnerVars.movementMethod
            multipUI.movementTime = self.skinnerVars.movementTime
            multipUI.idleTime = self.skinnerVars.idleTime
            
            multipUI.requireStillnessVar = self.skinnerVars.requireStillnessVar
        
        #############################
        
        
        
        
        
        multipUI.ocondVars.toneStart = self.ocondVars.toneStart
        multipUI.ocondVars.toneEnd = self.ocondVars.toneEnd
        multipUI.ocondVars.movementWindowStart = self.ocondVars.movementWindowStart
        multipUI.ocondVars.movementWindowEnd = self.ocondVars.movementWindowEnd
        multipUI.ocondVars.interTrialStart = self.ocondVars.interTrialStart
        multipUI.ocondVars.interTrialEnd = self.ocondVars.interTrialEnd
        multipUI.ocondVars.probabilityToneOne = self.ocondVars.probabilityToneOne
        multipUI.ocondVars.frequencyTone1 = self.ocondVars.frequencyTone1
        multipUI.ocondVars.frequencyTone2 = self.ocondVars.frequencyTone2
        multipUI.ocondVars.volumeTone1 = self.ocondVars.volumeTone1
        multipUI.ocondVars.volumeTone2 = self.ocondVars.volumeTone2
        
        #multipUI.ocondVars.movementAmount = self.ocondVars.movementAmount
        #multipUI.ocondVars.movementMethod = self.ocondVars.movementMethod
        multipUI.ocondVars.movementTime = self.ocondVars.movementTime
        multipUI.ocondVars.idleTime = self.ocondVars.idleTime
        
        multipUI.ocondVars.requireStillnessVar = self.ocondVars.requireStillnessVar
        
        
        if (self.current_type == "oc"):
            #overwrite "default" vars
            multipUI.toneStart = self.ocondVars.toneStart
            multipUI.toneEnd = self.ocondVars.toneEnd
            multipUI.movementWindowStart = self.ocondVars.movementWindowStart
            multipUI.movementWindowEnd = self.ocondVars.movementWindowEnd
            multipUI.interTrialStart = self.ocondVars.interTrialStart
            multipUI.interTrialEnd = self.ocondVars.interTrialEnd
            multipUI.probabilityToneOne = self.ocondVars.probabilityToneOne
            multipUI.frequencyTone1 = self.ocondVars.frequencyTone1
            multipUI.frequencyTone2 = self.ocondVars.frequencyTone2
            multipUI.volumeTone1 = self.ocondVars.volumeTone1
            multipUI.volumeTone2 = self.ocondVars.volumeTone2
            
            #multipUI.movementAmount = self.ocondVars.movementAmount
            #multipUI.movementMethod = self.ocondVars.movementMethod
            multipUI.movementTime = self.ocondVars.movementTime
            multipUI.idleTime = self.ocondVars.idleTime
            
            multipUI.requireStillnessVar = self.ocondVars.requireStillnessVar
        
        #############################
        
        
        multipUI.discrVars.toneStart = self.discrVars.toneStart
        multipUI.discrVars.toneEnd = self.discrVars.toneEnd
        multipUI.discrVars.movementWindowStart = self.discrVars.movementWindowStart
        multipUI.discrVars.movementWindowEnd = self.discrVars.movementWindowEnd
        multipUI.discrVars.interTrialStart = self.discrVars.interTrialStart
        multipUI.discrVars.interTrialEnd = self.discrVars.interTrialEnd
        multipUI.discrVars.probabilityToneOne = self.discrVars.probabilityToneOne
        multipUI.discrVars.frequencyTone1 = self.discrVars.frequencyTone1
        multipUI.discrVars.frequencyTone2 = self.discrVars.frequencyTone2
        multipUI.discrVars.volumeTone1 = self.discrVars.volumeTone1
        multipUI.discrVars.volumeTone2 = self.discrVars.volumeTone2
        
        #multipUI.discrVars.movementAmount = self.discrVars.movementAmount
        #multipUI.discrVars.movementMethod = self.discrVars.movementMethod
        multipUI.discrVars.movementTime = self.discrVars.movementTime
        multipUI.discrVars.idleTime = self.discrVars.idleTime
        
        multipUI.discrVars.requireStillnessVar = self.discrVars.requireStillnessVar
        
        if (self.current_type == "discr"):
            #overwrite "default" vars
            multipUI.toneStart = self.discrVars.toneStart
            multipUI.toneEnd = self.discrVars.toneEnd
            multipUI.movementWindowStart = self.discrVars.movementWindowStart
            multipUI.movementWindowEnd = self.discrVars.movementWindowEnd
            multipUI.interTrialStart = self.discrVars.interTrialStart
            multipUI.interTrialEnd = self.discrVars.interTrialEnd
            multipUI.probabilityToneOne = self.discrVars.probabilityToneOne
            multipUI.frequencyTone1 = self.discrVars.frequencyTone1
            multipUI.frequencyTone2 = self.discrVars.frequencyTone2
            multipUI.volumeTone1 = self.discrVars.volumeTone1
            multipUI.volumeTone2 = self.discrVars.volumeTone2
            
            #multipUI.movementAmount = self.discrVars.movementAmount
            #multipUI.movementMethod = self.discrVars.movementMethod
            multipUI.movementTime = self.discrVars.movementTime
            multipUI.idleTime = self.discrVars.idleTime
            
            multipUI.requireStillnessVar = self.discrVars.requireStillnessVar
        
        #############################
        
        
        
        
        
        print ".- %d" % self.requireStillnessVar
        print "all variables set."
        if (toStart):
            multipUI.launch_GUI()
        
    def getSubjName(self):
        a = multiproc_userInterface_API()
        a.usingTK = self.usingTK
        a.subj_list = self.subj_list
        a.multiProcSubjectNameQuery = self.multiProcSubjectNameQuery
        return a.getSubjName()
    
    def checkInputObjToApi(self):
        if (self.messageObjToAPI.qsize() > 0 or self.messageObjToAPI.empty() == False ):
                try:
                        tempvar = self.messageObjToAPI.get()
                        self.messageObjToAPI.task_done()
                except:
                        return;
                #print str("checkJobList: queue: " + str(tempvar) )
                index = tempvar[0]
                try:
                    argument = tempvar[1]
                except:
                    argument = ""
                    pass
                
                #print "checkInputObjToApi: Got a Message:", index
                #print "checkInputObjToApi: Message's argument:", argument
                logger.debug("checkInputObjToApi: Got a Message: %s    %s" % (str( index) , str(argument) ) )
                self.last_message = index
                self.last_argument = argument
                if (index == 9):
                    print "Exiting GUI API"
                    self.exit()
    
    def __launchProcess(self):
        import multiprocessing
        self.displayProc = multiprocessing.Process(target=self.launch_multiproc, args=(self.messageObjToAPI, True,) )
        time.sleep(0.5)
        #print "post display defined: %r" % self.displayProc
        self.displayProc.start()
        import threading
        self.checkMsgThread = threading.Thread(target = self.iLoopCheckInputObjToAPI);
        self.checkMsgThread.start()
    
    def iLoopCheckInputObjToAPI(self):
        print "Thread started: iLoopCheckInputObjToAPI"
        while self.stopAll == False:
            self.checkInputObjToApi()
            time.sleep(0.110) #warning: this time sleep should be at least bigger than frequency from main training.
            #else there'll be unread messages.
            pass
    
    def __init__(self, toStart = False):
        print "starting front end API process"
        import multiprocessing
        self.messageObjToAPI = multiprocessing.JoinableQueue()
        if (toStart):
            self.__launchProcess()
        print "process started."
        logger.debug("userInterface_API process Started.")
        pass
    
    def launch_GUI(self):
        print "launching GUI.."
        self.__launchProcess()
        pass
    
    def exit(self):
        time.sleep(1)
        self.displayProc.terminate()
        time.sleep(0.05)
        del self.messageObjToAPI
        del self.displayProc
        
        self.stopAll = True;
        time.sleep(0.2)
        sys.exit()



class multiproc_userInterface_API:
    usingTK = 0 #0: using GTk;   1: using TK
    multiProcSubjectNameQuery = 1 #if 0, use non-multiprocessing autocompleteentry. if 1, use multiprocessing. def 1
    jobList = 0 # message Job Queue between processes.
    ns = 0
    subj_list = [""]
    subj_name = ""
    type_pavlov = 0
    type_skinner = 0;
    type_ocond = 0;
    type_discr = 0;
    requireStillnessVar = 0;
    
    current_type = 0;
    
    pavlovVars = track_bola_utils.dummyClass()
    skinnerVars = track_bola_utils.dummyClass()
    ocondVars = track_bola_utils.dummyClass()
    discrVars = track_bola_utils.dummyClass()
    
    
    pavlovVars.toneStart = 1
    pavlovVars.toneEnd = 1
    pavlovVars.movementWindowStart = 1
    pavlovVars.movementWindowEnd = 1
    pavlovVars.interTrialStart = 1
    pavlovVars.interTrialEnd = 1
    pavlovVars.probabilityToneOne = 1
    pavlovVars.frequencyTone1 = 1
    pavlovVars.frequencyTone2 = 1
    pavlovVars.volumeTone1 = 1
    pavlovVars.volumeTone2 = 1
    #pavlovVars.movementAmount = 1
    #pavlovVars.movementMethod = 1
    pavlovVars.movementTime = 1
    pavlovVars.idleTime = 1
    
    skinnerVars.toneStart = 1
    skinnerVars.toneEnd = 1
    skinnerVars.movementWindowStart = 1
    skinnerVars.movementWindowEnd = 1
    skinnerVars.interTrialStart = 1
    skinnerVars.interTrialEnd = 1
    skinnerVars.probabilityToneOne = 1
    skinnerVars.frequencyTone1 = 1
    skinnerVars.frequencyTone2 = 1
    skinnerVars.volumeTone1 = 1
    skinnerVars.volumeTone2 = 1
    #skinnerVars.movementAmount = 1
    #skinnerVars.movementMethod = 1
    skinnerVars.movementTime = 1
    skinnerVars.idleTime = 1
    
    ocondVars.toneStart = 1
    ocondVars.toneEnd = 1
    ocondVars.movementWindowStart = 1
    ocondVars.movementWindowEnd = 1
    ocondVars.interTrialStart = 1
    ocondVars.interTrialEnd = 1
    ocondVars.probabilityToneOne = 1
    ocondVars.frequencyTone1 = 1
    ocondVars.frequencyTone2 = 1
    ocondVars.volumeTone1 = 1
    ocondVars.volumeTone2 = 1
    #ocondVars.movementAmount = 1
    #ocondVars.movementMethod = 1
    ocondVars.movementTime = 1
    ocondVars.idleTime = 1
    
    discrVars.toneStart = 1
    discrVars.toneEnd = 1
    discrVars.movementWindowStart = 1
    discrVars.movementWindowEnd = 1
    discrVars.interTrialStart = 1
    discrVars.interTrialEnd = 1
    discrVars.probabilityToneOne = 1
    discrVars.frequencyTone1 = 1
    discrVars.frequencyTone2 = 1
    discrVars.volumeTone1 = 1
    discrVars.volumeTone2 = 1
    #discrVars.movementAmount = 1
    #discrVars.movementMethod = 1
    discrVars.movementTime = 1
    discrVars.idleTime = 1
    
    
    def getSubjName(self):
        
        
        if (self.usingTK == 0):
            logger.debug("GTK GUI Subject List started.")
            if (self.multiProcSubjectNameQuery == 1):
                logger.debug("Using multiprocessing for Subject Name query.")
                print "Using multiprocessing for Subject Name query."
                import autoCompleteEntry_gtk
                app = autoCompleteEntry_gtk.autoCompleteDialog(self.subj_list);
                app.initAll()
                self.subj_name = app.getSubjectName()
                app.exit()
                del app
            elif (self.multiProcSubjectNameQuery == 0):
                logger.debug("Not using multiprocessing for Subject Name query.")
                print "Not using  multiprocessing for Subject Name query."
                import autoCompleteEntry_gtk
                a = autoCompleteEntry_gtk.multiproc_autoCompleteDialog(self.subj_list, None)
                self.subj_name = a.subj_name
            logger.debug("GUI Job ended.")
            logger.debug("GTK GUI Subject List ended.")
            pass
        elif (self.usingTK == 1):
            logger.debug("TK GUI Subject List started.")
            if (self.multiProcSubjectNameQuery == 1):
                logger.debug("Using multiprocessing for Subject Name query.")
                print "Using multiprocessing for Subject Name query."
                import autoCompleteEntry_tk
                app3 =  autoCompleteEntry_tk.autoCompleteEntry_tk(self.subj_list)
                app3.initAll()
                self.subj_name = app3.getSubjectName()
                app3.exit()
                del app3 #.
            elif (self.multiProcSubjectNameQuery == 0):
                logger.debug("Not using multiprocessing for Subject Name query.")
                print "Not using  multiprocessing for Subject Name query."
                import autoCompleteEntry_tk
                a = autoCompleteEntry_tk.multiproc_autoCompleteDialog(self.subj_list, None)
                self.subj_name = a.subj_name
            logger.debug("TK GUI Subject List ended.")
        #print "API subj_name %s" % self.subj_name
        logger.debug( "subject name: %s" % self.subj_name )
        return self.subj_name
    
    def __init__(self, jobl = None, toStart = False):
        logger.info( "initializing userInterfaceAPI" )
        #Variables: setting up to 0 before assigning any values.
        self.jobListOutput = jobl
        print self.jobListOutput
        print ";;"
        self.toneStart = 0
        self.toneEnd = 0
        self.movementWindowStart = 0
        self.movementWindowEnd = 0
        self.interTrialStart = 0
        self.interTrialEnd = 0
        self.probabilityToneOne = 0
        self.frequencyTone1 = 0
        self.frequencyTone2 = 0
        self.volumeTone1 = 0
        self.volumeTone2 = 0
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
        #self.jobListOutput = nuevoqueue
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
        self.currentGUI.volumeTone1 = self.volumeTone1
        self.currentGUI.volumeTone2 = self.volumeTone2
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
        #self.currentGUI.startGUI()
        
        pass
    
    def dummy_fn(self):
        print "Dummy Function"
        logger.info ( "Dummy function." )
        pass
    
    def setNameSpaceMessage(self, arg1, arg2=0):
        #print "setNameSpaceMessage"
        self.jobListOutput.put( (arg1, arg2) )
        self.jobListOutput.join()
        #self.jobList.put_nowait((arg1, arg2jobListOutput    #print "done."
        pass
    
    def commitChangesToGUI(self):
        self.currentGUI.commitInitialData()
    
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
        
        self.setNameSpaceMessage(35, self.currentGUI.volumeTone1 )
        #logger.debug ( "ns: " + ns.__str__() )
        #print "API Namespace:", ns
        
        self.setNameSpaceMessage(36, self.currentGUI.volumeTone2 )
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
    
    def overrideaction_noisefiltering(self):
        logger.debug( "Default API: Noise Filtering Camera" )
        self.setNameSpaceMessage(34)
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
        if (self.current_type!= 0 and self.current_type != self.currentGUI.current_type):
            self.current_type = self.currentGUI.current_type
            
            if (self.current_type == "pavlov"):
                #pavlov
                print "------------------------------------"
                print "setting pavlov vars to currentGUI"
                print "------------------------------------"
                obj = self.pavlovVars
                self.currentGUI.toneStart = obj.toneStart
                self.currentGUI.toneEnd = obj.toneEnd
                self.currentGUI.movementWindowStart = obj.movementWindowStart
                self.currentGUI.movementWindowEnd = obj.movementWindowEnd
                self.currentGUI.interTrialStart = obj.interTrialStart
                self.currentGUI.interTrialEnd = obj.interTrialEnd
                self.currentGUI.probabilityToneOne = obj.probabilityToneOne
                self.currentGUI.frequencyTone1 = obj.frequencyTone1
                self.currentGUI.frequencyTone2 = obj.frequencyTone2
                #self.currentGUI.movementAmount = obj.movementAmount
                #self.currentGUI.movementMethod = obj.movementMethod
                self.currentGUI.movementTime = obj.movementTime
                self.currentGUI.idleTime = obj.idleTime
                self.currentGUI.type_pavlov = 1
                self.currentGUI.type_skinner = 0
                self.currentGUI.type_ocond = 0
                self.currentGUI.type_discr = 0
                self.currentGUI.requireStillnessVar = obj.requireStillnessVar;
                print "..................-"
                #print self.requireStillnessVar
                self.currentGUI.commitInitialData()
            
            if (self.current_type == "skinner"):
                #pavlov
                print "------------------------------------"
                print "setting skinner vars to currentGUI"
                print "------------------------------------"
                obj = self.skinnerVars
                self.currentGUI.toneStart = obj.toneStart
                self.currentGUI.toneEnd = obj.toneEnd
                self.currentGUI.movementWindowStart = obj.movementWindowStart
                self.currentGUI.movementWindowEnd = obj.movementWindowEnd
                self.currentGUI.interTrialStart = obj.interTrialStart
                self.currentGUI.interTrialEnd = obj.interTrialEnd
                self.currentGUI.probabilityToneOne = obj.probabilityToneOne
                self.currentGUI.frequencyTone1 = obj.frequencyTone1
                self.currentGUI.frequencyTone2 = obj.frequencyTone2
                #self.currentGUI.movementAmount = obj.movementAmount
                #self.currentGUI.movementMethod = obj.movementMethod
                self.currentGUI.movementTime = obj.movementTime
                self.currentGUI.idleTime = obj.idleTime
                self.currentGUI.type_pavlov = 0
                self.currentGUI.type_skinner = 1
                self.currentGUI.type_ocond = 0
                self.currentGUI.type_discr = 0
                self.currentGUI.requireStillnessVar = obj.requireStillnessVar;
                print "..................-"
                #print self.requireStillnessVar
                self.currentGUI.commitInitialData()
            
            
            if (self.current_type == "oc"):
                #pavlov
                print "------------------------------------"
                print "setting oc vars to currentGUI"
                print "------------------------------------"
                obj = self.ocondVars
                self.currentGUI.toneStart = obj.toneStart
                self.currentGUI.toneEnd = obj.toneEnd
                self.currentGUI.movementWindowStart = obj.movementWindowStart
                self.currentGUI.movementWindowEnd = obj.movementWindowEnd
                self.currentGUI.interTrialStart = obj.interTrialStart
                self.currentGUI.interTrialEnd = obj.interTrialEnd
                self.currentGUI.probabilityToneOne = obj.probabilityToneOne
                self.currentGUI.frequencyTone1 = obj.frequencyTone1
                self.currentGUI.frequencyTone2 = obj.frequencyTone2
                #self.currentGUI.movementAmount = obj.movementAmount
                #self.currentGUI.movementMethod = obj.movementMethod
                self.currentGUI.movementTime = obj.movementTime
                self.currentGUI.idleTime = obj.idleTime
                self.currentGUI.type_pavlov = 0
                self.currentGUI.type_skinner = 0
                self.currentGUI.type_ocond = 1
                self.currentGUI.type_discr = 0
                self.currentGUI.requireStillnessVar = obj.requireStillnessVar;
                print "..................-"
                #print self.requireStillnessVar
                self.currentGUI.commitInitialData()
            
            
            if (self.current_type == "discr"):
                #pavlov
                print "------------------------------------"
                print "setting discr vars to currentGUI"
                print "------------------------------------"
                obj = self.discrVars
                self.currentGUI.toneStart = obj.toneStart
                self.currentGUI.toneEnd = obj.toneEnd
                self.currentGUI.movementWindowStart = obj.movementWindowStart
                self.currentGUI.movementWindowEnd = obj.movementWindowEnd
                self.currentGUI.interTrialStart = obj.interTrialStart
                self.currentGUI.interTrialEnd = obj.interTrialEnd
                self.currentGUI.probabilityToneOne = obj.probabilityToneOne
                self.currentGUI.frequencyTone1 = obj.frequencyTone1
                self.currentGUI.frequencyTone2 = obj.frequencyTone2
                #self.currentGUI.movementAmount = obj.movementAmount
                #self.currentGUI.movementMethod = obj.movementMethod
                self.currentGUI.movementTime = obj.movementTime
                self.currentGUI.idleTime = obj.idleTime
                self.currentGUI.type_pavlov = 0
                self.currentGUI.type_skinner = 0
                self.currentGUI.type_ocond = 0
                self.currentGUI.type_discr = 1
                self.currentGUI.requireStillnessVar = obj.requireStillnessVar;
                print "..................-"
                #print self.requireStillnessVar
                self.currentGUI.commitInitialData()
            
            print "change in trial type detected."
        self.current_type = self.currentGUI.current_type
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
    
    
    def action_noisefiltering(self):
        logger.debug( "API: Recalibrate Camera" )
        try:
            self.overrideaction_noisefiltering()
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
        self.currentGUI.exit()
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
        self.currentGUI.overrideaction_noisefiltering = self.action_noisefiltering
        #self.comment = ""
        #self.thread_function(
        #thread1 = threading.Thread(target=self.thread_function, name="glade_GUI")
        #thread1.start()
        logger.debug( "message variables: "+ self.ns.__str__() )
        logger.info( str(self) +  "  Glade Interface Started" )
        print "Glade interface started."
        self.setInitialValues() #loops in this function infinitely
        #self.currentGUI.launchMainLoop()
        self.currentGUI.startGUI()
        #while True:
        #    time.sleep(1.0)
        pass
    
    
    def launch_tkinter(self):
        import userInterface_tk
        self.currentGUI = userInterface_tk.GUIGTK_Class()
        
        print "Overriding functions:"
        
        print "-,"
        self.currentGUI.initAll(False);
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
        self.currentGUI.overrideaction_noisefiltering = self.action_noisefiltering
        self.currentGUI.overrideaction_exit = self.action_exit
        logger.debug( "message variables: "+ self.ns.__str__() )
        logger.info( str(self) +  "  Tkinter Interface Started" )
        print "Tkinter Interface Started"
        self.setInitialValues()
        #self.currentGUI.initAll();
        self.currentGUI.launchMainLoop()
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
    a = userInterface_API(True);
    logger.info('End userInterfaceAPI Test')
    #a.launch_GUI() #redundant because it was instantiated API with value True
