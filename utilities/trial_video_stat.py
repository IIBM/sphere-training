'''
python script that prints statistics of a sphere-training video.
usage:
trial_video_stat.py video.avi

part of sphere-training repo: https://github.com/IIBM/sphere-training/
'''
import time
import sys
import cv2
input_video = str(sys.argv[1])
cap = cv2.VideoCapture(input_video)

workingTrial = []
vidcount = 0

def is_cv2():
    # if we are using OpenCV 2, then our cv2.__version__ will start with '2.'
    return check_opencv_version("2.")

def is_cv3():
    # if we are using OpenCV 3.X, then our cv2.__version__ will start with '3.'
    return check_opencv_version("3.")

def check_opencv_version(major, lib=None):
    # if the supplied library is None, import OpenCV
    if lib is None:
        import cv2 as lib
        pass
    # return whether or not the current OpenCV version matches the
    # major version number
    return lib.__version__.startswith(major)

print "Reading video: %s" % input_video
framecount = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == False:
        break
    framecount +=1
    pixel= frame[0, 0]
    #print pixel
    if pixel[2] >= 240:
        print "-------- red square detected --------"
        print "frame: ", framecount
        print "pixel color: ", pixel[0], pixel[1], pixel[2]
    workingTrial.append(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print "-------------------------------"
print "Video end reached."
print "total frames: " + str(framecount)
