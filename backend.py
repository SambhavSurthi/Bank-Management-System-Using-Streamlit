import json
import os
import random
import string

DATA_FILE = "data.json"


def load_data():
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def generate_account_no():
    letters = random.choices(string.ascii_letters, k=4)
    upper = random.choices(string.ascii_uppercase, k=1)
    digits = random.choices(string.digits, k=8)
    return "".join(letters + upper + digits)


class Bank:
    def __init__(self):
        self.data = load_data()

    def create_account(self, name, age, email, phone, pin):
        if age < 18 or len(str(pin)) != 4 or '@' not in email:
            return False, "Invalid details"

        account = {
            "Name": name,
            "Age": age,
            "Email": email,
            "Phone": phone,
            "AccountNo": generate_account_no(),
            "Pin": pin,
            "Balance": 0
        }
        self.data.append(account)
        save_data(self.data)
        return True, account["AccountNo"]

    def find_account(self, acno, pin):
        for acc in self.data:
            if acc["AccountNo"] == acno and acc["Pin"] == pin:
                return acc
        return None

    def update_account(self, acno, pin, new_info):
        acc = self.find_account(acno, pin)
        if not acc:
            return False
        acc.update(new_info)
        save_data(self.data)
        return True

    def delete_account(self, acno, pin):
        acc = self.find_account(acno, pin)
        if not acc:
            return False
        self.data.remove(acc)
        save_data(self.data)
        return True

    def deposit(self, acno, pin, amount):
        acc = self.find_account(acno, pin)
        if not acc:
            return False
        acc["Balance"] += amount
        save_data(self.data)
        return True

    def withdraw(self, acno, pin, amount):
        acc = self.find_account(acno, pin)
        if not acc or acc["Balance"] < amount:
            return False
        acc["Balance"] -= amount
        save_data(self.data)
        return True

    def check_balance(self, acno, pin):
        acc = self.find_account(acno, pin)
        if not acc:
            return None
        return acc["Balance"]

    def get_all_accounts(self):
        return self.data
