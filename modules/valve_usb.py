
import time
import track_bola_utils
import logging
logger = logging.getLogger('valve')

IDVendor = 0x16c0
IDProduct = 0x05dc

class dummydevice () :
    def __init__(self) :
        self.data = 0
    def ctrl_transfer(self, num1, num2, num3, num4):
        print "dummy control transfer: %r %r %r %r" % (num1, num2, num3, num4);
        pass
        
    def write(self,data) :
        self.data = data
        return self.data
    
    def getData(self):
        return self.data

    def setData(self,data) :
        self.data = data
        return self.data
  
  

class multiproc_Valve():
    def __init__(self, jobl):
        self.displayJobList = jobl
        self.val = None
        self.using_dev = 0; #if 1, currently using device and it is working
        self.using_dummy = 0 #if 1, using dummy device and will never use a hardware device.
        #print "init valve."
        try :
          self.createUSBDevice()
        except :
          logger.warning('USB device idVendor = ' + str(hex(IDVendor)) + ' and idProduct = ' + str(hex(IDProduct)) + ' not found. Using dummy device')
          self.p = dummydevice()
          self.using_dummy = 1
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
            raise ValueError("Error creating USB device.")
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
                     a = self.p.ctrl_transfer(num1, num2, num3, num4) #this might fail, leaving next ctrltransf in a p=None state
                     logger.debug('Done re-send control transfer.')
                 except:
                     a = -1
                     logger.debug('Error recreating or re-sending control transfer.')
            return a
        else:
            if (self.using_dummy == 1 ):
                a = self.p.ctrl_transfer(num1, num2, num3, num4)
            else:
                #using_dev = 0 AND using_dummy = 0 : so it is using dev but it has disconnected and not reconnected correctly.
                logger.debug("Tried to send a message to the device but it was disconnected and couldn't recreate it: %r %r %r %r" % (num1, num2, num3, num4) );
    
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

