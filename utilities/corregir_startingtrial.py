#!/usr/bin/python
# -*- coding: utf-8 -*-

with open("training3_2013_12_13 mañana.txt") as f:
    content = f.readlines()

j=0;
with open('salida', 'a') as the_file:
    for i in range(0, len(content)):
      if "Starting new trial" in content[i]:
          the_file.write( content[i][:-1] + " End trial:"+str(j) + "\n" );
          the_file.write( content[i][:-1] + " Starting trial:"+str(j) + "\n" );
          j+=1;
      else:
          the_file.write(content[i]);