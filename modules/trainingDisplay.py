import pygame, sys
import time

class trainingDisplay() :
    #Class that renders relevant text added by the user, lets you update its information.
    #Created because the need of showing Trials and Successful trials to the user on a regular training.
    #This class should be able to display two different types of information (important, in a bigger font, and 
    # less important information in a regular font) and adjust the graphical window according to the amount of information.
    #This class is a WIP.

    def renderAgain(self):
        #render things in pygame again.
        if (self.isUserWriting == False):
            # draw the white background onto the surface
            self.windowSurface.fill((55,55,55))
            #
            for i in range(0, len(self.displayText1)):
                text1 = self.basicFont.render('%s: %r' % (self.displayText1[i][0],self.displayText1[i][1]), True, (255,255,255))
                textRect1 = text1.get_rect()
                textRect1.centerx = self.windowSurface.get_rect().centerx
                textRect1.centery = 25+ i*35
                self.windowSurface.blit(text1, textRect1)
            
            for i in range(0, len(self.displayText2)):
                text1 = self.secondaryFont.render('%s: %r' % (self.displayText2[i][0],self.displayText2[i][1]), True, (255,255,255))
                textRect1 = text1.get_rect()
                textRect1.centerx = self.windowSurface.get_rect().centerx
                textRect1.centery = 25+60+len(self.displayText1)*25 + i*30
                self.windowSurface.blit(text1, textRect1)
            # draw the window onto the screen
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
        
    def __init__(self):
        self.displayText1 = [] #important text to display in a relatively big font
        self.displayText2 = [] #less important text to display in a smaller font
        pygame.init()
        self.windowWidth = 500
        self.windowHeight = 200
        self.windowSurface = pygame.display.set_mode((self.windowWidth, self.windowHeight), 0, 32)
        self.isUserWriting = False
        pygame.display.set_caption('Variables')
        self.basicFont = pygame.font.SysFont(None, 48)
        time.sleep(1)
        self.renderAgain()
        self.secondaryFont = pygame.font.SysFont(None, 36)

    
    def askUserInput(self, texts):
        self.isUserWriting = True
        #print "Asking user input:"
        import inputbox
        s = inputbox.ask(self.windowSurface, "Comment on this training")
        print s
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
    
    def updateInfo(self, text, newValue):
        #sets from the class lists. the one that has "text", and updates it with newValue
        a = False
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

if __name__ == '__main__':
    print "trainingDisplay module"
    a = trainingDisplay()
    a.addImportantInfo(("Trials", 300))
    a.addImportantInfo(("Succesful Trials", 200))
    a.addSecondaryInfo(("Time: 00:22::33", 0))
    a.addSecondaryInfo(("% s/t", 45.0))
    a.addSecondaryInfo(("Other secondary information", 45.5))
    a.renderAgain()
    while(True):
        time.sleep(1)
        a.updateInfo("Text2 : example", 7)
        