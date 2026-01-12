def CheckEven(No):
    return (No % 2 == 0)


def main():

    Data = [11,10,15,20,22,27,30]
    print("Actual data is : ",Data)
    
    # filter functions only accepts such a function whoes return value is boolean
    fData = list(filter(CheckEven,Data))
    print("Data after filter is : ",fData)



if __name__ == "__main__":
    main()
    