import json


class Database:
    def __init__(self):
        self.file = "bankdb.json"
        self.load_data()

    def load_data(self):
        try:
            with open(self.file, "r") as f:
                self.data = json.load(f)
        except (FileNotFoundError, ValueError):
            self.data = {}
            with open(self.file, "w") as f:
                json.dump(self.data, f)

    def save_data(self):
        with open(self.file, "w") as f:
            json.dump(self.data, f)

    def add_user(self, name, email, password):
        if email in self.data:
            return False

        self.data[email] = {
            "name": name,
            "email": email,
            "password": password,
            "balance": 0,
        }

        self.save_data()
        return True

    def authenticate_user(self, email, password):
        return email in self.data and self.data[email]["password"] == password

    def get_balance(self, email):
        return self.data[email]["balance"]

    def update_balance(self):
        pass
