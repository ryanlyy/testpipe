#!/usr/bin/env python
import signal
import os
import fcntl
import sys



F_SETPIPE_SZ = 1031  # Linux 2.6.35+
F_GETPIPE_SZ = 1032  # Linux 2.6.35+



def open_fifo(fifo):
    print("Checking fifo file ...")
    fifo_fd = open(fifo, "rb")
    print ("Pipe size            : "+str(fcntl.fcntl(fifo_fd, F_GETPIPE_SZ)))
    #fifo_fd.close()

fifo_fd = open_fifo(sys.argv[1])
