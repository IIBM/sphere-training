# -*- coding: utf-8 -*-
import pygame
#from pygame.locals import *
import math
import numpy
import time
import logging
import track_bola_utils
import sys
import os

logger = logging.getLogger('soundGen')

PROCESS_SLEEP_TIME = 0.035 #in seconds

def checkImports():
    track_bola_utils.__importFromString("configSoundGenerator")

class soundGen():
    def __init__(self,freq=None,duration=None,sample_rate=44100, bits=16,volume=1.0):
        self.freq = freq
        self.duration = duration
        self.volume = volume
        checkImports()
        import configSoundGenerator
        self.generation_method = configSoundGenerator.generation_method; #0: pygame ; 1: pyaudio
        
        if (self.generation_method == 0):
            import soundGen_pygame as soundGenMethod
        else:
            import soundGen_pyaudio as soundGenMethod
        import multiprocessing
        self.soundGenJobList = multiprocessing.JoinableQueue()
        
        self.soundGenProc = multiprocessing.Process(target=self.launch_multiproc, args=(self.soundGenJobList, soundGenMethod, freq,duration,sample_rate, bits,volume,) )
        self.soundGenProc.start()
        
        logger.debug('soundGen process started')

    def launch_multiproc(self, jobl,soundGenMethod, freq, duration, sample_rate, bits, volume):
        a = soundGenMethod.multiproc_soundGen(jobl, freq, duration, sample_rate, bits, volume)
        time.sleep(0.5)
        while(a.toExit != 1):
            a.checkJobList()
            if (a.toExit == 1):
                #del a
                #print "Exiting soundGenerator soundGen class."
                a.toExit = 1;
                logger.debug( "exiting soundGenerator launch_multiproc" )
                #self.exit()
                break;
            pass
            #print "loop. %s %d" % (str(a), a.toExit)
            time.sleep(PROCESS_SLEEP_TIME)

    def exit(self):
        self.soundGenJobList.put( ( "exit", "" ) )
        logger.debug("soundGen exit message.")
        time.sleep(0.5)
        self.soundGenProc.terminate()
        del self.soundGenProc
        del self.soundGenJobList
        del self.freq
        del self.duration
        #sys.exit()
        pass

    def tone(self, duration=1.0, freq=1000.0) :
        self.soundGenJobList.put( ( "tone" , duration, freq ) )

    def play(self): #there is needed a delay, after the play command.
        self.soundGenJobList.put( ( "play", "" ) )

    def getFrequency(self):
        return self.freq
    
    def getDuration(self):
        return self.duration

        

if __name__ == '__main__':
    # create a logging format
    dateformat = '%Y/%m/%d %H:%M:%S'
    formatter_str = '%(asctime)s.%(msecs)d - %(name)s - %(levelname)s - %(message)s'
    filename_to_log='logs/sound.log'
    
    
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
    
    print "Start sound test"
    logger.info('Start sound test')
    s1 = soundGen()
    duration = 3.0 # in seconds
    freq1 = 1440
    freq2 = 1550

    s1.tone(duration, freq1)
    s1.play()
    time.sleep(duration)

    time.sleep(4)

    s1.tone(duration, freq2)
    s1.play()
    time.sleep(duration)

    time.sleep(4)


    s2 = soundGen(3*freq1,2*duration)
    s2.play()
    time.sleep(2*duration)
    logger.info('End sound test')
    print "End sound test"
    s1.exit()
    s2.exit()
    sys.exit()
