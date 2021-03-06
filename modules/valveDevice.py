import time
import track_bola_utils
import logging
import os

logger = logging.getLogger('valvedevice')

ValvePinMask = 0x04
DropTime = .1


def checkImports():
    track_bola_utils.__importFromString("configValve")

class Valve(object):
  ### singleton inner class: valve.
  class __Valve:
    def __init__(self):
        self.val = None
        import multiprocessing
        self.displayJobList = multiprocessing.JoinableQueue()
        checkImports()
        import configValve
        self.valve_type = configValve.valve_type; #0: valve_parallel ; 1: valve_serial ; 2: valve_usb
        
        if self.valve_type == 0:
            import valve_parallel as valve_generic
            logger.info( "Using parallel valve" );
        if self.valve_type == 1:
            import valve_serial as valve_generic
            logger.info( "Using serial valve" );
        if self.valve_type == 2:
            import valve_usb as valve_generic
            logger.info( "Using USB valve" );
        
        
        
        self.displayProc = multiprocessing.Process(target=self.launch_multiproc, args=(self.displayJobList,valve_generic,) )
        self.displayProc.start()
        
        logger.debug("valve_generic process Started.")
        pass
    def __str__(self):
      return repr(self)
    
    def open(self):
        self.displayJobList.put( ("open", "") )
    
    def drop(self):
        self.displayJobList.put( ("drop", "") )
    
    def close(self):
        self.displayJobList.put( ("close", "") )
    
    def launch_multiproc(self, jobl, valve_generic, ):
        a = valve_generic.multiproc_Valve(jobl)
        while(True):
            time.sleep(0.010)
            a.checkJobList()
            #a.updateInfo("Other secondary information", var)
            #for event in pygame.event.get():
            #        if event.type == pygame.QUIT: sys.exit()
            pass
    
    def exit(self):
        self.displayProc.terminate()
        del self.displayProc
        
        self.displayJobList.close()
        del self.displayJobList
        pass
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
    v2 = Valve()
    v2.open()
    time.sleep(2)
    v2.close()
    print v2
    
    logger.info('End Valve Test')
    v1.exit()

