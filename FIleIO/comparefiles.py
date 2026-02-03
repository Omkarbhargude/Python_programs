import os
import sys

def CheckContent(Fname1,Fname2):

    Ret = os.path.exists(Fname1)
    Bet = os.path.exists(Fname2)

    if(Ret == False or Bet == False):
        print("There is no such file")
        return
    
    fobj = open(Fname1,"r")

    nobj = open(Fname2,"r")

    Data = fobj.read(1024)
    Buffer = nobj.read(1024)

    Ret = True
    while(len(Data) and len(Buffer) > 0):
        if(Data != Buffer):
            Ret = False
            break
        
        Data = fobj.read(1024)
        Buffer = nobj.read(1024)

    if(Ret == True):
        print("Success")
    else:
        print("Contents are not same")

def main():
    
    if(len(sys.argv) == 3):
        CheckContent(sys.argv[1],sys.argv[2])
    else:
        print("Wrong number of input")

if __name__ == "__main__":
    main()