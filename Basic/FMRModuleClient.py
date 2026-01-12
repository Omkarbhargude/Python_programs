from MarvellousFMR import filterX, mapX, reduceX

CheckEven = lambda No : (No % 2 == 0)       
Increment = lambda No : No+1                
Add = lambda A,B : A+B     
                 

def main():

    Data = [11,10,15,20,22,27,30]
    print("Actual data is : ",Data)
    
    fData = list(filterX(CheckEven,Data))
    print("Data after Filter is : ",fData)

    mData = list(mapX(Increment,fData))
    print("Data after Mapping is: ",mData)

    rData = reduceX(Add,mData)
    print("Data after reduce is : ",rData)                             

if __name__ == "__main__":
    main()
    