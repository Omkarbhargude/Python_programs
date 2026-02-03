import os
import sys

def DisplayLine(Fname):

    try:
        Ret = os.path.exists(Fname)

        if(Ret == False):
            print("There is no such file")
            return

        fobj = open(Fname,"r")
        Buffer = fobj.read()

        for i in Buffer:
                print(i,end="")
        print()
       

        
    except:
        print("File not found")

def main():
    
    if(len(sys.argv) == 2):
        DisplayLine(sys.argv[1])
    else:
        print("Wrong number of input")

if __name__ == "__main__":
    main()