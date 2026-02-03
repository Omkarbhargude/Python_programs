import os

def main():
    
    print("Enter file name : ")
    fname = input()

    Ret = os.path.exists(fname)

    if(Ret == True):
    
        Ret = os.path.isfile(fname)

    if(Ret == True):
        print(f"{fname} exists in current directory")
    else:
        print(f"{fname} doesnt exists")

if __name__ == "__main__":
    main()