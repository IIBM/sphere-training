CAM_NUMBER = 0 #cam number, 0 for integrated webcam, 1 for the next detected camera.
    
PATH = "../../../Labyrinth/files_movement/videos_prueba/"
FILE = "capture_bola_prueba_humano.mkv"

VIDEOSOURCE = PATH + FILE
# or
#VIDEOSOURCE = CAM_NUMBER

# VIDEOSOURCE will be invoqued as 
# cv2.VideoCapture(videosource)

CAM_WIDTH = 640
CAM_HEIGHT = 480



#var index for the camera.
CAM_BRIGHTNESS_VAR = 10
CAM_CONTRAST_VAR = 11
CAM_SATURATION_VAR = 12
CAM_HUE_VAR = 13
CAM_GAIN_VAR = 14
CAM_EXPOSURE_VAR = 15

#properties for camera.
CAM_BRIGHTNESS_VALUE = 0.298
CAM_CONTRAST_VALUE = 1.0
CAM_SATURATION_VALUE = 0.0
CAM_HUE_VALUE = 0.5
CAM_GAIN_VALUE = 0.1587
CAM_EXPOSURE_VALUE = 0.0

