import time
import track_bola_utils
import logging
logger = logging.getLogger('valveparallel')

ValvePinMask = 0x04
DropTime = .1

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
        #print "init valve."
        try :
           logger.info('New instance of valve')
           import parallel
           self.p = parallel.Parallel()
        except :
           logger.warning('Could not find any parallel port. Using dummy parallel port')
           self.p = dummydevice()
        
    
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
         a = self.p.getData()
         return self.p.setData(a|ValvePinMask)
    def close(self) :
         logger.debug('Valve closed')
         a = self.p.getData()
         return self.p.setData(a&(~ValvePinMask))
     
    def drop(self) :
         logger.debug('Valve drop')
         self.open()
         time.sleep(DropTime)
         self.close()
     



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

