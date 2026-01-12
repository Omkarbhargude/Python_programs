from functools import reduce            

def main():
    
    Data = [11,10,15,20,22,27,30]
    print("Actual data is : ",Data)
    
    # Filter functions only accepts such a function whoes return value is boolean
    fData = list(filter((lambda No : (No % 2 == 0)),Data))
    print("Data after Filter is : ",fData)

    # List is mutable so it can change
    mData = list(map((lambda No : No+1),fData))
    print("Data after Mapping is: ",mData)

    # Reduce   
    rData = reduce((lambda A,B : A+B),mData)
    print("Data after reduce is : ",rData)                             

if __name__ == "__main__":
    main()
    