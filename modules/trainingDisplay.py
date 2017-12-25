import pygame
import sys
import time
import logging
logger = logging.getLogger('trainingDisplay')
import track_bola_utils
import multiprocessing


PROCESS_SLEEP_TIME = 0.010 #in seconds

class multiproc_trainingDisplay():
    #Class that renders relevant text added by the user, lets you update its information.
    #Created because the need of showing Trials and Successful trials to the user on a regular training.
    #This class should be able to display two different types of information (important, in a bigger font, and 
    # less important information in a regular font) and adjust the graphical window according to the amount of information.
    #This class is a WIP.
    def __init__(self, jobl, caption="Variables"):
        self.displayJobList = jobl
        self.available = True
        self.displayText1 = [] #important text to display in a relatively big font
        self.displayText2 = [] #less important text to display in a smaller font
        try:
            pygame.init()
        except:
            #print "pygame already initialized."
            pass
        self.windowWidth = 500
        self.windowHeight = 200
        self.windowSurface = pygame.display.set_mode((self.windowWidth, self.windowHeight), 0, 32)
        self.TEXT1_FONT_SIZE = 35 #size in height of the font 1
        self.TEXT2_FONT_SIZE = 30 #size in height of the font 2
        self.TEXT_1_2_SEPARATION = 25 #separation between the two texts
        self.INITIAL_SEPARATION = 25 #separation between top of the window and text1
        self.isUserWriting = False
        pygame.display.set_caption(caption)
        self.basicFont = pygame.font.SysFont(None, 48)
        self.secondaryFont = pygame.font.SysFont(None, 36)
        pass

    def discardOldJobList(self):
        if (self.displayJobList.qsize() > 0 or self.displayJobList.empty() == False ):
            try:
                tempvar = self.displayJobList.get()
                self.displayJobList.task_done()
            except:
                return;

    def checkJobList(self):
        if (self.displayJobList.qsize() > 0 or self.displayJobList.empty() == False ):
                try:
                        tempvar = self.displayJobList.get()
                        self.displayJobList.task_done()
                except:
                        return;
                #print str("checkJobList: queue: " + str(tempvar) )
                if (len(tempvar) < 1):
                    return; #probably ill-formed message
                index = tempvar[0]
                if (len(tempvar) > 1):
                    argument = tempvar[1]
                else:
                    argument = "__" #two chars to prevent error in updateInfo if above try fails..
                if (index == "updateInfo"):
                    #print "Command updateInfo received."
                    self.updateInfo(argument[0], argument[1])
                if (index == "cleanInfo"):
                    self.discardOldJobList()
                    pass
                if (index == "multipleUpdateInfo"):
                    for i in range (0, len(argument)):
                        self.updateInfo(argument[i][0], argument[i][1])
                    pass
                elif (index == "importantInfo"):
                    #print "Command importantInfo received."
                    self.addImportantInfo(argument)
                elif (index == "secondaryInfo"):
                    #print "Command secondaryInfo received."
                    self.addSecondaryInfo(argument)
                elif (index == "exitDisplay"):
                    #print "Command exitDisplay received."
                    self.exitDisplay()
                elif (index == "askUserInput"):
                    #print "Command askUserInput received."
                    self.askUserInput(a)
                elif (index == "renderAgain"):
                    #print "Command renderAgain received."
                    self.renderAgain()

    def renderAgain(self):
        pass #render things in pygame again.
        if (self.available == True):
            if ( (len(self.displayText1) <= 0) and  (len(self.displayText2) <= 0) ):
                    return;
            if (self.isUserWriting == False):
                # draw background onto the surface
                self.windowSurface.fill((55,55,55))
                for i in range(0, len(self.displayText1)):
                    text1 = self.basicFont.render('%s: %r' % (self.displayText1[i][0],self.displayText1[i][1]), True, (255,255,255))
                    textRect1 = text1.get_rect()
                    textRect1.centerx = self.windowSurface.get_rect().centerx
                    textRect1.centery = self.INITIAL_SEPARATION+ i*self.TEXT1_FONT_SIZE
                    self.windowSurface.blit(text1, textRect1)
                for i in range(0, len(self.displayText2)):
                    text1 = self.secondaryFont.render('%s: %r' % (self.displayText2[i][0],self.displayText2[i][1]), True, (255,255,255))
                    textRect1 = text1.get_rect()
                    textRect1.centerx = self.windowSurface.get_rect().centerx
                    textRect1.centery = (self.INITIAL_SEPARATION + self.TEXT_1_2_SEPARATION + len(self.displayText1) * self.TEXT1_FONT_SIZE + i*self.TEXT2_FONT_SIZE)
                    self.windowSurface.blit(text1, textRect1)
                # draw the window onto the screen
                pygame.display.update()

    def askUserInput(self, texts):
        self.isUserWriting = True
        #print "Asking user input:"
        #import inputbox #not used anymore.
        #s = inputbox.ask(self.windowSurface, "Comment on this training")
        s = ""
        self.isUserWriting = False
        return s
    
    def addImportantInfo(self, info):
        self.displayText1.append(info)
        self.windowHeight = 55 + len(self.displayText1) * 32 + len(self.displayText2) * 29
        self.windowSurface = pygame.display.set_mode((self.windowWidth, self.windowHeight), 0, 32)
        self.renderAgain()
    
    def addSecondaryInfo(self, info):
        self.displayText2.append(info)
        self.windowHeight = 55 + len(self.displayText1) * 32 + len(self.displayText2) * 29
        self.windowSurface = pygame.display.set_mode((self.windowWidth, self.windowHeight), 0, 32)
        self.renderAgain()
    
    def exitDisplay(self):
        #print "exiting Display."
        self.available = False
        pygame.quit()
        #sys.exit()
        logger.debug("trainingDisplay process finished.")
        pass
    
    def updateInfo(self, text, newValue):
        pass #sets from the class lists. the one that has "text", and updates it with newValue
        a = False
        if (self.available == False): return
        if ( (len(self.displayText1) <= 0) and  (len(self.displayText2) <= 0) ):
                return;
        for i in range(0, len(self.displayText1)):
            if str(self.displayText1[i][0]) == str(text):
                self.displayText1[i] = (text,newValue)
                #print "updated : " + text
                a= True
        for i in range(0, len(self.displayText2)):
            if str(self.displayText2[i][0]) == str(text):
                self.displayText2[i] = (text,newValue)
                #print "updated : " + text
                a = True
        self.renderAgain()


class trainingDisplay() :
    #This class relays information to the multiproc_trainingDisplay class..
    #check that class for information about trainingDisplay functionality.>< 
    def __init__(self, caption="Variables"):
        import multiprocessing
        self.displayJobList = multiprocessing.JoinableQueue()
        self.displayProc = multiprocessing.Process(target=self.launch_multiproc, args=(self.displayJobList, caption,) )
        self.displayProc.start()
        logger.debug("trainingDisplay process Started.")

    def launch_multiproc(self, jobl, caption):
        multiprocObjDisplay = multiproc_trainingDisplay(jobl, caption)
        time.sleep(0.5)
        while(True):
            time.sleep(PROCESS_SLEEP_TIME)
            multiprocObjDisplay.checkJobList()
        pass
    
    def getSleepTime(self):
        return PROCESS_SLEEP_TIME

    def renderAgain(self):
        #render things in pygame again.
        self.displayJobList.put( ("renderAgain", "") )
        pass

    def removeOldInfo(self):
        self.displayJobList.put( ("cleanInfo", ("") ) );
        pass
    
    def askUserInput(self, texts):
        self.displayJobList.put( ("askUserInput", texts) )
        
    
    def addImportantInfo(self, info):
        self.displayJobList.put( ("importantInfo", info) )
    
    def addSecondaryInfo(self, info):
        self.displayJobList.put( ("secondaryInfo", info) )
    
    def exitDisplay(self):
        #print "exiting Display."
        self.displayJobList.put( ("exitDisplay", "") )
        time.sleep(0.3)
        self.displayProc.terminate()
        pass
    
    def updateMultipleInfo(self, lista):
        self.displayJobList.put( ("multipleUpdateInfo", lista ) );
        pass
    
    def updateInfo(self, text, newValue):
        self.displayJobList.put( ("updateInfo", (text, newValue)) , timeout=PROCESS_SLEEP_TIME+0.001);
        pass

if __name__ == '__main__':
    # create a logging format
    dateformat = '%Y/%m/%d %H:%M:%S'
    formatter_str = '%(asctime)s.%(msecs)d - %(name)s - %(levelname)s - %(message)s'
    filename_to_log='logs/trainingDisplay.log'
    
    
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
    
    print "Start trainingDisplay Test"
    a = trainingDisplay("Custom Test Caption")
    a.addImportantInfo(("Trials", 300))
    a.addImportantInfo(("Succesful Trials", 200))
    a.addSecondaryInfo(("Time: 00:22::33", 0))
    a.addSecondaryInfo(("% s/t", 45.0))
    a.addSecondaryInfo(("Other secondary information", 45.5))
    a.renderAgain()
    b = trainingDisplay("Only Trials: ")
    b.addImportantInfo(("Trials", 300))
    b.renderAgain()
    c = trainingDisplay("Other info displayed:")
    c.addImportantInfo(("other", 222))
    c.renderAgain()
    var = 0
    while(True):
        time.sleep(1)
        a.updateInfo("Other secondary information", var)
        b.updateInfo("Trials", 100+var)
        c.updateInfo("other", 222+var)
        var+=1
        c.updateInfo("other", 222+var)
        var+=1
        c.updateInfo("other", 222+var)
        var+=1
        c.updateInfo("other", 222+var)
        print "loop: " , var
        logger.info( str("loop: " + str(var) ) )
