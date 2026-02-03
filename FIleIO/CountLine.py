import os
import sys

def CountLines(Fname):

    try:
        Ret = os.path.exists(Fname)

        if(Ret == False):
            print("There is no such file")
            return

        fobj = open(Fname)

        Count = 0
        Buffer = fobj.read()

        for i in Buffer:
            if(i == "\n"):
                Count = Count + 1

        print("Total number of lines in file are : ",Count)
        
    except:
        print("File not found")

def main():
    
    if(len(sys.argv) == 2):
        CountLines(sys.argv[1])
    else:
        print("Wrong number of input")

if __name__ == "__main__":
    main()