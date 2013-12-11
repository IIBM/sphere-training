# -*- coding: utf-8 -*-

######################################################
#Training 2:
"""
    Se crea un objeto de detección de video y se espera que durante 1 segundo haya movimiento significativo.
    Si lo hay, se da recompensa (gota de agua), caso contrario, se sigue esperando a que haya un movimiento
    significativo durante 1 segundo sostenido.
"""
######################################################><
import os, sys
lib_path = os.path.abspath('../modules/')
sys.path.append(lib_path)

if __name__ == '__main__':
    print "Training 2."
    try:
        from configvideo import *
    except ImportError:
        print "No existe el archivo configvideo.py"
    except:
        print "otro error"
    import sphereVideoDetection
    videoDet = sphereVideoDetection.sphereVideoDetection(VIDEOSOURCE, CAM_WIDTH, CAM_HEIGHT)
    import time
    import valve
    movementVector = [0,0,0,0,0,0,0,0,0,0] #has the history of previous movements, separated by 0.1 seconds
    countMovement = 0 #si llega a 7, es que durante 1000 ms estuvo moviéndose => dar recompensa
    val1 = valve.Valve()
    while(True):
        time.sleep(0.1)
        movementVector[0] = movementVector[1]
        movementVector[1] = movementVector[2]
        movementVector[2] = movementVector[3]
        movementVector[3] = movementVector[4]
        movementVector[4] = movementVector[5]
        movementVector[5] = movementVector[6]
        movementVector[6] = movementVector[7]
        movementVector[7] = movementVector[8]
        movementVector[8] = movementVector[9]
        movementVector[9] = abs(videoDet.getAccumX())  + abs( videoDet.getAccumY() )
        print movementVector
        vectorSum = 0
        for i in range(0,len(movementVector)):
            vectorSum+= movementVector[i]
        if (vectorSum  > 70):
            countMovement += 1
        videoDet.resetX()
        videoDet.resetY()
        if (countMovement > 9):
            #se estuvo moviendo durante 1000 ms. Dar recompensa.
            countMovement = 0
            for i in range(0,len(movementVector)):
                movementVector[i] = 0
            print "Release drop of water."
            val1.drop()

