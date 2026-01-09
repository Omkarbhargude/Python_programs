def EmployeeInfo(Name, Age, Salary, City = "Pune"):
    print("Name : ",Name)
    print("Age : ",Age)
    print("Salary : ",Salary)
    print("City : ",City)

def main():
    EmployeeInfo("rahul",28,2000.50)        # Correct 
    EmployeeInfo("rahul",28,2000.50,"Mumbai")        # Correct 


if __name__ == "__main__":
    main()