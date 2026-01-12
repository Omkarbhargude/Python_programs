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
def mapX(Task,Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)

    return Result
# ------------------------------------------------------

# ------------------------------------------------------
def reduceX(Task,Elements):
    Sum = 0

    # [11,21,23,31]
    for no in Elements:
        Sum = Task(Sum,no)

    return Sum
# ------------------------------------------------------

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
    