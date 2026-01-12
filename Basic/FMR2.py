def CheckEven(No):
    return (No % 2 == 0)

def Increment(No):
    return No+1

def main():

    Data = [11,10,15,20,22,27,30]
    print("Actual data is : ",Data)
    
    # Filter functions only accepts such a function whoes return value is boolean
    fData = list(filter(CheckEven,Data))
    print("Data after Filter is : ",fData)

    # List is mutable so it can change
    mData = list(map(Increment,fData))
    print("Data after Mapping : ",mData)


if __name__ == "__main__":
    main()
    