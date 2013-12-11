import time
import logging

logger = logging.getLogger('valve')

ValvePinMask = 0x04
DropTime = .1

class dummypp () :
    def __init__(self) :
        self.data = 0

    def getData(self):
        return self.data

    def setData(self,data) :
        self.data = data
        return self.data
  
  
class Valve() :
    def __init__(self) :
        try :
          logger.info('New instance of valve')
          import parallel
          self.p = parallel.Parallel()
        except :
          logger.warning('Could not find any parallel port. Using dummy parallel port')
          self.p = dummypp()

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

if __name__ == '__main__':
    # create a logging format
    formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    dateformat = '%Y/%m/%d %I:%M:%S %p'

    logging.basicConfig(filename='logs/valve.log', filemode='w',
        level=logging.DEBUG, format=formatter, datefmt = dateformat)
    logging.info('Start Valve Test')
    v1 = Valve()
    v1.open()
    time.sleep(2)
    v1.close()
    time.sleep(2)
    v1.close()
    logging.info('End Valve Test')
