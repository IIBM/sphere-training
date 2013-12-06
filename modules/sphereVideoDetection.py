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



class sphereVideoDetection():

	def __init__ (self,videosource, width=640, height=480) :
		    self.winName = "Track-bola - Video Detection"
		    import threading
		    # Create one non-blocking thread for capturing video Stream
		    fred1 = threading.Thread(target=self.mainVideoDetection)
		    fred1.start()
		    #declare self variables to use.
		    import track_bola_utils
		    self.vectorInstantaneo = track_bola_utils.vectorSimple() #cummulative vector
		    
	def resetCumX(self):
		self.vectorInstantaneo.x = 0

	def resetCumY(self):
		self.vectorInstantaneo.y = 0

	def getCumX(self):
		return self.vectorInstantaneo.x

	def getCumY(self):
		return self.vectorInstantaneo.y

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
		Se enciende timer de socket para enviar datos de mouse.
		Se enciende y configura cámara.
		Por cada ciclo de programa, se compara el fotograma actual con el anterior.
		    Si hay diferencias en el movimiento de un círculo particular (comparando
		    si son iguales por el hecho de que hay colisión en el espacio 2D-tiempo)
		    entonces añadir valor en el vector en el que este círculo se movió.
		    En cada ciclo se envía por socket.
	"""    
	    CAM_NUMBER = 0 #cam number, 0 for integrated webcam, 1 for the next detected camera.
	    
	    #TCP_IP = 'localhost' #ip a donde conecto a socket
	    #TCP_PORT = 50007 #puerto del socket
	    #variables "de movimiento":
	    CAM_WIDTH = 640
	    CAM_HEIGHT = 480
	    MIN_CONTOUR_AREA = 60 #mínimo área del contorno para que sea válido.
	    MAX_CONTOUR_AREA = 2600 #máximo área del contorno para que sea válido.
	    WORKING_MIN_CONTOUR_AREA = 9999 #ídem pero calibrado para situación actual
	    WORKING__CONTOUR_AREA = 0 #ídem pero calibrado para situación actual
	    MIN_CIRCLE_MOVEMENT = 3 #mínima diferencia en movimiento del círculo para considerarlo como movimiento
	    MAX_CIRCLE_MOVEMENT = 35 #máx diferencia en movimiento del círculo para considerarlo como movimiento
	    
	    #Timer, envIa por socket algunas coordenadas de acuerdo a si hay movimiento.
	    #socketTmr = threading.Timer(4.0, socketTimer)
	    #socketTmr.start() # luego de 4 segundos arranca.
	    
	    #Inicio de programa: se declara como se captura video.
	    #cam = cv2.VideoCapture("../files_movement/videos_prueba/slow_izquierda.avi")
	    #cam = cv2.VideoCapture("../files_movement/videos_prueba/fast_diag1.avi")
	    #cam = cv2.VideoCapture("../files_movement/videos_prueba/video_distorted2.avi")
	    #cam = cv2.VideoCapture("../files_movement/videos_prueba/video_webm.avi")
	    #cam = cv2.VideoCapture("../files_movement/videos_prueba/abajo_y_arriba_2.avi")
	    cam = cv2.VideoCapture(CAM_NUMBER)
	    
	    #Opciones de ejecuciOn: 640x480 => 60 fps.
	    cam.set(3,CAM_WIDTH)
	    cam.set(4,CAM_HEIGHT)
	    time.sleep(0.5)
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
	    
	    if not cam:
		print "Error opening capture device"
		sys.exit(1)

	    
	    #Nombre: track-bola
	    cv2.namedWindow(self.winName, cv2.CV_WINDOW_AUTOSIZE)
	    
	    # Se declaran unas imágenes, para inicializar correctamente cámara y variables.
	    t_current = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
	    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
	    calibrar = True
	    time.sleep(1.5)
	    #################################################################
	    ###    CALIBRACIÓN  ##
	    #################################################################
	    print "Calibrando"
	    im = cam.read()[1]
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
		if cv2.contourArea(cnt) > MIN_CONTOUR_AREA and cv2.contourArea(cnt) < MAX_CONTOUR_AREA: 
		    #áreas muy chicas pueden significar ruido que se mueve, mejor ignorarlo..
		    cv2.circle(im,center,radius,(0,255,0),2)
		    circleCenters.append(center)
		    circleRadius.append(radius)
		  
	    expectedValue = 0
	    minRadius = 9999
	    maxRadius = 0
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
	    time.sleep(4)
	    print "Fin calibración."
	    calibrar = False
	    #################################################################
	    ######### fin calibración
	    #################################################################
	    
	    while True:
		###########################################<>
		# Preparo las imgs antigûa, actual y futura
		###########################################
		
		#im toma una captura para t_plus, y para algunas geometrías que se dibujan encima de él.
		im = cam.read()[1]
		
		#t_current es el del anterior ciclo, t_plus es el recién capturado (procesándolo 1ero..),
		t_current = t_plus
		t_plus = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
		
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
		        if (math.sqrt((Lnuevo[index][0] - L[j][0]) ** 2 + (Lnuevo[index][1] - L[j][1]) **
		                       2)) <= MAX_CIRCLE_MOVEMENT and (math.sqrt((Lnuevo[index][0] - L[j][0]) ** 2 + (Lnuevo[index][1] - L[j][1]) **
		                                                 2)) >= MIN_CIRCLE_MOVEMENT:
		            #print "Hay colisión: %d %d" % (index,j)
		            cv2.circle(im, (Lnuevo[index][0], Lnuevo[index][1]),3,(0,0,255),2)
		            cv2.line(im, (Lnuevo[index][0], Lnuevo[index][1]), (L[j][0], L[j][1]), (0,255,0), 5)
		            
		            
		            #Condición para que se procese la colisión: esté en la mitad inferior. (ver doc.)
		            movEjeY+=Lnuevo[index][1] - L[j][1]
		            numberOfVectors+=1
		            if (Lnuevo[index][1] > CAM_HEIGHT / 2):
		                movEjeX+= Lnuevo[index][0] - L[j][0]
		            #print "colisión entre %r -y- %r :: %r %r ::: " % (index, j, Lnuevo[index], L[j])
		
		#falta dividir las componentes del vector obtenido, dividiendo por N, para obtener vector Instantáneo
		movEjeX /= numberOfVectors
		movEjeY /= numberOfVectors
		global vectorInstantaneo
		self.vectorInstantaneo.x += movEjeX
		self.vectorInstantaneo.y += movEjeY
		
		#Se tiene el vector instantáneo para este fotograma: vectorInstantáneo = (movEjeX, movEjeY)
		#print ("(%d %d .. %d)"%(movEjeX, movEjeY, numberOfVectors))
		        
		#finalmente se "muestra" el resultado al usuario (feedback)
		cv2.imshow( self.winName , im ) #obs.: NO es estrictamente necesario dar feedback acá.. también está mainFunction
		#(imshow se puede sacar si el CPU es un problema.)
		
		time.sleep(0.01)
		
		#para finalizar programa, usuario presiona "Escape":
		key = cv2.waitKey(10)
		if (key == 27 or key==1048603): #escape pressed
		    #end Program.
		    cv2.destroyWindow(self.winName)
		    os.kill(os.getpid(), signal.SIGINT)
		    sys.exit()






if __name__ == '__main__':
    #ver http://stackoverflow.com/questions/12376224/python-threading-running-2-different-functions-simultaneously
    #import threading
    #import threading
    # Create two threads, one for video Detection, the other with the game per se.
    #fred1 = threading.Thread(target=mainFunction)
    #fred1.start()
    
    #fred2 = threading.Thread(target=mainVideoDetection)
    #fred2.start()
    videoDet = sphereVideoDetection(0,0)
    print "prueba ejecutada."
    import valve
    import time
    val1 = valve.Valve()
    while(True):
	print "x:  "+str(videoDet.getCumX())
	print "y:  "+str(videoDet.getCumY()) #<>
	if (abs(videoDet.getCumX()) > 80  or abs(videoDet.getCumY()) > 80):
		#resetear lo acumulado:
		videoDet.resetCumX()
		videoDet.resetCumY()
		#abrir la válvula
		print "abro VAlvula"

		val1.open()
		time.sleep(1)
		val1.close()
		time.sleep(0.2)

