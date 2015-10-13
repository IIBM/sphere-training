import logging
import datetime

class dummyClass:
    #skeleton of a dummy class, to load variables into it, or other issues.
    def __init__(self):
        pass

class vectorSimple:
    x=0;
    y=0;
    intensidad=0;
    angulo=0;

class formatterWithMillis(logging.Formatter):
    
    #formats time with millisecond info added. Use this with a StreamHandler()
    converter=datetime.datetime.fromtimestamp
    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            t = ct.strftime("%Y-%m-%d %H:%M:%S")
            s = "%s,%03d" % (t, record.msecs)
        return s


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