#simple camera class. When created, starts showing the device.
# -*- coding: utf-8 -*-

import track_bola_utils
import logging
logger = logging.getLogger('simpleCam')
import time

PROCESS_SLEEP_TIME = 70 #in milliseconds


class multiproc_simpleCam():
    
    def __init__(self, devnum=-1):
        
        import os
        logger.info("Initializing simpleCam")
        try:
            import configSimpleCam
        except ImportError:
            print "File configSimpleCam.py not found. Generating a new copy..."
            logger.info("File configSimpleCam.py not found. Generating a new copy...")
            a = os.getcwd() + "/"
            print a
            import shutil
            shutil.copyfile(a + "configSimpleCam.py.example", a + "configSimpleCam.py")
            import configSimpleCam
            print "configSimpleCam.py copied and imported successfully."
            logger.info("configSimpleCam.py copied and imported successfully.")
        except:
            print "Error importing configSimpleCam."
            logger.error("Error importing configSimpleCam.")
            os._exit(1)
        
        
        time.sleep(4)
        CAM_WIDTH = 320;
        CAM_HEIGHT = 240;
        import cv2
        time.sleep(1)
        if (devnum == -1):
            try:
                import configSimpleCam
                devnum = configSimpleCam.VIDEOSOURCE
            except:
                devnum = 0
        else:
            pass    #use devnum passed through argument
        if (devnum == -1):
            #disable module completely:
            pass
        else:
            cap = cv2.VideoCapture(devnum)
            print cap
            cap.set(3, CAM_WIDTH);
            cap.set(4, CAM_HEIGHT);
            time.sleep(1)
            print "starting"
            logger.debug("simpleCam starting.")
            window_name = "Device: %s" % str(devnum)
            cv2.namedWindow(window_name)
            time.sleep(1)
            logger.debug("namedWindow created. About to enter loop")
        while(True):
            if (devnum == -1):
                time.sleep(0.1);
            else:
                if (cv2.waitKey(PROCESS_SLEEP_TIME) == 27):
                    break
                ret, frame = cap.read()
                cv2.imshow(window_name, frame)
        if (devnum == -1):
            #disable module completely:
            pass
        else:
            print "Exiting.-"
            cap.release()
            cv2.destroyWindow(window_name)




class simpleCam():
    
    def launch_multiproc(self, devnum):
        a = multiproc_simpleCam(devnum)
    
    def __init__(self, devnum=-1):
        import multiprocessing
        self.displayProc = multiprocessing.Process(target=self.launch_multiproc, args=(devnum,) )
        self.displayProc.start()
    
    def exit(self):
        self.displayProc.terminate()
        del self.displayProc


if __name__ == '__main__':
    # create a logging format
    dateformat = '%Y/%m/%d %H:%M:%S'
    formatter_str = '%(asctime)s.%(msecs)d - %(name)s - %(levelname)s - %(message)s'
    filename_to_log='logs/simpleCam.log'
    
    
    logging.basicConfig(filename=filename_to_log, filemode='w+',
        level=logging.DEBUG, format=formatter_str,
        datefmt=dateformat)
    
    #===========================================================================
    #the following lines are only to ALSO log to stdout, are not strictly necessary
    #===========================================================================
    console = logging.StreamHandler()
    console.setLevel(logging.WARNING)
    formatter = track_bola_utils.formatterWithMillis(fmt=formatter_str,datefmt=dateformat)
    console.setFormatter(formatter)
    logger.addHandler(console)
    #===========================================================================
    a = simpleCam();
    #b = simpleCam(0); #it is possible to execute both simultaneously.
    time.sleep(30)
    a.exit()
