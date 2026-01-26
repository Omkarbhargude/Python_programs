class Parent:
    def __init__(self):
        print("Inside parent constructor")

    def Fun(self):
        print("Inside Fun method of parent")

class Child(Parent):
    def __init__(self):
        super().__init__()                      
        print("Inside child constructor")

    def Fun(self):
        super().Fun()
        print("Inside Fun method of child")

cobj = Child()

cobj.Fun()


