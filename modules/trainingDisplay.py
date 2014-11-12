import pygame
import sys
import time
import logging
logger = logging.getLogger('trainingDisplay')
import track_bola_utils
import multiprocessing

class multiproc_trainingDisplay():
    #Class that renders relevant text added by the user, lets you update its information.
    #Created because the need of showing Trials and Successful trials to the user on a regular training.
    #This class should be able to display two different types of information (important, in a bigger font, and 
    # less important information in a regular font) and adjust the graphical window according to the amount of information.
    #This class is a WIP.>< 
    
    
    def __init__(self, jobl):
        self.jobList = jobl
        
        
        
        self.available = True
        self.displayText1 = [] #important text to display in a relatively big font
        self.displayText2 = [] #less important text to display in a smaller font
        pygame.init()
        self.windowWidth = 500
        self.windowHeight = 200
        self.windowSurface = pygame.display.set_mode((self.windowWidth, self.windowHeight), 0, 32)
        self.TEXT1_FONT_SIZE = 35 #size in height of the font 1
        self.TEXT2_FONT_SIZE = 30 #size in height of the font 2
        self.TEXT_1_2_SEPARATION = 25 #separation between the two texts
        self.INITIAL_SEPARATION = 25 #separation between top of the window and text1
        self.isUserWriting = False
        pygame.display.set_caption('Variables')
        self.basicFont = pygame.font.SysFont(None, 48)
        self.secondaryFont = pygame.font.SysFont(None, 36)
        time.sleep(0.5)
        self.renderAgain()
        pass

    def checkJobList(self):
        if (self.jobList.qsize() > 0 or self.jobList.empty() == False ):
                try:
                        tempvar = self.jobList.get()
                        self.jobList.task_done()
                except:
                        return;
                print str("checkJobList: queue: " + str(tempvar) )
                index = tempvar[0]
                try:
                    argument = tempvar[1]
                except:
                    argument = ""
                    pass
                
                print "checkJobList: Got a Message:", index
                print "checkJobList: Message's argument:", argument
#                 try:
#                     a = str(argument)
#                     print "Argument: %s" %a
#                 except:
#                     print "Message's argument cannot be parsed to str."
#                     pass
                if (index == "updateInfo"):
                    print "Command updateInfo received."
                    self.updateInfo(argument[0], argument[1])
                elif (index == "importantInfo"):
                    print "Command importantInfo received."
                    self.addImportantInfo(argument)
                elif (index == "secondaryInfo"):
                    print "Command secondaryInfo received."
                    self.addSecondaryInfo(argument)
                elif (index == "exitDisplay"):
                    print "Command exitDisplay received."
                    self.exitDisplay()
                elif (index == "askUserInput"):
                    print "Command askUserInput received."
                    self.askUserInput(a)
                elif (index == "renderAgain"):
                    print "Command renderAgain received."
                    self.renderAgain()

    def renderAgain(self):
        #render things in pygame again.
        if (self.available == True):
            try:
                if ( (len(self.displayText1) <= 0) and  (len(self.displayText2) <= 0) ):
                    return;
            except:
                return;
            
            if (self.isUserWriting == False):
                # draw the white background onto the surface
                self.windowSurface.fill((55,55,55))
                #
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
                    textRect1.centery = (self.INITIAL_SEPARATION + self.TEXT_1_2_SEPARATION + len(self.displayText1) * self.TEXT1_FONT_SIZE +
                                          i*self.TEXT2_FONT_SIZE)
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
        sys.exit()
    
    def updateInfo(self, text, newValue):
        #sets from the class lists. the one that has "text", and updates it with newValue
        a = False
        try:
            if ( (len(self.displayText1) <= 0) and  (len(self.displayText2) <= 0) ):
                return;
        except:
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
        """
        if (a == False):
            print "Info with text : " + text + " not found, value: " + str(newValue) + " not updated."
            print self.displayText1
            print self.displayText2
        """
        self.renderAgain()


class trainingDisplay() :
    #This class relays information to the multiproc_trainingDisplay class..
    #check that class for information about trainingDisplay functionality.>< 
    
    def launch_multiproc(self, jobl):
        a = multiproc_trainingDisplay(jobl)
        while(True):
            time.sleep(0.01)
            a.checkJobList()
            #a.updateInfo("Other secondary information", var)
            for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
    
    def __init__(self):
        import multiprocessing
        self.jobList = multiprocessing.JoinableQueue()
        
        self.displayProc = multiprocessing.Process(target=self.launch_multiproc, args=(self.jobList,) )
        self.displayProc.start()
        
        print "process started."


    def renderAgain(self):
        #render things in pygame again.
        self.jobList.put( ("renderAgain", "") )
        pass

    
    def askUserInput(self, texts):
        self.jobList.put( ("askUserInput", texts) )
        
    
    def addImportantInfo(self, info):
        self.jobList.put( ("importantInfo", info) )
    
    def addSecondaryInfo(self, info):
        self.jobList.put( ("secondaryInfo", info) )
    
    def exitDisplay(self):
        #print "exiting Display."
        self.jobList.put( ("exitDisplay", "") )
        sys.exit()
    
    def updateInfo(self, text, newValue):
        self.jobList.put( ("updateInfo", (text, newValue)) );

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
    a = trainingDisplay()
    a.addImportantInfo(("Trials", 300))
    a.addImportantInfo(("Succesful Trials", 200))
    a.addSecondaryInfo(("Time: 00:22::33", 0))
    a.addSecondaryInfo(("% s/t", 45.0))
    a.addSecondaryInfo(("Other secondary information", 45.5))
    a.renderAgain()
    var = 0
    while(True):
        time.sleep(1)
        a.updateInfo("Other secondary information", var)
        var+=1
        print "loop: " , var
        logger.info( str("loop: " + str(var) ) )