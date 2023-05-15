class LoginSystem:
    def __init__(self, users):
        self.users = users

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:  # a gdyby z tego zrobić słownik, a nie listę?
                print(
                    "Successful logged")  # lepiej zostawić wypisywanie kodowi wyższego poziomu; tutaj samo zwrócenie wystarczy
                return user
        print("Wrong credentials")
        return False
