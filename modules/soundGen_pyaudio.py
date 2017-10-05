# -*- coding: utf-8 -*-
import math
import numpy
import time
import logging
import track_bola_utils
import sys

logger = logging.getLogger('soundGen')




class multiproc_soundGen():
    toExit = 0;
    soundGenJobList = 0;
    def __init__(self,jobl, duration=None, freq=None,sample_rate=44100, bits=16, volume=1.0):
        self.soundGenJobList = jobl
        logger.info('New instance of soundGen')
        #pygame.mixer.pre_init(sample_rate, -bits, 2)
        self.sample_rate = sample_rate
        self.bits = bits
        self.volume = volume
        if ((duration == None) or (freq == None)) :
            self.duration = 1.0
            self.freq = 1000.0
        else :
            self.duration = duration
            self.freq = freq
        import math
        import pyaudio
        
        #sudo apt-get install python-pyaudio
        PyAudio = pyaudio.PyAudio
        self.soundp = PyAudio()
        self.stream = self.soundp.open(format = self.soundp.get_format_from_width(1), channels = 2, rate = self.sample_rate, output = True)
        self.tone(self.duration, self.freq, self.volume)

        
        
        
        print "finish sound test."
        logger.debug("soundGen(multiproc) instance initialized.")

    def checkJobList(self):
        if (self.soundGenJobList.qsize() > 0 or self.soundGenJobList.empty() == False ):
                try:
                        tempvar = self.soundGenJobList.get()
                        self.soundGenJobList.task_done()
                except:
                        return;
                #print str("checkJobList: queue: " + str(tempvar) )
                index = tempvar[0]
                try:
                    argument = tempvar[1]
                except:
                    argument = ""
                    pass
                
                #print "checkJobList: Got a Message:", index
                #print "checkJobList: Message's argument:", argument
#                 try:
#                     a = str(argument)
#                     print "Argument: %s" %a
#                 except:
#                     print "Message's argument cannot be parsed to str."
#                     pass
                if (index == "tone"):
                    #print "Command secondaryInfo received."
                    logger.debug( str(tempvar[1]) )
                    logger.debug( str(tempvar[2]) )
                    logger.debug( str(tempvar[3]) )
                    self.tone(tempvar[1], tempvar[2], tempvar[3])
                    logger.debug('tone..')
                elif (index == "play"):
                    #print "Command exitDisplay received."
                    
                    self.play()
                elif (index == "exit"):
                    #print "Command exitDisplay received."
                    logger.debug('exiting..')
                    self.exit()
                    return;
                else:
                    print "unknown message: %s" % str(index)

    def exit(self):
        print "SoundGen exiting."
        self.toExit = 1;
        try:
            self.stream.stop_stream()
            self.stream.close()
            self.soundp.terminate()
            time.sleep(0.2)
            sys.exit()
        except:
            pass
        pass

    def tone(self, duration=1.0, freq=1000.0,volume=1.0) :
        self.duration = duration
        self.freq = freq
        self.volume = volume
        logger.info('Tone freq = %s Hz, duration = %s s, sample_rate = %s, bits = %s, volume = %s',self.freq,self.duration,self.sample_rate,self.bits,self.volume)
        #See http://en.wikipedia.org/wiki/Bit_rate#Audio
        BITRATE = self.sample_rate #number of frames per second/frameset.      
        
        #See http://www.phy.mtu.edu/~suits/notefreqs.html
        FREQUENCY = self.freq #Hz, waves per second, 261.63=C4-note.
        LENGTH = 2*self.duration #seconds to play sound # for some reason, needs to be 2 times the number..
        
        NUMBEROFFRAMES = int(BITRATE * LENGTH)
        RESTFRAMES = int(NUMBEROFFRAMES % BITRATE)
        WAVEDATA = ''
        
        for x in xrange(NUMBEROFFRAMES):
         WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127*self.volume+128))
        
        #fill remainder of frameset with silence
        for x in xrange(RESTFRAMES): 
         WAVEDATA = WAVEDATA+chr(128)
        
        self.WAVEDATA = WAVEDATA
        #self.stream.write(self.WAVEDATA) #does not play tone when calling tone function by default..
        
        #logger.debug(str(self.soundp))
        #return self.sound
        return;

    def play(self):
        logger.info('Tone freq = %s Hz, duration = %s s',self.freq,self.duration)
        if (float(self.duration)  < 0.000003571):
            #print "not played because duration is less than audible."
            logger.debug("Not played tone because duration is less than audible.")
        else:
            self.stream.write(self.WAVEDATA)
            #print "playing tone %s" % self.freq
            #print self.sound
            logger.debug("playing")
        pass

    def getFrequency(self):
        return self.freq
    
    def getDuration(self):
        return self.duration


class soundGen():
    def __init__(self,duration=None,freq=None,sample_rate=44100, bits=16, volume = 1.0):
        self.freq = freq
        self.duration = duration
        self.volume = volume
        import multiprocessing
        self.soundGenJobList = multiprocessing.JoinableQueue()
        self.soundGenProc = multiprocessing.Process(target=self.launch_multiproc, args=(self.soundGenJobList, duration, freq,sample_rate, bits, volume,) )
        self.soundGenProc.start()
        logger.debug('soundGen process started')
        
    def launch_multiproc(self, jobl, duration,freq,  sample_rate, bits, volume):
        a = multiproc_soundGen(jobl,  duration,freq, sample_rate, bits, volume)
        time.sleep(0.5)
        while(a.toExit != 1):
            a.checkJobList()
            if (a.toExit == 1):
                #del a
                #print "Exiting soundGen_pyaudio soundGen class."
                a.toExit = 1;
                logger.debug( "exiting soundGen_pyaudio launch_multiproc" )
                #self.exit()
                break;
            pass
            #print "loop. %s %d" % (str(a), a.toExit)
            time.sleep(0.030)
        pass
    
    def exit(self):
        self.soundGenJobList.put( ( "exit", "" ) )
        logger.debug("soundGen exit message.")
        time.sleep(0.5)
        self.soundGenProc.terminate()
        del self.soundGenProc
        del self.soundGenJobList
        del self.freq
        del self.duration
        del self.volume
        #sys.exit()
        pass

    def tone(self, duration=1.0, freq=1000.0, volume=1.0) :
        self.soundGenJobList.put( ( "tone" , duration, freq, volume ) )

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
    
    
    
    logger.info('Start Sound Test')
    s1 = soundGen(duration=1.0, freq=1000, volume=0.1)
    duration = 3.0 # in seconds
    freq1 = 1440
    freq2 = 1550
    print "pre play"
    time.sleep(5)
    s1.play()
    time.sleep(5)
    print "post play"
    time.sleep(duration)

    time.sleep(4)
    print "pre play2"
    s1.tone(duration, freq2, volume=0.1)
    
    time.sleep(duration)
    print "post play2"
    time.sleep(4)
    print "pre play3"
    s1.play()
    time.sleep(4)
    print "post play3"
    time.sleep(4)

    print "pre play4"
    s2 = soundGen(2*duration, 3*freq1, volume=0.1)
    s2.play()
    time.sleep(2*duration)
    print "post play4"
    s2.tone(2*duration, 0.5*freq2, volume=0.1)
    logger.info('End Sound Test')
    s1.exit()
    s2.exit()
    sys.exit()
