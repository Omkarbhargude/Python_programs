class Circle:

    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Acc(self,A):
        self.Radius = A

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
        
    def Circumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
        
    def Display(self):
        print("Radius : ",self.Radius)
        print("Area : ",self.Area)
        print("Circumference : ",self.Circumference)
    
def main():

    Obj1 = Circle()
    Obj2 = Circle()
    Obj3 = Circle()

    Obj1.Acc(7)
    Obj1.CalculateArea()
    Obj1.Circumference()
    Obj1.Display()



if __name__ == "__main__":
    main()