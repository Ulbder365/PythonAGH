class User:
    def __init__(self, uuid, username, password, role, catalog):
        self.uuid = uuid
        self.username = username
        self.password = password
        self.role = role
        self.catalog = catalog

    def __str__(self):
        return f"{self.uuid},{self.username},{self.password},{self.role}"

    def printCatalog(self):
        for book in self.catalog:
            print(book)

    def searchBook(self, field, value):
        booksFound = []
        for book in self.catalog:
            if field == 'title' and value.lower() in book.title.lower():
                booksFound.append(book)
            elif field == 'author' and value.lower() in book.author.lower():
                booksFound.append(book)
            elif field == 'keywords' and value.lower() in book.keywords.lower():
                booksFound.append(book)
        return booksFound

    def searchBookByISBN(self, isbn):
        for book in self.catalog:
            if book.isbn == isbn:
                return book
        print('There is no book with given isbn number')
        return False
