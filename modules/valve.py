
import time
import track_bola_utils
import logging
logger = logging.getLogger('valve')

IDVendor = 0x16c0
IDProduct = 0x05dc

class dummydev () :
    def __init__(self) :
        self.data = 0

    def ctrl_transfer(self,bmRequestType,bmRequest,wValue,wIndex) :
        self.data = wValue
        #print self.data
        return self.data
  
class Valve(object):
  ### singleton inner class: valve.
  class __Valve:
    def __init__(self):
      self.val = None
      self.using_dev = 0;
      #print "init valve."
      try :
        self.createUSBDevice()
      except :
        logger.warning('Device idVendor = ' + str(hex(IDVendor)) + ' and idProduct = ' + str(hex(IDProduct)) + ' not found. Using dummy device')
        self.p = dummydev()
    def __str__(self):
      return repr(self)
    
    def createUSBDevice(self):
        logger.info('New instance of valve')
        self.using_dev = 0;
        #requires pyusb
        import usb.core
        import usb.util
        logger.debug("imports done succesfully.");
        self.p = usb.core.find(idVendor=IDVendor, idProduct=IDProduct)
        # was it found?
        if self.p is None:
            raise ValueError(msg)
        # set the active configuration. With no arguments, the first
        # configuration will be the active one
        self.p.set_configuration()
        self.using_dev = 1;
        print "USB device created successfully."
        logger.info('USB device created successfully.')
    
    def open(self) :
         logger.debug('Valve opened')
         retmsg = self.control_transfer(0x40, 1, 1, 0);
         return retmsg

    def close(self) :
         logger.debug('Valve closed')
         retmsg = self.control_transfer(0x40, 1, 2, 0);
         return retmsg

    def drop(self) :
         logger.debug('Valve drop')
         retmsg = self.control_transfer(0x40, 1, 3, 0);
         return retmsg
    
    def control_transfer(self, num1, num2, num3, num4):
        if (self.using_dev == 1):
            a = -1
            try:
                 a = self.p.ctrl_transfer(num1, num2, num3, num4)
            except:
            logger.error('Valve disconnected')
                 try:
                     time.sleep(0.05)
                     self.createUSBDevice()
                     a = self.p.ctrl_transfer(num1, num2, num3, num4)
                 except:
                     a = -1
            return a
        else:
            a = self.p.ctrl_transfer(num1, num2, num3, num4)
    
    
  ###

  
  instance = None
  def __new__(cls): # __new__ always a classmethod
    if not Valve.instance:
      Valve.instance = Valve.__Valve()
    return Valve.instance
  def __getattr__(self, name):
    return getattr(self.instance, name)
  def __setattr__(self, name):
    return setattr(self.instance, name)



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

