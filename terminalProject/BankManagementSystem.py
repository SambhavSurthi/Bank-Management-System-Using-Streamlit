import random
from pathlib import Path
import json
import string
# from traceback import print_tb

with open("data.json", "r") as file:
    data = json.load(file)  # convert json to python dictionary
def readAllData():
    print(data)



def updateData(info):
    if isinstance(data,list):
        data.append(info)

    if isinstance(data,dict):
        data.update(info)

    with open("data.json", "w") as file:
        json.dump(data,file)

def updateUserData(acno,pin,info):
    for account in data:
        if account["AccountNo"]==acno and account["Pin"]==pin:
            account.update(info)
            break

    with open("data.json", 'w') as file:
        json.dump(data,file)


class Bank:
    @staticmethod
    def __accountNoGenerator():
        x=random.choices(string.ascii_letters,k=4)
        y=random.choices(string.ascii_uppercase,k=1)
        z=random.choices(string.digits,k=8)
        return "".join(x+y+z)



    def createAccount(self):
        try:
            info = {
                "Name": input("Enter Your Name: "),
                "Age": int(input("Enter Your Age: ")),
                "Email": input("Enter Your Email: "),
                "Phone": int(input("Enter Your Phone Number: ")),
                "AccountNo": Bank.__accountNoGenerator(),
                "Pin": int(input("Enter a 4 digit Pin to Secure Your Account: ")),
                "Balance": 0
            }

            if info["Age"] >= 18 and len(str(info["Pin"])) == 4 and info["Email"].__contains__('@'):
                updateData(info)
                print("Account Created Successfully")
                print(
                    f"Your Account Number is {info["AccountNo"]} . Please Remember this, 4 digit Pin to Access Your Account")

            else:
                print("Account Creation Failed. Please Check All your Details and Try Again")

        except Exception as err:
            print(f"An Exception Has Occured {err}")



    def checkDetails(self):
        try:
            acno = input("Enter Your Account Number: ")
            pin = int(input("Enter Your Account Pin: "))

            for account in data:
                if (account["AccountNo"] == acno) and (account["Pin"] == pin):
                    print(account)
                    return
                else:
                    print("Account Not Found. Please Check Your details properly")

        except Exception as err:
            print(f"An Exception Has Occured {err}")


    def updateDetails(self):
        try:
            acno = input("Enter Your Account Number: ")
            pin = int(input("Enter You Account Pin: "))

            print("Your Initial Details Are: ")
            for account in data:
                if (account["AccountNo"] == acno) and (account["Pin"] == pin):
                    print(account)
                else:
                    print("Account Not Found. Please Check Your details properly")

            print("Enter the Details That Needs to be Updated: ")
            info = {
                "Name": input("Enter Your Name: "),
                "Age": int(input("Enter Your Age: ")),
                "Email": input("Enter Your Email: "),
                "Phone": int(input("Enter Your Phone Number: "))
            }

            updateUserData(acno, pin, info)

            print("Your Details After Updates Are: ")
            for account in data:
                if (account["AccountNo"] == acno) and (account["Pin"] == pin):
                    print(account)
                    return
                else:
                    print("Account Not Found. Please Check Your details properly")

        except Exception as err:
            print(f"An Exception has Occured {err}")

    def deleteUser(self):
        try:
            acno = input("Enter Your Account Number: ")
            pin = int(input("Enter Your Account Pin: "))

            account_data = None
            for account in data:
                if account["AccountNo"] == acno and account["Pin"] == pin:
                    account_data = account
                    break

            if account_data:
                print("Your Initial Account Details")
                print(account_data)

                data.remove(account_data)

                with open('data.json', "w") as file:
                    json.dump(data, file)

                print("Account Deleted Successfully")
            else:
                print("Account Not Found. Please Check Your details properly")

        except Exception as err:
            print(f"An Exception has Occured {err}")

    def depositAmount(self):
        try:
            acno = input("Enter Your Account Number: ")
            pin = int(input("Enter Your Account Pin: "))

            for account in data:
                if account["AccountNo"] == acno and account["Pin"] == pin:
                    print(f"Your Initial Balance is: {account['Balance']}")
                    amount = int(input("Enter Amount to Deposit: "))
                    account["Balance"] += amount
                    with open('data.json', 'w') as file:
                        json.dump(data, file)
                    print(f"Deposit Successful! New Balance: {account['Balance']}")
                    return

            print("Account Not Found. Please Check Your details properly")

        except Exception as err:
            print(f"An Exception has Occured {err}")

    def withDrawAmount(self):
        try:
            acno = input("Enter Your Account Number: ")
            pin = int(input("Enter Your Account Pin: "))

            for account in data:
                if account["AccountNo"] == acno and account["Pin"] == pin:
                    print(f"Your Initial Balance is: {account['Balance']}")
                    amount = int(input("Enter Amount to WithDraw: "))
                    account["Balance"] -= amount
                    with open('data.json', 'w') as file:
                        json.dump(data, file)
                    print(f"WithDraw Successful! New Balance: {account['Balance']}")
                    return

            print("Account Not Found. Please Check Your details properly")

        except Exception as err:
            print(f"An Exception has Occured {err}")

    def checkBalance(self):
        try:
            acno = input("Enter Your Account Number: ")
            pin = int(input("Enter Your Account Pin: "))

            for account in data:
                if account["AccountNo"] == acno and account["Pin"] == pin:
                    print(f"Your Balance is: {account['Balance']}")
                    return

            print("Account Not Found. Please Check Your details properly")

        except Exception as err:
            print(f"An Exception has Occured {err}")



class User(Bank):
    def mainClass(self):

        while True:
            print("1. Create Your Account")
            print("2. Check You Details")
            print("3. Update You Details")
            print("4. Delete You Account")
            print("5. Deposit Amount")
            print("6. Withdraw Amount")
            print("7. Check Balance")
            print("0. Quit")

            choice = int(input("Enter Your Choice: "))

            bank = Bank()

            if choice == 1:
                bank.createAccount()

            if choice == 2:
                bank.checkDetails()

            if choice == 3:
                bank.updateDetails()

            if choice == 4:
                bank.deleteUser()

            if choice == 5:
                bank.depositAmount()

            if choice == 6:
                bank.withDrawAmount()

            if choice == 7:
                bank.checkBalance()

            if choice==0:
                break

            else:
                print("Wrong Choice")



u=User()
u.mainClass()