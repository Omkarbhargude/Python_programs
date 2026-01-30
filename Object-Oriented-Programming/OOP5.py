class BankAccount:

    ROI = 10.5

    def __init__(self,A,B):
        self.Name = A
        self.Amount = B

    def Display(self):
        print("Account Holder Name : ",self.Name)
        print("Current Balance : ",self.Amount)

    def Deposit(self,Bal):
        self.Amount = self.Amount + Bal
        print("Current Balance : ",self.Amount)

    def Withdraw(self,draw):
        if((self.Amount <= 0) or (draw > self.Amount)):
            print("Insufficient Balance")
            print("Current Balance : ",self.Amount)
        else:
            self.Amount = self.Amount - draw
            print("Withdrawn succesfully")
            print("Total amount remaining : ",self.Amount)

    def CalculateInterest(self):
        self.Interest = (self.Amount * BankAccount.ROI) / 100
        print("Calculated Interest rate is : ",self.Interest)

def main():
    iCommon = None

    print("Enter your name : ")
    iVal1 = input()

    print("Enter your amount: ")
    iVal2 = int(input())

    obj1 = BankAccount(iVal1,iVal2)

    obj1.Display()

    print("Enter deposit amount : ")
    iCommon = int(input())

    obj1.Deposit(iCommon)

    print("Enter amount for withdraw : ")
    iCommon = int(input())

    obj1.Withdraw(iCommon)
    obj1.CalculateInterest()


if __name__ == "__main__":
    main()