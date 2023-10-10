import sys
import time

def main():
    infile= open(sys.argv[1], 'rb')
    while True:
        time.sleep(0.1)
        try:
             buf = infile.read(65530)
        except ValueError:
             print("Oops!  That was no valid number.  Try again...")
        else:
             pass
    infile.close()

main()
