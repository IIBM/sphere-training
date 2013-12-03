# -*- coding: utf-8 -*-

import cv as cv
import cv2
import math
#import threading
#import socket
import time
import sys
import os
import signal

class spherevideotracker():
    def __init__ (self,videosource, width=640, height=480) :

        self.cam = cv2.VideoCapture(videosource)
        if not self.cam:
            print "Error opening capture device"
            sys.exit(1)

        #Nombre: Movement Indicator
        self.winName = "Track-bola - Video Detection"
        self.cam.set(3,width)
        self.cam.set(4,height)
        self.width = width
        self.height = height
        time.sleep(0.5)
        self.movEjeX = 0
        self.movEjeY = 0
        self.movCumEjeX = 0
        self.movCumEjeY = 0
        self.fps = 30 # if not other info, asume fps = 30
        self.MIN_CONTOUR_AREA = 60 #mínimo área del contorno para que sea válido.
        self.MAX_CONTOUR_AREA = 2600 #máximo área del contorno para que sea válido.

    def getState(self) :
      return [self.movEjeX, self.movEjeY]

    def getCumState(self) :
      a = self.movCumEjeX
      b = self.movCumEjeY
      self.movCumEjeX = 0
      self.movCumEjeY = 0
      return [a, b]

    def startcapture(self):
        """
            Programa de detección de movimiento:
            Se enciende y configura cámara.
            Por cada ciclo de programa, se compara el fotograma actual con el anterior.
            Si hay diferencias en el movimiento de un círculo particular (comparando
            si son iguales por el hecho de que hay colisión en el espacio 2D-tiempo)
            entonces añadir valor en el vector en el que este círculo se movió.
            En cada ciclo se actualiza un "vector movimiento". El vector promedio resultante
            se lee en el main() para actualizar la posición del personaje.
        """
        
        #Timer, envIa por socket algunas coordenadas de acuerdo a si hay movimiento.
        #socketTmr = threading.Timer(4.0, socketTimer)
        #socketTmr.start() # luego de 4 segundos arranca.
        
        
        #Opciones de ejecuciOn: 640x480 => 60 fps.

        """
        CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
        CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
        CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
        CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
        CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
        CV_CAP_PROP_FPS Frame rate.
        CV_CAP_PROP_FOURCC 4-character code of codec.
        CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
        CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
        CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
        CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
        CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
        CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
        CV_CAP_PROP_HUE Hue of the image (only for cameras).
        CV_CAP_PROP_GAIN Gain of the image (only for cameras).
        CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
        CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
        CV_CAP_PROP_WHITE_BALANCE Currently unsupported
        CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
        """
        

        
        #Nombre: Movement Indicator
        cv2.namedWindow(self.winName, cv2.CV_WINDOW_AUTOSIZE)

        im = self.cam.read()[1]

        t_calib = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
        cv.Smooth(cv.fromarray(t_calib), cv.fromarray(t_calib), cv.CV_BLUR, 3);
        #ret,thresh = cv2.threshold(t_calib,127,255,cv2.THRESH_BINARY)
        ret,thresh = cv2.threshold(t_calib,50,255,cv2.THRESH_BINARY)
        #Tomo los contornos (lo importante para analizar)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
        #recorro los contornos capturando centros de los contornos cuando son englobados por un círculo
        circleCenters = []
        circleRadius = []
        for i in range(0,len(contours)):
            cnt = contours[i]
            (x,y),radius = cv2.minEnclosingCircle(cnt)
            center = (int(x),int(y))
            radius = int(radius)
            if cv2.contourArea(cnt) > self.MIN_CONTOUR_AREA and cv2.contourArea(cnt) < self.MAX_CONTOUR_AREA: 
                #áreas muy chicas pueden significar ruido que se mueve, mejor ignorarlo..
                cv2.circle(im,center,radius,(0,255,0),2)
                circleCenters.append(center)
                circleRadius.append(radius)
              
        expectedValue = 0
        minRadius = 9999
        maxRadius = 0

        #TODO cual es el objeto de esto???
        for i in range (0,10):
            cv2.imshow( self.winName , im )
            time.sleep(0.01)
            key = cv2.waitKey(10)

        for i in range(0, len(circleRadius)):
            expectedValue +=  circleRadius[i]
             
        expectedValue /= len(circleCenters)
        for i in range (0, len(circleCenters)):
            if (circleRadius[i] > maxRadius and abs(circleRadius[i] - expectedValue)< expectedValue/2 ):
                maxRadius = circleRadius[i]
            if (circleRadius[i] < minRadius and abs(circleRadius[i] - expectedValue)< expectedValue/2):
                minRadius = circleRadius[i]
        MAX_CIRCLE_MOVEMENT = expectedValue*1.5
        MIN_CIRCLE_MOVEMENT = expectedValue/5
        if (MIN_CIRCLE_MOVEMENT > 2 and expectedValue > 15 and expectedValue < 35):
            MIN_CIRCLE_MOVEMENT = 2
        print "Número de muestras: %d" % len(circleCenters)
        print "Valor Esperado: %d" % expectedValue
        print "Radio menor: %d" % minRadius
        print "Radio mayor: %d" % maxRadius
        print "Círculo Máximo de movimiento: %d" % MAX_CIRCLE_MOVEMENT
        print "Círculo Mínimo de movimiento: %d" % MIN_CIRCLE_MOVEMENT
        WORKING_MIN_CONTOUR_AREA = minRadius * minRadius * 3.142 * 0.7
        WORKING_MAX_CONTOUR_AREA = maxRadius * maxRadius * 3.142 * 1.3
        time.sleep(.5)
        print "Fin calibración."
        self.calibrated = True
        #################################################################
        ######### fin calibración
        #################################################################

        # Se declaran unas imágenes, para inicializar correctamente cámara y variables.
        t_current = cv2.cvtColor(self.cam.read()[1], cv2.COLOR_RGB2GRAY)
        t_plus = cv2.cvtColor(self.cam.read()[1], cv2.COLOR_RGB2GRAY)

        time.sleep(1.5)

        while True:
            ###########################################<>
            # Preparo las imgs antigûa, actual y futura
            ###########################################
            
            #im toma una captura para t_plus, y para algunas geometrías que se dibujan encima de él.
            im = self.cam.read()[1]
            
            #t_current es el del anterior ciclo, t_plus es el recién capturado (procesándolo 1ero..),
#            if im.any():
            t_plus = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
#            else:
#                print "FIN"
            
            cv.Smooth(cv.fromarray(t_plus), cv.fromarray(t_plus), cv.CV_BLUR, 3);
            #cv.Smooth(cv.fromarray(t_plus), cv.fromarray(t_plus), cv.CV_GAUSSIAN, 3, 0);
            
            #############################
            #Proceso la imagen "antigUa": t_current
            #############################
            ret,thresh = cv2.threshold(t_current,50,255,cv2.THRESH_BINARY)
            #Tomo los contornos (lo importante para analizar)
            contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            
            ############
            #Recorrido1:
            ############
            #recorro los contornos capturando centros de los contornos cuando son englobados por un círculo
            L = []
            for i in range(0,len(contours)):
                cnt = contours[i]
                (x,y),radius = cv2.minEnclosingCircle(cnt)
                center = (int(x),int(y))
                radius = int(radius)
                if cv2.contourArea(cnt) > WORKING_MIN_CONTOUR_AREA and cv2.contourArea(cnt) < WORKING_MAX_CONTOUR_AREA: 
                    #áreas muy chicas pueden significar ruido que se mueve, mejor ignorarlo..
                    cv2.circle(im,center,radius,(0,255,0),2)
                    L.append(center)
            
            #############################
            #Proceso la imagen "futura": t_plus
            #############################        
            ret,thresh = cv2.threshold(t_plus,50,255,cv2.THRESH_BINARY)
            contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            
            ############
            #Recorrido2:
            ############
            #recorro los contornos NUEVAMENTE, capturando centros. Esta vez, para el frame "futuro"
            Lnuevo = []
            for i in range(0,len(contours)):
                cnt = contours[i]
                (x,y),radius = cv2.minEnclosingCircle(cnt)
                center = (int(x),int(y))
                radius = int(radius)
                #a continuaciOn, si el contorno tiene suficiente área, pero también si no es TAN grande:
                if cv2.contourArea(cnt) > WORKING_MIN_CONTOUR_AREA and cv2.contourArea(cnt) < WORKING_MAX_CONTOUR_AREA:
                    cv2.circle(im,center,radius,(0,255,0),2)
                    Lnuevo.append(center)
            
            
            ##################################################
            #analizo si hay colisiones en el espacio 2D-tiempo
            ##################################################
            
            #Si las hubiera, voy sumando contribuciones para ver hacia donde apunta el movimiento medio.
            #Se analizan ambos versores del vector en el plano bidireccional:
            movEjeX=0
            movEjeY=0
            numberOfVectors=1
            
            for index in range(len(Lnuevo)):
                for j in range(index, len(L)):
                    if (math.sqrt((Lnuevo[index][0] - L[j][0]) ** 2 + (Lnuevo[index][1] - L[j][1]) ** 2)) <= MAX_CIRCLE_MOVEMENT and (math.sqrt((Lnuevo[index][0] - L[j][0]) ** 2 + (Lnuevo[index][1] - L[j][1]) ** 2)) >= MIN_CIRCLE_MOVEMENT:
                        #print "Hay colisión: %d %d" % (index,j)
                        cv2.circle(im, (Lnuevo[index][0], Lnuevo[index][1]),3,(0,0,255),2)
                        cv2.line(im, (Lnuevo[index][0], Lnuevo[index][1]), (L[j][0], L[j][1]), (0,255,0), 5)
                        
                        
                        #Condición para que se procese la colisión: esté en la mitad inferior. (ver doc.)
                        movEjeY+=Lnuevo[index][1] - L[j][1]
                        numberOfVectors+=1
                        if (Lnuevo[index][1] > self.height / 2):
                            movEjeX+= Lnuevo[index][0] - L[j][0]
                        #print "colisión entre %r -y- %r :: %r %r ::: " % (index, j, Lnuevo[index], L[j])
            
            #falta dividir las componentes del vector obtenido, dividiendo por N, para obtener vector Instantáneo
            movEjeX /= numberOfVectors
            movEjeY /= numberOfVectors

            self.movEjeX = movEjeX
            self.movEjeY = movEjeY
            self.movCumEjeX += movEjeX
            self.movCumEjeY += movEjeY

            #Se tiene el vector instantáneo para este fotograma: vectorInstantáneo = (movEjeX, movEjeY)
            #print ("(%d %d .. %d)"%(movEjeX, movEjeY, numberOfVectors))
                    
            #finalmente se "muestra" el resultado al usuario (feedback)
            cv2.imshow( self.winName , im ) #obs.: NO es estrictamente necesario dar feedback acá.. también está mainFunction
            #(imshow se puede sacar si el CPU es un problema.)
            
            #para finalizar programa, usuario presiona "Escape":
            delayMS = int((1.0/self.fps)*1000)
            delayMS = int(5)
            key = cv2.waitKey(delayMS) #in miliseconds
            if (key == 27 or key==1048603): #escape pressed
                #end Program.
                cv2.destroyWindow(self.winName)
                os.kill(os.getpid(), signal.SIGINT)
                sys.exit()
#        except:
#          cv2.destroyWindow(self.winName)
#          os.kill(os.getpid(), signal.SIGINT)
#          sys.exit()


if __name__ == '__main__':
    try:
        from configvideo import *
    except ImportError:
        print "No existe el archivo configvideo.py"
    except:
        print "otro error"

    sp = spherevideotracker(VIDEOSOURCE,CAM_WIDTH,CAM_HEIGHT)
    import threading
    fread = threading.Thread(target=sp.startcapture)
    fread.start()
    time.sleep(2)

    while(1):
        a = sp.getCumState()
        print "x = "+str(a[0])+" | y = " + str(a[1])
        time.sleep(.2)

    
