# Procedural


def CheckEven(iNo):
    if(iNo % 2 == 0):
        print("It is Even")
    else:
        print("It is Odd")

def main():
    iValue = 0

    print("Enter the number : ",end="")
    iValue = int(input())

    CheckEven(iValue)

if __name__ == "__main__":
    main()