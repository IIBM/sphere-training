
import time
import track_bola_utils
import logging
logger = logging.getLogger('deviceusb')

IDVendor = 0x16c0
IDProduct = 0x05dc


  

class deviceUSB(object):
  ### singleton inner class: deviceUSB.
  class __deviceUSB:
    def __init__(self):
        self.val = None
        self.using_dev = 0; #if 1, currently using device and it is working
        self.using_dummy = 0 #if 1, using dummy device and will never use a hardware device.
        self.initDevice()
        logger.debug("deviceusb initialized.")
        pass
    def __str__(self):
      return repr(self)
    
    def initDevice(self):
        logger.debug("deviceusb initDevice start.")
        self.using_dev = 0;
        self.using_dummy = 0;
        try :
          self.createUSBDevice()
        except :
          logger.warning('USB device idVendor = ' + str(hex(IDVendor)) + ' and idProduct = ' + str(hex(IDProduct)) + ' not found. Using dummy device')
          self.p = track_bola_utils.dummydevice()
          self.using_dummy = 1;
          self.using_dev = 0;
        logger.debug("deviceusb initDevice end.")
    
    def createUSBDevice(self):
        logger.info('createUSBDevice: Creating new USB device')
        self.using_dev = 0;
        #requires pyusb
        import usb.core
        import usb.util
        logger.debug("createUSBDevice: imports done succesfully.");
        self.p = usb.core.find(idVendor=IDVendor, idProduct=IDProduct)
        logger.debug("createUSBDevice: find done successfully.");
        # was it found?
        if self.p is None:
            raise ValueError("Error creating USB device.")
        # set the active configuration. With no arguments, the first
        # configuration will be the active one
        self.p.set_configuration()
        logger.debug("createUSBDevice: configuration set successfully.");
        self.using_dev = 1;
        self.using_dummy = 0;
        print "USB device created successfully."
        logger.info('USB device created successfully.')
        

    def control_transfer(self, num1, num2, num3, num4):
        if (self.using_dev == 1):
            a = -1
            try:
                 logger.debug('Control transfer %r %r %r %r' % (num1, num2, num3, num4) )
                 a = self.p.ctrl_transfer(num1, num2, num3, num4)
                 logger.debug('Control transfer done.')
            except:
                 logger.error('deviceusb disconnected.')
                 time.sleep(0.1)
                 logger.debug('About to recreate device.')
                 self.initDevice()
                 if (self.using_dummy):
                         logger.debug('Failed to recreate device')
                         a = -1;
                 else:
                        logger.debug('Device correctly recreated.')
                        logger.debug('About to re-send control transfer.')
                        try:
                            a = self.p.ctrl_transfer(num1, num2, num3, num4) #this might fail, leaving next ctrltransf in a p=None state
                            logger.debug('Done re-send control transfer.')
                        except:
                            logger.debug('Failed to re-send control transfer after recreating device')
                            a = -1;
            return a
        else:
            #using dummy so it won't fail.
            a = self.p.ctrl_transfer(num1, num2, num3, num4)
            return a;
        pass
    
    def exit(self):
        
        pass
  ###
  instance = None
  def __new__(cls): # __new__ always a classmethod
    if not deviceUSB.instance:
      deviceUSB.instance = deviceUSB.__deviceUSB()
    return deviceUSB.instance
  def __getattr__(self, name):
    return getattr(self.instance, name)
  def __setattr__(self, name):
    return setattr(self.instance, name)






if __name__ == '__main__':
    # create a logging format
    dateformat = '%Y/%m/%d %H:%M:%S'
    formatter_str = '%(asctime)s.%(msecs)d - %(name)s - %(levelname)s - %(message)s'
    filename_to_log='logs/deviceUSB.log'
    
    
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
    
    logger.info('Start deviceUSB Test1')
    time.sleep(0.3)
    v1 = deviceUSB()
    v1.control_transfer( 1, 2, 3, 4);
    time.sleep(2)
    print v1
    v2 = deviceUSB()
    v1.control_transfer( 3, 4, 5, 6);
    time.sleep(2)
    print v2
    
    logger.info('End deviceUSB Test')
    v1.exit()
