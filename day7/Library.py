class Library:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.borrowed_books = []

    def borrow(self, book):
        self.borrowed_books.append(book)
        print(book, "borrowed")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(book, "returned")
        else:
            print(book, "not found")

    def checkBookPresent(self, book):
        return book in self.borrowed_books


# Creating object
member1 = Library(1, "Vivek")

# Using functions
member1.borrow("Python")
member1.borrow("Java")

print(member1.checkBookPresent("Python"))  # True
member1.return_book("Python")
print(member1.checkBookPresent("Python"))  # False

