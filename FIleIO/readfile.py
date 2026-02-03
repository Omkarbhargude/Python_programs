import os

def main():
    
    try:
        print("Enter file name : ")
        fname = input()
        fobj = open(fname,"r")

        data = fobj.read()

        print("Data from file is : ",data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file")
        

if __name__ == "__main__":
    main()