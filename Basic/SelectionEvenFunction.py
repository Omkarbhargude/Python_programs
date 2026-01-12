def CheckEven(iNo):
    if(iNo % 2 == 0):
        print("It is Even")
    else:
        print("It is Odd")

def main():

    CheckEven(21)               # Positional args
    CheckEven(iNo = 22)         # Keyword args

if __name__ == "__main__":
    main()