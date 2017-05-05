# netstat-pid-and-imagename
Python script to see netstat port list with PID and Image Name. PID + Image name for easy identification.

Platform - Windows (tested on Window 7)
Language - python 2.7

# usage
run the python file in command prompt:
eg. --> python nestats-namedpid.py

# sample output

Proto   "Local Address"   " Foreign Address"    " PID"    "Image Name" 
==============================================================================
TCP   0.0.0.0:135   0.0.0.0:0   LISTENING   264   svchost.exe
TCP   0.0.0.0:443   0.0.0.0:0   LISTENING   4128   vmware-hostd.exe

# note

The script currently only parse the TCP connection rows
Similar result can be achieve with command --> netstat -anob


