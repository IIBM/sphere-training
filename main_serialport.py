# -*- coding: utf-8 -*-

######################################################
####################
#track-bola v0.1 Modificado para uso de Serial Port:
####################
#Se toma como entrada un flujo de video (webcam o archivo de video), se procesan y detectan círculos negros para
#mover un entorno virtual (Laberinto tipo T).
# Se enciende válvula de agua si se detecta movimiento en la bola.
######################################################><


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

def mainSerialMessage():
    import time
    while(1):
        print "x"+str(vectorInstantaneo.x)
        print "y"+str(vectorInstantaneo.y)
        if (abs(vectorInstantaneo.y)>22 or abs(vectorInstantaneo.x)>22):
            print "Detectado movimiento. Se manda mensaje serie:"
            sendSerialMessage()
        vectorInstantaneo.x = 0
        vectorInstantaneo.y = 0
        time.sleep(0.8)

def sendSerialMessage():
    import serial
    import time
    ser = serial.Serial()
    #ser.port = "/dev/ttyUSB0"
    ser.port = "/dev/ttyUSB7"
    #ser.port = "/dev/ttyS2"
    ser.baudrate = 9600
    ser.bytesize = serial.EIGHTBITS #number of bits per bytes
    ser.parity = serial.PARITY_NONE #set parity check: no parity
    ser.stopbits = serial.STOPBITS_ONE #number of stop bits
    ser.timeout = 1            #non-block read
    ser.xonxoff = False     #disable software flow control
    ser.rtscts = False     #disable hardware (RTS/CTS) flow control
    ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
    ser.writeTimeout = 2     #timeout for write
    try: 
        ser.open()
    except Exception, e:
        print "error open serial port: " + str(e)
    if ser.isOpen():
        while(1):
            try:
                ser.flushOutput()#flush output buffer, aborting current output 
                ser.write("aaaaa")
            except Exception, e1:
                print "error communicating...: " + str(e1)
            time.sleep(0.6)


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
    import spherevideotracker
    try:
        from configvideo import *
    except ImportError:
        print "No existe el archivo configvideo.py"
    except:
        print "otro error"

    sp1 = spherevideotracker.spherevideotracker(VIDEOSOURCE,CAM_WIDTH,CAM_HEIGHT)
    import threading
    import time
    fread = threading.Thread(target=sp1.startcapture)
    fread.start()
    time.sleep(2)
    
    while(1):
        a = sp1.getCumState()
        vectorInstantaneo.x = a[0]
        vectorInstantaneo.y = a[1]
        print "x"+str(vectorInstantaneo.x)
        print "y"+str(vectorInstantaneo.y)
        if (abs(vectorInstantaneo.y)>22 or abs(vectorInstantaneo.x)>22):
            print "Detectado movimiento. Se manda mensaje serie:"
            sendSerialMessage()
        vectorInstantaneo.x = 0
        vectorInstantaneo.y = 0
        time.sleep(0.8)
