# Procedural

def CheckEven(iNo):
    if(iNo % 2 == 0):
        print("It is Even")
    else:
        print("It is Odd")

iValue = 0

print("Enter the number : ",end="")
iValue = int(input())

CheckEven(iValue)
main()