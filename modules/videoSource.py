import timeit
import pygame
import math
import threading
import time
import os
import signal
import cv2
import sys
import track_bola_utils
import logging
logger = logging.getLogger('videosource')

WIDTH_INDEX_CAMERA = 3
HEIGHT_INDEX_CAMERA = 4

"""
videoSource: This class creates a VideoCapture, sets its values (brightness, etc.).
"""

class videoSource() :
    def __init__(self) :
        
        try:
            import configVideoSource
        except ImportError:
            print "File configVideoSource.py not found. Generating a new copy..."
            logger.info("File configVideoSource.py not found. Generating a new copy...")
            a = os.getcwd() + "/"
            print a
            import shutil
            shutil.copyfile(a + "configVideoSource.py.example", a + "configVideoSource.py")
            import configCamera
            print "configVideoSource.py copied and imported successfully."
            logger.info("configVideoSource.py copied and imported successfully.")
        except:
            print "Error importing configVideoSource."
            logger.error("Error importing configVideoSource.")
            os._exit(1)
        
        try:
            import configVideoSource as configvideo
        except ImportError:
            print "File configVideoSource.py doesn't exist"
            logger.info("File configVideoSource.py doesn't exist")
            sys.exit(1);
        except:
            print "Error with configVideoSource"
            logger.info("Error with configVideoSource")
            sys.exit(1);
        
        # import configCamera
        cam = cv2.VideoCapture(configvideo.VIDEOSOURCE)
        print "Videosource: %s" % configvideo.VIDEOSOURCE;
        # Opciones de ejecuciOn: 640x480 => 60 fps.
        cam.set(WIDTH_INDEX_CAMERA, configvideo.CAM_WIDTH)
        cam.set(HEIGHT_INDEX_CAMERA, configvideo.CAM_HEIGHT)
        
        # set camera properties: this configuration is very dependent on the type and model of camera.
        
        cam.set(configvideo.CAM_BRIGHTNESS_VAR, configvideo.CAM_BRIGHTNESS_VALUE)
        cam.set(configvideo.CAM_CONTRAST_VAR, configvideo.CAM_CONTRAST_VALUE)
        cam.set(configvideo.CAM_SATURATION_VAR, configvideo.CAM_SATURATION_VALUE)
        cam.set(configvideo.CAM_HUE_VAR, configvideo.CAM_HUE_VALUE)
        cam.set(configvideo.CAM_GAIN_VAR, configvideo.CAM_GAIN_VALUE)
        cam.set(configvideo.CAM_EXPOSURE_VAR, configvideo.CAM_EXPOSURE_VALUE)
        print "camera: Width %r" % cam.get(WIDTH_INDEX_CAMERA)
        logger.info(str("camera: Width %r" % cam.get(WIDTH_INDEX_CAMERA)))
        print "camera: Height %r" % cam.get(HEIGHT_INDEX_CAMERA)
        logger.info(str("camera: Height %r" % cam.get(HEIGHT_INDEX_CAMERA)))
        # print "camera: FPS %r" % cam.get(5) #prints error for most cameras.
        print "camera: Brightness %r" % cam.get(configvideo.CAM_BRIGHTNESS_VAR)
        logger.info(str("camera: Brightness %r" % cam.get(configvideo.CAM_BRIGHTNESS_VAR)))
        print "camera: Contrast %r" % cam.get(configvideo.CAM_CONTRAST_VAR)
        logger.info(str("camera: Contrast %r" % cam.get(configvideo.CAM_CONTRAST_VAR)))
        print "camera: Saturation %r" % cam.get(configvideo.CAM_SATURATION_VAR)
        logger.info(str("camera: Saturation %r" % cam.get(configvideo.CAM_SATURATION_VAR)))
        print "camera: Hue %r" % cam.get(configvideo.CAM_HUE_VAR)
        logger.info(str("camera: Hue %r" % cam.get(configvideo.CAM_HUE_VAR)))
        print "camera: Gain %r" % cam.get(configvideo.CAM_GAIN_VAR)
        logger.info(str("camera: Gain %r" % cam.get(configvideo.CAM_GAIN_VAR)))
        print "camera: Exposure %r" % cam.get(configvideo.CAM_EXPOSURE_VAR)
        logger.info(str("camera: Exposure %r" % cam.get(configvideo.CAM_EXPOSURE_VAR)))
        
        
                # import camera parameters from file:
        self.CAM_BRIGHTNESS_VAR = configvideo.CAM_BRIGHTNESS_VAR
        self.CAM_CONTRAST_VAR = configvideo.CAM_CONTRAST_VAR
        self.CAM_SATURATION_VAR = configvideo.CAM_SATURATION_VAR
        self.CAM_HUE_VAR = configvideo.CAM_HUE_VAR
        self.CAM_GAIN_VAR = configvideo.CAM_GAIN_VAR
        self.CAM_EXPOSURE_VAR = configvideo.CAM_EXPOSURE_VAR
        
        self.CAM_BRIGHTNESS_VALUE = configvideo.CAM_BRIGHTNESS_VALUE
        self.CAM_CONTRAST_VALUE = configvideo.CAM_CONTRAST_VALUE
        self.CAM_SATURATION_VALUE = configvideo.CAM_SATURATION_VALUE
        self.CAM_HUE_VALUE = configvideo.CAM_HUE_VALUE
        self.CAM_GAIN_VALUE = configvideo.CAM_GAIN_VALUE
        self.CAM_EXPOSURE_VALUE = configvideo.CAM_EXPOSURE_VALUE
        logger.info("Initial config done.")
        
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
            logger.error("Error opening capture device")
            sys.exit(1)
        self.cam = cam
 
    def getVideoSource(self):
        return self.cam
    
    def exit(self):
        return;
    

if __name__ == '__main__':
    # create a logging format
    dateformat = '%Y/%m/%d %H:%M:%S'
    formatter_str = '%(asctime)s.%(msecs)d - %(name)s - %(levelname)s - %(message)s'
    filename_to_log='logs/videoSource.log'
    
    
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
    
    logger.info('Start videoSource test')
    time.sleep(0.3)
    v1 = videoSource()
    v2 = v1.getVideoSource()
    
    print v1
    print v2
    
    logger.info('End videoSource test')
    v1.exit()
    

