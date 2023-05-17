import tkinter as tk

from auth.LoginSystem import LoginSystem
from book.Book import Book
from role.Librarian import Librarian
from role.Reader import Reader
from role.User import User
from system.Localhost import LocalSession

librarySystem = LocalSession()
loginSystem = LoginSystem(librarySystem.users)


class LibraryGUI:
    def __init__(self, master):
        self.login_user = None
        self.master = master
        master.title("Library System")
        self.main_view()

    # Views
    def main_view(self):
        label = tk.Label(text="Welcome to the Library System!")
        label.pack()
        username_field = tk.Entry(root)
        username_field.pack()
        password_field = tk.Entry(root)
        password_field.pack()
        button = tk.Button(text="Login to system",
                           command=lambda: self.get_login_credentials(username_field, password_field))
        button.pack()

    def reader_view(self):
        self.clear_window()
        label_main = tk.Label(text="Reader main menu view!")
        label_main.pack()
        button_catalog = tk.Button(text="Show book catalog", command=self.catalog_view)
        button_catalog.pack()
        button_borrowed = tk.Button(text="My borrowed books", command=self.borrowed_books_view)
        button_borrowed.pack()
        button_reserved = tk.Button(text="My reserved books", command=self.reserved_books_view)
        button_reserved.pack()
        button_reserve = tk.Button(text="Reserve book", command=self.reserve_book_view)
        button_reserve.pack()
        button_borrow = tk.Button(text="Borrow book", command=self.borrow_book_view)
        button_borrow.pack()
        button_extend_time = tk.Button(text="Extend the book borrowing time", command=self.extend_time_view)
        button_extend_time.pack()
        button_logout = tk.Button(text="Logout", command=self.logout)
        button_logout.pack()

    def librarian_view(self):
        self.clear_window()
        label_main = tk.Label(text="Librarian main menu view!")
        label_main.pack()
        button_catalog = tk.Button(text="Show book catalog", command=self.catalog_view)
        button_catalog.pack()
        button_return_book = tk.Button(text="Return book", command=self.return_book_view)
        button_return_book.pack()
        button_add_book = tk.Button(text="Add new book", command=self.add_book_view)
        button_add_book.pack()
        button_add_reader = tk.Button(text="Add new reader", command=self.add_reader_view)
        button_add_reader.pack()
        button_delete_book = tk.Button(text="Delete book", command=self.delete_book_view)
        button_delete_book.pack()
        button_logout = tk.Button(text="Logout", command=self.logout)
        button_logout.pack()

    def catalog_view(self):
        self.clear_window()
        text = tk.Text(height=10, width=50)
        text.pack()
        button_show = tk.Button(text="Show books", command=lambda: self.load_books(text, "catalog"))
        button_show.pack()
        self.menu_button()

    def reserved_books_view(self):
        self.clear_window()
        text = tk.Text(height=10, width=50)
        text.pack()
        button_show = tk.Button(text="Show books", command=lambda: self.load_books(text, "reserved"))
        button_show.pack()
        self.menu_button()

    def borrowed_books_view(self):
        self.clear_window()
        text = tk.Text(height=10, width=50)
        text.pack()
        button_show = tk.Button(text="Show books", command=lambda: self.load_books(text, "borrowed"))
        button_show.pack()
        self.menu_button()

    def reserve_book_view(self):
        self.clear_window()
        isbn_field = tk.Entry(root)
        isbn_field.pack()
        button_borrow = tk.Button(text="Reserve book", command=lambda: self.reserve_book(isbn_field))
        button_borrow.pack()
        self.menu_button()

    def borrow_book_view(self):
        self.clear_window()
        isbn_field = tk.Entry(root)
        isbn_field.pack()
        button_borrow = tk.Button(text="Borrow book", command=lambda: self.borrow_book(isbn_field))
        button_borrow.pack()
        self.menu_button()

    def extend_time_view(self):
        self.clear_window()
        isbn_field = tk.Entry(root)
        isbn_field.pack()
        button_borrow = tk.Button(text="Extend time", command=lambda: self.extend_time(isbn_field))
        button_borrow.pack()
        self.menu_button()

    def delete_book_view(self):
        self.clear_window()
        isbn_field = tk.Entry(root)
        isbn_field.pack()
        button_borrow = tk.Button(text="Delete book", command=lambda: self.delete_book(isbn_field))
        button_borrow.pack()
        self.menu_button()

    def return_book_view(self):
        self.clear_window()
        isbn_field = tk.Entry(root)
        isbn_field.pack()
        button_borrow = tk.Button(text="Return book", command=lambda: self.return_book(isbn_field))
        button_borrow.pack()
        self.menu_button()

    def add_book_view(self):
        self.clear_window()

        isbn_label = tk.Label(text="ISBN Number")
        isbn_label.pack()
        isbn_field = tk.Entry(root)
        isbn_field.pack()

        title_label = tk.Label(text="Title")
        title_label.pack()
        title_field = tk.Entry(root)
        title_field.pack()

        author_label = tk.Label(text="Author")
        author_label.pack()
        author_field = tk.Entry(root)
        author_field.pack()

        keyword_label = tk.Label(text="Keyword")
        keyword_label.pack()
        keyword_field = tk.Entry(root)
        keyword_field.pack()

        button_add_book = tk.Button(text="Add book",
                                    command=lambda: self.add_book(isbn_field, title_field, author_field, keyword_field))
        button_add_book.pack()
        self.menu_button()

    def add_reader_view(self):
        self.clear_window()

        uuid_label = tk.Label(text="UUID")
        uuid_label.pack()
        uuid_field = tk.Entry(root)
        uuid_field.pack()

        username_label = tk.Label(text="Username")
        username_label.pack()
        username_field = tk.Entry(root)
        username_field.pack()

        password_label = tk.Label(text="Password")
        password_label.pack()
        password_field = tk.Entry(root)
        password_field.pack()

        button_add_reader = tk.Button(text="Add reader",
                                      command=lambda: self.add_reader(uuid_field, username_field, password_field))
        button_add_reader.pack()
        self.menu_button()

    # Functions

    def select_menu(self):
        if self.login_user.role == "Reader":
            self.reader_view()
        elif self.login_user.role == "Librarian":
            self.librarian_view()

    def menu_button(self):
        button_show = tk.Button(text="Menu", command=self.select_menu)
        button_show.pack()

    def load_books(self, text, kind):
        text.delete("1.0", tk.END)
        books_to_found = []
        if kind == "catalog":
            books_to_found = self.login_user.catalog
        elif kind == "reserved":
            books_to_found = self.login_user.bookReserved()
        elif kind == "borrowed":
            books_to_found = self.login_user.bookBorrowed()

        for book in books_to_found:
            text.insert(tk.END, f"ISBN Number: {book.isbn}\n")
            text.insert(tk.END, f"Title: {book.title}\n")
            text.insert(tk.END, f"Author: {book.author}\n")
            text.insert(tk.END, f"Borrowed: {book.borrowed}\n")
            text.insert(tk.END, f"Borrowed_till: {book.borrowed_till}\n")
            text.insert(tk.END, f"Reserved: {book.reserved}\n")
            text.insert(tk.END, "\n")

    def logout(self):
        self.login_user = None
        self.clear_window()
        self.main_view()

    def get_login_credentials(self, username_field, password_field):
        username = username_field.get()
        password = password_field.get()
        user: User = loginSystem.login(username, password)
        if user is not False:
            if user.role == "Reader":
                self.login_user = Reader(user.uuid, user.username, user.password, user.role, librarySystem.books)
                self.reader_view()
            elif user.role == "Librarian":
                self.login_user = Librarian(user.uuid, user.username, user.password, user.role, librarySystem.books,
                                            librarySystem.users)
                self.librarian_view()

    def borrow_book(self, isbn_field):
        isbn = isbn_field.get()
        self.login_user.borrowBook(isbn)
        librarySystem.save_data()
        self.borrowed_books_view()

    def reserve_book(self, isbn_field):
        isbn = isbn_field.get()
        self.login_user.reserveBook(isbn)
        librarySystem.save_data()
        self.reserved_books_view()

    def extend_time(self, isbn_field):
        isbn = isbn_field.get()
        self.login_user.extendTime(isbn)
        librarySystem.save_data()
        self.borrowed_books_view()

    def return_book(self, isbn_field):
        isbn = isbn_field.get()
        self.login_user.returnBook(isbn)
        librarySystem.save_data()
        self.catalog_view()

    def delete_book(self, isbn_field):
        isbn = isbn_field.get()
        self.login_user.deleteBook(isbn)
        librarySystem.save_data()
        self.catalog_view()

    def add_book(self, isbn_field, title_field, author_field, keywords_field):
        isbn = isbn_field.get()
        title = title_field.get()
        author = author_field.get()
        keyword = keywords_field.get()
        book = Book(isbn, title, author, keyword, False, False, False)

        self.login_user.addBook(book)
        librarySystem.save_data()
        self.catalog_view()

    def add_reader(self, uuid_field, username_field, password_field):
        uuid = uuid_field.get()
        username = username_field.get()
        password = password_field.get()
        reader = Reader(uuid, username, password, "Reader", self.login_user.catalog)

        self.login_user.addReader(reader)
        librarySystem.save_data()
        self.select_menu()

    def clear_window(self):
        for child in root.winfo_children():
            child.destroy()


# Start
root = tk.Tk()
my_gui = LibraryGUI(root)
root.mainloop()
