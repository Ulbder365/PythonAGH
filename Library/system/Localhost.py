from book.Book import Book
from role.User import User


class LocalSession:
    def __init__(self):
        self.books = []
        self.users = []
        self.books_file = "books.txt"
        self.users_file = "users.txt"
        self.load_data()

    def load_data(self):
        with open(self.books_file, 'r') as file:
            for line in file:
                isbn, title, author, keywords, borrowed, reserved, borrowed_till = line.strip().split(",")
                book = Book(isbn, title, author, keywords, borrowed, reserved, borrowed_till)
                self.books.append(book)

        with open(self.users_file, 'r') as file:
            for line in file:
                uuid, username, password, role = line.strip().split(",")
                user = User(uuid, username, password, role, self.books)
                self.users.append(user)

    def save_data(self):
        with open(self.books_file, 'w') as file:
            for book in self.books:
                file.write(f"{str(book)}\n")
        with open(self.users_file, 'w') as file:
            for user in self.users:
                file.write(f"{str(user)}\n")
