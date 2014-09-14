#!/usr/bin/python
# -*- coding: utf-8 -*-

with open("training3_2013_12_13 mañana_MODIF.txt_binary.csv") as f:
    content = f.readlines()


with open('somefile', 'a') as the_file:
    for i in range(0, len(content)):
      if (i>0):
          the_file.write(content[i].split(",")[0] + ","+ content[i-1].split(",")[1] );
      else:
          the_file.write(content[i].split(",")[0] + ",0\n" );