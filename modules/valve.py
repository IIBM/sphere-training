
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
  
  

class multiproc_Valve():
    def __init__(self, jobl):
        self.displayJobList = jobl
        self.val = None
        self.using_dev = 0;
        #print "init valve."
        try :
          self.createUSBDevice()
        except :
          logger.warning('Device idVendor = ' + str(hex(IDVendor)) + ' and idProduct = ' + str(hex(IDProduct)) + ' not found. Using dummy device')
          self.p = dummydev()
    def createUSBDevice(self):
        logger.info('createUSBDevice: New instance of valve')
        self.using_dev = 0;
        #requires pyusb
        import usb.core
        import usb.util
        logger.debug("createUSBDevice: imports done succesfully.");
        self.p = usb.core.find(idVendor=IDVendor, idProduct=IDProduct)
        logger.debug("createUSBDevice: find done successfully.");
        # was it found?
        if self.p is None:
            raise ValueError(msg)
        # set the active configuration. With no arguments, the first
        # configuration will be the active one
        self.p.set_configuration()
        logger.debug("createUSBDevice: configuration set successfully.");
        self.using_dev = 1;
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
                 logger.error('Valve disconnected.')
                 try:
                     time.sleep(0.05)
                     logger.debug('About to recreate device.')
                     self.createUSBDevice()
                     logger.debug('About to re-send control transfer.')
                     a = self.p.ctrl_transfer(num1, num2, num3, num4)
                     logger.debug('Done re-send control transfer.')
                 except:
                     a = -1
                     logger.debug('Error recreating or re-sending control transfer.')
            return a
        else:
            a = self.p.ctrl_transfer(num1, num2, num3, num4)
    
    def checkJobList(self):
        if (self.displayJobList.qsize() > 0 or self.displayJobList.empty() == False ):
                try:
                        tempvar = self.displayJobList.get()
                        self.displayJobList.task_done()
                except:
                        return;
                #print str("checkJobList: queue: " + str(tempvar) )
                index = tempvar[0]
                try:
                    argument = tempvar[1]
                except:
                    argument = ""
                    pass
                
                #print "checkJobList: Got a Message:", index
                #print "checkJobList: Message's argument:", argument
#                 try:
#                     a = str(argument)
#                     print "Argument: %s" %a
#                 except:
#                     print "Message's argument cannot be parsed to str."
#                     pass
                if (index == "open"):
                    self.open()
                elif (index == "drop"):
                    self.drop()
                elif (index == "close"):
                    self.close()
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
     
     
class Valve(object):
  ### singleton inner class: valve.
  class __Valve:
    def __init__(self):
        import multiprocessing
        self.displayJobList = multiprocessing.JoinableQueue()
        
        self.displayProc = multiprocessing.Process(target=self.launch_multiproc, args=(self.displayJobList,) )
        self.displayProc.start()
        
        logger.debug("trainingDisplay process Started.")
        pass
    def __str__(self):
      return repr(self)
    
    def exit(self):
        self.displayProc.terminate()
        self.displayJobList.close()
    
    def launch_multiproc(self, jobl):
        a = multiproc_Valve(jobl)
        while(True):
            time.sleep(0.010)
            a.checkJobList()
            #a.updateInfo("Other secondary information", var)
            #for event in pygame.event.get():
            #        if event.type == pygame.QUIT: sys.exit()
            pass
    
    def open(self):
        self.displayJobList.put( ("open", "") )
    
    def drop(self):
        self.displayJobList.put( ("drop", "") )
    
    def close(self):
        self.displayJobList.put( ("close", "") )
    
  
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
    v2.exit()
    logger.info('End Valve Test')

