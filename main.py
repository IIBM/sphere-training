# -*- coding: utf-8 -*-

######################################################
####################
#track-bola v0.1:
####################
#Se toma como entrada un flujo de video (webcam o archivo de video), se procesan y detectan círculos negros para
#mover un entorno virtual (Laberinto tipo T).
######################################################


import pygame
from pygame.locals import *

fps = 8 #frames per second
CYCLE_LOOP_NUMBER = 2 #cantidad de ciclos que deben pasar para que se ejecuten los movimientos en el mapa 3D
                      #más ciclos => más lento update pero menos rebote..

worldMap =[
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
  [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
  [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
  [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
  [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
  [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
  [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
  [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
  [2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2],
  [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
];

sprite_positions=[
  (20.5, 11.5, 2), #green light in front of playerstart
  #green lights in every room
  (18.5,4.5, 2),
  (10.0,4.5, 2),
  (10.0,12.5,2),
  (3.5, 6.5, 2),
  (3.5, 20.5,2),
  (3.5, 14.5,2),
  (14.5,20.5,2),
]

def mainFunction():
    ##########################################################
    #Función principal, en cada iteración actualiza el render del laberinto. 
    #Mueve al personaje según el resultado
    #de la función de captura de video.
    ##########################################################
    
    import math
    import worldManager
    import time
    
    t = time.clock() #time of current frame
    oldTime = 0. #time of previous frame
    pygame.mixer.init()
    #pygame.mixer.music.load("MuseUprising.mp3")
    #pygame.mixer.music.play(-1)
    size = w, h = 640,480
    pygame.init()
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Track-bola - v"+str(CURRENT_VERSION))
    screen = pygame.display.get_surface()
    #pixScreen = pygame.surfarray.pixels2d(screen)
    pygame.mouse.set_visible(True)
    clock = pygame.time.Clock()
    
    f = pygame.font.SysFont(pygame.font.get_default_font(), 20)
    
    #wm = worldManager.WorldManager(worldMap,sprite_positions, 12, 11.5, -1, 0, 0, .66)
    wm = worldManager.WorldManager(worldMap,sprite_positions, 40, 11.5, -1, 0, 0, .66)
    
    weapons = [Weapon("fist"),
               Weapon("pistol"),
               Weapon("shotgun"),
               Weapon("dbshotgun"),
               Weapon("chaingun"),
               Weapon("plasma"),
               Weapon("rocket"),
               Weapon("bfg"),
               Weapon("chainsaw")
               ]
    weapon_numbers = [K_1,K_2,K_3,K_4,K_5,K_6,K_7,K_8,K_0]
    weapon = weapons[0]
    
    #################################################################
    #declaro unas variables útiles para calcular deltas de movimiento
    #################################################################
    xmouse=10
    xoldmouse=10
    ymouse=10
    yoldmouse=10
    contadorm=CYCLE_LOOP_NUMBER
    firstRun=True
    #t = threading.Timer(4.0, socketTimer)
    #t.start() # luego de 4 segundos arranca.
    time.sleep(0.5)
    
    
    while(True):
        clock.tick(60)
        
        wm.draw(screen)
        
        # timing for input and FPS counter
        
        frameTime = float(clock.get_time()) / 1000.0 # frameTime is the time this frame has taken, in seconds
        t = time.clock()
        text = f.render(str(clock.get_fps()), False, (255, 255, 0))
        screen.blit(text, text.get_rect(), text.get_rect())
        weapon.draw(screen, t)
        pygame.display.flip()

        # speed modifiers MODIFICADOS PARA PROYECTO MOUSE
        #moveSpeed = frameTime * 6.0 # the constant value is in squares / second
        #rotSpeed = frameTime * 2.0 # the constant value is in radians / second
        moveSpeed = frameTime * 1.6 # the constant value is in squares / second
        rotSpeed = frameTime * 0.4 # the constant value is in radians / second
        
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                os.kill(os.getpid(), signal.SIGINT)
                sys.exit()
                return 
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    os.kill(os.getpid(), signal.SIGINT)
                    sys.exit()
                    return
                elif event.key == K_LCTRL:
                    pygame.mixer.music.load("alarm2.mp3")
                    pygame.mixer.music.play(1)
                elif event.key == K_SPACE:
                    #shoot
                    #weapon.play()
                #elif event.key == K_H: VER CUAL K ES PARA PYTHON
                    #Reproducir sonido.
                    pygame.mixer.music.load("alarm1.mp3")
                    pygame.mixer.music.play(1)
                elif event.key in weapon_numbers:
                    weapon.stop()
                    weapon = weapons[weapon_numbers.index(event.key)]
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    weapon.stop()
            else:
                pass 
        ############################################
        # EDICIÓN PARA PROYECTO DISPOSITIVO MOUSE
        ############################################
        
        #cada CYCLE_LOOP_NUMBER ciclos, se ejecutan acciones de movimiento en el mapa 3D
        if contadorm==CYCLE_LOOP_NUMBER:
          ################################
          #comandos ejecutados una sola vez.
          ################################
          """
          if (firstRun is True):
              #esto lo hago para "enderezar" la vista; sin esto aparece inicialmente torcido (un detalle)
              oldDirX = wm.camera.dirx
              wm.camera.dirx = wm.camera.dirx * math.cos(- rotSpeed) - wm.camera.diry * math.sin(- rotSpeed)
              wm.camera.diry = oldDirX * math.sin(- rotSpeed) + wm.camera.diry * math.cos(- rotSpeed)
              oldPlaneX = wm.camera.planex
              wm.camera.planex = wm.camera.planex * math.cos(- rotSpeed) - wm.camera.planey * math.sin(- rotSpeed)
              wm.camera.planey = oldPlaneX * math.sin(- rotSpeed) + wm.camera.planey * math.cos(- rotSpeed)
              firstRun=False
          """
          ################################
          #Analizo vector Instantáneo
          ################################
          #--------------- procesamiento de los valores normales de operación ----------------
          global vectorInstantaneo
          #print "Se ve en main: (%d, %d)"%(vectorInstantaneo.x, vectorInstantaneo.y)
          #falta hacer el tema de intensidad por vector.
          #falta disminuir lo más que se pueda el delay.
          #falta CALIBRAR.
          if vectorInstantaneo.x < 0:
                  #for each rotation unit divided by 30 (maximum vector module allowed)
                  # rotate to the left
                  # both camera direction and camera plane must be rotated
                  for ind in range(0,-vectorInstantaneo.x):
                      oldDirX = wm.camera.dirx
                      wm.camera.dirx = wm.camera.dirx * math.cos(rotSpeed) - wm.camera.diry * math.sin(rotSpeed)
                      wm.camera.diry = oldDirX * math.sin(rotSpeed) + wm.camera.diry * math.cos(rotSpeed)
                      oldPlaneX = wm.camera.planex
                      wm.camera.planex = wm.camera.planex * math.cos(rotSpeed) - wm.camera.planey * math.sin(rotSpeed)
                      wm.camera.planey = oldPlaneX * math.sin(rotSpeed) + wm.camera.planey * math.cos(rotSpeed)

          if vectorInstantaneo.y < 0:
                  #print "movió arriba"
                  # move forward if no wall in front of you
                  for ind in range(0,-vectorInstantaneo.y):
                      moveX = wm.camera.x + wm.camera.dirx * moveSpeed
                      if(worldMap[int(moveX)][int(wm.camera.y)]==0 and worldMap[int(moveX + 0.1)][int(wm.camera.y)]==0):
                          wm.camera.x += wm.camera.dirx * moveSpeed
                      moveY = wm.camera.y + wm.camera.diry * moveSpeed
                      if(worldMap[int(wm.camera.x)][int(moveY)]==0 and worldMap[int(wm.camera.x)][int(moveY + 0.1)]==0):
                          wm.camera.y += wm.camera.diry * moveSpeed
                  
          if vectorInstantaneo.x > 0:
                  #print "movió derecha"
                  # rotate to the right
                  # both camera direction and camera plane must be rotated
                  for ind in range(0,vectorInstantaneo.x):
                      oldDirX = wm.camera.dirx
                      wm.camera.dirx = wm.camera.dirx * math.cos(- rotSpeed) - wm.camera.diry * math.sin(- rotSpeed)
                      wm.camera.diry = oldDirX * math.sin(- rotSpeed) + wm.camera.diry * math.cos(- rotSpeed)
                      oldPlaneX = wm.camera.planex
                      wm.camera.planex = wm.camera.planex * math.cos(- rotSpeed) - wm.camera.planey * math.sin(- rotSpeed)
                      wm.camera.planey = oldPlaneX * math.sin(- rotSpeed) + wm.camera.planey * math.cos(- rotSpeed)

          if vectorInstantaneo.y > 0:
                  #print "movió abajo"
                  # move backwards if no wall behind you
                  for ind in range(0,vectorInstantaneo.y):
                      if(worldMap[int(wm.camera.x - wm.camera.dirx * moveSpeed)][int(wm.camera.y)] == 0):
                          wm.camera.x -= wm.camera.dirx * moveSpeed
                      if(worldMap[int(wm.camera.x)][int(wm.camera.y - wm.camera.diry * moveSpeed)] == 0):
                          wm.camera.y -= wm.camera.diry * moveSpeed
          contadorm=0
          vectorInstantaneo.x = 0
          vectorInstantaneo.y = 0
          
        else:
          #suma contador hasta llegar a CYCLE_LOOP_NUMBER nuevamente.
          contadorm+=1
        
        ####################################################################
        #ahora el procesamiento normal con teclas. (fin de cosas que edito.)
        ####################################################################
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            # move forward if no wall in front of you
            moveX = wm.camera.x + wm.camera.dirx * moveSpeed
            if(worldMap[int(moveX)][int(wm.camera.y)]==0 and worldMap[int(moveX + 0.1)][int(wm.camera.y)]==0):wm.camera.x += wm.camera.dirx * moveSpeed
            moveY = wm.camera.y + wm.camera.diry * moveSpeed
            if(worldMap[int(wm.camera.x)][int(moveY)]==0 and worldMap[int(wm.camera.x)][int(moveY + 0.1)]==0):wm.camera.y += wm.camera.diry * moveSpeed
        if keys[K_DOWN]:
            # move backwards if no wall behind you
            if(worldMap[int(wm.camera.x - wm.camera.dirx * moveSpeed)][int(wm.camera.y)] == 0):wm.camera.x -= wm.camera.dirx * moveSpeed
            if(worldMap[int(wm.camera.x)][int(wm.camera.y - wm.camera.diry * moveSpeed)] == 0):wm.camera.y -= wm.camera.diry * moveSpeed
        if (keys[K_RIGHT] and not keys[K_DOWN]) or (keys[K_LEFT] and keys[K_DOWN]):
            # rotate to the right
            # both camera direction and camera plane must be rotated
            oldDirX = wm.camera.dirx
            wm.camera.dirx = wm.camera.dirx * math.cos(- rotSpeed) - wm.camera.diry * math.sin(- rotSpeed)
            wm.camera.diry = oldDirX * math.sin(- rotSpeed) + wm.camera.diry * math.cos(- rotSpeed)
            oldPlaneX = wm.camera.planex
            wm.camera.planex = wm.camera.planex * math.cos(- rotSpeed) - wm.camera.planey * math.sin(- rotSpeed)
            wm.camera.planey = oldPlaneX * math.sin(- rotSpeed) + wm.camera.planey * math.cos(- rotSpeed)
        if (keys[K_LEFT] and not keys[K_DOWN]) or (keys[K_RIGHT] and keys[K_DOWN]): 
            # rotate to the left
            # both camera direction and camera plane must be rotated
            oldDirX = wm.camera.dirx
            wm.camera.dirx = wm.camera.dirx * math.cos(rotSpeed) - wm.camera.diry * math.sin(rotSpeed)
            wm.camera.diry = oldDirX * math.sin(rotSpeed) + wm.camera.diry * math.cos(rotSpeed)
            oldPlaneX = wm.camera.planex
            wm.camera.planex = wm.camera.planex * math.cos(rotSpeed) - wm.camera.planey * math.sin(rotSpeed)
            wm.camera.planey = oldPlaneX * math.sin(rotSpeed) + wm.camera.planey * math.cos(rotSpeed)

def mainVideoDetection():
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
            En cada ciclo se actualiza un "vector movimiento". El vector promedio resultante
            se lee en el main() para actualizar la posición del personaje.
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
    #cam = cv2.VideoCapture("../../../files_movement/videos_prueba/slow_izquierda.avi")
    #cam = cv2.VideoCapture("../../../files_movement/videos_prueba/fast_diag1.avi")
    #cam = cv2.VideoCapture("../../../files_movement/videos_prueba/video_distorted2.avi")
    #cam = cv2.VideoCapture("../../../files_movement/videos_prueba/video_webm.avi")
    cam = cv2.VideoCapture("../../../files_movement/videos_prueba/abajo_y_arriba_2.avi")
    #cam = cv2.VideoCapture(CAM_NUMBER)
    
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

    
    #Nombre: Movement Indicator
    winName = "Track-bola v"+str(CURRENT_VERSION)+" - Detección de video"
    cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)
    
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
        cv2.imshow( winName , im )
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
        vectorInstantaneo.x += movEjeX
        vectorInstantaneo.y += movEjeY
        
        #Se tiene el vector instantáneo para este fotograma: vectorInstantáneo = (movEjeX, movEjeY)
        #print ("(%d %d .. %d)"%(movEjeX, movEjeY, numberOfVectors))
                
        #finalmente se "muestra" el resultado al usuario (feedback)
        cv2.imshow( winName , im ) #obs.: NO es estrictamente necesario dar feedback acá.. también está mainFunction
        #(imshow se puede sacar si el CPU es un problema.)
        
        time.sleep(0.01)
        
        #para finalizar programa, usuario presiona "Escape":
        key = cv2.waitKey(10)
        if (key == 27 or key==1048603): #escape pressed
            #end Program.
            cv2.destroyWindow(winName)
            os.kill(os.getpid(), signal.SIGINT)
            sys.exit()




class Weapon(object):
    
    def __init__(self, weaponName="shotgun", frameCount = 5):
        self.images = []
        self.loop = False
        self.playing = False
        self.frame = 0
        self.oldTime = 0
        for i in range(frameCount):
            img = pygame.image.load("pics/weapons/%s%s.bmp" % (weaponName, i+1)).convert()
            img = pygame.transform.scale2x(img)
            img = pygame.transform.scale2x(img)
            img.set_colorkey(img.get_at((0,0)))
            self.images.append(img)
    def play(self):
        self.playing = True
        self.loop = True
    def stop(self):
        self.playing = False
        self.loop = False
    def draw(self, surface, time):
        if(self.playing or self.frame > 0):
            if(time > self.oldTime + 1./fps):
                self.frame = (self.frame+1) % len(self.images)
                if self.frame == 0: 
                    if self.loop:
                        self.frame = 1
                    else:
                        self.playing = False
                        
                self.oldTime = time
        img = self.images[self.frame]
        surface.blit(img, (surface.get_width()/2 - img.get_width()/2, surface.get_height()-img.get_height()))

import worldManager
vectorInstantaneo = worldManager.vectorSimple()
CURRENT_VERSION = 0.1
if __name__ == '__main__':
    #ver http://stackoverflow.com/questions/12376224/python-threading-running-2-different-functions-simultaneously
    #import threading
    import threading
    # Create two threads, one for video Detection, the other with the game per se.
    fred1 = threading.Thread(target=mainFunction)
    fred1.start()
    
    fred2 = threading.Thread(target=mainVideoDetection)
    fred2.start()
