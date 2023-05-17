from auth.LoginSystem import LoginSystem
from role.Librarian import Librarian
from role.Reader import Reader
from role.User import User
from system.Localhost import LocalSession

librarySystem = LocalSession()
loginSystem = LoginSystem(librarySystem.users)
# user: User = loginSystem.login('Reader', 'weakPass')
user: User = loginSystem.login('Librarian', 'strongPass')
if user.role == "Reader":
    loginUser = Reader(user.uuid, user.username, user.password, user.role, librarySystem.books)
elif user.role == "Librarian":
    loginUser = Librarian(user.uuid, user.username, user.password, user.role, librarySystem.books, librarySystem.users)

print(loginUser.searchBookByISBN('1'))
for book in loginUser.searchBook('title', 'filo'):
    print(book)
# loginUser.reserveBook('1')
loginUser.returnBook('1')
librarySystem.save_data()
