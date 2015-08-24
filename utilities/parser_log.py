#!/usr/bin/python

import sys,getopt
import time

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

def parser(inputf,outputf) :
    of = open(outputf,'w')
    of.write ( '%trialnum,trialtype,trialresult,trialtreact,trialtreact2,trialtwindowdet,trialtintertrial,trialresult2==trialresult\n' )
    of.write ( 'session = [\n' )
    newline = False
    trialnum = 0
    trialtype = 0
    trialresult = 0
    trialtreact = 0
    trialtreact2 = 0
    trialtstart = 0

    with open(inputf, 'r') as f:
        for line in f:
            if 'training - INFO - Starting trial' in line:
                if newline:
                    of.write ( ('%4d,\t%d,\t%d,\t%4.3f,\t%4.3f,\t%4.3f,\t%4.3f' % 
                      (trialnum,trialtype,trialresult,trialtreact,trialtreact2,trialtwindowdet,trialtintertrial)) + ',\t' + str(trialresult2==trialresult))
                    of.write(';\n')
                trialnum = 0
                trialtype = 0
                trialresult = 0
                trialtstart = 0
                trialtwindowdet = 0
                trialtreact = 0
                trialtreact2 = 0
                trialtintertrial = 0
                trialttemp = 0
                trialnum = int(line.split(':')[3])
                t1 = line.split(' ')[1]
                t2 = t1.split('.')
                t3 = t2[0].split(':')
                trialtstart = int(t3[0]) *3600 + int(t3[1]) * 60 + int(t3[2]) + int(t2[1])/1000.0
                newline = False

            #tipo de trial '1' go/move, '2' nogo/still
            if 'training - INFO - Trial type' in line:
                if 'move' in line.split(':')[3]:
                    trialtype = 1
                elif 'still' in line.split(':')[3]:
                    trialtype = 2
                else:
                    raise ValueError('Trial not specified')

            if 'training - INFO - Start trial movement detection' in line:
                t1 = line.split(' ')[1]
                t2 = t1.split('.')
                t3 = t2[0].split(':')
                trialtwindowdet = int(t3[0]) *3600 + int(t3[1]) * 60 + int(t3[2]) + int(t2[1])/1000.0
                trialtwindowdet =  trialtwindowdet- trialtstart

            #para el trial go, encontramos el tiempo de reaccion
            if 'sphereVideoDetection - DEBUG -        isMoving' in line:
                if ('True' in line.split(':')[3]) and (trialtype is 1) and (trialtreact == 0):
                    t1 = line.split(' ')[1]
                    t2 = t1.split('.')
                    t3 = t2[0].split(':')
                    trialtreact = int(t3[0]) *3600 + int(t3[1]) * 60 + int(t3[2]) + int(t2[1])/1000.0
                    trialtreact = trialtreact - trialtstart

            #para el trial go, encontramos el tiempo de reaccion
            if 'training - INFO - Movement threshold reached' in line:
                if (trialtype is 1) and (trialtreact2 == 0):
                    t1 = line.split(' ')[1]
                    t2 = t1.split('.')
                    t3 = t2[0].split(':')
                    trialtreact2 = int(t3[0]) *3600 + int(t3[1]) * 60 + int(t3[2]) + int(t2[1])/1000.0
                    trialtreact2 = trialtreact2 - trialtstart

            #para el trial nogo, encontramos el tiempo de reaccion
            if 'sphereVideoDetection - DEBUG -        isMoving' in line:
                if ('True' in line.split(':')[3]) and (trialtype is 2) and (trialtreact == 0):
                    t1 = line.split(' ')[1]
                    t2 = t1.split('.')
                    t3 = t2[0].split(':')
                    trialtreact = int(t3[0]) *3600 + int(t3[1]) * 60 + int(t3[2]) + int(t2[1])/1000.0
                    trialtreact = trialtreact - trialtstart

            #para el trial nogo, encontramos el tiempo de reaccion
            if 'training - INFO - Movement threshold reached' in line:
                if (trialtype is 2) and (trialtreact2 == 0):
                    t1 = line.split(' ')[1]
                    t2 = t1.split('.')
                    t3 = t2[0].split(':')
                    trialtreact2 = int(t3[0]) *3600 + int(t3[1]) * 60 + int(t3[2]) + int(t2[1])/1000.0
                    trialtreact2 = trialtreact2 - trialtstart

            if 'training - INFO - Start inter-trial delay' in line:
                t1 = line.split(' ')[1]
                t2 = t1.split('.')
                t3 = t2[0].split(':')
                trialtreact2 = int(t3[0]) *3600 + int(t3[1]) * 60 + int(t3[2]) + int(t2[1])/1000.0
                trialtreact2 = trialtreact2 - trialtstart

            # resultado
            if 'training - INFO - Reward' in line:
                if 'not' in line:
                    trialresult = 0
                else:
                    trialresult = 1
                newline = True

            if 'training - INFO - Start inter-trial delay' in line:
                t1 = line.split(' ')[1]
                t2 = t1.split('.')
                t3 = t2[0].split(':')
                trialttemp = int(t3[0]) *3600 + int(t3[1]) * 60 + int(t3[2]) + int(t2[1])/1000.0

            # resultado
            if 'training - INFO - Trial' in line:
                if 'not' in line:
                    trialresult2 = 0
                else:
                    trialresult2 = 1
                t1 = line.split(' ')[1]
                t2 = t1.split('.')
                t3 = t2[0].split(':')
                trialtintertrial = int(t3[0]) *3600 + int(t3[1]) * 60 + int(t3[2]) + int(t2[1])/1000.0
                trialtintertrial = trialtintertrial - trialttemp

    if newline:
        of.write ( ('%4d,\t%d,\t%d,\t%4.3f,\t%4.3f,\t%4.3f,\t%4.3f' % 
          (trialnum,trialtype,trialresult,trialtreact,trialtreact2,trialtwindowdet,trialtintertrial)) + ',\t' + str(trialresult2==trialresult))
    of.write(']')
    of.close()


def main(argv):
  inputfile = ''
  outputfile = ''
  try:
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
    print 'parser_log.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
  for opt, arg in opts:
    print opt
    print arg
    if opt == '-h':
      print 'parser_log.py -i <inputfile> -o <outputfile>'
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--ofile"):
      outputfile = arg
  print 'Input file is "', inputfile
  print 'Output file is "', outputfile
  parser(inputfile,outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])

