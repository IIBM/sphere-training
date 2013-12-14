import pygame, sys
import time

class trainingDisplay() :

    def renderAgain(self):
        #render things in pygame again.
        # draw the white background onto the surface
        self.windowSurface.fill((55,55,55))
        #
        for i in range(0, len(self.displayText1)):
            text1 = self.basicFont.render('%s: %d' % (self.displayText1[i][0],self.displayText1[i][1]), True, (255,255,255))
            textRect1 = text1.get_rect()
            textRect1.centerx = self.windowSurface.get_rect().centerx
            textRect1.centery = self.windowSurface.get_rect().centery -50+ i*30
            self.windowSurface.blit(text1, textRect1)

        
        text2 = self.basicFont.render('Successful Trials: %d' % 5, True, (255,255,255))
        textRect2 = text2.get_rect()
        textRect2.centerx = self.windowSurface.get_rect().centerx
        textRect2.centery = self.windowSurface.get_rect().centery+len(self.displayText1)*25 + 20
        # draw the text onto the surface
        
        self.windowSurface.blit(text2, textRect2)
        # draw the window onto the screen
        pygame.display.update()
    def __init__(self):
        self.displayText1 = [] #important text to display in a relatively big font
        self.displayText2 = [] #less important text to display in a smaller font
        pygame.init()
        self.windowSurface = pygame.display.set_mode((400, 200), 0, 32)
        pygame.display.set_caption('Variables')
        self.basicFont = pygame.font.SysFont(None, 48)
        time.sleep(1)
        self.renderAgain()
    def addImportantInfo(self, info):
        self.displayText1.append(info)
        self.renderAgain()
    def updateInfo(self, text, newValue):
        #sets from the class lists. the one that has "text", and updates it with newValue
        for i in range(0, len(self.displayText1)):
            if self.displayText1[i][0] is text:
                self.displayText1[i] = (text,newValue)
        self.renderAgain()

if __name__ == '__main__':
    print "trainingDisplay module"
    a = trainingDisplay()
    a.addImportantInfo(("Text1 example", 3))
    a.addImportantInfo(("Text2 : example", 2))
    a.renderAgain()
    while(True):
        time.sleep(1)
        a.updateInfo("Text2 : example", 7)
        