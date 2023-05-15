from role.User import User  # lepszy byłby import względny


class Librarian(User):
    def __init__(self, uuid, username, password, role, catalog, users):
        super().__init__(uuid, username, password, role, catalog)
        self.users = users

    def returnBook(self, isbn):  # snake_case
        book = self.searchBookByISBN(isbn)
        if book:
            book.borrowed = False
            book.borrowed_till = False

    def deleteBook(self, isbn):
        book = self.searchBookByISBN(isbn)
        if book is not False:
            self.catalog.remove(book)

    def addBook(self, book):
        self.catalog.append(book)

    def addReader(self, reader):
        self.users.append(reader)
