class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=False

    def borrow(self):
        self.is_borrowed=True
        print(self.title)
    
    def return_book(self):
        self.is_borrowed=False
        print(self.title)
book1=Book("Percy Jackson","Rick Riordan")
book2=Book("Harry Potter","Jk Rowling")
book3=Book("One Piece","Eiichiro Oda")

book1.borrow()
book1.return_book()

book2.borrow()
book2.return_book()

book3.borrow()
book3.return_book()
