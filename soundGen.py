import pygame
from pygame.locals import *

import math
import numpy

class soundGen():

    def __init__(self, sample_rate=44100, bits=16):
        pygame.mixer.pre_init(sample_rate, -bits, 2)
        pygame.init()
        self.sample_rate = sample_rate
        self.bits = bits
        self.sound = pygame.sndarray.make_sound(numpy.zeros((10, 2), dtype = numpy.int16))

    def tone(self, duration=1.0, freq=1000.0) :
        n_samples = int(round(duration*self.sample_rate))
        buf = numpy.zeros((n_samples, 2), dtype = numpy.int16)
        max_sample = 2**(self.bits - 1) - 1
        for s in range(n_samples):
            t = float(s)/self.sample_rate    # time in seconds

            buf[s][0] = int(round(max_sample*math.sin(2*math.pi*freq*t)))  # left
            buf[s][1] = int(round(max_sample*math.sin(2*math.pi*freq*t))) # right

        self.sound = pygame.sndarray.make_sound(buf)
        return self.sound

    def play(self):
        self.sound.play()
        #there is needed a delay, after the play command.

if __name__ == '__main__':
    import time
    s1 = soundGen()
    duration = 3.0 # in seconds
    #freqency for the left speaker
    frequency_l = 440
    #frequency for the right speaker
    frequency_r = 550

    s1.tone(duration, frequency_l)
    s1.play()
    time.sleep(duration)

    time.sleep(1)

    s1.tone(duration, frequency_r)
    s1.play()
    time.sleep(duration)

    time.sleep(1)

    a = s1.tone(duration)
    a.play()
    time.sleep(duration)
