import os
import sys

def CountWord(Fname):

    try:
        Ret = os.path.exists(Fname)

        if(Ret == False):
            print("There is no such file")
            return  

        fobj = open(Fname,"r")
        Buffer = fobj.read()

        Data = Buffer.split()        

        print(Data)

        print("Number of words in file are : ",len(Data))
        
    except:
        print("File not found")

def main():
    
    if(len(sys.argv) == 2):
        CountWord(sys.argv[1])
    else:
        print("Wrong number of input")

if __name__ == "__main__":
    main()