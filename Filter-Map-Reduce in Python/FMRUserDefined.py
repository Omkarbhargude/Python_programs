from functools import reduce            


CheckEven = lambda No : (No % 2 == 0)       
Increment = lambda No : No+1                
Add = lambda A,B : A+B                      

# ------------------------------------------------------
def filterX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)

        if (Ret == True):
            Result.append(no)

    return Result
# ------------------------------------------------------

# ------------------------------------------------------




# ------------------------------------------------------
def main():

    Data = [11,10,15,20,22,27,30]
    print("Actual data is : ",Data)
    
    fData = list(filterX(CheckEven,Data))
    print("Data after Filter is : ",fData)

    mData = list(map(Increment,fData))
    print("Data after Mapping is: ",mData)

    rData = reduce(Add,mData)
    print("Data after reduce is : ",rData)                             

if __name__ == "__main__":
    main()
    