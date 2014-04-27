#!/usr/bin/python

import rpErrorHandler
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
            import threading
            print "Initializing GUI GTK class."
            thread0 = threading.Thread(target=startFrame0 , name="Frame0")
            thread0.start()
            
            thread1 = threading.Thread(target=startFrame1 , name="Frame1")
            time.sleep(0.2)
            thread1.start()
            
            thread3 = threading.Thread(target=startFrame3 , name="Frame3")
            time.sleep(0.2)
            thread3.start()
            
            thread5 = threading.Thread(target=startFrame5 , name="Frame5")
            time.sleep(0.2)
            thread5.start()
            
            #startFrame1()
            pass
    
    @staticmethod
    def overrideaction_drop():
        logging.info( "Default: Drop" )
        return 0
    
    @staticmethod
    def overrideaction_reward():
        logging.info( "Default: Reward" )
        return 0
    
    @staticmethod
    def overrideaction_open():
        logging.info( "Default: Open" )
        return 0
    
    @staticmethod
    def overrideaction_close():
        logging.info( "Default: Close" )
        return 0
    
    @staticmethod
    def overrideaction_startTraining():
        #print "Start / Stop training"
        logging.info( "Default: Start / Stop Training" )
        return 0
    
    @staticmethod
    def overrideaction_stopTraining():
        #NOT USED
        #print "Start / Stop training"
        logging.info( "Default: Stop Training" )
        return 0
    
    @staticmethod
    def overrideaction_pauseTraining():
        #print "Pause / Resume training"
        logging.info( "Default: Pause / Resume Training" )
        return 0
    
    @staticmethod
    def overrideaction_resumeTraining():
        #NOT USED
        #print "Pause / Resume training"
        logging.info( "Default: Resume Training" )
        return 0
    
    @staticmethod
    def overrideaction_applyTE():
        logging.info( "Default: Apply Trials Events" )
        return 0
    
    @staticmethod
    def overrideaction_applyP():
        logging.info( "Default: Apply Parameters" )
        return 0
    
    @staticmethod
    def overrideaction_applyC():
        logging.info( "Default: Apply Comments" )
        return 0
    
    @staticmethod
    def overrideaction_showfeedback():
        logging.info( "Default: Show Feedback" )
        return 0
    
    @staticmethod
    def overrideaction_hidefeedback():
        logging.info( "Default: Hide Feedback" )
        return 0
    
    @staticmethod
    def overrideaction_showtracking():
        logging.info( "Default: Show Tracking" )
        return 0
    
    @staticmethod
    def overrideaction_hidetracking():
        logging.info( "Default: Hide Tracking" )
        return 0
    
    @staticmethod
    def overrideaction_testT1():
        logging.info( "Default: Test T1" )
        return 0
    
    @staticmethod
    def overrideaction_testT2():
        logging.info( "Default: Test T2" )
        return 0

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
        print "Form1: Trial Events loaded"
    #
    #Start of event handler methods
    #


    def __on_ApplyBtn_ButRel_1(self,Event=None):
        print "Test Apply Frm1"
        self.get_changes()
        GUIGTK_Class.App.hideForm1(False)
        GUIGTK_Class.overrideaction_applyTE()
        pass
    
    def __on_CloseBtn_ButRel_1(self,Event=None):
        GUIGTK_Class.App.hideForm1(True)
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
        prob = self.gVariables.toneOneProbability * 100
        self.__Scale2.set(int(prob))
        
        self.__Entry1TStart.delete(0,10) #removes 10 characters.
        self.__Entry1TStart.insert(0, self.gVariables.soundGenDuration1 )
        
        self.__Entry2TEnd.delete(0,10) #removes 10 characters.
        self.__Entry2TEnd.insert(0, self.gVariables.soundGenDuration2 )
        
        self.__Entry3MvmntWindowStart.delete(0,10) #removes 10 characters.
        self.__Entry3MvmntWindowStart.insert(0, self.gVariables.eventTime1_movement_start )
        
        self.__Entry4MvntWindowEnd.delete(0,10) #removes 10 characters.
        self.__Entry4MvntWindowEnd.insert(0, self.gVariables.eventTime2_movement )
        
        self.__Entry5ITStart.delete(0,10) #removes 10 characters.
        self.__Entry5ITStart.insert(0, self.gVariables.interTrialRandom1Time )
        
        self.__Entry6ITEnd.delete(0,10) #removes 10 characters.
        self.__Entry6ITEnd.insert(0, self.gVariables.interTrialRandom2Time )
    
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
        self.var7_Probab1 = self.__Scale2.get()
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
        print "Form3: Parameters loaded"
        #
    #
    #Start of event handler methods
    #

    def __on_CloseBtn_ButRel_1(self,Event=None):
        GUIGTK_Class.App.hideForm3(True)
        pass

    def __on_ApplyBtn_ButRel_1(self,Event=None):
        print "Test Apply Frm3"
        self.get_changes()
        GUIGTK_Class.App.hideForm3(False)
        GUIGTK_Class.overrideaction_applyP()
        pass
    
    def configureData(self):
        print "configuring initial data for Form3."
        self.__Entry1Tone1.delete(0,10) #removes 10 characters.
        freq1 = int(self.gVariables.soundGenFrequency1)
        self.__Entry1Tone1.insert(0, str(freq1))
        
        self.__Entry2Tone2.delete(0,10) #removes 10 characters.
        freq1 = int(self.gVariables.soundGenFrequency2)
        self.__Entry2Tone2.insert(0, str(freq1))
        
        
        self.__Entry3MvntAm.delete(0,10) #removes 10 characters.
        freq1 = int( self.gVariables.videoDet.getMovementThreshold() )
        self.__Entry3MvntAm.insert(0, str(freq1))
        
        self.__Entry4MvntTime.delete(0,10) #removes 10 characters.
        freq1 = float( self.gVariables.movementTime )
        self.__Entry4MvntTime.insert(0, str(freq1))
        
        self.__Entry5IdleTime.delete(0,10) #removes 10 characters.
        freq1 = float( self.gVariables.idleTime )
        self.__Entry5IdleTime.insert(0, str(freq1))
        
        #self.gVariables.videoMovementMethod
        
        pass

    def __on_Button1TestT1_ButRel_1(self,Event=None):
        print "Test Tone 1"
        GUIGTK_Class.overrideaction_testT1()
        pass

    def __on_Button2TestT2_ButRel_1(self,Event=None):
        print "Test Tone 2"
        GUIGTK_Class.overrideaction_testT2()
        pass

    def __on_Button3SHTracking_ButRel_1(self,Event=None):
        if ( self.__showTracking == 0):
            print "hiding tracking"
            self.__showTracking = 1
            GUIGTK_Class.overrideaction_hidetracking()
        elif ( self.__showTracking == 1):
            print "showing tracking"
            self.__showTracking = 0
            GUIGTK_Class.overrideaction_showtracking()
        pass

    def __on_Button4SHFeedback_ButRel_1(self,Event=None):
        if ( self.__showFeedback == 0):
            print "hiding feedback"
            self.__showFeedback = 1
            GUIGTK_Class.overrideaction_hidefeedback()
            
        elif ( self.__showFeedback == 1):
            print "showing feedback"
            self.__showFeedback = 0
            GUIGTK_Class.overrideaction_showfeedback()
        pass

    def __on_Button5_ButRel_1(self,Event=None):
        pass

    def __on_Form3_Dstry(self,Event=None):
        pass
    #
    #Start of non-Rapyd user code
    #
    def get_changes(self):
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
        self.var8_num_selected = -1
        tempnum = -1
        try:
            tempnum = self.__Listbox1.curselection()[0]
        except:
            pass
        if (tempnum != -1):
            self.var8_num_selected = tempnum


class Form5(Toplevel):
#------------------------------------------------------------------------------#
#                                                                              #
#                                    Form5                                     #
#                                                                              #
#------------------------------------------------------------------------------#
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
        print "Form5: Comment Frame loaded"
    
    
    def __on_ApplyBtn_ButRel_1(self,Event=None):
        self.get_changes()
        GUIGTK_Class.App.hideForm5(True)
        GUIGTK_Class.overrideaction_applyC()
        pass

    def __on_EntryComment_KeyRel(self,Event=None):
        self.commentStr = self.__EntryComment.get()
        #print self.__CommentString
        pass
    
    def configureData(self):
        print "configuring initial data for Form5."
        self.__EntryComment.delete(0,30)
        tempstr = self.gVariables.trial_comment
        self.__EntryComment.insert(0,tempstr)
        pass
    
    def get_changes(self):
        try:
            self.commentStr = unicode(self.__EntryComment.get(), "utf-8")
        except:
            self.commentStr = self.__EntryComment.get()
    
    def __on_Form5_Dstry(self,Event=None):
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
    
    
    @staticmethod
    def hideForm1(toHide = True):
        print "Hide Form 1."
        #a = gVariables.AppFrm1.__Entry3MvmntWindowStart.get() 
        if (toHide == True):
            GUIGTK_Class.AppFrm1.withdraw()
            return;
        #GUIGTK_Class.AppFrm1.get_changes()
        
        print "Reading variables "
        a = GUIGTK_Class.AppFrm1.var1_TStart #tone duration
        b = GUIGTK_Class.AppFrm1.var2_TEnd
        c = GUIGTK_Class.AppFrm1.var3_MWS
        d = GUIGTK_Class.AppFrm1.var4_MWE
        e = GUIGTK_Class.AppFrm1.var5_ITStart #changed to intertrial random1 time
        f = GUIGTK_Class.AppFrm1.var6_ITEnd #changed to intertrial random2 time
        g = GUIGTK_Class.AppFrm1.var7_Probab1
        print a
        print b
        print c
        print d
        print e
        print f
        print g
        GUIGTK_Class.toneStart = a
        GUIGTK_Class.toneEnd = b
        GUIGTK_Class.movementWindowStart = c
        GUIGTK_Class.movementWindowEnd = d
        GUIGTK_Class.interTrialStart = e
        GUIGTK_Class.interTrialEnd = f
        GUIGTK_Class.probabilityToneOne = g
    
    
    @staticmethod
    def hideForm3(toHide = True):
        print "Hide Form 3."
        
        if (toHide == True):
            GUIGTK_Class.AppFrm3.withdraw()
            return;
        
        #GUIGTK_Class.AppFrm3.get_changes()
        
        print "Reading variables "
        a = GUIGTK_Class.AppFrm3.var1_T1
        b = GUIGTK_Class.AppFrm3.var2_T2
        c = GUIGTK_Class.AppFrm3.var3_MA
        d = GUIGTK_Class.AppFrm3.var4_MT
        e = GUIGTK_Class.AppFrm3.var5_IT
        f = GUIGTK_Class.AppFrm3.var6_ShowTracking
        g = GUIGTK_Class.AppFrm3.var7_ShowFeedback
        h = GUIGTK_Class.AppFrm3.var8_num_selected
        print a
        print b
        print c
        print d
        print e
        print f
        print g
        print h
        GUIGTK_Class.frequencyTone1 = a
        GUIGTK_Class.frequencyTone2 = b
        GUIGTK_Class.movementAmount = c
        GUIGTK_Class.movementMethod = h
        GUIGTK_Class.movementTime = d
        GUIGTK_Class.idleTime = e
        
        if (toHide == True):
            GUIGTK_Class.AppFrm3.withdraw()
    
    @staticmethod
    def hideForm5(toHide = True):
        print "Hide Form 5."
        GUIGTK_Class.comment = GUIGTK_Class.AppFrm5.commentStr
        print GUIGTK_Class.comment
        if (toHide == True):
            GUIGTK_Class.AppFrm5.withdraw()
            #GUIGTK_Class.AppFrm5.apply_comment()
            #print "current comment: ", gVariables.trial_comment
            return;

        pass
    
    @staticmethod
    def showFrame1():
        print "Showing Frame 1"
        GUIGTK_Class.AppFrm1.deiconify()
        pass
    
    @staticmethod
    def showFrame3():
        GUIGTK_Class.AppFrm3.deiconify()
        print "Showing Frame 3"
    
    @staticmethod
    def showFrame5():
        GUIGTK_Class.AppFrm5.deiconify()
        print "Showing Frame 5"
    

    def __on_Text1KeyInput_Key(self,Event=None):
        #print "Key Pressed."
        pass

    def __on_Text1KeyInput_KeyRel_o(self,Event=None):
        print "Pressed o : ","Open Valve"
        GUIGTK_Class.overrideaction_open()
        pass

    def __on_Text1KeyInput_Key_C(self,Event=None):
        print "Pressed C : ", "Close Valve"
        GUIGTK_Class.overrideaction_close()
        pass

    def __on_Text1KeyInput_Key_D(self,Event=None):
        print "Pressed D : ", "Drop"
        GUIGTK_Class.overrideaction_drop()
        pass

    def __on_Text1KeyInput_Key_K(self,Event=None):
        print "Pressed K : ","Start / Stop Training"
        GUIGTK_Class.overrideaction_startTraining()
        pass

    def __on_Text1KeyInput_Key_O(self,Event=None):
        print "Pressed O : ","Open Valve"
        GUIGTK_Class.overrideaction_open()
        pass

    def __on_Text1KeyInput_Key_P(self,Event=None):
        print "Pressed P : ", "Pause / Resume Training"
        GUIGTK_Class.overrideaction_pauseTraining()
        pass

    def __on_Text1KeyInput_Key_R(self,Event=None):
        print "Pressed R : ","Reward"
        GUIGTK_Class.overrideaction_reward()
        pass

    def __on_Text1KeyInput_Key_c(self,Event=None):
        print "Pressed c : ", "Close Valve"
        GUIGTK_Class.overrideaction_close()
        pass

    def __on_Text1KeyInput_Key_d(self,Event=None):
        print "Pressed d : ", "Drop"
        GUIGTK_Class.overrideaction_drop()
        pass

    def __on_Text1KeyInput_Key_k(self,Event=None):
        print "Pressed k : ","Start / Stop Training"
        GUIGTK_Class.overrideaction_startTraining()
        pass

    def __on_Text1KeyInput_Key_p(self,Event=None):
        print "Pressed p : ", "Pause / Resume Training"
        GUIGTK_Class.overrideaction_pauseTraining()
        pass

    def __on_Text1KeyInput_Key_r(self,Event=None):
        print "Pressed r : ","Reward"
        GUIGTK_Class.overrideaction_reward()
        pass

    def __on_btnClose_ButRel_1(self,Event=None):
        #pressed Close
        print "Close Valve"
        GUIGTK_Class.overrideaction_close()
        pass

    def __on_btnComment_ButRel_1(self,Event=None):
        self.showFrame5()

    def __on_btnDrop_ButRel_1(self,Event=None):
        #pressed Drop
        print "Drop"
        #self.gVariables.fn_giveDrop()
        GUIGTK_Class.overrideaction_drop()
        pass

    def __on_btnExit_ButRel_1(self,Event=None):
        #Exiting program.
        #Frame.destroy(Frame)
        GUIGTK_Class.App.exitingUserInterface()
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
        GUIGTK_Class.overrideaction_open()
        pass

    def __on_btnPause_ButRel_1(self,Event=None):
        #pressed Pause
        print "Pause / Resume Training"
        GUIGTK_Class.overrideaction_pauseTraining()
        pass

    def __on_btnReward_ButRel_1(self,Event=None):
        #pressed Reward
        print "Reward"
        GUIGTK_Class.overrideaction_reward()
        pass

    def __on_btnStart_ButRel_1(self,Event=None):
        #pressed Start
        print "Start / Stop Training"
        GUIGTK_Class.overrideaction_startTraining()
        pass


    def __on_userInput_Dstry(self,Event=None):
        if ( self.__alive == 0):
            GUIGTK_Class.App.exitingUserInterface()
        pass
    
    def exitingUserInterface(self):
        print "Exiting userInterface_tk Program"
        logging.info('Exiting userInterface_tk')
        os._exit(0)
    #
    #Start of non-Rapyd user code
    #

def startFrame0():
    Root = Tk()
    import Tkinter
    #Tkinter.CallWrapper = rpErrorHandler.CallWrapper
    del Tkinter
    GUIGTK_Class.App = userInput(Root)
    GUIGTK_Class.App.pack(expand='yes',fill='both')
    
    Root.geometry('640x480+10+10')
    Root.title('tk GUI Main Frame.')
    Root.mainloop()

def startFrame1():
    import Tkinter
    Root2 = Tkinter.Tk()
    Root2.withdraw()
    #Tkinter.CallWrapper = rpErrorHandler.CallWrapper
    del Tkinter
    
    GUIGTK_Class.AppFrm1 = Form1(Root2)
    #AppFrm1.gVariables = gVariables
    #AppFrm1.configureData()
    #App.pack(expand='yes', fill='both')
    #App.gVariables = gVariables
    GUIGTK_Class.AppFrm1.protocol('WM_DELETE_WINDOW', GUIGTK_Class.App.hideForm1)
    
    #gVariables.AppFrm1.geometry('640x480+10+10')
    GUIGTK_Class.AppFrm1.title('Trial Events.')
    GUIGTK_Class.AppFrm1.withdraw()
    GUIGTK_Class.AppFrm1.mainloop()
    pass

def startFrame3():
    import Tkinter
    Root = Tkinter.Tk()
    Root.withdraw()
    #Tkinter.CallWrapper = rpErrorHandler.CallWrapper
    del Tkinter
    
    GUIGTK_Class.AppFrm3 = Form3(Root)
    #AppFrm1.gVariables = gVariables
    #AppFrm1.configureData()
    #App.pack(expand='yes', fill='both')
    #App.gVariables = gVariables
    GUIGTK_Class.AppFrm3.protocol('WM_DELETE_WINDOW', GUIGTK_Class.App.hideForm3)
    
    #gVariables.AppFrm1.geometry('640x480+10+10')
    GUIGTK_Class.AppFrm3.title('Parameters.')
    GUIGTK_Class.AppFrm3.withdraw()
    GUIGTK_Class.AppFrm3.mainloop()
    pass

def startFrame5():
    import Tkinter
    Root = Tkinter.Tk()
    Root.withdraw()
    #Tkinter.CallWrapper = rpErrorHandler.CallWrapper
    del Tkinter
    GUIGTK_Class.AppFrm5 = Form5(Root)
    #AppFrm1.gVariables = gVariables
    #AppFrm1.configureData()
    #App.pack(expand='yes', fill='both')
    #App.gVariables = gVariables
    GUIGTK_Class.AppFrm5.protocol('WM_DELETE_WINDOW', GUIGTK_Class.App.hideForm5)
    
    #gVariables.AppFrm1.geometry('640x480+10+10')
    GUIGTK_Class.AppFrm5.title('Comment.')
    GUIGTK_Class.AppFrm5.withdraw()
    GUIGTK_Class.AppFrm5.mainloop()
    pass

if __name__ == '__main__':
    # create a logging format
    formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    dateformat = '%Y/%m/%d %I:%M:%S %p'
    
    logging.basicConfig(filename='logs/userInterface_tk.log', filemode='w',
        level=logging.DEBUG, format=formatter, datefmt = dateformat)
    logging.info('Start userInterface_tk Test')
    a = GUIGTK_Class()