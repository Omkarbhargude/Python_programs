class BookStore:

    NoOfBook = 0

    def __init__(self,A,B):
        self.Name = A
        self.Author = B
        BookStore.NoOfBook = BookStore.NoOfBook + 1 


    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books :",BookStore.NoOfBook)
        

    
def main():

    print("Enter name of book : ")
    iVal1 =input()

    print("Enter  author of book : ")
    iVal2 = input()

    obj1 = BookStore(iVal1,iVal2)

    obj1.Display()


    print("Enter name of book : ")
    iVal1 =input()

    print("Enter  author of book : ")
    iVal2 = input()

    obj2 = BookStore(iVal1,iVal2)

    obj2.Display()
if __name__ == "__main__":
    main()