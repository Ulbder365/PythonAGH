class LoginSystem:
    def __init__(self, users):
        self.users = users

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                print("Successful logged")
                return user
        print("Wrong credentials")
        return False
