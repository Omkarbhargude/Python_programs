from functools import reduce            

#def CheckEven(No):
 #   return (No % 2 == 0)

CheckEven = lambda No : (No % 2 == 0)

#def Increment(No):
#return No+1

Increment = lambda No : No+1

#def Add(A,B):
#   return A+B

Add = lambda A,B : A+B

def main():

    Data = [11,10,15,20,22,27,30]
    print("Actual data is : ",Data)
    
    # Filter functions only accepts such a function whoes return value is boolean
    fData = list(filter(CheckEven,Data))
    print("Data after Filter is : ",fData)

    # List is mutable so it can change
    mData = list(map(Increment,fData))
    print("Data after Mapping is: ",mData)

    # Reduce   
    rData = reduce(Add,mData)
    print("Data after reduce is : ",rData)                             

if __name__ == "__main__":
    main()
    