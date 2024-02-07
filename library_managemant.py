class library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
    
    def displayAvailableBooks(self):
        print("Books present in library: ")
        for book in self.books:
            print(" -> "+book)

   
    def BorrowBook(self, bookName):
        if bookName in self.books:
            print(f"Succesfully Borrow {bookName} Book.")
            self.books.remove(bookName)
            return True
        
        else:
            print("The Book is already issued to someone else!")
            return False
 
    def ReturnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning the Book!")

class Student:
    # def __init__(self):
    #     self.bookList=[]
    
    def RequestBook(self):
        self.books = input("Enter the Name of Book: ")
        return self.books
    
    def ReturnBook(self):
        self.books = input("Enter the Name of Book you want to return: ")
        return self.books

if __name__=="__main__":
    centrallibrary = library(["Electronics", "Physics", "M1", "M2", "Electrical", "Mechanics", "PPS", "SME", "Aptitude"])
    student=Student()

    while (True):
        welcomeMSG='''\n### Welcome to central library ###
        Please chose an Option: 
        1. list all Books
        2. Request Book 
        3. Return Book / Add Book
        4. Exit Library
        '''
        print(welcomeMSG)
        a=int(input("Enter a choice: "))
        
        if a==1:
            centrallibrary.displayAvailableBooks()
        elif a==2:
            centrallibrary.BorrowBook(student.RequestBook())
        elif a==3:
            centrallibrary.ReturnBook(student.ReturnBook())
        elif a== 4:
            print("Thankyou!")
            exit()

        else:
            print("Invalid Choice!")
        
