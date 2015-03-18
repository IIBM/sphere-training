#!/usr/bin/python

import Tkinter
#from Tkinter import *
import time
import os
import logging
logger = logging.getLogger('userInterface_tk')
import track_bola_utils


class GUIGTK_Class:
    requireStillnessVar = 0;
    
    class Empty_cl():
        #Used to save our variables' previous states.
        def __init__(self):
            pass
    
    
    
    def __init__(self):
            #object created. Pending initialization..
            pass
    
    def launchMainLoop(self):
        print "launching main loop"
        self.AppFrm5.mainloop()
    
    def initAll(self, launchMainLoop = False):
            self.customVariablesInit()
            print "Initializing GUI GTK class."
            #self.thread0 = threading.Thread(target=self.startFrame0 , name="Frame0")
            #self.thread0.start()
            self.startFrame0()
            time.sleep(2.25)
            
            #self.thread1 = threading.Thread(target=self.startFrame1 , name="Frame1")
            #time.sleep(0.25)
            #self.thread1.start()
            self.startFrame1()
            
            self.startFrame3()
            print ".---------"
            time.sleep(1)
            self.startFrame5(launchMainLoop)

#             while True:
#                 #print ""
#                 if (self.allowGUIContinue == 1):
#                     self.thread1 = threading.Thread(target=self.startFrame1 , name="Frame1")
#                     time.sleep(0.25)
#                     self.thread1.start()
#                     
#                     self.thread3 = threading.Thread(target=self.startFrame3 , name="Frame3")
#                     time.sleep(0.25)
#                     self.thread3.start()
#                     
#                     self.thread5 = threading.Thread(target=self.startFrame5 , name="Frame5")
#                     time.sleep(0.25) #i can swear without this delay it won't work properly
#                     self.thread5.start()
#                     break;
            
            
            #print "GUI GTK class initialized."
            pass
    
    def customVariablesInit(self):
        self.allowGUIContinue = 0;
        
        self.previousVars = self.Empty_cl()
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
        
        self.type_pavlov = 0;
        self.type_skinner = 0;
        self.type_ocond = 0;
        self.type_discr = 0;
        
        self.current_type = ""
        
        self.comment = ""
        
        self.helpNumber = 0;
        pass
    
    
    def start_everything(self):
        self.thread0.start()
        self.thread1.start()
        self.thread3.start()
        self.thread5.start()
        while True:
            time.sleep(0.5)
    
    def commitInitialData(self):
        #some arguments have been passed as variables (with direct access)
        #The Graphic Elements should change according to current state of the vars that we received.
        #time.sleep(0.2)
        self.AppFrm1.configureData()
        self.AppFrm3.configureData()
        self.AppFrm5.configureData()
        time.sleep(0.5)
        
        #print "    Done with configuration of initial data to GUI"
        logger.info("    Done with configuration of data to GUI")
        pass
    
    def startGUI(self):
        self.App.pack() #was forgotten previously to avoid flickering of appfrm1-5
    
    def startFrame0(self):
        print "frame0 starting."
        Rootn = Tkinter.Tk()
        print "frame0 starting1."
        Rootn.withdraw() #to prevent user from touching vars before initialization
        self.App = self.userInput(Rootn)
        self.App.pack(expand='yes',fill='both')
        self.App.reference = self
        print "frame0 starting2."
        Rootn.geometry('440x240+10+10')
        Rootn.title('Main Form (TK)')
        print "frame0 starting3."
        self.allowGUIContinue = 1;
        time.sleep(0.5) #to prevent user from touching GUI before the other frames are well-displayed.
        Rootn.deiconify()
        print "frame0 starting4."
        #self.App.mainloop()
        #print "frame0 started."
        
        
        
        
        
        
        #while True:
        #    time.sleep(1.0)
        pass
    
    def startFrame1(self):
        print "Starting frame1"
        print ""
        Root2 = Tkinter.Tk()
        Root2.withdraw()
        print "frame1 starting0."
        self.AppFrm1 = self.Form1(Root2)
        
        self.AppFrm1.reference = self
        print "frame1 starting1."
        self.AppFrm1.initAll()
        print "frame1 starting2."
        #AppFrm1.gVariables = gVariables
        #AppFrm1.configureData()
        #App.pack(expand='yes', fill='both')
        #App.gVariables = gVariables
        self.AppFrm1.protocol('WM_DELETE_WINDOW', self.App.hideForm1)
        
        print "frame1 starting3."
        #gVariables.AppFrm1.geometry('640x480+10+10')
        self.AppFrm1.title('Trial Events.')
        self.AppFrm1.withdraw()
        print "frame1 starting4."
        #self.AppFrm1.mainloop()
        #print "frame1 started."
        #while True:
        #    time.sleep(1.0)
        pass
    
    def startFrame3(self):
        Root = Tkinter.Tk()
        Root.withdraw()
        
        
        self.AppFrm3 = self.Form3(Root)
        self.AppFrm3.reference = self
        self.AppFrm3.initAll()
        #AppFrm1.gVariables = gVariables
        #AppFrm1.configureData()
        #App.pack(expand='yes', fill='both')
        #App.gVariables = gVariables
        self.AppFrm3.protocol('WM_DELETE_WINDOW', self.App.hideForm3)
        
        #gVariables.AppFrm1.geometry('640x480+10+10')
        self.AppFrm3.title('Parameters.')
        self.AppFrm3.withdraw()
        #self.AppFrm3.mainloop()
        #while True:
        #    time.sleep(1.0)
        pass
    
    def startFrame5(self, launchMainLoop=False):
        Root = Tkinter.Tk()
        Root.withdraw()
        
        self.AppFrm5 = self.Form5(Root)
        self.AppFrm5.reference = self
        self.AppFrm5.initAll()
        #AppFrm1.gVariables = gVariables
        #AppFrm1.configureData()
        #App.pack(expand='yes', fill='both')
        #App.gVariables = gVariables
        self.AppFrm5.protocol('WM_DELETE_WINDOW', self.App.hideForm5)
        
        #gVariables.AppFrm1.geometry('640x480+10+10')
        self.AppFrm5.title('Comment.')
        self.AppFrm5.withdraw()
        if (launchMainLoop):
            self.AppFrm5.mainloop()
        #while True:
        #    time.sleep(1.0)
        pass
    
    def exit_all(self):
        logger.info('Exiting userInterface_tk')
        os._exit(0)
    
    
    class ToolTip:
        def __init__(self, master, text='Your text here', delay=1500, **opts):
            self.master = master
            self._opts = {'anchor':'center', 'bd':1, 'bg':'lightyellow', 'delay':delay, 'fg':'black',\
                          'follow_mouse':0, 'font':None, 'justify':'left', 'padx':4, 'pady':2,\
                          'relief':'solid', 'state':'normal', 'text':text, 'textvariable':None,\
                          'width':0, 'wraplength':150}
            self.configure(**opts)
            self._tipwindow = None
            self._id = None
            self._id1 = self.master.bind("<Enter>", self.enter, '+')
            self._id2 = self.master.bind("<Leave>", self.leave, '+')
            self._id3 = self.master.bind("<ButtonPress>", self.leave, '+')
            self._follow_mouse = 0
            if self._opts['follow_mouse']:
                self._id4 = self.master.bind("<Motion>", self.motion, '+')
                self._follow_mouse = 1
        
        def configure(self, **opts):
            for key in opts:
                if self._opts.has_key(key):
                    self._opts[key] = opts[key]
                else:
                    KeyError = 'KeyError: Unknown option: "%s"' %key
                    raise KeyError
        
        ##----these methods handle the callbacks on "<Enter>", "<Leave>" and "<Motion>"---------------##
        ##----events on the parent widget; override them if you want to change the widget's behavior--##
        
        def enter(self, event=None):
            self._schedule()
            
        def leave(self, event=None):
            self._unschedule()
            self._hide()
        
        def motion(self, event=None):
            if self._tipwindow and self._follow_mouse:
                x, y = self.coords()
                self._tipwindow.wm_geometry("+%d+%d" % (x, y))
        
        ##------the methods that do the work:---------------------------------------------------------##
        
        def _schedule(self):
            self._unschedule()
            if self._opts['state'] == 'disabled':
                return
            self._id = self.master.after(self._opts['delay'], self._show)
    
        def _unschedule(self):
            id = self._id
            self._id = None
            if id:
                self.master.after_cancel(id)
    
        def _show(self):
            if self._opts['state'] == 'disabled':
                self._unschedule()
                return
            if not self._tipwindow:
                self._tipwindow = tw = Tkinter.Toplevel(self.master)
                # hide the window until we know the geometry
                tw.withdraw()
                tw.wm_overrideredirect(1)
    
                if tw.tk.call("tk", "windowingsystem") == 'aqua':
                    tw.tk.call("::tk::unsupported::MacWindowStyle", "style", tw._w, "help", "none")
    
                self.create_contents()
                tw.update_idletasks()
                x, y = self.coords()
                tw.wm_geometry("+%d+%d" % (x, y))
                tw.deiconify()
        
        def _hide(self):
            tw = self._tipwindow
            self._tipwindow = None
            if tw:
                tw.destroy()
                    
        ##----these methods might be overridden in derived classes:----------------------------------##
        
        def coords(self):
            # The tip window must be completely outside the master widget;
            # otherwise when the mouse enters the tip window we get
            # a leave event and it disappears, and then we get an enter
            # event and it reappears, and so on forever :-(
            # or we take care that the mouse pointer is always outside the tipwindow :-)
            tw = self._tipwindow
            twx, twy = tw.winfo_reqwidth(), tw.winfo_reqheight()
            w, h = tw.winfo_screenwidth(), tw.winfo_screenheight()
            # calculate the y coordinate:
            if self._follow_mouse:
                y = tw.winfo_pointery() + 20
                # make sure the tipwindow is never outside the screen:
                if y + twy > h:
                    y = y - twy - 30
            else:
                y = self.master.winfo_rooty() + self.master.winfo_height() + 3
                if y + twy > h:
                    y = self.master.winfo_rooty() - twy - 3
            # we can use the same x coord in both cases:
            x = tw.winfo_pointerx() - twx / 2
            if x < 0:
                x = 0
            elif x + twx > w:
                x = w - twx
            return x, y
    
        def create_contents(self):
            opts = self._opts.copy()
            for opt in ('delay', 'follow_mouse', 'state'):
                del opts[opt]
            label = Tkinter.Label(self._tipwindow, **opts)
            label.pack()
    
    class userInput(Tkinter.Frame):
    #------------------------------------------------------------------------------#
    #                                                                              #
    #                                  userInput                                   #
    #                                                                              #
    #------------------------------------------------------------------------------#
        def __init__(self,Master=None,**kw):
            kw['takefocus'] = None
            #
            #Your code here
            #
            apply(Tkinter.Frame.__init__,(self,Master),kw)
            self.bind('<Destroy>',self.__on_userInput_Dstry)
            self.__Frame25 = Tkinter.Frame(self)
            self.__Frame25.pack(side='top')
            self.__Frame26 = Tkinter.Frame(self)
            self.__Frame26.pack(side='top')
            self.__Frame28 = Tkinter.Frame(self.__Frame25,width=320)
            self.__Frame28.pack(side='left')
            self.__Frame27 = Tkinter.Frame(self.__Frame25)
            self.__Frame27.pack(side='left')
            self.__btnHelp = Tkinter.Button(self.__Frame27,anchor='w',justify='right'
                ,text='Help')
            self.__btnHelp.bind('<ButtonRelease-1>' \
                ,self.__btnHelp_pressed)
            
            self.__tooltip11_Help = GUIGTK_Class.ToolTip(self.__btnHelp, text=
                                    "Help:"+"\n"+
                                     "Displays a frame with help topics.")
            self.__btnHelp.pack(side='left')
            
            self.__EspacioHelpSS = Tkinter.Canvas(self.__Frame27, width=35, height=35, highlightthickness=0,
                                          selectborderwidth=0)
            self.__EspacioHelpSS.pack(side='left')
            
            
            
            self.__btnSaveState = Tkinter.Button(self.__Frame27,anchor='w',justify='right'
                ,text='Save State')
            self.__btnSaveState.bind('<ButtonRelease-1>' \
                ,self.____btnSaveState_pressed)
            
            self.__tooltip11_SaveState = GUIGTK_Class.ToolTip(self.__btnSaveState, text=
                                    "Save State:"+"\n"+
                                     "Saves current state, including trial variables and parameters.")
            
            #find working directory, replace training with modules , to handle case where it is executed from training
            if (os.sep +"training" in os.getcwd()):
                executingPath = (os.getcwd().split(os.sep + "training") [0]) + os.sep + "modules"+os.sep 
            else:
                executingPath = os.getcwd() + os.sep;
            try:
                photoLocation = executingPath+"res"+os.sep +"savebtn.gif"
                logger.debug("Location: %s" % photoLocation)
                print "Location: %s" % photoLocation
                imgf = Tkinter.PhotoImage(file=photoLocation);
                self.photo=imgf
                self.__btnSaveState.config(image=self.photo);
            except:
                logger.warning("Couldn't set saveBtn.png image.");
            self.__btnSaveState.pack(side='left')
            
            self.__Frame2 = Tkinter.Frame(self.__Frame26)
            self.__Frame2.pack(side='left')
            self.__Frame1 = Tkinter.Frame(self.__Frame26)
            self.__Frame1.pack(side='left')
            self.__Frame5 = Tkinter.Frame(self.__Frame2)
            self.__Frame5.pack(side='top')
            self.__Frame4 = Tkinter.Frame(self.__Frame2)
            self.__Frame4.pack(side='top')
            self.__Frame8 = Tkinter.Frame(self.__Frame1)
            self.__Frame8.pack(side='top')
            self.__Frame7 = Tkinter.Frame(self.__Frame1,height=30)
            self.__Frame7.pack(side='top')
            self.__Frame13 = Tkinter.Frame(self.__Frame1)
            self.__Frame13.pack(side='top')
            self.__btnFrmTrialEvents = Tkinter.Button(self.__Frame13
                ,text='Edit Trial Events')
            self.__btnFrmTrialEvents.pack(side='top')
            self.__btnFrmTrialEvents.bind('<ButtonRelease-1>' \
                ,self.__on_btnFrmTrialEvents_ButRel_1)
            
            self.__tooltip10_TrialEvents = GUIGTK_Class.ToolTip(self.__btnFrmTrialEvents, text=
                                    "Edit Trial Events:"+"\n"+
                                     "Displays a frame to edit the training trial events.")
            
            self.__Frame9 = Tkinter.Frame(self.__Frame1,height=15,width=15)
            self.__Frame9.pack(side='top')
            self.__Frame16 = Tkinter.Frame(self.__Frame1)
            self.__Frame16.pack(side='top')
            self.__btnFrmEditParameters = Tkinter.Button(self.__Frame16
                ,text='Edit Parameters')
            self.__btnFrmEditParameters.pack(side='top')
            self.__btnFrmEditParameters.bind('<ButtonRelease-1>' \
                ,self.__on_btnFrmEditParameters_ButRel_1)
            
            self.__tooltip9_Parameters = GUIGTK_Class.ToolTip(self.__btnFrmEditParameters, text=
                                    "Edit Parameters:"+"\n"+
                                     "Displays a frame to edit parameters of the training modules.")
            
            
            self.__Frame15 = Tkinter.Frame(self.__Frame1,height=5)
            self.__Frame15.pack(side='top')
            self.__Frame14 = Tkinter.Frame(self.__Frame1)
            self.__Frame14.pack(side='top')
            #self.__Text1KeyInput = Text(self.__Frame14,background=self.__btnFrmEditParameters['bg'],height=5
            #    ,relief='flat',state='disabled',width=30, borderwidth=0)
            self.__Text1KeyInput = Tkinter.Canvas(self.__Frame14, width=20, height=20, highlightthickness=0,
                                          selectborderwidth=0)
            self.__Text1KeyInput.pack(side='top')
            self.__Text1KeyInput.bind('<KeyPress>',self.__on_Text1KeyInput_Key)
            self.__Text1KeyInput.bind('<KeyPress-C>',self.__on_Text1KeyInput_Key_C)
            self.__Text1KeyInput.bind('<KeyPress-D>',self.__on_Text1KeyInput_Key_D)
            self.__Text1KeyInput.bind('<KeyPress-K>',self.__on_Text1KeyInput_Key_K)
            self.__Text1KeyInput.bind('<KeyPress-O>',self.__on_Text1KeyInput_Key_O)
            self.__Text1KeyInput.bind('<KeyPress-P>',self.__on_Text1KeyInput_Key_P)
            self.__Text1KeyInput.bind('<KeyPress-R>',self.__on_Text1KeyInput_Key_R)
            self.__Text1KeyInput.bind('<KeyPress-c>',self.__on_Text1KeyInput_Key_c)
            self.__Text1KeyInput.bind('<KeyPress-d>',self.__on_Text1KeyInput_Key_d)
            self.__Text1KeyInput.bind('<KeyPress-k>',self.__on_Text1KeyInput_Key_k)
            self.__Text1KeyInput.bind('<KeyPress-p>',self.__on_Text1KeyInput_Key_p)
            self.__Text1KeyInput.bind('<KeyPress-r>',self.__on_Text1KeyInput_Key_r)
            self.__Text1KeyInput.bind('<KeyRelease-o>' \
                ,self.__on_Text1KeyInput_KeyRel_o)
            self.__Frame3 = Tkinter.Frame(self.__Frame5)
            self.__Frame3.pack(side='left')
            self.__Frame6 = Tkinter.Frame(self.__Frame5,takefocus=1,width=80)
            self.__Frame6.pack(side='left')
            self.__Frame23 = Tkinter.Frame(self.__Frame8)
            self.__Frame23.pack(side='left')
            self.__btnComment = Tkinter.Button(self.__Frame23
                ,text='Comment about this training')
            self.__btnComment.pack(side='top')
            self.__btnComment.bind('<ButtonRelease-1>' \
                ,self.__on_btnComment_ButRel_1)
            
            self.__tooltip8_Comment = GUIGTK_Class.ToolTip(self.__btnComment, text=
                                    "Comment about this training:"+"\n"+
                                     "Displays an input box for writing a comment about this training session.")
            
            self.__Frame24 = Tkinter.Frame(self.__Frame8,width=10)
            self.__Frame24.pack(side='left')
            self.__Frame10 = Tkinter.Frame(self.__Frame3)
            self.__Frame10.pack(side='top')
            self.__btnDrop = Tkinter.Button(self.__Frame10,text='Drop')
            self.__btnDrop.pack(side='top')
            self.__btnDrop.bind('<ButtonRelease-1>',self.__on_btnDrop_ButRel_1)
            
            self.__tooltip1_Drop = GUIGTK_Class.ToolTip(self.__btnDrop, text=
                                    'Drop: '+ "\n" + '(shortcut: D) Gives a drop of water.')
            
            
            self.__Frame20 = Tkinter.Frame(self.__Frame3)
            self.__Frame20.pack(side='top')
            self.__btnReward = Tkinter.Button(self.__Frame20,text='Reward')
            self.__btnReward.pack(side='top')
            self.__btnReward.bind('<ButtonRelease-1>',self.__on_btnReward_ButRel_1)
            
            self.__tooltip2_Reward = GUIGTK_Class.ToolTip(self.__btnReward, text=
                                    'Reward '+ "\n" + '(shortcut: R) Gives a drop of water and counts the trial as successful.')
            
            self.__Frame12 = Tkinter.Frame(self.__Frame3)
            self.__Frame12.pack(side='top')
            self.__btnOpen = Tkinter.Button(self.__Frame12,text='Open Valve')
            self.__btnOpen.pack(side='top')
            self.__btnOpen.bind('<ButtonRelease-1>',self.__on_btnOpen_ButRel_1)
            
            self.__tooltip3_Open = GUIGTK_Class.ToolTip(self.__btnOpen, text=
                                    'Open: '+ "\n" + '(shortcut: O) Opens the valve.')
            
            self.__Frame17 = Tkinter.Frame(self.__Frame3)
            self.__Frame17.pack(side='top')
            self.__btnClose = Tkinter.Button(self.__Frame17,text='Close Valve')
            self.__btnClose.pack(side='top')
            self.__btnClose.bind('<ButtonRelease-1>',self.__on_btnClose_ButRel_1)
            
            self.__tooltip4_Close = GUIGTK_Class.ToolTip(self.__btnClose, text=
                                    'Close: '+ "\n" + '(shortcut: C) Closes the valve.')
            
            self.__Frame11 = Tkinter.Frame(self.__Frame3)
            self.__Frame11.pack(side='top')
            self.__btnStart = Tkinter.Button(self.__Frame11,text='Start / Stop Training')
            self.__btnStart.pack(side='top')
            self.__btnStart.bind('<ButtonRelease-1>',self.__on_btnStart_ButRel_1)
            
            self.__tooltip5_Start = GUIGTK_Class.ToolTip(self.__btnStart, text=
                                    "Start / Stop Training:"+
                                    "\n" +"(shortcut: K) Starts the training if it hasn't started before."+"\n"
                                    +"Else stops the training.")
            
            self.__Frame21 = Tkinter.Frame(self.__Frame3)
            self.__Frame21.pack(side='top')
            self.__btnPause = Tkinter.Button(self.__Frame21,text='Pause / Resume Training')
            self.__btnPause.pack(side='top')
            self.__btnPause.bind('<ButtonRelease-1>',self.__on_btnPause_ButRel_1)
            
            self.__tooltip6_Pause = GUIGTK_Class.ToolTip(self.__btnPause, text=
                                    "Pause/Resume Training:"+"\n"+
                                     "(shortcut: P) Pauses the training if it is currently running."+"\n"
                                    +"Else resumes the paused training.")
            
            self.__Frame19 = Tkinter.Frame(self.__Frame3)
            self.__Frame19.pack(side='top')
    #         self.__btnResume = Button(self.__Frame19,text='Resume Training')
    #         self.__btnResume.pack(side='top')
    #         self.__btnResume.bind('<ButtonRelease-1>',self.__on_btnResume_ButRel_1)
            self.__Frame22 = Tkinter.Frame(self.__Frame3)
            self.__Frame22.pack(side='top')
    #         self.__btnStop = Button(self.__Frame22,text='Stop Training')
    #         self.__btnStop.pack(side='top')
    #         self.__btnStop.bind('<ButtonRelease-1>',self.__on_btnStop_ButRel_1)
            self.__Frame18 = Tkinter.Frame(self.__Frame3)
            self.__Frame18.pack(side='top')
            self.__btnExit = Tkinter.Button(self.__Frame18,text='Exit')
            self.__btnExit.pack(side='top')
            self.__btnExit.bind('<ButtonRelease-1>',self.__on_btnExit_ButRel_1)
            
            self.__tooltip7_Exit = GUIGTK_Class.ToolTip(self.__btnExit, text=
                                    "Exit Training:"+"\n"+
                                     "Exits the training and all its modules.")
            
            
            self.__alive = 0
            self.__Text1KeyInput.focus_set()
            #print "Main User Input Form loaded"
            logger.info("Main User Input Form loaded")
            pass
        
        
        def hideForm1(self, toHide = True):
            logger.debug("Hide Form 1.")
            #a = gVariables.AppFrm1.__Entry3MvmntWindowStart.get() 
            if (toHide == True):
                self.reference.AppFrm1.withdraw()
                return;
            #GUIGTK_Class.AppFrm1.get_changes()
            
            logger.debug("Reading variables ");
            a = self.reference.AppFrm1.var1_TStart #tone duration
            b = self.reference.AppFrm1.var2_TEnd
            c = self.reference.AppFrm1.var3_MWS
            d = self.reference.AppFrm1.var4_MWE
            e = self.reference.AppFrm1.var5_ITStart #changed to intertrial random1 time
            f = self.reference.AppFrm1.var6_ITEnd #changed to intertrial random2 time
            g = self.reference.AppFrm1.var7_Probab1
            #print a
            #print b
            #print c
            #print d
            #print e
            #print f
            #print g
            self.reference.toneStart = a
            self.reference.toneEnd = b
            self.reference.movementWindowStart = c
            self.reference.movementWindowEnd = d
            self.reference.interTrialStart = e
            self.reference.interTrialEnd = f
            self.reference.probabilityToneOne = g
        
        def hideForm3(self, toHide = True):
            logger.debug("Hide Form 3.")
            
            if (toHide == True):
                self.reference.AppFrm3.withdraw()
                return;
            
            #GUIGTK_Class.AppFrm3.get_changes()
            
            logger.debug("Reading variables ")
            a = self.reference.AppFrm3.var1_T1
            b = self.reference.AppFrm3.var2_T2
            c = self.reference.AppFrm3.var3_MA
            d = self.reference.AppFrm3.var4_MT
            e = self.reference.AppFrm3.var5_IT
            f = self.reference.AppFrm3.var6_ShowTracking
            g = self.reference.AppFrm3.var7_ShowFeedback
            h = self.reference.AppFrm3.var8_num_selected
#             print a
#             print b
#             print c
#             print d
#             print e
#             print f
#             print g
#             print h
            self.reference.frequencyTone1 = a
            self.reference.frequencyTone2 = b
            self.reference.movementAmount = c
            self.reference.movementMethod = h
            self.reference.movementTime = d
            self.reference.idleTime = e
            
            if (toHide == True):
                self.reference.AppFrm3.withdraw()
        
        def hideForm5(self, toHide = True):
            logger.debug("Hide Form 5.")
            self.reference.comment = self.reference.AppFrm5.commentStr
            print self.reference.comment
            if (toHide == True):
                self.reference.AppFrm5.withdraw()
                return;
            pass
        
        def showFrame1(self):
            logger.info( "Trial Events frame shown." )
            self.reference.AppFrm1.saveTrialEventsPreviousState()
            self.reference.AppFrm1.deiconify()
            #print "Showing Frame 1: Trial Events"
            pass
        
        def showFrame3(self):
            logger.info( "Parameters frame shown." )
            self.reference.AppFrm3.saveParametersPreviousState()
            self.reference.AppFrm3.deiconify()
            #print "Showing Frame 3: Parameters"
        
        def showFrame5(self):
            self.reference.AppFrm5.deiconify()
            #print "Showing Frame 5"
        
    
        def __on_Text1KeyInput_Key(self,Event=None):
            #print "Key Pressed."
            pass
    
        def __on_Text1KeyInput_KeyRel_o(self,Event=None):
            print "Pressed o : ","Open Valve"
            self.reference.overrideaction_open()
            pass
    
        def __on_Text1KeyInput_Key_C(self,Event=None):
            print "Pressed C : ", "Close Valve"
            self.reference.overrideaction_close()
            pass
    
        def __on_Text1KeyInput_Key_D(self,Event=None):
            print "Pressed D : ", "Drop"
            self.reference.overrideaction_drop()
            pass
    
        def __on_Text1KeyInput_Key_K(self,Event=None):
            print "Pressed K : ","Start / Stop Training"
            self.reference.overrideaction_startTraining()
            pass
    
        def __on_Text1KeyInput_Key_O(self,Event=None):
            print "Pressed O : ","Open Valve"
            self.reference.overrideaction_open()
            pass
    
        def __on_Text1KeyInput_Key_P(self,Event=None):
            print "Pressed P : ", "Pause / Resume Training"
            self.reference.overrideaction_pauseTraining()
            pass
    
        def __on_Text1KeyInput_Key_R(self,Event=None):
            print "Pressed R : ","Reward"
            self.reference.overrideaction_reward()
            pass
    
        def __on_Text1KeyInput_Key_c(self,Event=None):
            print "Pressed c : ", "Close Valve"
            self.reference.overrideaction_close()
            pass
    
        def __on_Text1KeyInput_Key_d(self,Event=None):
            print "Pressed d : ", "Drop"
            self.reference.overrideaction_drop()
            pass
    
        def __on_Text1KeyInput_Key_k(self,Event=None):
            print "Pressed k : ","Start / Stop Training"
            self.reference.overrideaction_startTraining()
            pass
    
        def __on_Text1KeyInput_Key_p(self,Event=None):
            print "Pressed p : ", "Pause / Resume Training"
            self.reference.overrideaction_pauseTraining()
            pass
    
        def __on_Text1KeyInput_Key_r(self,Event=None):
            print "Pressed r : ","Reward"
            self.reference.overrideaction_reward()
            pass
    
        def __on_btnClose_ButRel_1(self,Event=None):
            #pressed Close
            print "Close Valve"
            self.reference.overrideaction_close()
            pass
        
        def __btnHelp_pressed(self, Event = None):
            print "Help button."
            if (self.reference.helpNumber != 0):
                return;
            import Tkinter as tk
            rootNW=tk.Tk()
            rootNW.wm_title("Help.")
            self.helpfrm = self.reference.Form_help(rootNW)
            #print self.reference
            self.helpfrm.reference = self.reference
            self.reference.helpNumber = 1;
            #print "ref"
            #print self.helpfrm.reference 
            self.helpfrm.pack(side="top", fill="both", expand=True)
            #rootNW.mainloop()
            pass
        
        def ____btnSaveState_pressed(self, Event = None):
            #habrIa que enviar un mensaje a training para que se salven los datos desde allI
            #print "Save State"
            self.reference.overrideaction_savestate();
            pass
    
        def __on_btnComment_ButRel_1(self,Event=None):
            self.showFrame5()
    
        def __on_btnDrop_ButRel_1(self,Event=None):
            #pressed Drop
            print "Drop"
            #self.gVariables.fn_giveDrop()
            self.reference.overrideaction_drop()
            pass
    
        def __on_btnExit_ButRel_1(self,Event=None):
            #Exiting program.
            #Frame.destroy(Frame)
            self.exitingUserInterface()
            pass
    
        def __on_btnFrmEditParameters_ButRel_1(self,Event=None):
            #print "Parameters
            self.showFrame3()
    
        def __on_btnFrmTrialEvents_ButRel_1(self,Event=None):
            self.showFrame1()
            pass
    
        def __on_btnOpen_ButRel_1(self,Event=None):
            #pressed open
            print "Open Valve"
            self.reference.overrideaction_open()
            pass
    
        def __on_btnPause_ButRel_1(self,Event=None):
            #pressed Pause
            print "Pause / Resume Training"
            self.reference.overrideaction_pauseTraining()
            pass
    
        def __on_btnReward_ButRel_1(self,Event=None):
            #pressed Reward
            print "Reward"
            self.reference.overrideaction_reward()
            pass
    
        def __on_btnStart_ButRel_1(self,Event=None):
            #pressed Start
            print "Start / Stop Training"
            self.reference.overrideaction_startTraining()
            pass
    
    
        def __on_userInput_Dstry(self,Event=None):
            if ( self.__alive == 0):
                self.reference.App.exitingUserInterface()
            pass
        
        def exitingUserInterface(self):
            print "Exiting userInterface_tk Program"
            try:
                    self.reference.overrideaction_exit()
            except:
                    logger.info( "Exit: No override for exit." )
            self.reference.exit_all()
    
    
    
    
    class Form5(Tkinter.Toplevel):
        #comment.
        #------------------------------------------------------------------------------#
        #                                                                              #
        #                                    Form5                                     #
        #                                                                              #
        #------------------------------------------------------------------------------#
        commentStr = ""
        
        def __init__(self,Master=None,**kw):
            kw['class_'] = 'Frame'
            #
            #Your code here
            #
            apply(Tkinter.Toplevel.__init__,(self,Master),kw)
            
        
        
        def initAll(self):
            self.bind('<Destroy>',self.__on_Form5_Dstry)
            self.__lblComment = Tkinter.Label(self,text='Comment about this training:')
            self.__lblComment.pack(side='top')
            
            
            self.__tooltipTE2_Com = GUIGTK_Class.ToolTip(self.__lblComment, text=
                                    "Comment about this training:"+"\n"+
                                     "Sets a comment line (max: 100 chars) about this training session.")
            
            
            self.__EntryComment = Tkinter.Entry(self)
            self.__EntryComment.pack(side='top')
            self.__EntryComment.bind('<KeyRelease>',self.__on_EntryComment_KeyRel)
            
            self.__Frame62 = Tkinter.Frame(self,height=30,width=30)
            self.__Frame62.pack(side='top')
            self.__ApplyBtn = Tkinter.Button(self.__Frame62,text='Apply')
            self.__ApplyBtn.pack(side='top')
            self.__ApplyBtn.bind('<ButtonRelease-1>',self.__on_ApplyBtn_ButRel_1)
            
            self.__tooltipTE1_Apply = GUIGTK_Class.ToolTip(self.__ApplyBtn, text=
                                    "Apply:"+"\n"+
                                     "Applies the Comment and closes this window.")
            #
            #Your code here
            self.__alreadyGone = 0
            self.__CommentString = ""
            self.get_changes()
            #print "Form5: Comment Frame loaded"
            logger.info("Form5: Comment Frame loaded")
        
        def __on_ApplyBtn_ButRel_1(self,Event=None):
            self.get_changes()
            self.reference.App.hideForm5(True)
            self.reference.overrideaction_applyC()
            pass
    
        def __on_EntryComment_KeyRel(self,Event=None):
            self.commentStr = self.__EntryComment.get()
            #print self.__CommentString
            pass
        
        def configureData(self):
            #print "configuring initial data for Form5."
            logging.info("configuring initial data for Form5.")
            self.__EntryComment.delete(0,30)
            self.__EntryComment.insert(0,self.reference.comment)
            pass
        
        def get_changes(self):
            try:
                self.commentStr = unicode(self.__EntryComment.get(), "utf-8")
            except:
                self.commentStr = self.__EntryComment.get()
        
        def __on_Form5_Dstry(self,Event=None):
            pass
    
    
    
    class Form3(Tkinter.Toplevel):
        #parameters
        #------------------------------------------------------------------------------#
        #                                                                              #
        #                                    Form3                                     #
        #                                                                              #
        #------------------------------------------------------------------------------#
        def __init__(self,Master=None,**kw):
            kw['class_'] = 'Frame'
            #
            #Your code here
            #FORM: Parameters
            apply(Tkinter.Toplevel.__init__,(self,Master),kw)
        
        def initAll(self):
            self.bind('<Destroy>',self.__on_Form3_Dstry)
            self.__Frame6 = Tkinter.Frame(self)
            self.__Frame6.pack(side='left')
            self.__Frame5 = Tkinter.Frame(self)
            self.__Frame5.pack(side='left')
            self.__Frame69 = Tkinter.Frame(self.__Frame6,width=10)
            self.__Frame69.pack(side='top')
            self.__Frame68 = Tkinter.Frame(self.__Frame6,width=10)
            self.__Frame68.pack(side='top')
            self.__Frame70 = Tkinter.Frame(self.__Frame5)
            self.__Frame70.pack(side='top')
            self.__Frame2 = Tkinter.Frame(self.__Frame5,height=5,width=15)
            self.__Frame2.pack(side='top')
            self.__Frame1 = Tkinter.Frame(self.__Frame5)
            self.__Frame1.pack(side='top')
            self.__Frame14 = Tkinter.Frame(self.__Frame5,height=30,width=30)
            self.__Frame14.pack(side='top')
            self.__Frame42 = Tkinter.Frame(self.__Frame5)
            self.__Frame42.pack(side='top')
            self.__Frame25 = Tkinter.Frame(self.__Frame5,height=30,width=30)
            self.__Frame25.pack(side='top')
            self.__Frame43 = Tkinter.Frame(self.__Frame5)
            self.__Frame43.pack(side='top')
            self.__Frame62 = Tkinter.Frame(self.__Frame5,height=30,width=30)
            self.__Frame62.pack(side='top')
            self.__ApplyBtn = Tkinter.Button(self.__Frame62,text='Apply')
            self.__ApplyBtn.pack(side='top')
            self.__ApplyBtn.bind('<ButtonRelease-1>',self.__on_ApplyBtn_ButRel_1)
            
            
            self.__tooltipTE1_Apply = GUIGTK_Class.ToolTip(self.__ApplyBtn, text=
                                    "Apply:"+"\n"+
                                     "Applies and saves all changes made to the Parameters.")
            
            
            self.__CloseBtn = Tkinter.Button(self.__Frame62,text='Close')
            self.__CloseBtn.pack(side='top')
            self.__CloseBtn.bind('<ButtonRelease-1>',self.__on_CloseBtn_ButRel_1)
            
            
            self.__tooltipTE2_Close = GUIGTK_Class.ToolTip(self.__CloseBtn, text=
                                    "Close:"+"\n"+
                                     "Closes this window without saving changes.")
            
            
            self.__Frame4 = Tkinter.Frame(self.__Frame70,height=30)
            self.__Frame4.pack(side='left')
            self.__Label1 = Tkinter.Label(self.__Frame4,text='Parameters')
            self.__Label1.pack(side='top')
            self.__Frame3 = Tkinter.Frame(self.__Frame70,height=30,width=250)
            self.__Frame3.pack(side='left')
            self.__Frame7 = Tkinter.Frame(self.__Frame1,width=20)
            self.__Frame7.pack(side='left')
            self.__Frame8 = Tkinter.Frame(self.__Frame1)
            self.__Frame8.pack(side='left')
            self.__Frame27 = Tkinter.Frame(self.__Frame42,width=20)
            self.__Frame27.pack(side='left')
            self.__Frame26 = Tkinter.Frame(self.__Frame42)
            self.__Frame26.pack(side='left')
            self.__Frame45 = Tkinter.Frame(self.__Frame43)
            self.__Frame45.pack(side='left')
            self.__Frame44 = Tkinter.Frame(self.__Frame43)
            self.__Frame44.pack(side='left')
            self.__Frame9 = Tkinter.Frame(self.__Frame8)
            self.__Frame9.pack(side='top')
            self.__Label2 = Tkinter.Label(self.__Frame9,text='Audio:')
            self.__Label2.pack(side='top')
            self.__Frame16 = Tkinter.Frame(self.__Frame8)
            self.__Frame16.pack(side='top')
            self.__Frame15 = Tkinter.Frame(self.__Frame8)
            self.__Frame15.pack(side='top')
            self.__Frame10 = Tkinter.Frame(self.__Frame8)
            self.__Frame10.pack(side='top')
            self.__Frame22 = Tkinter.Frame(self.__Frame8)
            self.__Frame22.pack(side='top')
            self.__Frame71 = Tkinter.Frame(self.__Frame27)
            self.__Frame71.pack(side='top')
            self.__Frame72 = Tkinter.Frame(self.__Frame27)
            self.__Frame72.pack(side='top')
            self.__Frame29 = Tkinter.Frame(self.__Frame26)
            self.__Frame29.pack(side='top')
            self.__Label7 = Tkinter.Label(self.__Frame29,text='Video:')
            self.__Label7.pack(side='top')
            self.__Frame28 = Tkinter.Frame(self.__Frame26)
            self.__Frame28.pack(side='top')
            self.__Frame35 = Tkinter.Frame(self.__Frame26)
            self.__Frame35.pack(side='top')
            self.__Frame46 = Tkinter.Frame(self.__Frame44)
            self.__Frame46.pack(side='top')
            self.__Label10 = Tkinter.Label(self.__Frame46,text='Trial:')
            self.__Label10.pack(side='top')
            self.__Frame47 = Tkinter.Frame(self.__Frame44)
            self.__Frame47.pack(side='top')
            self.__Frame17 = Tkinter.Frame(self.__Frame16)
            self.__Frame17.pack(side='left')
            self.__Label3 = Tkinter.Label(self.__Frame17,text='Tone1:')
            self.__Label3.pack(side='top')
            self.__Frame18 = Tkinter.Frame(self.__Frame16,width=100)
            self.__Frame18.pack(side='left')
            self.__Frame11 = Tkinter.Frame(self.__Frame15)
            self.__Frame11.pack(side='left')
            self.__Entry1Tone1 = Tkinter.Entry(self.__Frame11,width=8)
            self.__Entry1Tone1.pack(side='top')
            
            
            self.__tooltipTE3_T1 = GUIGTK_Class.ToolTip(self.__Label3, text=
                                    "Tone 1:"+"\n"+
                                     "Sets the frequency of the Tone 1.")
            
            
            self.__Frame13 = Tkinter.Frame(self.__Frame15)
            self.__Frame13.pack(side='left')
            self.__Label4 = Tkinter.Label(self.__Frame13,text='Hz')
            self.__Label4.pack(side='top')
            self.__Frame12 = Tkinter.Frame(self.__Frame15)
            self.__Frame12.pack(side='left')
            self.__Button1TestT1 = Tkinter.Button(self.__Frame12,text='Test')
            self.__Button1TestT1.pack(side='top')
            self.__Button1TestT1.bind('<ButtonRelease-1>' \
                ,self.__on_Button1TestT1_ButRel_1)
            
            
            self.__tooltipTE3_1_T1 = GUIGTK_Class.ToolTip(self.__Button1TestT1, text=
                                    "Test Tone 1:"+"\n"+
                                     "Saves frequency changes and plays Tone 1.")
            
            
            self.__Frame23 = Tkinter.Frame(self.__Frame10)
            self.__Frame23.pack(side='left')
            self.__Label6 = Tkinter.Label(self.__Frame23,text='Tone2:')
            self.__Label6.pack(side='top')
            self.__Frame24 = Tkinter.Frame(self.__Frame10,width=100)
            self.__Frame24.pack(side='left')
            self.__Frame19 = Tkinter.Frame(self.__Frame22)
            self.__Frame19.pack(side='left')
            self.__Entry2Tone2 = Tkinter.Entry(self.__Frame19,width=8)
            self.__Entry2Tone2.pack(side='top')
            
            
            self.__tooltipTE4_T2 = GUIGTK_Class.ToolTip(self.__Label6, text=
                                    "Tone 2:"+"\n"+
                                     "Sets the frequency of the Tone 2.")
            
            
            self.__Frame20 = Tkinter.Frame(self.__Frame22)
            self.__Frame20.pack(side='left')
            self.__Label5 = Tkinter.Label(self.__Frame20,text='Hz')
            self.__Label5.pack(side='top')
            self.__Frame21 = Tkinter.Frame(self.__Frame22)
            self.__Frame21.pack(side='left')
            self.__Button2TestT2 = Tkinter.Button(self.__Frame21,text='Test')
            self.__Button2TestT2.pack(side='top')
            self.__Button2TestT2.bind('<ButtonRelease-1>' \
                ,self.__on_Button2TestT2_ButRel_1)
            
            
            self.__tooltipTE4_2_T2 = GUIGTK_Class.ToolTip(self.__Button2TestT2, text=
                                    "Test Tone 2:"+"\n"+
                                     "Saves frequency changes and plays Tone 2.")
            
            
            self.__Frame32 = Tkinter.Frame(self.__Frame28)
            self.__Frame32.pack(side='left')
            self.__Frame31 = Tkinter.Frame(self.__Frame28,width=100)
            self.__Frame31.pack(side='left')
            self.__Frame48 = Tkinter.Frame(self.__Frame47)
            self.__Frame48.pack(side='left')
            self.__Frame49 = Tkinter.Frame(self.__Frame47,width=50)
            self.__Frame49.pack(side='left')
            self.__Frame33 = Tkinter.Frame(self.__Frame32)
            self.__Frame33.pack(side='top')
            self.__Frame30 = Tkinter.Frame(self.__Frame32)
            self.__Frame30.pack(side='top')
            self.__Frame36 = Tkinter.Frame(self.__Frame32)
            self.__Frame36.pack(side='top')
            self.__Frame34 = Tkinter.Frame(self.__Frame32)
            self.__Frame34.pack(side='top')
            self.__Frame52 = Tkinter.Frame(self.__Frame48)
            self.__Frame52.pack(side='top')
            self.__Frame51 = Tkinter.Frame(self.__Frame48)
            self.__Frame51.pack(side='top')
            self.__Frame50 = Tkinter.Frame(self.__Frame48)
            self.__Frame50.pack(side='top')
            self.__Frame67 = Tkinter.Frame(self.__Frame33)
            self.__Frame67.pack(side='left')
            self.__Button3SHTracking = Tkinter.Button(self.__Frame67
                ,text='Show / Hide Tracking')
            self.__Button3SHTracking.pack(side='top')
            self.__Button3SHTracking.bind('<ButtonRelease-1>' \
                ,self.__on_Button3SHTracking_ButRel_1)
            
            
            self.__tooltipTE5_SHT = GUIGTK_Class.ToolTip(self.__Button3SHTracking, text=
                                    "Show / Hide Tracking:"+"\n"+
                                     "Shows / hides computer-generated tracking lines and circles on the display.")
            
            
            self.__Frame66 = Tkinter.Frame(self.__Frame33,width=39)
            self.__Frame66.pack(side='left')
            self.__Frame65 = Tkinter.Frame(self.__Frame30)
            self.__Frame65.pack(side='left')
            self.__Button4SHFeedback = Tkinter.Button(self.__Frame65
                ,text='Show / Hide Feedback')
            self.__Button4SHFeedback.pack(side='top')
            self.__Button4SHFeedback.bind('<ButtonRelease-1>' \
                ,self.__on_Button4SHFeedback_ButRel_1)
            
            
            self.__tooltipTE6_SHF = GUIGTK_Class.ToolTip(self.__Button4SHFeedback, text=
                                    "Show / Hide Feedback:"+"\n"+
                                     "Shows / hides the feedback window (the video or camera input)."
                                     +"\n"+"Note that hiding the feedback will not affect the movement detection modules."
                                     )
            
            
            self.__Button4_5recalibrate = Tkinter.Button(self.__Frame65
                ,text='Recalibrate Camera')
            self.__Button4_5recalibrate.pack(side='top')
            self.__Button4_5recalibrate.bind('<ButtonRelease-1>' \
                ,self.__on_Button4_5recalibrate_ButRel_1)
            #
            
            
            self.__tooltipTE6_REC = GUIGTK_Class.ToolTip(self.__Button4_5recalibrate, text=
                                    "Recalibrate Camera:"+"\n"+
                                     "Generates a new calibration file for the movement detection,"+
                                     " taking as sample the current video output.")
            
            
            self.__Button5_5NoiseFiltering = Tkinter.Button(self.__Frame65
                ,text='Noise Filtering')
            self.__Button5_5NoiseFiltering.pack(side='top')
            self.__Button5_5NoiseFiltering.bind('<ButtonRelease-1>' \
                ,self.__on_Button5_5NoiseF_ButRel_1)
            #
            
            
            self.__tooltipTE7_NOISEF = GUIGTK_Class.ToolTip(self.__Button5_5NoiseFiltering, text=
                                    "Noise Filtering:"+"\n"+
                                     "If Noise Filtering is enabled, the minimum allowed radius will be the smallest possible,"+
                                     "therefore allowing more precise movement detection.")
            
            
            
            self.__Frame64 = Tkinter.Frame(self.__Frame30,width=39)
            self.__Frame64.pack(side='left')
            self.__Frame38 = Tkinter.Frame(self.__Frame36)
            self.__Frame38.pack(side='left')
            self.__Label8 = Tkinter.Label(self.__Frame38,text='Movement Amount:')
            self.__Label8.pack(side='top')
            
            
            self.__tooltipTE7_MA = GUIGTK_Class.ToolTip(self.__Label8, text=
                                    "Movement Amount:"+"\n"+
                                     "Sets the movement threshold to consider a given frame as 'moving'."+
                                     "\n"+"(see sphereVideoDetection docs)")
            
            
            self.__Frame37 = Tkinter.Frame(self.__Frame36)
            self.__Frame37.pack(side='left')
            self.__Entry3MvntAm = Tkinter.Entry(self.__Frame37,width=6)
            self.__Entry3MvntAm.pack(side='top')
            self.__Frame63 = Tkinter.Frame(self.__Frame36,width=39)
            self.__Frame63.pack(side='left')
            self.__Frame39 = Tkinter.Frame(self.__Frame34)
            self.__Frame39.pack(side='left')
            self.__Label9 = Tkinter.Label(self.__Frame39,text='Method Used:')
            self.__Label9.pack(side='top')
            
            
            self.__tooltipTE8_MU = GUIGTK_Class.ToolTip(self.__Label9, text=
                                    "Method Used:"+"\n"+
                                     "Establishes the method to use for the movement detection."+
                                     "\n"+"(see sphereVideoDetection docs)"+"\n"+
                                     "Valid current methods are:"+
                                     "\n"+"0 : Accumulate Time"+"\n"+
                                     "\n"+"1 : Movement Vector"+"\n"+
                                     "\n"+"2 : Movement Vector - Binary (default)"+"\n")
            
            
            self.__Frame41 = Tkinter.Frame(self.__Frame34)
            self.__Frame41.pack(side='left')
            #self.__Listbox1 = Listbox(self.__Frame41,height=1,width=19)
            pass
            #self.__Listbox1.pack(side='top')
            #
            self.__EntryMethodUsed = Tkinter.Entry(self.__Frame41,width=6)
            self.__EntryMethodUsed.pack(side='top')
            #
            self.__Frame40 = Tkinter.Frame(self.__Frame34)
            self.__Frame40.pack(side='left')
            pass
            #self.__Button5 = Button(self.__Frame40,text='Apply')
            #self.__Button5.pack(side='left')
            #self.__Button5.bind('<ButtonRelease-1>',self.__on_Button5_ButRel_1)
            pass
            self.__Frame53 = Tkinter.Frame(self.__Frame52)
            self.__Frame53.pack(side='left')
            self.__Label11 = Tkinter.Label(self.__Frame53,text='Movement Time:')
            self.__Label11.pack(side='top')
            
            
            self.__tooltipTE9_MT = GUIGTK_Class.ToolTip(self.__Label11, text=
                                    "Movement Time:"+"\n"+
                                    "(for Tone1 trials)"+"\n"+
                                     "Amount of 'continuous movement' time that should be detected to consider the trial as successful.")
            
            
            self.__Frame54 = Tkinter.Frame(self.__Frame52)
            self.__Frame54.pack(side='left')
            self.__Entry4MvntTime = Tkinter.Entry(self.__Frame54,width=10)
            self.__Entry4MvntTime.pack(side='top')
            self.__Frame56 = Tkinter.Frame(self.__Frame52,width=2)
            self.__Frame56.pack(side='left')
            self.__Frame55 = Tkinter.Frame(self.__Frame52)
            self.__Frame55.pack(side='left')
            self.__Label12 = Tkinter.Label(self.__Frame55,text='s.')
            self.__Label12.pack(side='top')
            self.__Frame57 = Tkinter.Frame(self.__Frame51)
            self.__Frame57.pack(side='left')
            self.__Label13 = Tkinter.Label(self.__Frame57,text='Idle Time:')
            self.__Label13.pack(side='top')
            
            
            self.__tooltipTE10_IT = GUIGTK_Class.ToolTip(self.__Label13, text=
                                    "Idle Time:"+"\n"+
                                    "(for Tone2 trials)"+"\n"+
                                     "Amount of 'continuous non-movement' time that should be detected to consider the trial as successful.")
            
            
            self.__Frame61 = Tkinter.Frame(self.__Frame51,width=40)
            self.__Frame61.pack(side='left')
            self.__Frame60 = Tkinter.Frame(self.__Frame51)
            self.__Frame60.pack(side='left')
            self.__Entry5IdleTime = Tkinter.Entry(self.__Frame60,width=10)
            self.__Entry5IdleTime.pack(side='top')
            self.__Frame59 = Tkinter.Frame(self.__Frame51,width=2)
            self.__Frame59.pack(side='left')
            self.__Frame58 = Tkinter.Frame(self.__Frame51)
            self.__Frame58.pack(side='left')
            self.__Label14 = Tkinter.Label(self.__Frame58,text='s.')
            self.__Label14.pack(side='top')
            #
            #Your code here
            self.__alreadyExecuted = 0
            pass
            #self.__Listbox1.insert( 0, "0-Accumulate Time")
            #self.__Listbox1.insert( 1, "1-Movement Vector")
            #self.__Listbox1.insert( 2, "2-Mvnt. Vector Binary")
            pass
            #let's read actual variables and assign them to the Entry classes and all that.
            
            self.__Entry1Tone1.insert(0, "1350")
            self.__Entry2Tone2.insert(0,"1750")
            self.__Entry3MvntAm.insert(0,"40")
            self.__Entry4MvntTime.insert(0,"0.5")
            self.__Entry5IdleTime.insert(0,"1.0")
            
            self.__EntryMethodUsed.insert(0, "3")
            self.__showTracking = 0
            self.__showFeedback = 0
            self.get_changes()
            #print "Form3: Parameters loaded"
            logger.info("Form3: Parameters loaded")
        
        def __on_CloseBtn_ButRel_1(self,Event=None):
            self.reference.App.hideForm3(True)
            pass
        
        def __on_ApplyBtn_ButRel_1(self,Event=None):
            print "Test Apply Frm3"
            self.get_changes()
            
            self.checkParametersVarsConsistency()
            
            self.saveParametersPreviousState()
            
            self.reference.App.hideForm3(False)
            self.reference.overrideaction_applyP()
            pass
        
        def configureData(self):
            #print "configuring initial data for Form3."
            logging.info("configuring initial data for Form3.")
            self.__Entry1Tone1.delete(0,10) #removes 10 characters.
            freq1 = int( self.reference.frequencyTone1 )
            self.__Entry1Tone1.insert(0, str(freq1))
            
            self.__Entry2Tone2.delete(0,10) #removes 10 characters.
            freq2 = int( self.reference.frequencyTone2 )
            self.__Entry2Tone2.insert(0, str(freq2))
            
            
            self.__Entry3MvntAm.delete(0,10) #removes 10 characters.
            mvmntam = int( self.reference.movementAmount )
            self.__Entry3MvntAm.insert(0, str(mvmntam))
            
            self.__Entry4MvntTime.delete(0,10) #removes 10 characters.
            movementTime = float( self.reference.movementTime )
            self.__Entry4MvntTime.insert(0, str(movementTime))
            
            self.__Entry5IdleTime.delete(0,10) #removes 10 characters.
            idleTime = float( self.reference.idleTime )
            self.__Entry5IdleTime.insert(0, str(idleTime))
            
            
            self.__EntryMethodUsed.delete(0,10) #removes 10 characters.
            movementMethod = int( self.reference.movementMethod )
            self.__EntryMethodUsed.insert(0, str(movementMethod))
            
            
            #parameters: nothing to save from initial state.
            
            self.resetGUIElements();
            self.setSkinnerVars();
            self.setOCVars();
            
            
            self.setPavlovVars();
            
            self.setDiscrVars()
            
            self.reference.App.showFrame3()
            self.reference.AppFrm3.withdraw()
            
            pass
        
        def __on_Button4_5recalibrate_ButRel_1(self, Event = None):
            self.reference.overrideaction_recalibratec()
            pass
        
        def __on_Button5_5NoiseF_ButRel_1(self, Event = None):
            print "noise filtering."
            self.reference.overrideaction_noisefiltering()
            pass
        
        
        def __on_Button1TestT1_ButRel_1(self,Event=None):
            print "Test Tone 1"
            self.var1_T1 = self.__Entry1Tone1.get()
            self.var2_T2 = self.__Entry2Tone2.get()
            self.checkParametersVarsConsistency()
            self.reference.frequencyTone1 = self.var1_T1
            self.reference.frequencyTone2 = self.var2_T2
            self.reference.overrideaction_testT1()
            pass
        
        def __on_Button2TestT2_ButRel_1(self,Event=None):
            print "Test Tone 2"
            self.reference.overrideaction_testT2()
            pass
        
        def __on_Button3SHTracking_ButRel_1(self,Event=None):
            if ( self.__showTracking == 0):
                print "hiding tracking"
                self.__showTracking = 1
                self.reference.overrideaction_hidetracking()
            elif ( self.__showTracking == 1):
                print "showing tracking"
                self.__showTracking = 0
                self.reference.overrideaction_showtracking()
            pass
        
        def __on_Button4SHFeedback_ButRel_1(self,Event=None):
            if ( self.__showFeedback == 0):
                print "hiding feedback"
                self.__showFeedback = 1
                self.reference.overrideaction_hidefeedback()
                
            elif ( self.__showFeedback == 1):
                print "showing feedback"
                self.__showFeedback = 0
                self.reference.overrideaction_showfeedback()
            pass
        
        def __on_Button5_ButRel_1(self,Event=None):
            pass
        
        def __on_Form3_Dstry(self,Event=None):
            pass
        
        def checkParametersVarsConsistency(self):
            try:
                a = float(self.var1_T1)
            except:
                self.var1_T1 = self.reference.previousVars.frequencyTone1
                self.reference.frequencyTone1 = self.reference.previousVars.frequencyTone1
                self.__Entry1Tone1.delete(0,10) #removes 10 characters.
                freq1 = int ( self.reference.previousVars.frequencyTone1 )
                self.__Entry1Tone1.insert(0, str(freq1))
                
                print "Bad input: frequencyTone1 to previous var."
            try:
                a = float(self.var2_T2)
            except:
                self.var2_T2 = self.reference.previousVars.frequencyTone2
                self.reference.frequencyTone2 = self.reference.previousVars.frequencyTone2
                self.__Entry2Tone2.delete(0,10) #removes 10 characters.
                freq1 = int( self.reference.previousVars.frequencyTone2 )
                self.__Entry2Tone2.insert(0, str(freq1))
                
                print "Bad input: frequencyTone2 to previous var."
            try:
                a = float(self.var3_MA)
            except:
                self.var3_MA = self.reference.previousVars.movementAmount
                self.reference.movementAmount = self.reference.previousVars.movementAmount
                self.__Entry3MvntAm.delete(0,10) #removes 10 characters.
                freq1 = int( self.reference.previousVars.movementAmount )
                self.__Entry3MvntAm.insert(0, str(freq1))
                
                print "Bad input: movementAmount to previous var."
            try:
                a = float(self.var4_MT)
            except:
                self.var4_MT = self.reference.previousVars.movementTime
                self.reference.movementTime = self.reference.previousVars.movementTime
                self.__Entry4MvntTime.delete(0,10) #removes 10 characters.
                freq1 = float( self.reference.previousVars.movementTime )
                self.__Entry4MvntTime.insert(0, str(freq1))
                
                print "Bad input: movementTime to previous var."
            try:
                a = float(self.var5_IT)
            except:
                self.var5_IT = self.reference.previousVars.idleTime
                self.reference.idleTime = self.reference.previousVars.idleTime
                self.__Entry5IdleTime.delete(0,10) #removes 10 characters.
                freq1 = float( self.reference.previousVars.idleTime )
                self.__Entry5IdleTime.insert(0, str(freq1))
                
                print "Bad input: idleTime to previous var."
            try:
                a = int(self.var8_num_selected)
            except:
                self.var8_num_selected = self.reference.previousVars.movementMethod
                self.reference.movementMethod = self.reference.previousVars.movementMethod
                self.__EntryMethodUsed.delete(0,10) #removes 10 characters.
                freq1 = int( self.reference.previousVars.movementMethod )
                self.__EntryMethodUsed.insert(0, str(freq1))
                
                print "Bad input: movementMethod to previous var."
            print "Parameters input checked."
            pass
        
        def saveParametersPreviousState(self):
            self.get_changes()
            
            self.reference.previousVars.frequencyTone1 = self.var1_T1
            self.reference.previousVars.frequencyTone2 = self.var2_T2
            self.reference.previousVars.movementAmount = self.var3_MA
            self.reference.previousVars.movementMethod = self.var8_num_selected
            self.reference.previousVars.movementTime = self.var4_MT
            self.reference.previousVars.idleTime = self.var5_IT
            #print "Parameters: Previous states saved."
            pass
        
        def setOCVars(self):
            print "oc vars"
            if (self.reference.type_ocond == 1):
                self.__Entry5IdleTime.config(state = "readonly")
                self.__Entry2Tone2.config(state = "readonly")
                self.reference.current_type = "oc"
                pass
        
        def setDiscrVars(self):
            print "discr vars"
            if (self.reference.type_discr == 1):
                self.reference.current_type = "discr"
            pass
        
        def setPavlovVars(self):
            print "pavlov vars"
            if (self.reference.type_pavlov == 1 ):
                print "pavlov"
                self.reference.current_type = "pavlov"
                self.__Entry2Tone2.config(state = "readonly")
                self.__Entry3MvntAm.config(state = "readonly")
                self.__EntryMethodUsed.config(state = "readonly")
                self.__Entry4MvntTime.config(state = "readonly")
                self.__Entry5IdleTime.config(state = "readonly")
        
        def setSkinnerVars(self):
            print "skinner vars"
            if (self.reference.type_skinner == 1):
                print "skinner"
                self.reference.current_type = "skinner"
                self.__Entry1Tone1.config(state = "readonly")
                self.__Entry2Tone2.config(state = "readonly")
                self.__Entry5IdleTime.config(state = "readonly")
        
        def resetGUIElements(self):
            self.reference.current_type = ""
            self.__Entry1Tone1.config(state = "normal")
            self.__Entry2Tone2.config(state = "normal")
            self.__Entry3MvntAm.config(state = "normal")
            self.__EntryMethodUsed.config(state = "normal")
            self.__Entry4MvntTime.config(state = "normal")
            self.__Entry5IdleTime.config(state = "normal")
            print "everything resetted."
            
        
        def get_changes(self):
            #Raw input data.
            #print "commiting changes to variables in Form 3.."
            logger.info("commiting changes to variables in Form 3..")
    #         print self.__Entry1TStart.get()
    #         print self.__Entry2TEnd.get()
    #         print self.__Entry3MvmntWindowStart.get()
    #         print self.__Entry4MvntWindowEnd.get()
    #         print self.__Entry5ITStart.get()
    #         print self.__Entry6ITEnd.get()
    #         print self.__Scale2.get()
            self.var1_T1 = self.__Entry1Tone1.get()
            self.var2_T2 = self.__Entry2Tone2.get()
            self.var3_MA = self.__Entry3MvntAm.get()
            self.var4_MT = self.__Entry4MvntTime.get()
            self.var5_IT = self.__Entry5IdleTime.get()
            self.var6_ShowTracking = self.__showTracking
            self.var7_ShowFeedback = self.__showFeedback 
            self.var8_num_selected = self.__EntryMethodUsed.get()
    
    
    
    class Form1(Tkinter.Toplevel):
        #Trial Events.
        orig_toneend = 0;
        orig_mvntwinend = 0;
        
        def __init__(self,Master=None,**kw):
            kw['class_'] = 'Frame'
            #
            #Your code here
            #FORM: Trial Events
            apply(Tkinter.Toplevel.__init__,(self,Master),kw)
        
        def initAll(self):
            self.pavlov = Tkinter.IntVar(self)
            self.skinner = Tkinter.IntVar(self)
            self.oc = Tkinter.IntVar(self)
            self.discr = Tkinter.IntVar(self)
            self.requireStillness = Tkinter.IntVar(self)
            
            self.bind('<Destroy>',self.__on_Form1_Dstry)
            self.__Frame2 = Tkinter.Frame(self)
            self.__Frame2.pack(side='left')
            self.__Frame1 = Tkinter.Frame(self)
            self.__Frame1.pack(side='left')
            self.__Frame4 = Tkinter.Frame(self.__Frame2)
            self.__Frame4.pack(side='top')
            self.__Frame3 = Tkinter.Frame(self.__Frame2)
            self.__Frame3.pack(side='top')
            self.__Frame5 = Tkinter.Frame(self.__Frame4)
            self.__Frame5.pack(side='left')
            self.__Frame6 = Tkinter.Frame(self.__Frame4,width=50)
            self.__Frame6.pack(side='left')
            self.__Frame7 = Tkinter.Frame(self.__Frame3)
            self.__Frame7.pack(side='left')
            self.__Frame8 = Tkinter.Frame(self.__Frame3)
            self.__Frame8.pack(side='left')
            self.__Frame21 = Tkinter.Frame(self.__Frame3)
            self.__Frame21.pack(side='left')
            self.__Frame9 = Tkinter.Frame(self.__Frame5)
            self.__Frame9.pack(side='top')
            self.__lblTrialEventsTitle = Tkinter.Label(self.__Frame9,text='Trial Events')
            self.__lblTrialEventsTitle.pack(side='top')
            self.__Frame10 = Tkinter.Frame(self.__Frame5)
            self.__Frame10.pack(side='top')
            self.__Frame14 = Tkinter.Frame(self.__Frame7,height=35)
            self.__Frame14.pack(side='top')
            self.__FrameCHEBKBTNS = Tkinter.Frame(self.__Frame7)
            self.__FrameCHEBKBTNS.pack(side='top')
            self.__Frame15 = Tkinter.Frame(self.__Frame7)
            self.__Frame15.pack(side='top')
            self.__Frame13 = Tkinter.Frame(self.__Frame7)
            self.__Frame13.pack(side='top')
            self.__Frame20 = Tkinter.Frame(self.__Frame7)
            self.__Frame20.pack(side='top')
            self.__Frame17 = Tkinter.Frame(self.__Frame7)
            self.__Frame17.pack(side='top')
            self.__Frame16 = Tkinter.Frame(self.__Frame7)
            self.__Frame16.pack(side='top')
            self.__Frame19 = Tkinter.Frame(self.__Frame7)
            self.__Frame19.pack(side='top')
            self.__Frame36 = Tkinter.Frame(self.__Frame7)
            self.__Frame36.pack(side='top')
            self.__Frame18 = Tkinter.Frame(self.__Frame7)
            self.__Frame18.pack(side='top')
            self.__Frame38 = Tkinter.Frame(self.__Frame7)
            self.__Frame38.pack(side='top')
            
            
            
            self.__CloseBtn = Tkinter.Button(self.__Frame38,text='Close')
            self.__CloseBtn.pack(side='bottom')
            self.__CloseBtn.bind('<ButtonRelease-1>',self.__on_CloseBtn_ButRel_1)
            
            self.__tooltipTE2_Close = GUIGTK_Class.ToolTip(self.__CloseBtn, text=
                                    "Close:"+"\n"+
                                     "Closes this window without saving changes.")
            
            
            self.__ApplyBtn = Tkinter.Button(self.__Frame38,text='Apply')
            self.__ApplyBtn.pack(side='bottom')
            self.__ApplyBtn.bind('<ButtonRelease-1>',self.__on_ApplyBtn_ButRel_1)
            
            self.__tooltipTE1_Apply = GUIGTK_Class.ToolTip(self.__ApplyBtn, text=
                                    "Apply:"+"\n"+
                                     "Applies and saves all changes made to the Trial Events.")
            
            self.__Frame37 = Tkinter.Frame(self.__Frame7)
            self.__Frame37.pack(side='top')
            self.__Frame11 = Tkinter.Frame(self.__Frame10,width=80)
            self.__Frame11.pack(side='left')
            self.__Frame12 = Tkinter.Frame(self.__Frame10)
            self.__Frame12.pack(side='left')
    #         self.__Scale1 = Scale(self.__Frame12,length=200,orient='horizontal'
    #             ,sliderlength=20)
    #         self.__Scale1.pack(side='top')
            self.__Frame24 = Tkinter.Frame(self.__Frame15)
            self.__Frame24.pack(side='left')
            
            
            self.__CheckPavlov = Tkinter.Checkbutton(self.__FrameCHEBKBTNS,text='Pavlov mode', variable=self.pavlov)
            self.__CheckPavlov.pack(side='top')
            
            self.__tooltipMODE_P = GUIGTK_Class.ToolTip(self.__CheckPavlov, text=
                                    "Pavlov mode"+"\n"+
                                     "Sets the training as a Pavlov training mode. (for more info check documentation)"+
                                     "")
            
            self.__CheckSkinner = Tkinter.Checkbutton(self.__FrameCHEBKBTNS,text='Skinner mode', variable=self.skinner)
            self.__CheckSkinner.pack(side='top')
            
            self.__tooltipMODE_S = GUIGTK_Class.ToolTip(self.__CheckSkinner, text=
                                    "Skinner mode"+"\n"+
                                     "Sets the training as a Skinner training mode. (for more info check documentation)"+
                                     "")
            
            self.__CheckOC = Tkinter.Checkbutton(self.__FrameCHEBKBTNS,text='Operant Conditioning mode', variable=self.oc)
            self.__CheckOC.pack(side='top')
            
            self.__tooltipMODE_OC = GUIGTK_Class.ToolTip(self.__CheckOC, text=
                                    "Operant Conditioning mode"+"\n"+
                                     "Sets the training as an Operant Conditioning training mode. (for more info check documentation)"+
                                     "")
            
            self.__CheckDiscrimination = Tkinter.Checkbutton(self.__FrameCHEBKBTNS,text='Discrimination mode', variable=self.discr)
            self.__CheckDiscrimination.pack(side='top')
            
            self.__tooltipMODE_D = GUIGTK_Class.ToolTip(self.__CheckDiscrimination, text=
                                    "Discrimination mode"+"\n"+
                                     "Sets the training as a Discrimination training mode. (for more info check documentation)"+
                                     "")
            
            
            self.__Label1 = Tkinter.Label(self.__Frame24,text='Tone Start:')
            self.__Label1.pack(side='top')
            self.__Frame25 = Tkinter.Frame(self.__Frame15)
            self.__Frame25.pack(side='left')
            self.__Entry1TStart = Tkinter.Entry(self.__Frame25,width=5)
            self.__Entry1TStart.pack(side='top')
            
            self.__tooltipTE3_TS = GUIGTK_Class.ToolTip(self.__Label1, text=
                                    "Tone Start:"+"\n"+
                                     "Instant of time when tone starts."+
                                     " It is defined as always 0 and cannot be changed")
            
            
            self.__Frame27 = Tkinter.Frame(self.__Frame13)
            self.__Frame27.pack(side='left')
            self.__Label2 = Tkinter.Label(self.__Frame27,text='Tone End:')
            self.__Label2.pack(side='top')
            self.__Frame26 = Tkinter.Frame(self.__Frame13)
            self.__Frame26.pack(side='left')
            self.__Entry2TEnd = Tkinter.Entry(self.__Frame26,width=5)
            self.__Entry2TEnd.pack(side='top')
            
            self.__tooltipTE4_TE = GUIGTK_Class.ToolTip(self.__Label2, text=
                                    "Tone End:"+"\n"+
                                     "Instant of time when tone stops.")
            
            self.__Frame28 = Tkinter.Frame(self.__Frame20)
            self.__Frame28.pack(side='left')
            self.__Label3 = Tkinter.Label(self.__Frame28,text='Movement Window Start:')
            self.__Label3.pack(side='top')
            self.__Frame29 = Tkinter.Frame(self.__Frame20)
            self.__Frame29.pack(side='left')
            self.__Entry3MvmntWindowStart = Tkinter.Entry(self.__Frame29,width=5)
            self.__Entry3MvmntWindowStart.pack(side='top')
            
            self.__tooltipTE5_MWS = GUIGTK_Class.ToolTip(self.__Label3, text=
                                    "Movement Window Start:"+"\n"+
                                     "Instant of time when movement starts to be considered.")
            
            
            self.__Frame30 = Tkinter.Frame(self.__Frame17)
            self.__Frame30.pack(side='left')
            self.__Label4 = Tkinter.Label(self.__Frame30,text='Movement Window End:')
            self.__Label4.pack(side='top')
            self.__Frame31 = Tkinter.Frame(self.__Frame17)
            self.__Frame31.pack(side='left')
            self.__Entry4MvntWindowEnd = Tkinter.Entry(self.__Frame31,width=5)
            self.__Entry4MvntWindowEnd.pack(side='top')
            
            self.__tooltipTE6_MWE = GUIGTK_Class.ToolTip(self.__Label4, text=
                                    "Movement Window End:"+"\n"+
                                     "Instant of time when movement stops being detected.")
            
            self.__Frame33 = Tkinter.Frame(self.__Frame16)
            self.__Frame33.pack(side='left')
            self.__Label5 = Tkinter.Label(self.__Frame33,text='InterTrial Start:')
            self.__Label5.pack(side='top')
            self.__Frame32 = Tkinter.Frame(self.__Frame16)
            self.__Frame32.pack(side='left')
            self.__Entry5ITStart = Tkinter.Entry(self.__Frame32,width=5)
            self.__Entry5ITStart.pack(side='top')
            
            self.__tooltipTE7_ITS = GUIGTK_Class.ToolTip(self.__Label5, text=
                                    "InterTrial Start:"+"\n"+
                                     "An intertrial stage runs between this value and ends in the 'InterTrial End' value."
                                     +"\n"+
                                     "The intertrial stage duration is random between these two values."
                                     )
            
            
            self.__Frame35 = Tkinter.Frame(self.__Frame19)
            self.__Frame35.pack(side='left')
            self.__Label6 = Tkinter.Label(self.__Frame35,text='InterTrial End:')
            self.__Label6.pack(side='top')
            self.__Frame34 = Tkinter.Frame(self.__Frame19)
            self.__Frame34.pack(side='left')
            self.__Entry6ITEnd = Tkinter.Entry(self.__Frame34,width=5)
            self.__Entry6ITEnd.pack(side='top')
            
            
            self.__tooltipTE8_ITE = GUIGTK_Class.ToolTip(self.__Label6, text=
                                    "InterTrial End:"+"\n"+
                                     "An intertrial stage runs between 'InterTrial Start' and ends in this value."
                                     +"\n"+
                                     "The intertrial stage duration is random between these two values."
                                     )
            
            
            self.__Frame22 = Tkinter.Frame(self.__Frame36)
            self.__Frame22.pack(side='left')
            self.__Label7 = Tkinter.Label(self.__Frame22,text='Probability Tone1:')
            self.__Label7.pack(side='top')
            self.__Frame23 = Tkinter.Frame(self.__Frame36)
            self.__Frame23.pack(side='left')
            self.__Scale2 = Tkinter.Scale(self.__Frame23,orient='horizontal')
            self.__Scale2.pack(side='top')
            
            
            self.__tooltipTE9_PT1 = GUIGTK_Class.ToolTip(self.__Label7, text=
                                    "Probability Tone1:"+"\n"+
                                     "Sets the probability that the Tone 1 plays."
                                     + "\n" +
                                     "The remaining probability is that of the Tone 2 playing."
                                     )
            
            
            self.__CheckRequireStillness = Tkinter.Checkbutton(self.__Frame38,text='Require stillness to end trial.',
                                                       variable=self.requireStillness);
            self.__CheckRequireStillness.pack(side='top')
            
            
            self.__tooltipREQSTILL = GUIGTK_Class.ToolTip(self.__CheckRequireStillness, text=
                                    "Require stillness to end trial"+"\n"+
                                     "If checked, it is required to stay still (with no movement) a certain amount of time (default: 1 sec) "+
                                     "to end the trial and start the next one.")
            
            
            self.__CheckRequireStillness.select(); #pending get this from config.
            
            self.__alreadyExecuted = 0
            self.__Entry1TStart.insert(0,"0.0")
            self.__Entry2TEnd.insert(0,"0.0")
            self.__Entry3MvmntWindowStart.insert(0,"0.0")
            self.__Entry4MvntWindowEnd.insert(0,"0.0")
            self.__Entry5ITStart.insert(0,"0.0")
            self.__Entry6ITEnd.insert(0,"0.0")
            self.__Scale2.set(50)
            
            self.__Entry1TStart.config(state = "readonly")
            
            self.get_changes()
            #print "Form1: Trial Events loaded"
            logger.info( "Form1: Trial Events loaded" )
        
        def __on_ApplyBtn_ButRel_1(self,Event=None):
            print "Test Apply Frm1"
            self.get_changes()
            
            self.checkTrialEventsVarsConsistency()
            
            self.saveTrialEventsPreviousState()
            
            
            self.reference.App.hideForm1(False)
            self.reference.overrideaction_applyTE()
            pass
        
        def __on_CloseBtn_ButRel_1(self,Event=None):
            self.reference.App.hideForm1(True)
            pass
        
        def __on_Form1_Dstry(self,Event=None):
            if ( self.__alreadyExecuted == 0):
                self.__alreadyExecuted = 1
                #print self.gVariables.movementTime
                self.withdraw()
                print "Leaving Form 1: Trial Events."
            pass
        
        def configureData(self):
            #print "configuring initial data for Form1."
            logging.info("configuring initial data for Form1.")
            
            self.requireStillness.set(self.reference.requireStillnessVar)
            #print "requireStillnessVar: %d" % self.reference.requireStillnessVar
            
            if (self.reference.requireStillnessVar == 0):
                self.__CheckRequireStillness.deselect();
            else:
                self.__CheckRequireStillness.select();
            
            self.requireStillness.set(self.reference.requireStillnessVar)            
            self.__Entry1TStart.delete(0,10) #removes 10 characters.
            self.__Entry1TStart.insert(0, self.reference.toneStart )
            
            self.__Entry2TEnd.delete(0,10) #removes 10 characters.
            self.__Entry2TEnd.insert(0, self.reference.toneEnd )
            
            self.__Entry3MvmntWindowStart.delete(0,10) #removes 10 characters.
            self.__Entry3MvmntWindowStart.insert(0, self.reference.movementWindowStart )
            
            self.__Entry4MvntWindowEnd.delete(0,10) #removes 10 characters.
            self.__Entry4MvntWindowEnd.insert(0, self.reference.movementWindowEnd )
            
            self.__Entry5ITStart.delete(0,10) #removes 10 characters.
            self.__Entry5ITStart.insert(0, self.reference.interTrialStart )
            
            self.__Entry6ITEnd.delete(0,10) #removes 10 characters.
            self.__Entry6ITEnd.insert(0, self.reference.interTrialEnd )
            
            prob = self.reference.probabilityToneOne * 100
            self.__Scale2.set(int(prob))
            
            
            self.orig_toneend = self.reference.toneEnd
            
            self.orig_mvntwinend = self.reference.movementWindowEnd
            
            self.resetGUIElements();
            self.setPavlovVars();
            self.setSkinnerVars();
            
            self.setOCVars();
            self.setDiscrVars();
            
            self.reference.App.showFrame1()
            self.reference.AppFrm1.withdraw()
            ###
            
#             prob = self.gVariables.toneOneProbability * 100
#             self.__Scale2.set(int(prob))
#             
#             self.__Entry1TStart.delete(0,10) #removes 10 characters.
#             self.__Entry1TStart.insert(0, self.gVariables.soundGenDuration1 )
#             
#             self.__Entry2TEnd.delete(0,10) #removes 10 characters.
#             self.__Entry2TEnd.insert(0, self.gVariables.soundGenDuration2 )
#             
#             self.__Entry3MvmntWindowStart.delete(0,10) #removes 10 characters.
#             self.__Entry3MvmntWindowStart.insert(0, self.gVariables.eventTime1_movement_start )
#             
#             self.__Entry4MvntWindowEnd.delete(0,10) #removes 10 characters.
#             self.__Entry4MvntWindowEnd.insert(0, self.gVariables.eventTime2_movement )
#             
#             self.__Entry5ITStart.delete(0,10) #removes 10 characters.
#             self.__Entry5ITStart.insert(0, self.gVariables.interTrialRandom1Time )
#             
#             self.__Entry6ITEnd.delete(0,10) #removes 10 characters.
#             self.__Entry6ITEnd.insert(0, self.gVariables.interTrialRandom2Time )
            pass
        
        def setPavlovVars(self):
            self.pavlov.set( self.reference.type_pavlov )
            print "pavlov vars"
            if (self.reference.type_pavlov == 1):
                print "pavlov"
                self.reference.current_type = "pavlov"
                self.__Entry4MvntWindowEnd.delete(0,10) #removes 10 characters.
                self.__Entry4MvntWindowEnd.insert(0, str( self.__Entry3MvmntWindowStart.get() ) )
                self.__Entry3MvmntWindowStart.config(state = "readonly")
                self.__Entry4MvntWindowEnd.config(state = "readonly")
                self.__CheckPavlov.select()
        
        def setSkinnerVars(self):
            print "skinner vars"
            self.skinner.set( self.reference.type_skinner )
            if (self.reference.type_skinner == 1):
                print "skinner"
                self.reference.current_type = "skinner"
                self.__Entry2TEnd.delete(0,10) #removes 10 characters.
                self.__Entry2TEnd.insert(0, str(0.0) )
                self.__Entry2TEnd.config(state = "readonly")
                self.__CheckSkinner.select()
        
        def setOCVars(self):
            print "oc vars"
            self.oc.set( self.reference.type_ocond )
            if (self.reference.type_ocond == 1):
                self.reference.current_type = "oc"
                self.__CheckOC.select()
                pass
        
        def setDiscrVars(self):
            print "Discr. vars"
            self.discr.set( self.reference.type_discr )
            if (self.reference.type_discr == 1):
                self.reference.current_type = "discr"
                self.__CheckDiscrimination.select()
                pass
            
        def resetGUIElements(self):
            self.__CheckDiscrimination.deselect()
            self.__CheckOC.deselect()
            self.__Entry2TEnd.config(state = "normal")
            self.__CheckSkinner.deselect()
            self.__Entry3MvmntWindowStart.config(state = "normal")
            self.__Entry4MvntWindowEnd.config(state = "normal")
            self.__CheckPavlov.deselect()
            self.__Entry2TEnd.delete(0,10) #removes 10 characters.
            self.__Entry2TEnd.insert(0, str(self.orig_toneend))
            self.__Entry4MvntWindowEnd.delete(0,10) #removes 10 characters.
            self.__Entry4MvntWindowEnd.insert(0, str(self.orig_mvntwinend))
            self.reference.current_type = ""
        
        def get_changes(self):
            #print "commiting changes to variables in Form 1.."
            logger.info("commiting changes to variables in Form 1..")
    #         print self.__Entry1TStart.get()
    #         print self.__Entry2TEnd.get()
    #         print self.__Entry3MvmntWindowStart.get()
    #         print self.__Entry4MvntWindowEnd.get()
    #         print self.__Entry5ITStart.get()
    #         print self.__Entry6ITEnd.get()
    #         print self.__Scale2.get()
            self.var1_TStart = self.__Entry1TStart.get()
            self.var2_TEnd = self.__Entry2TEnd.get()
            self.var3_MWS = self.__Entry3MvmntWindowStart.get()
            self.var4_MWE = self.__Entry4MvntWindowEnd.get()
            self.var5_ITStart = self.__Entry5ITStart.get()
            self.var6_ITEnd = self.__Entry6ITEnd.get()
            self.var7_Probab1 = float (self.__Scale2.get()) / 100
            pass
        
        def saveTrialEventsPreviousState(self):
            self.get_changes() #because maybe changes weren't successfull
            self.reference.previousVars.toneStart = self.var1_TStart
            self.reference.previousVars.toneEnd = self.var2_TEnd
            self.reference.previousVars.movementWindowStart = self.var3_MWS
            self.reference.previousVars.movementWindowEnd = self.var4_MWE
            self.reference.previousVars.interTrialStart = self.var5_ITStart
            self.reference.previousVars.interTrialEnd = self.var6_ITEnd
            self.reference.previousVars.probabilityToneOne = self.var7_Probab1
            
            #print "Trial Events: Previous states saved."
            pass
        
        def checkTrialEventsVarsConsistency(self):
            
            print self.pavlov.get()
            print self.skinner.get()
            print self.oc.get()
            print self.discr.get()
            
            changed = 0;
            
            if ( self.reference.type_pavlov != self.pavlov.get() or 
            self.reference.type_skinner != self.skinner.get() or
            self.reference.type_ocond != self.oc.get() or
            self.reference.type_discr != self.discr.get() ):
                changed = 1;
            
            if (self.pavlov.get() == 1):
                self.skinner.set(0)
                self.oc.set(0)
                self.discr.set(0)
            
            if (self.skinner.get() == 1):
                self.pavlov.set(0)
                self.oc.set(0)
                self.discr.set(0)
            
            
            if (self.oc.get() == 1):
                self.skinner.set(0)
                self.pavlov.set(0)
                self.discr.set(0)
            
            if (self.discr.get() == 1 ):
                self.skinner.set(0)
                self.pavlov.set(0)
                self.oc.set(0)
            
            self.reference.type_pavlov = self.pavlov.get()
            self.reference.type_skinner = self.skinner.get()
            self.reference.type_ocond = self.oc.get()
            self.reference.type_discr = self.discr.get()
            
            if (changed):
                self.resetGUIElements()
                self.setSkinnerVars();
                self.setPavlovVars();
                self.setOCVars()
                self.setDiscrVars();
                
                print self.pavlov.get()
                print self.skinner.get()
                print self.oc.get()
                print self.discr.get()
                
                self.reference.AppFrm3.resetGUIElements()
                self.reference.AppFrm3.setPavlovVars()
                self.reference.AppFrm3.setSkinnerVars()
                self.reference.AppFrm3.setOCVars()
                self.reference.AppFrm3.setDiscrVars()
            pass
            try:
                self.reference.toneStart = float(self.var1_TStart)
            except:
                self.var1_TStart = self.reference.previousVars.toneStart
                self.reference.toneStart = self.reference.previousVars.toneStart
                self.__Entry1TStart.delete(0,10) #removes 10 characters.
                freq1 = float ( self.reference.previousVars.toneStart )
                self.__Entry1TStart.insert(0, str(freq1))
                
                print "Bad input: ToneStart to previous var."
            try:
                self.reference.toneEnd = float(self.var2_TEnd)
            except:
                self.var2_TEnd = self.reference.previousVars.toneEnd
                self.reference.toneEnd = self.reference.previousVars.toneEnd
                self.__Entry2TEnd.delete(0,10) #removes 10 characters.
                freq1 = float ( self.reference.previousVars.toneEnd )
                self.__Entry2TEnd.insert(0, str(freq1))
                
                print "Bad input: toneEnd to previous var."
            try:
                self.reference.movementWindowStart = float(self.var3_MWS)
            except:
                self.var3_MWS = self.reference.previousVars.movementWindowStart
                self.reference.movementWindowStart = self.reference.previousVars.movementWindowStart
                self.__Entry3MvmntWindowStart.delete(0,10) #removes 10 characters.
                freq1 = float ( self.reference.previousVars.movementWindowStart )
                self.__Entry3MvmntWindowStart.insert(0, str(freq1))
                
                print "Bad input: movementWindowStart to previous var."
            try:
                self.reference.movementWindowEnd = float(self.var4_MWE)
            except:
                self.var4_MWE = self.reference.previousVars.movementWindowEnd
                self.reference.movementWindowEnd = self.reference.previousVars.movementWindowEnd
                self.__Entry4MvntWindowEnd.delete(0,10) #removes 10 characters.
                freq1 = float ( self.reference.previousVars.movementWindowEnd )
                self.__Entry4MvntWindowEnd.insert(0, str(freq1))
                
                print "Bad input: movementWindowEnd to previous var."
            try:
                self.reference.interTrialStart = float(self.var5_ITStart)
            except:
                self.var5_ITStart = self.reference.previousVars.interTrialStart
                self.reference.interTrialStart = self.reference.previousVars.interTrialStart
                self.__Entry5ITStart.delete(0,10) #removes 10 characters.
                freq1 = float ( self.reference.previousVars.interTrialStart )
                self.__Entry5ITStart.insert(0, str(freq1))
                
                print "Bad input: interTrialStart to previous var."
            try:
                self.reference.interTrialEnd = float(self.var6_ITEnd)
            except:
                self.var6_ITEnd = self.reference.previousVars.interTrialEnd
                self.reference.interTrialEnd = self.reference.previousVars.interTrialEnd
                self.__Entry6ITEnd.delete(0,10) #removes 10 characters.
                freq1 = float ( self.reference.previousVars.interTrialEnd )
                self.__Entry6ITEnd.insert(0, str(freq1))
                
                print "Bad input: interTrialEnd to previous var."
            try:
                self.reference.probabilityToneOne = float(self.var7_Probab1)
            except:
                #very improbable since the probability is set with a sliding bar..
                self.var7_Probab1 = self.reference.previousVars.probabilityToneOne
                self.reference.probabilityToneOne = self.reference.previousVars.probabilityToneOne
                freq1 = float ( self.reference.previousVars.probabilityToneOne )
                self.__Scale2.set(int (freq1 * 100) )
                
                print "Bad input: probabilityToneOne to previous var."
            pass
            self.reference.requireStillness = self.requireStillness
            self.reference.requireStillnessVar = self.requireStillness.get()
    
    
    class Form_help(Tkinter.Frame):
        def __init__(self, root):
    
            Tkinter.Frame.__init__(self, root)
            self.root = root
            self.canvas = Tkinter.Canvas(root, borderwidth=0, background="#ffffff")
            self.DefClr = self.canvas.cget("bg")
            self.frame = Tkinter.Frame(self.canvas, background="#ffffff")
            self.vsb = Tkinter.Scrollbar(root, orient="vertical", command=self.canvas.yview)
            self.hsb = Tkinter.Scrollbar(root, orient="horizontal", command=self.canvas.xview)
            self.canvas.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set )
    
            self.vsb.pack(side="right", fill="y")
            self.hsb.pack(side="bottom", fill="x")
            self.canvas.pack(side="left", fill="both", expand=True)
            self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
                                      tags="self.frame")
            
            self.bind('<Destroy>',self.dummy_fn)
            self.frame.bind("<Configure>", self.OnFrameConfigure)
            self.current_help_page = 3
            self.change_page()
            self.calculateBestSize()
        
        def change_page(self):
            #print "Help form: changing page"
            logger.debug("Help form: changing page")
            #self.calculateBestSize()
            for child in self.frame.winfo_children():
                child.destroy()
            if self.current_help_page == 1:
                self.populate_pg2()
            elif self.current_help_page == 2:
                self.populate_pg3()
            elif self.current_help_page == 3:
                self.populate_pg1()
            #print "Current page: %r" % self.current_help_page
            logger.debug("Current page: %r" % self.current_help_page)

        def dummy_fn(self, arg):
            logger.debug("test fn.") 
            #print self.reference.helpNumber
            self.reference.helpNumber = 0;
            #print self.reference.helpNumber
            pass
    
        def populate_pg1(self):
            '''populate frame.'''
            self.current_help_page = 1
            button = Tkinter.Button(self.frame,
                                     text = 'Next Page', command = self.change_page).grid(row=0, column=0)
            
            rowcount = 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Drop", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Drop: </b>Gives a drop of water, by opening the parallel port valve for 100 ms.
    The count of successful trials is not being affected by this function."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Reward", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Reward: </b>Gives a drop of water, by opening the parallel port valve for 100 ms.
    The count of successful trials is increased by a value of one."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Open", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Open: </b>Opens the parallel port valve (indefinitely until it is closed manually)."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Close", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """Closes the parallel port valve."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Start / Stop Training:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Start / Stop Training: </b>If the training hasn't started or has been stopped, starts the training session.
    Else, this function will stop the training session."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Pause / Resume Training:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Pause / Resume Training: </b>If the training has started and is currently running, pauses the training session.
    Else if the training session has been paused, resumes the training in the same state as it was paused."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Exit:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Exit: </b>Exits the training program, and all its submodules, previously saving and closing all logging files."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Comment about this training:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b> Comment about this training: </b>Opens a form to write a comment about this training session.
    The comment written will be logged for this session."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Trial Events:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b> Trial Events: </b> Opens a form to configure Trial Events.
    This includes the duration of tone, the length of the detection window, among other variables."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Parameters:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b> Parameters: </b> Opens a form to configure Parameters
    This includes tone frequencies, video options and movement detection variables."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            #for row in range(100):
            #    Label(self.frame, text="%s" % row, width=3, borderwidth="1", 
            #             relief="solid").grid(row=row, column=0)
            #    t="this is the second colum for row %s" %row
            #    Label(self.frame, text=t).grid(row=row, column=1)
            pass
    
    
        def populate_pg2(self):
            '''populate frame.'''
            self.current_help_page = 2
            rowcount = 0
            button = Tkinter.Button(self.frame, text = 'Next Page',
                                     command = self.change_page).grid(row=rowcount, column=0)
            #Label(self.frame, text=" . ", borderwidth="1", 
            #             relief="solid").grid(row=0, column=0)
            TEXTO = """A 'trial' is defined as the time between two successive tones.
      
      Thus, the start of the tone defines the beginning of the trial.
      It has a certain duration (determined by the 'Tone End' variable).
      
      After the tone has finished, a Movement Window follows, during which movement
      is detected. Its limits are determined by two variables.
      
      The reward is given at the end of the Movement Window, if the trial was successful.
      
      After the movement window ends, there is an 'Intertrial' gap, during
      which no tone or drop is given (unless given manually).
      This gap's duration is controlled by two variables, and is random between these 2 values.
      
      For additional help regarding the types of modes, and other topics, please consult the project's webpage:
        https://github.com/yagui/sphere-training
    """
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
                        #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Pavlov Mode:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Pavlov Mode: </b> Configures all training variables to set a Pavlov mode trial.
This mode generates a tone and gives a reward, regardless of the subject's performance."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Skinner Mode:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Skinner Mode: </b> Configures all training variables to set a Skinner mode trial.
This mode waits for the subject to make the desired response (go type) and gives a reward when it is done."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Operant Conditioning Mode:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Operant Conditioning Mode: </b> Configures all training variables to set an Operant Conditioning mode trial.
This mode has trials consisting of: one tone, an opportunity window time where the subject can perform a go-type
response, and a reward is given at the end of this window if the trial was successful. An intertrial follows, before
the start of a new trial."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Discrimination Mode:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Discrimination Mode: </b> Configures all training variables to set a Discrimination mode trial.
This mode has trials consisting of: one tone (of two possible, one for go and other for no-go), an opportunity window time
where the subject can perform a go-type response for go-trials or no-go type response for nogo-trials,
and a reward is given at the end of this window if the trial was successful. An intertrial follows, before
the start of a new trial."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Tone Start:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Tone Start: </b> Instant of the trial time when the tone starts playing.
    By the definition of a trial, it is always 0 and cannot be changed."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Tone End:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Tone End: </b> Instant of the trial time when the tone ends.
    This variable defines the duration of the Tone, and should be less than Intertrial End."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Movement Window Start:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Movement Window Start: </b> Instant of the trial time when the movement starts being detected.
    This value should be greater than 0 and less than Intertrial Start"""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Movement Window End:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Movement Window End: </b> Instant of the trial time when the movement stops being detected.
    This value should be greater than Movement Window Start, and less than Intertrial Start.
    When the trial time passes this value, the system will check if the trial was successful or not."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Intertrial Start:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Intertrial Start: </b> Instant of time when Intertrial Starts.
    The drop (if trial was successfull) will be given in this instant of the trial time."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Intertrial End:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Intertrial End: </b> Maximum instant of time when Intertrial ends.
    The 'Intertrial Duration' is a random value between Intertrial Start and Intertrial End."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Probability Tone 1:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Probability Tone 1: </b> This value sets the probability of the Tone 1 being played
    in each trial.
    By default, a given trial will play Tone 1 or Tone 2, so this variable sets the Tone 2
    probability.
    Note that all trials will always play at least one of the two tones."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Require Stillness to end trial:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Require Stillness to end trial: </b> If checked, it is required to stay still a certain amount of time (default: 1 sec) 
to end the trial and start the next one."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            #for row in range(100):
            #    Label(self.frame, text="%s" % row, width=3, borderwidth="1", 
            #             relief="solid").grid(row=row, column=0)
            #    t="this is the second colum for row %s" %row
            #    Label(self.frame, text=t).grid(row=row, column=1)
            pass
    
    
        def populate_pg3(self):
            '''populate frame.'''
            self.current_help_page = 3
            rowcount = 0;
            button = Tkinter.Button(self.frame, text = 'Next Page', command = self.change_page).grid(row=rowcount, column=0)
            #Label(self.frame, text=" . ", borderwidth="1", 
            #             relief="solid").grid(row=0, column=0)
            TEXTO = """This form sets some general parameters used by the training session.
      Audio:
        Tone 1: It is a tone played during a trial where movement will be detected.
        Tone 1: It is a tone played during a trial where idle (or 'no-movement') will be detected.
        
        Two Entry boxes are provided for setting the frequency of Tone 1, and Tone 2.
        Both are integer values, and in 'Hertz'.
        
        Test buttons are provided to play the tone independently of the current trial status.
        
      Video:
        Feedback and camera settings.
        The Video variables include some movement detection parameters, like Threshold amount and
        method to use for movement detection.
        
        There are three methods currently available:
          0=Accumulate time:
              This Method analyzes continuous movement. If detected, saves the amount of seconds
              of the movement so far.
              If idle is detected, it saves how much time the subject is idle.
          1= movementVector:
              Each cycle, an element is added to movement vector.
              If there are N past 1's in the vector, then it was moving and currently is. (includes certain 0's tolerance)
              Else: it is idle.
              This method returns the estimated movement time (how much time it was moving) or idle time.
              This method does not considers anything different than moving or idle (there is no extra state).
          2= movementVectorBinary:
              This method will set the movement time in a preset value, and no more or less, only if that much time
              is detected. For example:
              If it was moving for 1 second, and the time window in the training
              files set this module to detect at least 0.5 s, this method will detect movingTIme to 0.5 s
              If this method does not detect 0.5 s , it will set movingTime to 0 and idle time to 0
      Trial:
        Variables associated with trial movement detection, like the amount of time needed to consider
        a trial's sample as a valid 'movement'."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Tone 1:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Tone 1: </b> This Entry sets the Tone 1 Frequency in Hertz."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Tone 2:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Tone 2: </b> This Entry sets the Tone 2 Frequency in Hertz."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Test:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Test: </b> Saves Frequency changes in the corresponding Tone and tests it."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Show / Hide Tracking:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Show / Hide Tracking: </b> Shows or Hides tracking lines, circles, and other
    shapes that helps visually in the movement detection interpretation.
    Note that hiding the Tracking lines won't affect movement detection functionality."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Show / Hide Feedback:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Show / Hide Feedback: </b> Shows or Hides the Feedback Window (camera or video window).
    Note that hiding the Feedback window won't affect movement detection functionality."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Recalibrate Camera:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Recalibrate Camera: </b> Grabs current video sample and uses it to adjust maximum and minimum
values for the tracking function according to this new sample.
The calibration file is used to determine maximum and minimum radius allowed for valid circles.
If Noise Filtering is enabled, the minimum allowed radius will be the smallest possible,
therefore allowing more precise movement detection.
(enable noise filtering only if your video input has no or very little noise)
This will also overwrite previous calibration file with the new values."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Movement Amount:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Movement Amount: </b> Sets the amount of 'movement' needed in a given frame of the movement detection
    module to consider this sample a valid 'movement' (or idle according to type of trial).
    This value is dependent on the camera, the processing capabilities,and the method used for detection."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Method Used:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Method Used: </b> Sets the method used for movement and idle detection.
    Currently 3 methods are available (read docs above)."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Movement Time:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Movement Time: </b> Sets the movement time needed for a 'movement type' trial to be successful."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Idle Time:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Idle Time: </b> Sets the idle time needed for a 'idle type' trial to be successful."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            Tkinter.Label(self.frame, text="Apply:", borderwidth="1", 
                         relief="solid").grid(row=rowcount, column=0)
            TEXTO = """<b>Apply: </b> This button applies all changes made to the variables."""
            Tkinter.Label(self.frame, text=TEXTO).grid(row=rowcount, column=1)
            #----
            rowcount += 2
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=0) #empty space 0
            Tkinter.Label(self.frame, text="", background=self.DefClr).grid(row=rowcount-1, column=1) #empty space 1
            #for row in range(100):
            #    Label(self.frame, text="%s" % row, width=3, borderwidth="1", 
            #             relief="solid").grid(row=row, column=0)
            #    t="this is the second colum for row %s" %row
            #    Label(self.frame, text=t).grid(row=row, column=1)
            pass
    
        def calculateBestSize(self):
            screen_width = self.frame.winfo_screenwidth()
            screen_height = self.frame.winfo_screenheight()
            
            #print screen_width
            #print screen_height
            
            #print ".."
            bestWidth = 0
            
            if (screen_width < 800):
                bestWidth = 500
                
            if (screen_width > 800):
                bestWidth = 800
            
            if (screen_width > 1000):
                bestWidth = 900
            
            bestHeight = 0
            
            if (screen_height < 550):
                bestHeight = 350
                
            if (screen_height > 550):
                bestHeight = 550
            
            if (screen_height > 650):
                bestHeight = 680
            
            #print self.root.winfo_width()
            #print self.root.winfo_height()
            
            #print self.frame.winfo_reqwidth()
            #print self.frame.winfo_reqheight()
            
            self.root.geometry("%dx%d" % (bestWidth,bestHeight) )
            pass
    
        def OnFrameConfigure(self, event):
            '''Reset the scroll region to encompass the inner frame'''
            #for child in self.frame.winfo_children():
            #    child.destroy()
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            #print "onframeconfigure done."
            pass
    
        def oldfunction(self):
            #     if __name__ == "__main__":
            #         root=Tk()
            #         Form_help(root).pack(side="top", fill="both", expand=True)
            #         root.mainloop()
            pass
    
    
    
    def overrideaction_savestate(self):
        logger.info( "Default: Save State" )
        return 0
    
    def overrideaction_drop(self):
        logger.info( "Default: Drop" )
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
        logger.info( "Default: Start / Stop Training" )
        return 0
    
    
    def overrideaction_stopTraining(self):
        #NOT USED
        #print "Start / Stop training"
        logger.info( "Default: Stop Training" )
        return 0
    
    
    def overrideaction_pauseTraining(self):
        #print "Pause / Resume training"
        logger.info( "Default: Pause / Resume Training" )
        return 0
    
    
    def overrideaction_resumeTraining(self):
        #NOT USED
        #print "Pause / Resume training"
        logger.info( "Default: Resume Training" )
        return 0
    
    
    def overrideaction_applyTE(self):
        logger.info( "Default: Apply Trials Events" )
        return 0
    
    
    def overrideaction_applyP(self):
        logger.info( "Default: Apply Parameters" )
        return 0
    
    
    def overrideaction_applyC(self):
        logger.info( "Default: Apply Comments" )
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
    
    def overrideaction_noisefiltering(self):
            logger.info( "Default: set camera noise filtering" )
            pass
    
    def overrideaction_testT1(self):
        logger.info( "Default: Test T1" )
        return 0
    
    
    def overrideaction_testT2(self):
        logger.info( "Default: Test T2" )
        return 0




if __name__ == '__main__':
    # create a logging format
    dateformat = '%Y/%m/%d %H:%M:%S'
    formatter_str = '%(asctime)s.%(msecs)d - %(name)s - %(levelname)s - %(message)s'
    filename_to_log='logs'+os.sep+'userInterface_tk.log'
    
    
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
    
    logger.info('Start userInterface_tk Test')
    gtkobj = GUIGTK_Class()
    print "tk class instantiated."
    gtkobj.initAll()
    print "Tk interface started."