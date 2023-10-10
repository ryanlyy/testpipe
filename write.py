import sys
import time

def main():
    infile = open('/usr/bin/zip', 'rb')
    outfile = open(sys.argv[1], 'wb')
    buf = infile.read(65530)
    if buf:
      while True:
        time.sleep(0.1)
        try:
            outfile.write(buf)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        else:
            pass

    outfile.close()
 

main()
