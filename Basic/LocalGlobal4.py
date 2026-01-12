No = 11        

def Fun():
    global No                                                           # like extern keyword
    print("Value of No from Fun is : ",No)                              # 11
    No = No + 1                 
    print("Value of No from Fun is : ",No)                              # 12                  

print("Value of No is : ",No)                       
Fun()
print("Value of No is : ",No)                       
