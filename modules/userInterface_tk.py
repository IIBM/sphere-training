#!/usr/bin/python

from Tkinter import *
import time
import sys
import os
import logging
logger = logging.getLogger('userInterface_tk')
#------------------------------------------------------------------------------#
#                                                                              #
#                                    Form1                                     #
#                                                                              #
#------------------------------------------------------------------------------#


class GUIGTK_Class:
    
    
    def __init__(self):
            self.customVariablesInit()
            import threading
            print "Initializing GUI GTK class."
            self.thread0 = threading.Thread(target=self.startFrame0 , name="Frame0")
            self.thread0.start()
            
            self.thread1 = threading.Thread(target=self.startFrame1 , name="Frame1")
            time.sleep(0.25)
            self.thread1.start()
            
            self.thread3 = threading.Thread(target=self.startFrame3 , name="Frame3")
            time.sleep(0.25)
            self.thread3.start()
            
            self.thread5 = threading.Thread(target=self.startFrame5 , name="Frame5")
            time.sleep(0.25) #i can swear without this delay it won't work properly
            self.thread5.start()
            print "GUI GTK class initialized."
            #startFrame1()
            pass
    
    def customVariablesInit(self):
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
        self.comment = ""
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
        self.AppFrm1.configureData()
        self.AppFrm3.configureData()
        self.AppFrm5.configureData()
        print "    Done with configuration of initial data to GUI"
        logger.info("    Done with configuration of initial data to GUI")
        
        pass
    
    def startFrame0(self):
        Root = Tk()
        import Tkinter
        
        del Tkinter
        self.App = self.userInput(Root)
        self.App.pack(expand='yes',fill='both')
        self.App.reference = self
        Root.geometry('480x240+10+10')
        Root.title('tk GUI Main Frame.')
        Root.mainloop()
        while True:
            time.sleep(1.0)
        pass
    
    def startFrame1(self):
        import Tkinter
        Root2 = Tkinter.Tk()
        Root2.withdraw()
        
        del Tkinter
        
        self.AppFrm1 = self.Form1(Root2)
        #AppFrm1.gVariables = gVariables
        #AppFrm1.configureData()
        #App.pack(expand='yes', fill='both')
        #App.gVariables = gVariables
        self.AppFrm1.protocol('WM_DELETE_WINDOW', self.App.hideForm1)
        self.AppFrm1.reference = self
        #gVariables.AppFrm1.geometry('640x480+10+10')
        self.AppFrm1.title('Trial Events.')
        self.AppFrm1.withdraw()
        self.AppFrm1.mainloop()
        while True:
            time.sleep(1.0)
        pass
    
    def startFrame3(self):
        import Tkinter
        Root = Tkinter.Tk()
        Root.withdraw()
        
        del Tkinter
        
        self.AppFrm3 = self.Form3(Root)
        #AppFrm1.gVariables = gVariables
        #AppFrm1.configureData()
        #App.pack(expand='yes', fill='both')
        #App.gVariables = gVariables
        self.AppFrm3.protocol('WM_DELETE_WINDOW', self.App.hideForm3)
        self.AppFrm3.reference = self
        #gVariables.AppFrm1.geometry('640x480+10+10')
        self.AppFrm3.title('Parameters.')
        self.AppFrm3.withdraw()
        self.AppFrm3.mainloop()
        while True:
            time.sleep(1.0)
        pass
    
    def startFrame5(self):
        import Tkinter
        Root = Tkinter.Tk()
        Root.withdraw()
        
        del Tkinter
        self.AppFrm5 = self.Form5(Root)
        self.AppFrm5.reference = self
        #AppFrm1.gVariables = gVariables
        #AppFrm1.configureData()
        #App.pack(expand='yes', fill='both')
        #App.gVariables = gVariables
        self.AppFrm5.protocol('WM_DELETE_WINDOW', self.App.hideForm5)
        
        #gVariables.AppFrm1.geometry('640x480+10+10')
        self.AppFrm5.title('Comment.')
        self.AppFrm5.withdraw()
        self.AppFrm5.mainloop()
        while True:
            time.sleep(1.0)
        pass
    
    def exit_all(self):
        logger.info('Exiting userInterface_tk')
        print "from GUITK"
        os._exit(0)
    
    class Empty_cl():
        #Used to save our variables' previous states.
        def __init__(self):
            pass
    
    class userInput(Frame):
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
            apply(Frame.__init__,(self,Master),kw)
            self.bind('<Destroy>',self.__on_userInput_Dstry)
            self.__Frame2 = Frame(self)
            self.__Frame2.pack(side='left')
            self.__Frame1 = Frame(self)
            self.__Frame1.pack(side='left')
            self.__Frame5 = Frame(self.__Frame2)
            self.__Frame5.pack(side='top')
            self.__Frame4 = Frame(self.__Frame2)
            self.__Frame4.pack(side='top')
            self.__Frame8 = Frame(self.__Frame1)
            self.__Frame8.pack(side='top')
            self.__Frame7 = Frame(self.__Frame1,height=30)
            self.__Frame7.pack(side='top')
            self.__Frame13 = Frame(self.__Frame1)
            self.__Frame13.pack(side='top')
            self.__btnFrmTrialEvents = Button(self.__Frame13
                ,text='Edit Trial Events')
            self.__btnFrmTrialEvents.pack(side='top')
            self.__btnFrmTrialEvents.bind('<ButtonRelease-1>' \
                ,self.__on_btnFrmTrialEvents_ButRel_1)
            self.__Frame9 = Frame(self.__Frame1,height=15,width=15)
            self.__Frame9.pack(side='top')
            self.__Frame16 = Frame(self.__Frame1)
            self.__Frame16.pack(side='top')
            self.__btnFrmEditParameters = Button(self.__Frame16
                ,text='Edit Parameters')
            self.__btnFrmEditParameters.pack(side='top')
            self.__btnFrmEditParameters.bind('<ButtonRelease-1>' \
                ,self.__on_btnFrmEditParameters_ButRel_1)
            self.__Frame15 = Frame(self.__Frame1,height=5)
            self.__Frame15.pack(side='top')
            self.__Frame14 = Frame(self.__Frame1)
            self.__Frame14.pack(side='top')
            self.__Text1KeyInput = Text(self.__Frame14,background='#f3f3f3',height=5
                ,relief='groove',state='disabled',width=30)
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
            self.__Frame3 = Frame(self.__Frame5)
            self.__Frame3.pack(side='left')
            self.__Frame6 = Frame(self.__Frame5,takefocus=1,width=80)
            self.__Frame6.pack(side='left')
            self.__Frame23 = Frame(self.__Frame8)
            self.__Frame23.pack(side='left')
            self.__btnComment = Button(self.__Frame23
                ,text='Comment about this training')
            self.__btnComment.pack(side='top')
            self.__btnComment.bind('<ButtonRelease-1>' \
                ,self.__on_btnComment_ButRel_1)
            self.__Frame24 = Frame(self.__Frame8,width=10)
            self.__Frame24.pack(side='left')
            self.__Frame10 = Frame(self.__Frame3)
            self.__Frame10.pack(side='top')
            self.__btnDrop = Button(self.__Frame10,text='Drop')
            self.__btnDrop.pack(side='top')
            self.__btnDrop.bind('<ButtonRelease-1>',self.__on_btnDrop_ButRel_1)
            self.__Frame20 = Frame(self.__Frame3)
            self.__Frame20.pack(side='top')
            self.__btnReward = Button(self.__Frame20,text='Reward')
            self.__btnReward.pack(side='top')
            self.__btnReward.bind('<ButtonRelease-1>',self.__on_btnReward_ButRel_1)
            self.__Frame12 = Frame(self.__Frame3)
            self.__Frame12.pack(side='top')
            self.__btnOpen = Button(self.__Frame12,text='Open Valve')
            self.__btnOpen.pack(side='top')
            self.__btnOpen.bind('<ButtonRelease-1>',self.__on_btnOpen_ButRel_1)
            self.__Frame17 = Frame(self.__Frame3)
            self.__Frame17.pack(side='top')
            self.__btnClose = Button(self.__Frame17,text='Close Valve')
            self.__btnClose.pack(side='top')
            self.__btnClose.bind('<ButtonRelease-1>',self.__on_btnClose_ButRel_1)
            self.__Frame11 = Frame(self.__Frame3)
            self.__Frame11.pack(side='top')
            self.__btnStart = Button(self.__Frame11,text='Start / Stop Training')
            self.__btnStart.pack(side='top')
            self.__btnStart.bind('<ButtonRelease-1>',self.__on_btnStart_ButRel_1)
            self.__Frame21 = Frame(self.__Frame3)
            self.__Frame21.pack(side='top')
            self.__btnPause = Button(self.__Frame21,text='Pause / Resume Training')
            self.__btnPause.pack(side='top')
            self.__btnPause.bind('<ButtonRelease-1>',self.__on_btnPause_ButRel_1)
            self.__Frame19 = Frame(self.__Frame3)
            self.__Frame19.pack(side='top')
    #         self.__btnResume = Button(self.__Frame19,text='Resume Training')
    #         self.__btnResume.pack(side='top')
    #         self.__btnResume.bind('<ButtonRelease-1>',self.__on_btnResume_ButRel_1)
            self.__Frame22 = Frame(self.__Frame3)
            self.__Frame22.pack(side='top')
    #         self.__btnStop = Button(self.__Frame22,text='Stop Training')
    #         self.__btnStop.pack(side='top')
    #         self.__btnStop.bind('<ButtonRelease-1>',self.__on_btnStop_ButRel_1)
            self.__Frame18 = Frame(self.__Frame3)
            self.__Frame18.pack(side='top')
            self.__btnExit = Button(self.__Frame18,text='Exit')
            self.__btnExit.pack(side='top')
            self.__btnExit.bind('<ButtonRelease-1>',self.__on_btnExit_ButRel_1)
            #
            #Your code here
            #
            self.__alive = 0
            self.__Text1KeyInput.focus_set()
            print "Main User Input Form loaded"
            pass
        
        
        def hideForm1(self, toHide = True):
            print "Hide Form 1."
            #a = gVariables.AppFrm1.__Entry3MvmntWindowStart.get() 
            if (toHide == True):
                self.reference.AppFrm1.withdraw()
                return;
            #GUIGTK_Class.AppFrm1.get_changes()
            
            print "Reading variables "
            a = self.reference.AppFrm1.var1_TStart #tone duration
            b = self.reference.AppFrm1.var2_TEnd
            c = self.reference.AppFrm1.var3_MWS
            d = self.reference.AppFrm1.var4_MWE
            e = self.reference.AppFrm1.var5_ITStart #changed to intertrial random1 time
            f = self.reference.AppFrm1.var6_ITEnd #changed to intertrial random2 time
            g = self.reference.AppFrm1.var7_Probab1
            print a
            print b
            print c
            print d
            print e
            print f
            print g
            self.reference.toneStart = a
            self.reference.toneEnd = b
            self.reference.movementWindowStart = c
            self.reference.movementWindowEnd = d
            self.reference.interTrialStart = e
            self.reference.interTrialEnd = f
            self.reference.probabilityToneOne = g
        
        def hideForm3(self, toHide = True):
            print "Hide Form 3."
            
            if (toHide == True):
                self.reference.AppFrm3.withdraw()
                return;
            
            #GUIGTK_Class.AppFrm3.get_changes()
            
            print "Reading variables "
            a = self.reference.AppFrm3.var1_T1
            b = self.reference.AppFrm3.var2_T2
            c = self.reference.AppFrm3.var3_MA
            d = self.reference.AppFrm3.var4_MT
            e = self.reference.AppFrm3.var5_IT
            f = self.reference.AppFrm3.var6_ShowTracking
            g = self.reference.AppFrm3.var7_ShowFeedback
            h = self.reference.AppFrm3.var8_num_selected
            print a
            print b
            print c
            print d
            print e
            print f
            print g
            print h
            self.reference.frequencyTone1 = a
            self.reference.frequencyTone2 = b
            self.reference.movementAmount = c
            self.reference.movementMethod = h
            self.reference.movementTime = d
            self.reference.idleTime = e
            
            if (toHide == True):
                self.reference.AppFrm3.withdraw()
        
        def hideForm5(self, toHide = True):
            print "Hide Form 5."
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
            print "Showing Frame 1: Trial Events"
            pass
        
        def showFrame3(self):
            logger.info( "Parameters frame shown." )
            self.reference.AppFrm3.saveParametersPreviousState()
            self.reference.AppFrm3.deiconify()
            print "Showing Frame 3: Parameters"
        
        def showFrame5(self):
            self.reference.AppFrm5.deiconify()
            print "Showing Frame 5"
        
    
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
    
    
    
    
    class Form5(Toplevel):
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
            apply(Toplevel.__init__,(self,Master),kw)
            self.bind('<Destroy>',self.__on_Form5_Dstry)
            self.__lblComment = Label(self,text='Comment about this training:')
            self.__lblComment.pack(side='top')
            self.__EntryComment = Entry(self)
            self.__EntryComment.pack(side='top')
            self.__EntryComment.bind('<KeyRelease>',self.__on_EntryComment_KeyRel)
            
            self.__Frame62 = Frame(self,height=30,width=30)
            self.__Frame62.pack(side='top')
            self.__ApplyBtn = Button(self.__Frame62,text='Apply')
            self.__ApplyBtn.pack(side='top')
            self.__ApplyBtn.bind('<ButtonRelease-1>',self.__on_ApplyBtn_ButRel_1)
            #
            #Your code here
            self.__alreadyGone = 0
            self.__CommentString = ""
            self.get_changes()
            print "Form5: Comment Frame loaded"
        
        
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
            print "configuring initial data for Form5."
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
    
    
    
    class Form3(Toplevel):
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
    
            apply(Toplevel.__init__,(self,Master),kw)
            self.bind('<Destroy>',self.__on_Form3_Dstry)
            self.__Frame6 = Frame(self)
            self.__Frame6.pack(side='left')
            self.__Frame5 = Frame(self)
            self.__Frame5.pack(side='left')
            self.__Frame69 = Frame(self.__Frame6,width=10)
            self.__Frame69.pack(side='top')
            self.__Frame68 = Frame(self.__Frame6,width=10)
            self.__Frame68.pack(side='top')
            self.__Frame70 = Frame(self.__Frame5)
            self.__Frame70.pack(side='top')
            self.__Frame2 = Frame(self.__Frame5,height=5,width=15)
            self.__Frame2.pack(side='top')
            self.__Frame1 = Frame(self.__Frame5)
            self.__Frame1.pack(side='top')
            self.__Frame14 = Frame(self.__Frame5,height=30,width=30)
            self.__Frame14.pack(side='top')
            self.__Frame42 = Frame(self.__Frame5)
            self.__Frame42.pack(side='top')
            self.__Frame25 = Frame(self.__Frame5,height=30,width=30)
            self.__Frame25.pack(side='top')
            self.__Frame43 = Frame(self.__Frame5)
            self.__Frame43.pack(side='top')
            self.__Frame62 = Frame(self.__Frame5,height=30,width=30)
            self.__Frame62.pack(side='top')
            self.__ApplyBtn = Button(self.__Frame62,text='Apply')
            self.__ApplyBtn.pack(side='top')
            self.__ApplyBtn.bind('<ButtonRelease-1>',self.__on_ApplyBtn_ButRel_1)
            self.__CloseBtn = Button(self.__Frame62,text='Close')
            self.__CloseBtn.pack(side='top')
            self.__CloseBtn.bind('<ButtonRelease-1>',self.__on_CloseBtn_ButRel_1)
            self.__Frame4 = Frame(self.__Frame70,height=30)
            self.__Frame4.pack(side='left')
            self.__Label1 = Label(self.__Frame4,text='Parameters')
            self.__Label1.pack(side='top')
            self.__Frame3 = Frame(self.__Frame70,height=30,width=250)
            self.__Frame3.pack(side='left')
            self.__Frame7 = Frame(self.__Frame1,width=20)
            self.__Frame7.pack(side='left')
            self.__Frame8 = Frame(self.__Frame1)
            self.__Frame8.pack(side='left')
            self.__Frame27 = Frame(self.__Frame42,width=20)
            self.__Frame27.pack(side='left')
            self.__Frame26 = Frame(self.__Frame42)
            self.__Frame26.pack(side='left')
            self.__Frame45 = Frame(self.__Frame43)
            self.__Frame45.pack(side='left')
            self.__Frame44 = Frame(self.__Frame43)
            self.__Frame44.pack(side='left')
            self.__Frame9 = Frame(self.__Frame8)
            self.__Frame9.pack(side='top')
            self.__Label2 = Label(self.__Frame9,text='Audio:')
            self.__Label2.pack(side='top')
            self.__Frame16 = Frame(self.__Frame8)
            self.__Frame16.pack(side='top')
            self.__Frame15 = Frame(self.__Frame8)
            self.__Frame15.pack(side='top')
            self.__Frame10 = Frame(self.__Frame8)
            self.__Frame10.pack(side='top')
            self.__Frame22 = Frame(self.__Frame8)
            self.__Frame22.pack(side='top')
            self.__Frame71 = Frame(self.__Frame27)
            self.__Frame71.pack(side='top')
            self.__Frame72 = Frame(self.__Frame27)
            self.__Frame72.pack(side='top')
            self.__Frame29 = Frame(self.__Frame26)
            self.__Frame29.pack(side='top')
            self.__Label7 = Label(self.__Frame29,text='Video:')
            self.__Label7.pack(side='top')
            self.__Frame28 = Frame(self.__Frame26)
            self.__Frame28.pack(side='top')
            self.__Frame35 = Frame(self.__Frame26)
            self.__Frame35.pack(side='top')
            self.__Frame46 = Frame(self.__Frame44)
            self.__Frame46.pack(side='top')
            self.__Label10 = Label(self.__Frame46,text='Trial:')
            self.__Label10.pack(side='top')
            self.__Frame47 = Frame(self.__Frame44)
            self.__Frame47.pack(side='top')
            self.__Frame17 = Frame(self.__Frame16)
            self.__Frame17.pack(side='left')
            self.__Label3 = Label(self.__Frame17,text='Tone1:')
            self.__Label3.pack(side='top')
            self.__Frame18 = Frame(self.__Frame16,width=100)
            self.__Frame18.pack(side='left')
            self.__Frame11 = Frame(self.__Frame15)
            self.__Frame11.pack(side='left')
            self.__Entry1Tone1 = Entry(self.__Frame11,width=8)
            self.__Entry1Tone1.pack(side='top')
            self.__Frame13 = Frame(self.__Frame15)
            self.__Frame13.pack(side='left')
            self.__Label4 = Label(self.__Frame13,text='Hz')
            self.__Label4.pack(side='top')
            self.__Frame12 = Frame(self.__Frame15)
            self.__Frame12.pack(side='left')
            self.__Button1TestT1 = Button(self.__Frame12,text='Test')
            self.__Button1TestT1.pack(side='top')
            self.__Button1TestT1.bind('<ButtonRelease-1>' \
                ,self.__on_Button1TestT1_ButRel_1)
            self.__Frame23 = Frame(self.__Frame10)
            self.__Frame23.pack(side='left')
            self.__Label6 = Label(self.__Frame23,text='Tone2:')
            self.__Label6.pack(side='top')
            self.__Frame24 = Frame(self.__Frame10,width=100)
            self.__Frame24.pack(side='left')
            self.__Frame19 = Frame(self.__Frame22)
            self.__Frame19.pack(side='left')
            self.__Entry2Tone2 = Entry(self.__Frame19,width=8)
            self.__Entry2Tone2.pack(side='top')
            self.__Frame20 = Frame(self.__Frame22)
            self.__Frame20.pack(side='left')
            self.__Label5 = Label(self.__Frame20,text='Hz')
            self.__Label5.pack(side='top')
            self.__Frame21 = Frame(self.__Frame22)
            self.__Frame21.pack(side='left')
            self.__Button2TestT2 = Button(self.__Frame21,text='Test')
            self.__Button2TestT2.pack(side='top')
            self.__Button2TestT2.bind('<ButtonRelease-1>' \
                ,self.__on_Button2TestT2_ButRel_1)
            self.__Frame32 = Frame(self.__Frame28)
            self.__Frame32.pack(side='left')
            self.__Frame31 = Frame(self.__Frame28,width=100)
            self.__Frame31.pack(side='left')
            self.__Frame48 = Frame(self.__Frame47)
            self.__Frame48.pack(side='left')
            self.__Frame49 = Frame(self.__Frame47,width=50)
            self.__Frame49.pack(side='left')
            self.__Frame33 = Frame(self.__Frame32)
            self.__Frame33.pack(side='top')
            self.__Frame30 = Frame(self.__Frame32)
            self.__Frame30.pack(side='top')
            self.__Frame36 = Frame(self.__Frame32)
            self.__Frame36.pack(side='top')
            self.__Frame34 = Frame(self.__Frame32)
            self.__Frame34.pack(side='top')
            self.__Frame52 = Frame(self.__Frame48)
            self.__Frame52.pack(side='top')
            self.__Frame51 = Frame(self.__Frame48)
            self.__Frame51.pack(side='top')
            self.__Frame50 = Frame(self.__Frame48)
            self.__Frame50.pack(side='top')
            self.__Frame67 = Frame(self.__Frame33)
            self.__Frame67.pack(side='left')
            self.__Button3SHTracking = Button(self.__Frame67
                ,text='Show / HideTracking')
            self.__Button3SHTracking.pack(side='top')
            self.__Button3SHTracking.bind('<ButtonRelease-1>' \
                ,self.__on_Button3SHTracking_ButRel_1)
            self.__Frame66 = Frame(self.__Frame33,width=39)
            self.__Frame66.pack(side='left')
            self.__Frame65 = Frame(self.__Frame30)
            self.__Frame65.pack(side='left')
            self.__Button4SHFeedback = Button(self.__Frame65
                ,text='Show / Hide Feedback')
            self.__Button4SHFeedback.pack(side='top')
            self.__Button4SHFeedback.bind('<ButtonRelease-1>' \
                ,self.__on_Button4SHFeedback_ButRel_1)
            self.__Frame64 = Frame(self.__Frame30,width=39)
            self.__Frame64.pack(side='left')
            self.__Frame38 = Frame(self.__Frame36)
            self.__Frame38.pack(side='left')
            self.__Label8 = Label(self.__Frame38,text='Movement Amount:')
            self.__Label8.pack(side='top')
            self.__Frame37 = Frame(self.__Frame36)
            self.__Frame37.pack(side='left')
            self.__Entry3MvntAm = Entry(self.__Frame37,width=6)
            self.__Entry3MvntAm.pack(side='top')
            self.__Frame63 = Frame(self.__Frame36,width=39)
            self.__Frame63.pack(side='left')
            self.__Frame39 = Frame(self.__Frame34)
            self.__Frame39.pack(side='left')
            self.__Label9 = Label(self.__Frame39,text='Method Used:')
            self.__Label9.pack(side='top')
            self.__Frame41 = Frame(self.__Frame34)
            self.__Frame41.pack(side='left')
            #self.__Listbox1 = Listbox(self.__Frame41,height=1,width=19)
            pass
            #self.__Listbox1.pack(side='top')
            #
            self.__EntryMethodUsed = Entry(self.__Frame41,width=6)
            self.__EntryMethodUsed.pack(side='top')
            #
            self.__Frame40 = Frame(self.__Frame34)
            self.__Frame40.pack(side='left')
            pass
            #self.__Button5 = Button(self.__Frame40,text='Apply')
            #self.__Button5.pack(side='left')
            #self.__Button5.bind('<ButtonRelease-1>',self.__on_Button5_ButRel_1)
            pass
            self.__Frame53 = Frame(self.__Frame52)
            self.__Frame53.pack(side='left')
            self.__Label11 = Label(self.__Frame53,text='Movement Time:')
            self.__Label11.pack(side='top')
            self.__Frame54 = Frame(self.__Frame52)
            self.__Frame54.pack(side='left')
            self.__Entry4MvntTime = Entry(self.__Frame54,width=10)
            self.__Entry4MvntTime.pack(side='top')
            self.__Frame56 = Frame(self.__Frame52,width=2)
            self.__Frame56.pack(side='left')
            self.__Frame55 = Frame(self.__Frame52)
            self.__Frame55.pack(side='left')
            self.__Label12 = Label(self.__Frame55,text='s.')
            self.__Label12.pack(side='top')
            self.__Frame57 = Frame(self.__Frame51)
            self.__Frame57.pack(side='left')
            self.__Label13 = Label(self.__Frame57,text='Idle Time:')
            self.__Label13.pack(side='top')
            self.__Frame61 = Frame(self.__Frame51,width=40)
            self.__Frame61.pack(side='left')
            self.__Frame60 = Frame(self.__Frame51)
            self.__Frame60.pack(side='left')
            self.__Entry5IdleTime = Entry(self.__Frame60,width=10)
            self.__Entry5IdleTime.pack(side='top')
            self.__Frame59 = Frame(self.__Frame51,width=2)
            self.__Frame59.pack(side='left')
            self.__Frame58 = Frame(self.__Frame51)
            self.__Frame58.pack(side='left')
            self.__Label14 = Label(self.__Frame58,text='s.')
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
            print "Form3: Parameters loaded"
        
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
            print "configuring initial data for Form3."
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
            
            
            self.reference.App.showFrame3()
            self.reference.AppFrm3.withdraw()
            
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
            print "Parameters: Previous states saved."
            pass
        
        def get_changes(self):
            #Raw input data.
            print "commiting changes to variables in Form 3.."
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
    
    
    
    class Form1(Toplevel):
        def __init__(self,Master=None,**kw):
            kw['class_'] = 'Frame'
            #
            #Your code here
            #FORM: Trial Events
            apply(Toplevel.__init__,(self,Master),kw)
            self.bind('<Destroy>',self.__on_Form1_Dstry)
            self.__Frame2 = Frame(self)
            self.__Frame2.pack(side='left')
            self.__Frame1 = Frame(self)
            self.__Frame1.pack(side='left')
            self.__Frame4 = Frame(self.__Frame2)
            self.__Frame4.pack(side='top')
            self.__Frame3 = Frame(self.__Frame2)
            self.__Frame3.pack(side='top')
            self.__Frame5 = Frame(self.__Frame4)
            self.__Frame5.pack(side='left')
            self.__Frame6 = Frame(self.__Frame4,width=50)
            self.__Frame6.pack(side='left')
            self.__Frame7 = Frame(self.__Frame3)
            self.__Frame7.pack(side='left')
            self.__Frame8 = Frame(self.__Frame3)
            self.__Frame8.pack(side='left')
            self.__Frame21 = Frame(self.__Frame3)
            self.__Frame21.pack(side='left')
            self.__Frame9 = Frame(self.__Frame5)
            self.__Frame9.pack(side='top')
            self.__lblTrialEventsTitle = Label(self.__Frame9,text='Trial Events')
            self.__lblTrialEventsTitle.pack(side='top')
            self.__Frame10 = Frame(self.__Frame5)
            self.__Frame10.pack(side='top')
            self.__Frame14 = Frame(self.__Frame7,height=66)
            self.__Frame14.pack(side='top')
            self.__Frame15 = Frame(self.__Frame7)
            self.__Frame15.pack(side='top')
            self.__Frame13 = Frame(self.__Frame7)
            self.__Frame13.pack(side='top')
            self.__Frame20 = Frame(self.__Frame7)
            self.__Frame20.pack(side='top')
            self.__Frame17 = Frame(self.__Frame7)
            self.__Frame17.pack(side='top')
            self.__Frame16 = Frame(self.__Frame7)
            self.__Frame16.pack(side='top')
            self.__Frame19 = Frame(self.__Frame7)
            self.__Frame19.pack(side='top')
            self.__Frame36 = Frame(self.__Frame7)
            self.__Frame36.pack(side='top')
            self.__Frame18 = Frame(self.__Frame7)
            self.__Frame18.pack(side='top')
            self.__Frame38 = Frame(self.__Frame7)
            self.__Frame38.pack(side='top')
            self.__ApplyBtn = Button(self.__Frame38,text='Apply')
            self.__ApplyBtn.pack(side='top')
            self.__ApplyBtn.bind('<ButtonRelease-1>',self.__on_ApplyBtn_ButRel_1)
            self.__CloseBtn = Button(self.__Frame38,text='Close')
            self.__CloseBtn.pack(side='top')
            self.__CloseBtn.bind('<ButtonRelease-1>',self.__on_CloseBtn_ButRel_1)
            self.__Frame37 = Frame(self.__Frame7)
            self.__Frame37.pack(side='top')
            self.__Frame11 = Frame(self.__Frame10,width=80)
            self.__Frame11.pack(side='left')
            self.__Frame12 = Frame(self.__Frame10)
            self.__Frame12.pack(side='left')
    #         self.__Scale1 = Scale(self.__Frame12,length=200,orient='horizontal'
    #             ,sliderlength=20)
    #         self.__Scale1.pack(side='top')
            self.__Frame24 = Frame(self.__Frame15)
            self.__Frame24.pack(side='left')
            self.__Label1 = Label(self.__Frame24,text='Tone Start:')
            self.__Label1.pack(side='top')
            self.__Frame25 = Frame(self.__Frame15)
            self.__Frame25.pack(side='left')
            self.__Entry1TStart = Entry(self.__Frame25,width=5)
            self.__Entry1TStart.pack(side='top')
            self.__Frame27 = Frame(self.__Frame13)
            self.__Frame27.pack(side='left')
            self.__Label2 = Label(self.__Frame27,text='Tone End:')
            self.__Label2.pack(side='top')
            self.__Frame26 = Frame(self.__Frame13)
            self.__Frame26.pack(side='left')
            self.__Entry2TEnd = Entry(self.__Frame26,width=5)
            self.__Entry2TEnd.pack(side='top')
            self.__Frame28 = Frame(self.__Frame20)
            self.__Frame28.pack(side='left')
            self.__Label3 = Label(self.__Frame28,text='Movement Window Start:')
            self.__Label3.pack(side='top')
            self.__Frame29 = Frame(self.__Frame20)
            self.__Frame29.pack(side='left')
            self.__Entry3MvmntWindowStart = Entry(self.__Frame29,width=5)
            self.__Entry3MvmntWindowStart.pack(side='top')
            self.__Frame30 = Frame(self.__Frame17)
            self.__Frame30.pack(side='left')
            self.__Label4 = Label(self.__Frame30,text='Movement Window End:')
            self.__Label4.pack(side='top')
            self.__Frame31 = Frame(self.__Frame17)
            self.__Frame31.pack(side='left')
            self.__Entry4MvntWindowEnd = Entry(self.__Frame31,width=5)
            self.__Entry4MvntWindowEnd.pack(side='top')
            self.__Frame33 = Frame(self.__Frame16)
            self.__Frame33.pack(side='left')
            self.__Label5 = Label(self.__Frame33,text='InterTrial Start:')
            self.__Label5.pack(side='top')
            self.__Frame32 = Frame(self.__Frame16)
            self.__Frame32.pack(side='left')
            self.__Entry5ITStart = Entry(self.__Frame32,width=5)
            self.__Entry5ITStart.pack(side='top')
            self.__Frame35 = Frame(self.__Frame19)
            self.__Frame35.pack(side='left')
            self.__Label6 = Label(self.__Frame35,text='InterTrial End:')
            self.__Label6.pack(side='top')
            self.__Frame34 = Frame(self.__Frame19)
            self.__Frame34.pack(side='left')
            self.__Entry6ITEnd = Entry(self.__Frame34,width=5)
            self.__Entry6ITEnd.pack(side='top')
            self.__Frame22 = Frame(self.__Frame36)
            self.__Frame22.pack(side='left')
            self.__Label7 = Label(self.__Frame22,text='Probability Tone1:')
            self.__Label7.pack(side='top')
            self.__Frame23 = Frame(self.__Frame36)
            self.__Frame23.pack(side='left')
            self.__Scale2 = Scale(self.__Frame23,orient='horizontal')
            self.__Scale2.pack(side='top')
            #
            #Your code here
            
            self.__alreadyExecuted = 0
            self.__Entry1TStart.insert(0,"0.0")
            self.__Entry2TEnd.insert(0,"0.0")
            self.__Entry3MvmntWindowStart.insert(0,"0.0")
            self.__Entry4MvntWindowEnd.insert(0,"0.0")
            self.__Entry5ITStart.insert(0,"0.0")
            self.__Entry6ITEnd.insert(0,"0.0")
            self.__Scale2.set(50)
            
            self.get_changes()
            print "Form1: Trial Events loaded"
        
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
            print "configuring initial data for Form1."
            
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
        
        def get_changes(self):
            print "commiting changes to variables in Form 1.."
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
            
            print "Trial Events: Previous states saved."
            pass
        
        def checkTrialEventsVarsConsistency(self):
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
    
    
    def overrideaction_drop(self):
        print "DROP from UI_TK"
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
    
    
    def overrideaction_testT1(self):
        logger.info( "Default: Test T1" )
        return 0
    
    
    def overrideaction_testT2(self):
        logger.info( "Default: Test T2" )
        return 0




if __name__ == '__main__':
    # create a logging format
    formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    dateformat = '%Y/%m/%d %I:%M:%S %p'
    
    logging.basicConfig(filename='logs/userInterface_tk.log', filemode='w',
        level=logging.DEBUG, format=formatter, datefmt = dateformat)
    logger.info('Start userInterface_tk Test')
    a = GUIGTK_Class()