import logging
import datetime

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