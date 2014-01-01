# -*- coding: utf-8 -*-
#sphereVideoDetection.py
'''
    Programa que detecta movimiento de un flujo de video (webcam o video) configurado en un archivo de configuración:
    En base al video, establece un vector que corresponde a la dirección del movimiento detectado.
    El movimiento se detecta de círculos negros en movimiento, comparando posición actual con su posición pasada (probable).
    Este archivo reemplaza spherevideotracker.py.<>
    
'''

import pygame
from pygame.locals import *
import logging
import timeit


class sphereVideoDetection():
    def __init__ (self,videosource, width=640, height=480) :
        import track_bola_utils
        import configSphereVideoDetection
        self.winName = configSphereVideoDetection.WINDOW_TITLE
        #declare self variables to use.
        
        self.vectorInstantaneo = track_bola_utils.vectorSimple() #vector acumulado
        self.vectorAcumulado = track_bola_utils.vectorSimple() #vector acumulado
        self.startCalibration = True #if True, a calibration will be performed
        
        self.firstCalibration = False #if True, a first calibration was performed.
        
        self.VIDEOSOURCE = videosource
        self.CAM_WIDTH = width
        self.CAM_HEIGHT = height
        
        
        self.CV2THRESHOLD = configSphereVideoDetection.CV2_THRESHOLD  #binary threshold. A black pixel is only considered if its color is greater than 160
        
        #variables for keeping track of continuous movement.
        self.noiseFiltering = configSphereVideoDetection.NOISE_FILTERING_INITIAL_VALUE
        self.internalMovementCounter = 0 #counter, amount of cycles over which integration of movement is made.
        
        self.sleepTime = configSphereVideoDetection.MAIN_SLEEP_TIME #Main loop sleep time in ms
        self.movement_loopNumberSpan = configSphereVideoDetection.MOVEMENT_LOOPS_INTEGRATED #amount of main loops that movement is integrated into.
        self.movementThreshold = configSphereVideoDetection.MOVEMENT_THRESHOLD_INITIAL_VALUE #threshold, below this, we consider it noise.
        
        self.movementMethod = configSphereVideoDetection.MOVEMENT_METHOD_INITIAL_VALUE #Type of movement analysis method used.0=Accumulate time, 1= movementVector
        
        
        self.continuousMovementTime = 0 #amount of seconds that a continous movement was detected last time it moved or currently
        self.continuousIdleTime = 0 #amount of seconds that no movement was detected last time it ceased movement or currently
        self.isMoving = False #if true, it is currently in movement. False => currently idle
        
        self.movementVector = [] #binary vector, each loop adds 1 if moving, 0 otherwise
        self.movementVectorLength = configSphereVideoDetection.MOVEMENT_VECTOR_LENGTH
        
        self.last_saved_time_idle = timeit.default_timer() #will be used to check differences in time (determine idle time)
        self.last_saved_time_movement = timeit.default_timer() #will be used to check differences in time (determine mvnt time)
        
        #import camera parameters from file:
        import configCamera
        self.CAM_BRIGHTNESS_VAR = configCamera.CAM_BRIGHTNESS_VAR
        self.CAM_CONTRAST_VAR = configCamera.CAM_CONTRAST_VAR
        self.CAM_SATURATION_VAR = configCamera.CAM_SATURATION_VAR
        self.CAM_HUE_VAR = configCamera.CAM_HUE_VAR
        self.CAM_GAIN_VAR = configCamera.CAM_GAIN_VAR
        self.CAM_EXPOSURE_VAR = configCamera.CAM_EXPOSURE_VAR
        
        self.CAM_BRIGHTNESS_VALUE = configCamera.CAM_BRIGHTNESS_VALUE
        self.CAM_CONTRAST_VALUE = configCamera.CAM_CONTRAST_VALUE
        self.CAM_SATURATION_VALUE = configCamera.CAM_SATURATION_VALUE
        self.CAM_HUE_VALUE = configCamera.CAM_HUE_VALUE
        self.CAM_GAIN_VALUE = configCamera.CAM_GAIN_VALUE
        self.CAM_EXPOSURE_VALUE = configCamera.CAM_EXPOSURE_VALUE
        
        import threading
        # Create one non-blocking thread for capturing video Stream
        fred1 = threading.Thread(target=self.mainVideoDetection)
        fred1.start()
            
    def getAccumulatedVector(self):
        return [self.vectorAcumulado.x, self.vectorAcumulado.y]
    
    def resetX(self):
        self.vectorInstantaneo.x = 0
        self.vectorAcumulado.x = 0
        self.movEjeX = 0

    def resetY(self):
        self.vectorInstantaneo.y = 0
        self.vectorAcumulado.y = 0
        self.movEjeY = 0

    def getAccumX(self):
        return self.vectorAcumulado.x

    def getAccumY(self):
        return self.vectorAcumulado.y
    
    def getInstantX(self):
       return self.vectorInstantaneo.x
    
    def getInstantY(self):
        return self.vectorInstantaneo.y

    def calibrate(self):
        self.startCalibration = True
        
    def setNoiseFiltering(self, bool):
        #Set Noise FIltering: False if you DON'T want noise filtering , because you consider that your input video has no noise.
        self.noiseFiltering = bool

    def getMovementTime(self):
        #return the time in seconds that continuous movement was detected:
        #if it is moving, current time it is moving until now.
        #if it has stopped, amount of time it was moving before stopping.
        return self.continuousMovementTime
    
    def getIdleTime(self):
        #return the time in seconds that no movement was detected:
        #if it is moving, amount of time it was not moving before starting to move.
        #if it is not moving now, amount of time it is idle until now.
        return self.continuousIdleTime
    
    def manageCalibrationVariables(self, flag):
        #this method loads calibration variables from file, if the file exists.
        #else: it will create a file where the calibration will be saved.
        
        if (self.firstCalibration == True):
            #A first calibration was executed. So the user is asking for a re-calibration, which means
            #that the calibration file shouldn' be used.
            if (flag == 0):
                return False
        
        self.firstCalibration = True
        
        if (flag == 0):
            #Flag 0: Check whether calibration file exists or not.
            try:
                import calibrationCamera
                self.MIN_CIRCLE_MOVEMENT = calibrationCamera.MIN_CIRCLE_MOVEMENT
                self.MAX_CIRCLE_MOVEMENT = calibrationCamera.MAX_CIRCLE_MOVEMENT
                self.WORKING_MIN_CONTOUR_AREA = calibrationCamera.WORKING_MIN_CONTOUR_AREA
                self.WORKING_MAX_CONTOUR_AREA = calibrationCamera.WORKING_MAX_CONTOUR_AREA
                return True #True, calibration file was there.
            except:
                #probably: file doesn't exist.
                return False #False, calibration file was not there. A new one will be created AFTER calib. variables are determined"

        if (flag == 1):
            #flag 1: A new calibration file should be created. It will have the calibrated variables just determined.
            try:
                import os
                os.remove("../modules/calibrationCamera.py")
                os.remove("../modules/calibrationCamera.pyc")
                print "Previous calibrationCamera file exists. File erased."
            except:
                print "Error creating / erasing previous calibration file. Probably file does not exist."
                
            with open("../modules/calibrationCamera.py", "w") as text_file:
                    text_file.write("#This file has calibration variables for the camera \n")
                    text_file.write("#if this file exists, these values will be used in execution. Else, a new file \n")
                    text_file.write("#with calibration variables will be created and used. \n")
                    
                    text_file.write("MAX_CIRCLE_MOVEMENT = %d \n"%int(self.MAX_CIRCLE_MOVEMENT) )
                    text_file.write("MIN_CIRCLE_MOVEMENT = %d \n"%int(self.MIN_CIRCLE_MOVEMENT)  )
                    text_file.write("WORKING_MIN_CONTOUR_AREA = %d \n"%int(self.WORKING_MIN_CONTOUR_AREA)  )
                    text_file.write("WORKING_MAX_CONTOUR_AREA = %d \n"%int(self.WORKING_MAX_CONTOUR_AREA)  )
                    
                    print self.MAX_CIRCLE_MOVEMENT
                    print self.MIN_CIRCLE_MOVEMENT
                    print self.WORKING_MIN_CONTOUR_AREA
                    print self.WORKING_MAX_CONTOUR_AREA
                    
                    
                    print "calibration file overwritten."
                    return True #True, file was written OK
            return False #False, file couldn't be written (or it was written and it's status is unknown)
    
    
    def resetMovementTime(self):
        self.continuousMovementTime = 0
        self.last_saved_time_movement = timeit.default_timer() 
        
    def resetIdleTime(self):
        self.continuousIdleTime = 0
        self.last_saved_time_idle = timeit.default_timer()
    
    def setMovementThreshold(self, thres):
        #Movement threshold: how much "movement" between two frames should be considered as "movement"
        #Be careful changing this value, it is extremely sensitive.
        self.movementThreshold = int(thres)
    
    def getMovementThreshold(self):
        return int(self.movementThreshold)
    
    def getMovementStatus(self):
        return self.isMoving #true if right now it is moving, false otherwise.
    
    
    def Method_MovementVector(self):
        #Movement Vector method:
        #Each cycle, an element is added to movement vector.
        #If there are N past 1's in the vector, then it was moving and currently is. (includes certain 0's tolerance)
        #Else: it is idle.
        if (abs(self.vectorInstantaneo.x * self.vectorInstantaneo.x) +
                    abs(self.vectorInstantaneo.y * self.vectorInstantaneo.y)  >= self.movementThreshold):
            self.movementVector.append(1)
        else:
            self.movementVector.append(0)
    
    
    def Method_AccumulateTime(self):
                #this function analyzes continuous movement. If detected, saves the amount of seconds of the movement so far.
        #if idle is detected, it saves how much time the subject is idle.
        self.internalMovementCounter+=1
        
        if (self.internalMovementCounter >self.movement_loopNumberSpan):
            self.internalMovementCounter = 0
            logging.debug("   ----" + 
                            str(abs(self.vectorInstantaneo.x * self.vectorInstantaneo.x) +
                abs(self.vectorInstantaneo.y * self.vectorInstantaneo.y)) )
            if (abs(self.vectorInstantaneo.x * self.vectorInstantaneo.x) +
                    abs(self.vectorInstantaneo.y * self.vectorInstantaneo.y)  >= self.movementThreshold):
                    #print "It is currently moving"
                    if (self.isMoving == False):
                        #was idle, now started to move. We erase time movement counter and start from 0 now
                        self.continuousMovementTime = 0
                        self.isMoving = True
                        #CHECK SOLUTION FOR THE NEXT LINE.
                        self.last_saved_time_movement = timeit.default_timer() #this substracts the first loop movement
                    
                    
                    now = timeit.default_timer()
                    timeDif = (now - self.last_saved_time_movement)
                    if (timeDif < 0.001): #prevent from saving extremely low values (exp-10 etc..)
                        timeDif = 0
                    self.continuousMovementTime = timeDif
                    #self.last_saved_time_movement = timeit.default_timer()
                    self.vectorInstantaneo.x = 0
                    self.vectorInstantaneo.y = 0
            else:
                    #print "not moving"
                    if (self.isMoving == True):
                        #was moving and now it is not. We erase the old idle time counter, and we start counting idle time from 0
                        self.isMoving = False
                        self.continuousIdleTime = 0
                        self.last_saved_time_idle = timeit.default_timer()
                    now = timeit.default_timer()
                    timeDif = (now - self.last_saved_time_idle)
                    if (timeDif < 0.001): #prevent from saving extremely low values
                        timeDif = 0
                    self.continuousIdleTime = timeDif
                    #self.last_saved_time_idle = timeit.default_timer()
                    self.vectorInstantaneo.x = 0
                    self.vectorInstantaneo.y = 0
            logging.debug("Continuous: "+ str(self.continuousMovementTime) +"  ...  Idle: " + str(self.continuousIdleTime) )
    
    def continuousMovementAnalysis(self):
        if (self.movementMethod == 0):
            self.Method_AccumulateTime()
        
    def setMovementMethod(self, mthd):
        """set Movement Analysis method. There are:
            0- Accumulate time method (default): 
                Each main cycle, the continuous movement (or idle) time is updated. 
                If the status changes, the counter is restarted.
            1- Movement vector method:
                Each main cycle, an element is added to a vector. 1 if movement detected, 0 else.
                The program returns if there is "movement" and for how much time if the vector contains
                enough 1's and 0's, and considers the case where a nearly smooth movement was detected (1111011111)
            2- Many cycles integration method:
                Similar to 0, it integrates among many cycles, averaging the movement, making less probable
                to have a false negatives, but losses certain precision.
            3- Goodness of fit method:
                A movement vector, with non-binary values, is compared against a statistical model that predicts
                the subject movement. If the movement is similar to the statistical model, then it is moving.
        """
        try:
            methodNumber = int(mthd)
        except:
            return
        self.movementMethod = methodNumber
    
    def mainVideoDetection(self):
        import cv as cv
        import cv2
        import math
        import threading
        import socket
        import time
        import sys
        import os
        import signal
    
        """
            Programa de detección de movimiento:
            Se enciende y configura cámara.
            Por cada ciclo de programa, se compara el fotograma actual con el anterior.
                Si hay diferencias en el movimiento de un círculo particular (comparando
                si son iguales por el hecho de que hay colisión en el espacio 2D-tiempo)
                entonces añadir valor en el vector en el que este círculo se movió.
    """    
        CAM_NUMBER = 0 #cam number, 0 for integrated webcam, 1 for the next detected camera.
        
        #TCP_IP = 'localhost' #ip a donde conecto a socket
        #TCP_PORT = 50007 #puerto del socket
        #variables "de movimiento":
        #CAM_WIDTH = 640
        #CAM_HEIGHT = 480
        MIN_CONTOUR_AREA = 60 #min contour area to be valid, used in calibration
        MAX_CONTOUR_AREA = 2600 #max contour area to be valid , used in calibration
        self.WORKING_MIN_CONTOUR_AREA = 9999 #min contour area to be valid, used in every main loop
        self.WORKING_MAX_CONTOUR_AREA = 0 #max contour area to be valid, used in every main loop
        self.MIN_CIRCLE_MOVEMENT = 3 #mínima diferencia en movimiento del círculo para considerarlo como movimiento
        self.MAX_CIRCLE_MOVEMENT = 35 #máx diferencia en movimiento del círculo para considerarlo como movimiento
        
        #Inicio de programa: se declara como se captura video.
        print "Video Source: ", (self.VIDEOSOURCE)
        cam = cv2.VideoCapture(self.VIDEOSOURCE)
        
        #Opciones de ejecuciOn: 640x480 => 60 fps.
        cam.set(3,self.CAM_WIDTH)
        cam.set(4,self.CAM_HEIGHT)
        
        #set camera properties: this configuration is very dependent on the type and model of camera.
        
        cam.set(self.CAM_BRIGHTNESS_VAR,self.CAM_BRIGHTNESS_VALUE)
        cam.set(self.CAM_CONTRAST_VAR,self.CAM_CONTRAST_VALUE)
        cam.set(self.CAM_SATURATION_VAR,self.CAM_SATURATION_VALUE)
        cam.set(self.CAM_HUE_VAR,self.CAM_HUE_VALUE)
        cam.set(self.CAM_GAIN_VAR,self.CAM_GAIN_VALUE)
        cam.set(self.CAM_EXPOSURE_VAR,self.CAM_EXPOSURE_VALUE)
        print "camera: Width %r" % cam.get(3)
        print "camera: Height %r" % cam.get(4)
        #print "camera: FPS %r" % cam.get(5) #prints error for most cameras.
        print "camera: Brightness %r" % cam.get(self.CAM_BRIGHTNESS_VAR)
        print "camera: Contrast %r" % cam.get(self.CAM_CONTRAST_VAR)
        print "camera: Saturation %r" % cam.get(self.CAM_SATURATION_VAR)
        print "camera: Hue %r" % cam.get(self.CAM_HUE_VAR)
        print "camera: Gain %r" % cam.get(self.CAM_GAIN_VAR)
        print "camera: Exposure %r" % cam.get(self.CAM_EXPOSURE_VAR)
        
        
        time.sleep(0.2)
        """
        1-CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
        2-CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
        3-CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
        4-CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
        5-CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
        6-CV_CAP_PROP_FPS Frame rate.
        7-CV_CAP_PROP_FOURCC 4-character code of codec.
        8-CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
        9-CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
        10-CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
        11-CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
        12-CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
        13-CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
        14-CV_CAP_PROP_HUE Hue of the image (only for cameras).
        15-CV_CAP_PROP_GAIN Gain of the image (only for cameras).
        16-CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
        17-CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
        18-CV_CAP_PROP_WHITE_BALANCE Currently unsupported
        19-CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
        """
        
        if not cam:
            print "Error opening capture device"
            sys.exit(1)
        
        
        cv2.namedWindow(self.winName, cv2.CV_WINDOW_AUTOSIZE)
        
        # Se declaran unas imágenes, para inicializar correctamente cámara y variables.
        t_before = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
        t_now = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
        capturedImage = cam.read()[1]
        time.sleep(0.1)

        self.startCalibration = True
        Lnew = []
        while True:
                #===============================================================
                # #calibrate if necessary
                #===============================================================
                if (self.startCalibration == True):
                    if (self.manageCalibrationVariables(0) == False):
                        print "Calibration file missing. A new calibration file will be created.."
                        print "Recalibrating:"
                        t_calib = cv2.cvtColor(capturedImage, cv2.COLOR_RGB2GRAY)
                        cv.Smooth(cv.fromarray(t_calib), cv.fromarray(t_calib), cv.CV_BLUR, 3);
                        ret,thresh = cv2.threshold(t_calib,self.CV2THRESHOLD,255,cv2.THRESH_BINARY)
                        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                        #recorro los contornos capturando centros de los contornos cuando son englobados por un círculo
                        circleCenters = []
                        circleRadius = []
                        for cnt in contours:
                            (x,y),radius = cv2.minEnclosingCircle(cnt)
                            center = (int(x),int(y))
                            radius = int(radius)
                            if cv2.contourArea(cnt) > MIN_CONTOUR_AREA and cv2.contourArea(cnt) < MAX_CONTOUR_AREA: 
                                #áreas muy chicas pueden significar ruido que se mueve, mejor ignorarlo..
                                cv2.circle(capturedImage,center,radius,(0,255,0),2)
                                circleCenters.append(center)
                                circleRadius.append(radius)
                        expectedValue = 0
                        minRadius = 9999
                        maxRadius = 0
                        for i in range (0,10):
                            cv2.imshow( self.winName , capturedImage )
                            time.sleep(0.01)
                            key = cv2.waitKey(10)
                        for i in range(0, len(circleRadius)):
                            expectedValue +=  circleRadius[i]
                        
                        if len(circleCenters) > 0:
                          expectedValue /= len(circleCenters)
                        else:
                          expectedValue = 1
    
                        for i in range (0, len(circleCenters)):
                            if (circleRadius[i] > maxRadius and abs(circleRadius[i] - expectedValue)< expectedValue/2 ):
                                maxRadius = circleRadius[i]
                            if (circleRadius[i] < minRadius and abs(circleRadius[i] - expectedValue)< expectedValue/2):
                                minRadius = circleRadius[i]
    
                        if (self.noiseFiltering == False):
                            print "No noise filtering set."
                            self.MAX_CIRCLE_MOVEMENT = expectedValue*2
                            self.MIN_CIRCLE_MOVEMENT = expectedValue/8
                            minRadius = 1
                            if (self.MIN_CIRCLE_MOVEMENT > 2 and expectedValue > 15 and expectedValue < 35):
                                self.MIN_CIRCLE_MOVEMENT = 2
                        else:
                             self.MAX_CIRCLE_MOVEMENT = expectedValue*1.5
                             self.MIN_CIRCLE_MOVEMENT = expectedValue/5
                             if (self.MIN_CIRCLE_MOVEMENT > 2 and expectedValue > 15 and expectedValue < 35):
                                 self.MIN_CIRCLE_MOVEMENT = 2

                        self.WORKING_MIN_CONTOUR_AREA = minRadius * minRadius * 3.142 * 0.5
                        self.WORKING_MAX_CONTOUR_AREA = maxRadius * maxRadius * 3.142 * 1.3
                        
                        print "Number of samples: %d" % len(circleCenters)
                        print "Radius expected value: %d" % expectedValue
                        print "Minor Radius: %d" % minRadius
                        print "Major Radius: %d" % maxRadius
                        print "Max Circle Movement: %d" % int(self.MAX_CIRCLE_MOVEMENT)
                        print "Min Circle Movement: %d" % int(self.MIN_CIRCLE_MOVEMENT)
                        print "Min contour area: %d" % int(self.WORKING_MIN_CONTOUR_AREA)
                        print "Max contour area: %d" % int(self.WORKING_MAX_CONTOUR_AREA)
                        
                        if (self.manageCalibrationVariables(1) == False):
                            print "Error writting calibration file."
                        else:
                            print "Calibration file saved."
                        self.startCalibration = False
                    else:
                        #Calibration file exists, there is no need to calibrate.
                        print " - Calibration file exists. Using calibration file. - "
                        print "Max Circle Movement: %d" % int(self.MAX_CIRCLE_MOVEMENT)
                        print "Min Circle Movement: %d" % int(self.MIN_CIRCLE_MOVEMENT)
                        print "Min contour area: %d" % int(self.WORKING_MIN_CONTOUR_AREA)
                        print "Max contour area: %d" % int(self.WORKING_MAX_CONTOUR_AREA)
                        self.startCalibration = False
                        pass
                
                #===============================================================
                # # Preparo las imgs antigûa, actual y futura<>
                #===============================================================
                #capturedImage toma una captura para t_now, y para algunas geometrías que se dibujan encima de él.
                capturedImage = cam.read()[1]
                #t_before es el del anterior ciclo, t_now es el recién capturado (procesándolo 1ero..),
                
                #t_before = t_now #saves old matrix unnecessary since what is important from old matrix is the circle and point matrix
                t_now = cv2.cvtColor(capturedImage, cv2.COLOR_RGB2GRAY) #current matrix
                
                cv.Smooth(cv.fromarray(t_now), cv.fromarray(t_now), cv.CV_BLUR, 3);
                #cv.Smooth(cv.fromarray(t_now), cv.fromarray(t_now), cv.CV_GAUSSIAN, 3, 0);
                
                
                #===============================================================
                # #Recorrido1:
                #===============================================================
                #recorro los contornos capturando centros de los contornos cuando son englobados por un círculo
                Lbefore = Lnew #guardo vieja matriz de movimiento; actualizo la nueva
#                for cnt in contours:
#                    (x,y),radius = cv2.minEnclosingCircle(cnt)
#                    center = (int(x),int(y))
#                    radius = int(radius)
#                    if cv2.contourArea(cnt) > self.WORKING_MIN_CONTOUR_AREA and cv2.contourArea(cnt) < self.WORKING_MAX_CONTOUR_AREA: 
#                        #áreas muy chicas pueden significar ruido que se mueve, mejor ignorarlo..
#                        cv2.circle(capturedImage,center,radius,(0,255,0),2)
#                        L.append(center)
                
                #===============================================================
                # #Proceso la imagen actual: t_now    
                #===============================================================
                ret,thresh = cv2.threshold(t_now,self.CV2THRESHOLD,255,cv2.THRESH_BINARY)
                contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                
                #===============================================================
                # #Recorrido2:
                #===============================================================
                #recorro los contornos NUEVAMENTE, capturando centros. Esta vez, para el frame "futuro"
                Lnew = []
                for cnt in contours:
                    (x, y), radius = cv2.minEnclosingCircle(cnt)
                    center = (int(x), int(y))
                    radius = int(radius)
                    # a continuaciOn, si el contorno tiene suficiente área, pero también si no es TAN grande:
                    if cv2.contourArea(cnt) > self.WORKING_MIN_CONTOUR_AREA and cv2.contourArea(cnt) < self.WORKING_MAX_CONTOUR_AREA:
                        cv2.circle(capturedImage, center, radius, (0, 255, 0), 2)
                        Lnew.append(center)
                #===============================================================
                # #analizo si hay colisiones en el espacio 2D-tiempo
                #===============================================================
                
                #Si las hubiera, voy sumando contribuciones para ver hacia donde apunta el movimiento medio.
                #Se analizan ambos versores del vector en el plano bidireccional:
                self.movEjeX = 0
                self.movEjeY = 0
                numberOfVectors = 1
                
                for index in range(len(Lnew)):
                    for j in range(index, len(Lbefore)):
                        if (math.sqrt((Lnew[index][0] - Lbefore[j][0]) ** 2 + (Lnew[index][1] - Lbefore[j][1]) ** 
                          2)) <= self.MAX_CIRCLE_MOVEMENT and (math.sqrt((Lnew[index][0] - Lbefore[j][0]) ** 
                          2 + (Lnew[index][1] - Lbefore[j][1]) **2)) >= self.MIN_CIRCLE_MOVEMENT:
                            #print "Hay colisión: %d %d" % (index,j)
                            cv2.circle(capturedImage, (Lnew[index][0], Lnew[index][1]),3,(0,0,255),2)
                            cv2.line(capturedImage, (Lnew[index][0], Lnew[index][1]),(Lbefore[j][0], Lbefore[j][1]), (0,255,0), 5)
                            
                            
                            #se suma a todos los desplazamientos (en x, en y).
                            self.movEjeY+=Lnew[index][1] - Lbefore[j][1]
                            numberOfVectors+=1
                            self.movEjeX+= Lnew[index][0] - Lbefore[j][0]
                            #print "colisión entre %r -y- %r :: %r %r ::: " % (index, j, Lnew[index], Lbefore[j])
                
                #we divide each instant vector components by N, to obtain average instant vector.
                if (numberOfVectors == 0):
                    numberOfVectors = 1
                
                self.movEjeX /= numberOfVectors  # movimiento x promedio, ponderación de todos los movimientos en x.
                self.movEjeY /= numberOfVectors  # movimiento y promedio, ponderación de todos los movimientos en y.
                
                self.vectorAcumulado.x += self.movEjeX
                self.vectorAcumulado.y += self.movEjeY
                
                self.vectorInstantaneo.x += self.movEjeX  # suma contrib. x en este ciclo (se establece a 0 en otro método)
                self.vectorInstantaneo.y += self.movEjeY  # suma contrib. y en este ciclo (se establece a 0 en otro método)
                
                # se analiza continuidad de movimiento en función:
                self.continuousMovementAnalysis()
                
                
                #===============================================================
                # se "muestra" el resultado al usuario (feedback)
                #===============================================================
                cv2.imshow( self.winName , capturedImage ) #obs.: NO es estrictamente necesario dar feedback acá.. también está mainFunction
                #(imshow se puede sacar si el CPU es un problema.)
                
                #===============================================================
                # #para finalizar programa, usuario presiona "Escape":
                #===============================================================
                key = cv2.waitKey(self.sleepTime)
                if (key == 27 or key==1048603): #escape pressed
                    #end Program.
                    cam.release()
                    cv2.destroyWindow(self.winName)
                    os.kill(os.getpid(), signal.SIGINT)
                    sys.exit()
                
################################################################
#Prueba unitaria de la clase si es ejecutada independientemente:
################################################################


if __name__ == '__main__':
    #Crea un objeto de captura de video, imprime 'x' e 'y' del vector movimiento detectado de forma acumulada.
    try:
        from configvideo import *
    except ImportError:
        print "File configvideo.py doesn't exist"
    except:
        print "Error with configVideo"
    
    videoDet = sphereVideoDetection(VIDEOSOURCE,CAM_WIDTH, CAM_HEIGHT)
    videoDet.setNoiseFiltering(True)
    import time
    #time.sleep(2)
    #videoDet.setNoiseFiltering(False)
    #videoDet.calibrate()
    
    while(True):
        #print "x:  "+str(videoDet.getAccumX())
        #print "y:  "+str(videoDet.getAccumY()) #<>
        print "Continuous movement time: %r    Idle movement time: %r   IsMoving: %r"  % (videoDet.getMovementTime() , videoDet.getIdleTime(), videoDet.getMovementStatus())
        time.sleep(0.3)

"""
if __name__ == '__main__':
    #ver http://stackoverflow.com/questions/12376224/python-threading-running-2-different-functions-simultaneously
    #import threading
    #import threading
    # Create two threads, one for video Detection, the other with the game per se.
    #fred1 = threading.Thread(target=mainFunction)
    #fred1.start()
    
    #fred2 = threading.Thread(target=mainVideoDetection)
    #fred2.start()
    print "prueba ejecutada."
    try:
        from configvideo import *
    except ImportError:
        print "No existe el archivo configvideo.py"
    except:
        print "otro error"
    videoDet = sphereVideoDetection(VIDEOSOURCE,CAM_WIDTH, CAM_HEIGHT)
    
    
    import time
    try:
    import valve
    except:
    print "error importing Valve"
    while(True):
    time.sleep(2)
    print "x:  "+str(videoDet.getAccumX())
    print "y:  "+str(videoDet.getAccumY()) #<>
    if (abs(videoDet.getAccumX()) > 100  or abs(videoDet.getAccumY()) > 100):
        #resetear lo acumulado:
        videoDet.resetX()
        videoDet.resetY()
        #abrir la válvula
        print "abro VAlvula"
        val1 = valve.Valve()
        val1.open()
        time.sleep(0.2)
        val1.close()
        time.sleep(0.2)
        print "fin apertura vAlvula"
"""
