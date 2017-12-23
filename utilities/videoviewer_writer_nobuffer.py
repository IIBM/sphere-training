'''
python script that reads a video (or camera) and writes output to file. It does so by reading a frame and writing to disk, without buffering.
created for testing purposes.

usage:
videoviewer_writer_nobuffer.py input_video_file.avi output_video_file.avi

part of sphere-training repo: https://github.com/IIBM/sphere-training/
'''
import numpy as np
import cv2
import sys

input_video = ""
output_video = ""
default_output_video = "output.avi"

if (len(sys.argv)) > 1:
    input_video = sys.argv[1]
    if (len(sys.argv)) > 2:
        output_video = sys.argv[2]
else:
    print "Not enough arguments."
    print """usage:
    videoviewer_writer_nobuffer.py input_video_file.avi output_video_file.avi
    """
    sys.exit()

print "input video: ", input_video
if (output_video == ""):
    print "Using default output video: ", default_output_video
    output_video = default_output_video
else:
    print "output video: ", output_video

if (len(input_video) == 1):
    input_video = int(input_video)
    print "Input regarded as camera #", input_video
cap = cv2.VideoCapture( input_video )
# Define the codec and create VideoWriter object
##fourcc = cv2.VideoWriter_fourcc(*'PIM1') #1.0MB
#fourcc = cv2.VideoWriter_fourcc(*'MJPG') #6.4MB
##fourcc = cv2.VideoWriter_fourcc(*'DIV3') #3.1MB
##fourcc = cv2.VideoWriter_fourcc(*'DIVX') #0.9MB
fourcc = cv2.VideoWriter_fourcc(*'FFV1') #3.7MB

capturedWidth = int(cap.get(3))
capturedHeight = int(cap.get(4))
capturedFPS = int(cap.get(5))

out = cv2.VideoWriter(output_video,fourcc, capturedFPS, (capturedWidth,capturedHeight))
#out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if (ret == False):
        break;
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame.astype('uint8'))

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()

