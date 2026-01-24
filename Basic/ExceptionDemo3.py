def main():
    Ans = 0
    try:
        print("Inside try")

        print("Enter first number : ")
        No1 = int(input())

        print("Enter second number : ")
        No2 = int(input())

        Ans = No1 / No2
    
    except ValueError as vobj:
        print("Inside except : ",vobj)

    except ZeroDivisionError as zobj:
        print("Inside except : ",zobj)

    except Exception as eobj:
        print("Inside Except : ",eobj)
        
    finally:
        print("Inisde finally")

    print("Division is : ",Ans)

if __name__ == "__main__":
    main()