# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how  you can print all books, add a book and get the number of books using  different methods. Show that your program doesnt persist the books after the program is stopped!
# [Next Lesson>>](https://replit.com/@codewithharry/65-Day-65-Static-Methods)

class Library:
    def __init__(self):
        self.number=0
        self.books=[]

    def add(self,*args):
        for arg in args:
            self.books.append(arg)
        self.number+=len(args)

    def show(self):
        for book in self.books:
            print(book,end=",")
        print("\n",self.number)
        print(len(self.books))

lib=Library()

lib.add("eng","bio")
lib.add("phy","socio")
lib.add("math")
lib.add("chem")

lib.show()