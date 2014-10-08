import time
import logging
logger = logging.getLogger('valve')
import datetime as dt

ValvePinMask = 0x04
DropTime = .1


class MyFormatter(logging.Formatter):
    converter=dt.datetime.fromtimestamp
    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            t = ct.strftime("%Y-%m-%d %H:%M:%S")
            s = "%s,%03d" % (t, record.msecs)
        return s

class dummypp () :
    def __init__(self) :
        self.data = 0

    def getData(self):
        return self.data

    def setData(self,data) :
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
           import parallel
           self.p = parallel.Parallel()
      except :
           logger.warning('Could not find any parallel port. Using dummy parallel port')
           self.p = dummypp()
    def __str__(self):
      return repr(self)
    def open(self) :
         logger.info('Valve opened')
         a = self.p.getData()
         return self.p.setData(a|ValvePinMask)
    def close(self) :
         logger.info('Valve closed')
         a = self.p.getData()
         return self.p.setData(a&(~ValvePinMask))
     
    def drop(self) :
         logger.info('Valve drop')
         self.open()
         time.sleep(DropTime)
         self.close()
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
    formatter_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    #dateformat = '%Y/%m/%d %I:%M:%S.%f %p'
    dateformat = '%Y-%m-%d,%H:%M:%S '
    #logging.Formatter(fmt='%(asctime)s.%(msecs)d',datefmt='%Y-%m-%d,%H:%M:%S')
    logging.basicConfig(filename='logs/valve.log', filemode='w',
        level=logging.DEBUG, format=formatter_str, datefmt = dateformat)
    
    console = logging.StreamHandler()
    logger.addHandler(console)
    
    formatter = MyFormatter(fmt=formatter_str,datefmt='%Y-%m-%d,%H:%M:%S.%f')
    console.setFormatter(formatter)
    
    
    #logging.Formatter(fmt='%(asctime)s.%(msecs)d',datefmt='%Y-%m-%d,%H:%M:%S')
    logger.info('Start Valve Test1')
    logger.info('Start Valve Test2')
    time.sleep(0.3)
    logger.info('Start Valve Test3')
    v1 = Valve()
    v1.open()
    time.sleep(2)
    v1.close()
    print v1
    time.sleep(2)
    v1.close()
    print v1
    v2 = Valve()
    v2.open()
    time.sleep(2)
    v2.close()
    print v2
    
    logger.info('End Valve Test')
