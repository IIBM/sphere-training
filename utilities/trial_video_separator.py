'''
python script that splits a training video obtained with the main training script, into smaller videos, one per trial.
usage:
trial_video_separator.py video.avi optional_prefix

part of sphere-training repo: https://github.com/IIBM/sphere-training/
'''
import time
import sys
import cv2
input_video = str(sys.argv[1])
cap = cv2.VideoCapture(input_video)

workingTrial = []
vidcount = 0
try:
    prefijoVideo = str(sys.argv[2])
    print "Prefix set to: ", prefijoVideo
except:
    prefijoVideo="separatedtrials_"
    print "Using default prefix: \"separatedtrials_\""


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

#def grabarTrial():
            #if (len(workingTrial) > 2):
                #videofps = 30
                #if is_cv2():
                    #video = cv2.VideoWriter("tester%d.avi"%vidcount, cv2.cv.CV_FOURCC(*'MPEG'), videofps, (320, 240))
                #elif is_cv3():
                    #video = cv2.VideoWriter("tester%d.avi"%vidcount, cv2.VideoWriter_fourcc(*'MPEG'), videofps, (320, 240))
                #for item in workingTrial:
                    #video.write(item)
                #video.release()
                #vidcount+=1
                #del workingTrial[:]
                #workingTrial = []

print "Video start."
startappending = False
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == False:
        break
    pixel= frame[0, 0]
    #print pixel
    if pixel[2] >= 249:
        #capture video frames between red dots. 
        startappending = True
        print "-------- Nuevo Trial --------"
        #grabarTrial()
        if len(workingTrial) > 0:
            videofps = 30
            if is_cv2():
                video = cv2.VideoWriter("%s%d.avi"%(prefijoVideo,vidcount), cv2.cv.CV_FOURCC(*'MPEG'), videofps, (320, 240))
            elif is_cv3():
                video = cv2.VideoWriter("%s%d.avi"%(prefijoVideo,vidcount), cv2.VideoWriter_fourcc(*'MPEG'), videofps, (320, 240))
            for item in workingTrial:
                video.write(item)
            video.release()
            vidcount+=1
            del workingTrial[:]
            workingTrial = []
    if startappending:
        workingTrial.append(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print "Video end.\nNumber of trials: %d" % vidcount
