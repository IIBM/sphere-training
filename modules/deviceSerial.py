
import time
import track_bola_utils
import logging
logger = logging.getLogger('deviceserial')

DEVICE = '/dev/ttyUSB0'
BAUDRATE = 115200



class deviceSerial(object):
    def __init__(self):
        self.val = None
        self.using_dev = 0; #if 1, currently using device and it is working
        self.using_dummy = 0 #if 1, using dummy device and will never use a hardware device.
        self.initDevice()
        logger.debug("deviceserial initialized.")
        pass
    def __str__(self):
      return repr(self)
    
    def initDevice(self):
        logger.debug("deviceserial initDevice start.")
        self.using_dev = 0;
        self.using_dummy = 0;
        try :
          self.createSERIALDevice()
        except :
          logger.warning('Serial device  = ' + str(DEVICE) + ' and BAUDRATE = ' + str(BAUDRATE) + ' not found. Using dummy device')
          self.p = track_bola_utils.dummydevice()
          self.using_dummy = 1;
          self.using_dev = 0;
        logger.debug("deviceserial initDevice end.")
    
    def createSERIALDevice(self):
        logger.info('createSERIALDevice: Creating new serial device')
        self.using_dev = 0;
        #requires pyusb
        from serial import *
        self.p = Serial(DEVICE, BAUDRATE, timeout=1.0, stopbits=1)
        logger.debug("createSERIALDevice: done.");
        # was it found?
        if self.p is None:
            raise ValueError("Error creating serial device.")
        self.using_dev = 1;
        self.using_dummy = 0;
        print "Serial device created successfully."
        logger.info('Serial device created successfully.')
        
    
    def writeToSerial(self, argument):
        self.p.write(str(argument));
    
    
    def exit(self):
        del self.p
        self.using_dev = 0
        self.using_dummy = 0
        pass




if __name__ == '__main__':
    # create a logging format
    dateformat = '%Y/%m/%d %H:%M:%S'
    formatter_str = '%(asctime)s.%(msecs)d - %(name)s - %(levelname)s - %(message)s'
    filename_to_log='logs/valve.log'
    
    
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
    
    logger.info('Start Valve Test1')
    time.sleep(0.3)
    v1 = Valve()
    v1.open()
    time.sleep(2)
    v1.close()
    time.sleep(2)
    v1.drop()
    time.sleep(2)
    print v1
    v2 = Valve()
    v2.open()
    time.sleep(2)
    v2.close()
    print v2
    
    logger.info('End Valve Test')
    v1.exit()
