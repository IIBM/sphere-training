#simple camera class. When created, starts showing the device.


class simpleCam():
    def __init__(self, devnum):
        import cv2
        cap = cv2.VideoCapture(devnum)
        print "starting"
        cv2.namedWindow("Device: %d" % devnum, 1)
        while(True):
            ret, frame = cap.read()
            cv2.imshow("Device: %d" % devnum, frame)
            cv2.waitKey(30)


if __name__ == '__main__':
    a = simpleCam(0);