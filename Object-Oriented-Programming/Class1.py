class Demo:
    def __init__(self):                         # self -> this pointer
        print("Inside Constructor")

    def __del__(self):                           
        print("Inside Destructor")

obj = Demo()                                # Object Creation

print("End of Application")
