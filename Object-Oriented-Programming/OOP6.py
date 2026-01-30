class Numbers:

    def __init__(self,A):
        self.Value = A

    def ChkPrime(self):
        if(self.Value <= 0):
            print("Wrong input")
            return 0
        
        bFlag = True
        for i in range(2,self.Value // 2 + 1):
            if(self.Value % i == 0):
                bFlag = False
                break

        return bFlag
    
    def SumFactor(self):
        self.iSum = 0

        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                self.iSum = self.iSum + i

        return self.iSum
    
    def ChkPerfect(self):
        self.iSum = 0
        for i in range(1,self.Value // 2 + 1):
            if(self.Value % i == 0):
                self.iSum = self.iSum + i

        return self.iSum == self.Value

        
    
    def Factor(self):
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                print(i)

def main():
    iCommon = False

    print("Enter number : ")
    iVal2 = int(input())

    obj1 = Numbers(iVal2)
    iCommon = obj1.ChkPerfect()

    if(iCommon == True):
        print("It is a prime number")


    iRet = obj1.SumFactor()

    print(iRet)

    obj1.Factor()

if __name__ == "__main__":
    main()