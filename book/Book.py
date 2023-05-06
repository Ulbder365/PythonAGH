class Book:
    def __init__(self, isbn, title, author, keywords, borrowed, reserved, borrowed_till):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.keywords = keywords
        self.borrowed = borrowed
        self.reserved = reserved
        self.borrowed_till = borrowed_till

    def __str__(self):
        return f"{self.isbn},{self.title},{self.author},{self.keywords}," \
               f"{self.borrowed},{self.reserved},{self.borrowed_till}"
