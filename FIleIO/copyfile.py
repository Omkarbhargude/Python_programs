import os
import sys

def CopyContent(fname):

    Ret = os.path.isfile(fname)

    if(Ret == False):
        print("It is not file")
        return
    
    fobj = open(fname,"r")

    nobj = open("Demo.txt","a")

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        nobj.write(Buffer)

        Buffer = fobj.read(1024)

    print("Data gets successfully writen in Demo.txt")

def main():
    
    if(len(sys.argv) == 2):
        CopyContent(sys.argv[1])
    else:
        print("Wrong number of input")

if __name__ == "__main__":
    main()