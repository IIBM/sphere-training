import pygame
from pygame.locals import *

import math
import numpy
import logging

logger = logging.getLogger('soundGen')

class soundGen():

    def __init__(self,freq=None,duration=None,sample_rate=44100, bits=16):
        logger.info('New instance of soundGen')
        pygame.mixer.pre_init(sample_rate, -bits, 2)
        pygame.init()
        self.sample_rate = sample_rate
        self.bits = bits
        if ((duration == None) or (freq == None)) :
            self.duration = 1.0
            self.freq = 1000.0
        else :
            self.duration = duration
            self.freq = freq
        self.sound = self.tone(self.duration,self.freq)

    def tone(self, duration=1.0, freq=1000.0) :
        self.duration = duration
        self.freq = freq
        logger.info('Tone freq = %s Hz, duration = %s s, sample_rate = %s, bits = %s',self.freq,self.duration,self.sample_rate,self.bits)

        n_samples = int(round(self.duration*self.sample_rate))
        buf = numpy.zeros((n_samples, 2), dtype = numpy.int16)
        max_sample = 2**(self.bits - 1) - 1
        for s in range(n_samples):
            t = float(s)/self.sample_rate    # time in seconds

            buf[s][0] = int(round(max_sample*math.sin(2*math.pi*self.freq*t))) # left
            buf[s][1] = int(round(max_sample*math.sin(2*math.pi*self.freq*t))) # right

        self.sound = pygame.sndarray.make_sound(buf)
        return self.sound

    #TODO add new waveforms

    def play(self):
        logger.info('Tone freq = %s Hz, duration = %s s',self.freq,self.duration)
        self.sound.play()
        #there is needed a delay, after the play command.

if __name__ == '__main__':
    import time
    formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    dateformat = '%Y/%m/%d %I:%M:%S %p'

    logging.basicConfig(filename='logs/sound.log', filemode='w',
        level=logging.DEBUG, format=formatter, datefmt = dateformat)
    logging.info('Start Sound Test')
    s1 = soundGen()
    duration = 3.0 # in seconds
    freq1 = 440
    freq2 = 550

    s1.tone(duration, freq1)
    s1.play()
    time.sleep(duration)

    time.sleep(1)

    s1.tone(duration, freq2)
    s1.play()
    time.sleep(duration)

    time.sleep(1)

    a = s1.tone(duration)
    a.play()
    time.sleep(duration)

    s2 = soundGen(3*freq1,2*duration)
    time.sleep(2*duration)
    logging.info('End Sound Test')
