#Log Parser: This simple program removes DEBUG info from logs, and saves output to a new file.

import sys
a = str(sys.argv[1])
b = open("NODEBUG_"+sys.argv[1],"a")
with open(a, 'r') as f:
    for line_number, line in enumerate(f, start=1):
        if "DEBUG" in line:
                continue
        b.write( line )
#        if line_number > 500000:
#            break
