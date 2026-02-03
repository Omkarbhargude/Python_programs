import os
import sys

def CountFreq(Fname,search):

    try:

        Ret = os.path.exists(Fname)

        if(Ret == False):
            print("There is no such file")
            return

        fobj = open(Fname,"r")

        Count = 0
        Buffer = fobj.read()

        Buffer = Buffer.split()

        for i in Buffer:
            if(i == search):
                Count = Count + 1

        print(f"Frequency of {search} in file is : ",Count)
    
    except:
        print("File not found")

def main():
    
    if(len(sys.argv) == 3):
        CountFreq(sys.argv[1],sys.argv[2])
    else:
        print("Wrong number of input")

if __name__ == "__main__":
    main()