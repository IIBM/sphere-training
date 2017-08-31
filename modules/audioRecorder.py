# -*- coding: utf-8 -*-
# audioRecorder.py
'''
    Programa que graba audio desde un micrófono a un archivo de salida configurable
'''
import time
import pyaudio

class audioRecorder():
    def __init__ (self) :
        self.available = True
        self.mustquit = 0
        pass
    
    def setOutputAudioFile(self,filename):
        self.outputAudioFile = filename
        print "filename: " + filename

    def mainAudioDetection(self):
        #self.open = True
        self.audioRate = 44100
        self.audioFrames_per_buffer = 1024
        self.audioChannels = 2
        self.audioFormat = pyaudio.paInt16
        self.audio = pyaudio.PyAudio()
        numdev=self.audio.get_device_count()
        devindex=None
        MICDESC = 'USB' #TODO find a bether way to search for microphne
        for i in range(numdev):
            if self.audio.get_device_info_by_index(i)['name'].find(MICDESC):
                devindex = i
        self.audioStream = self.audio.open(format=self.audioFormat,
                                      channels=self.audioChannels,
                                      rate=self.audioRate,
                                      input=True,
                                      input_device_index=devindex,
                                      frames_per_buffer = self.audioFrames_per_buffer)
        self.audioFrames = []
        
        audiotimes = []
        audiotimes.append(time.time())

        self.audioStream.start_stream()
        while(self.available == True):
            audiotimes.append(time.time()-audiotimes[0])
            data = self.audioStream.read(self.audioFrames_per_buffer) 
            self.audioFrames.append(data)
            
            if (self.mustquit == 1 or self.available != True):  # escape pressed
                # end Program.
                try:
                    self.audioStream.stop_stream()
                    self.audioStream.close()
                    self.audio.terminate()

                    import wave
                    waveFile = wave.open(self.outputAudioFile, 'wb')
                    waveFile.setnchannels(self.audioChannels)
                    waveFile.setsampwidth(self.audio.get_sample_size(self.audioFormat))
                    waveFile.setframerate(self.audioRate)
                    waveFile.writeframes(b''.join(self.audioFrames))
                    waveFile.close()

                    logger.info("AUDIOTIMES")
                    logger.info(audiotimes)
                except:
                    pass
                return

    def exit(self):
        # os._exit(0)
        self.mustquit = 1
        self.available = False
