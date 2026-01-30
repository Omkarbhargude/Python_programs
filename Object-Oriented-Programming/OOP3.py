class Arithematic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0


    def Accept(self,A,B):
        self.Value1 = A
        self.Value2 = B
    
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
  
    def Division(self):
        Ans =  self.Value1 / self.Value2
    
def main():

    print("Enter first number : ")
    iVal1 = int(input())

    print("Enter second number : ")
    iVal2 = int(input())

    obj1 = Arithematic()
    obj1.Accept(iVal1,iVal2)

    Ret = obj1.Addition()
    print("Addition is : ",Ret)

    Ret = obj1.Substraction()
    print("substraction is : ",Ret)

if __name__ == "__main__":
    main()