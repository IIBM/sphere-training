#simple camera class. When created, starts showing the device.
import track_bola_utils
import logging
logger = logging.getLogger('simpleCam')
import time

class simpleCam():
    def __init__(self, devnum):
        import cv2
        time.sleep(1)
        cap = cv2.VideoCapture(devnum)
        print cap
        time.sleep(1)
        print "starting"
        logger.debug("simpleCam starting.")
        cv2.namedWindow("Device: %d" % devnum)
        time.sleep(1)
        logger.debug("namedWindow created. About to enter loop")
        while(True):
            cv2.waitKey(100)
            ret, frame = cap.read()
            cv2.imshow("Device: %d" % devnum, frame)


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
    a = simpleCam(0);