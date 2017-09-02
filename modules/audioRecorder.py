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
        self.recording = False #grabando, implica haber inicializado
        self.mustquit = 0
        self.audioRecordingInitialized = False #inicializado, no necesariamente grabando
        pass
    
    def saveToOutputFile(self):
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
    
    def startAudioRecording(self):
        if (self.audioRecordingInitialized == False):
            #self.open = True
            self.audioRate = 44100
            self.audioFrames_per_buffer = 1024
            self.audioChannels = 2
            self.audioFormat = pyaudio.paInt16
            self.audio = pyaudio.PyAudio()
            numdev=self.audio.get_device_count()
            devindex=None
            MICDESC = 'USB' #TODO find a better way to search for microphone
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
            self.audiotimes = []
            self.audiotimes.append(time.time())
            self.audioStream.start_stream()
            self.audioRecordingInitialized = True
        self.recording = True
    
    def stopAudioRecording(self):
        self.recording = False
    
    def setOutputAudioFile(self,filename):
        self.outputAudioFile = filename
        print "filename: " + filename

    def mainAudioRecording(self):
        while(True):
            if (self.mustquit == 1 or self.available != True):  # escape pressed
                # end Program.
                if (self.audioRecordingInitialized == True):
                    self.saveToOutputFile() #graba sólo si inicializó
                return
            if (self.audioRecordingInitialized != True):
                time.sleep(0.1)
                continue
            if (self.recording != True):
                time.sleep(0.1)
                pass
            else:
                self.audiotimes.append(time.time()-self.audiotimes[0])
                data = self.audioStream.read(self.audioFrames_per_buffer) 
                self.audioFrames.append(data)
        return

    def exit(self):
        # os._exit(0)
        self.mustquit = 1
        self.available = False
