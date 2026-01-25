import gc

class Demo:
    def __init__(self):                        
        print("Inside Constructor")

    def __del__(self):                           
        print("Inside Destructor")

# Allocation
obj = Demo()                                

# Use

# Deallocation
del obj                                         # del keyword is like free 

gc.collect()                                    # explicite call of garbage collector

print("End of Application")

# Python doesnt support static memory allocation