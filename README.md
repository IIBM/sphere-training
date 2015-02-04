sphere-training
==========

This software helps to automatically control a classical conditioning training.
The setup consist of a rat over a sphere.
The system generates one or two different tones as stimulus and detects the movement of the sphere through video processing.

Installation

In "modules" directory
 - create a file configvideo.py using configvideo.py.example
 - select between videocam and example file, with variable VIDEOSOURCE
    VIDEOSOURCE = CAM_NUMBER
    or
    VIDEOSOURCE = PATH + FILE 
 - complete CAM_NUMBER or PATH and FILE with the proper option. PATH could be absolute or relative to the directory where configvideo.py is located

Dependence:

valve.py ->
  pyusb

