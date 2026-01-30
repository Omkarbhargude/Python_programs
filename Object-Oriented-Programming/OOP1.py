class Demo:
    Value = 23

    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def fun(self):
        print("Value of Instance variable from fun are : ",self.No1,self.No2)

    def gun(self):
        print("Value of Instance variable from gun are : ",self.No1,self.No2)
        
def main():

    Obj1 = Demo(11,21)
    Obj2 =  Demo(51,101)

    Obj1.fun()
    Obj1.gun()

    Obj2.fun()
    Obj2.gun()

if __name__ == "__main__":
    main()