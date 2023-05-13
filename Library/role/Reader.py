from datetime import datetime

from role.User import User


class Reader(User):
    def __init__(self, uuid, username, password, role, catalog):
        super().__init__(uuid, username, password, role, catalog)

    def reserveBook(self, isbn):
        book = self.searchBookByISBN(isbn)
        if book.reserved == "False":
            book.reserved = self.uuid
        else:
            print('This Book is already reserved')

    def borrowBook(self, isbn):
        book = self.searchBookByISBN(isbn)
        if book is not False:
            x = datetime.now()
            if book.borrowed == "False":
                book.borrowed = self.uuid
                book.borrowed_till = f"{x.year}-{x.month}-{x.day}"

            else:
                print('This Book is already borrowed')

    def extendTime(self, isbn):
        book = self.searchBookByISBN(isbn)
        if book.borrowed == self.uuid:
            print(book.borrowed_till)
            date = datetime.strptime(book.borrowed_till, "%Y-%m-%d")
            date = f"{date.year}-{date.month}-{date.day + 7}"
            book.borrowed_till = date
        else:
            print('This Book is not borrowed by you')

    def bookReserved(self):
        booksReserved = []
        for book in self.catalog:
            if book.reserved == self.uuid:
                booksReserved.append(book)
        return booksReserved

    def bookBorrowed(self):
        booksBorrowed = []
        for book in self.catalog:
            if book.borrowed == self.uuid:
                booksBorrowed.append(book)
        return booksBorrowed
