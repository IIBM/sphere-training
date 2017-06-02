import logging
import datetime
import os
import importlib
import sys


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


def __importFromString(importname, modulesFolder = True):
    print importname
    try:
        tempModule = importlib.import_module(importname)
    except ImportError:
        print "File "+ str(importname) +".py not found. Generating a new copy..."
        if modulesFolder:
            a= os.getcwd()[:-8] + "modules/" #scan in "modules" folder
        else:
            pass #scan in "training" folder
        import shutil
        shutil.copyfile(a+""+ str(importname) +".py.example", a+str(importname)+".py")
        tempModule = importlib.import_module(str(importname))
        print ""+ str(importname) + ".py copied and imported successfully."
    except:
        print "Error importing configvideo."
        os._exit(1)
                
    if importname in sys.modules:  
        del(sys.modules[importname]) 
        del tempModule

