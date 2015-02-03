from serial import *
import time
import track_bola_utils
import logging
logger = logging.getLogger('valve')

ValvePinMask = 0x04
DropTime = .1

DEVICE = '/dev/ttyACM0'
BAUDRATE = 57600

class dummypp () :
    def __init__(self) :
        self.data = 0

    def write(self,data) :
        self.data = data
        return self.data
  



class Valve(object):
  ### singleton inner class: valve.
  class __Valve:
    def __init__(self):
      self.val = None
      #print "init valve."
      try :
           logger.info('New instance of valve')
           self.p = Serial(DEVICE, BAUDRATE, timeout=1.0, stopbits=1)
      except :
           logger.warning('Could not find any serial port. Using dummy parallel port')
           self.p = dummypp()
    def __str__(self):
      return repr(self)
    def open(self) :
         logger.debug('Valve opened')
         return self.p.write('o')

    def close(self) :
         logger.debug('Valve closed')
         return self.p.write('c')

    def drop(self) :
         logger.debug('Valve drop')
         return self.p.write('d')
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





#===============================================================================
# class Valve() :
#     def __init__(self) :
#         try :
#           logger.info('New instance of valve')
#           import parallel
#           self.p = parallel.Parallel()
#         except :
#           logger.warning('Could not find any parallel port. Using dummy parallel port')
#           self.p = dummypp()
# 
#     def open(self) :
#         logger.info('Valve opened')
#         a = self.p.getData()
#         return self.p.setData(a|ValvePinMask)
# 
#     def close(self) :
#         logger.info('Valve closed')
#         a = self.p.getData()
#         return self.p.setData(a&(~ValvePinMask))
#     
#     def drop(self) :
#         logger.info('Valve drop')
#         self.open()
#         time.sleep(DropTime)
#         self.close()
#===============================================================================

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
#    v2 = Valve()
#    v2.open()
#    time.sleep(2)
#    v2.close()
#    print v2
    
    logger.info('End Valve Test')
