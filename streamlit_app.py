import streamlit as st
from backend import Bank

bank = Bank()

st.set_page_config(page_title="Bank Management System", page_icon="🏦", layout="centered")

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Navigation",
    ["Create Account", "Check Details", "Update Details", "Delete Account",
     "Deposit Amount", "Withdraw Amount", "Check Balance", "View All Accounts"]
)

if menu == "Create Account":
    st.header("Create a New Bank Account")
    with st.form("create_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0)
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        pin = st.number_input("4-digit PIN", min_value=1000, max_value=9999)
        submitted = st.form_submit_button("Create Account")
        if submitted:
            success, result = bank.create_account(name, age, email, phone, pin)
            if success:
                st.success(f"Account Created! Your Account Number: {result}")
            else:
                st.error(f"Failed to create account: {result}")

elif menu == "Check Details":
    st.header("Check Account Details")
    acno = st.text_input("Account Number")
    pin = st.number_input("PIN", min_value=1000, max_value=9999)
    if st.button("Check"):
        acc = bank.find_account(acno, pin)
        if acc:
            st.json(acc)
        else:
            st.error("Account not found.")

elif menu == "Update Details":
    st.header("Update Account Details")
    acno = st.text_input("Account Number")
    pin = st.number_input("PIN", min_value=1000, max_value=9999)
    name = st.text_input("New Name")
    age = st.number_input("New Age", min_value=0)
    email = st.text_input("New Email")
    phone = st.text_input("New Phone")
    if st.button("Update"):
        if bank.update_account(acno, pin, {"Name": name, "Age": age, "Email": email, "Phone": phone}):
            st.success("Account updated successfully.")
        else:
            st.error("Account not found or invalid details.")

elif menu == "Delete Account":
    st.header("Delete Account")
    acno = st.text_input("Account Number")
    pin = st.number_input("PIN", min_value=1000, max_value=9999)
    if st.button("Delete"):
        if bank.delete_account(acno, pin):
            st.success("Account deleted successfully.")
        else:
            st.error("Account not found.")

elif menu == "Deposit Amount":
    st.header("Deposit Money")
    acno = st.text_input("Account Number")
    pin = st.number_input("PIN", min_value=1000, max_value=9999)
    amount = st.number_input("Amount", min_value=1)
    if st.button("Deposit"):
        if bank.deposit(acno, pin, amount):
            st.success("Deposit successful.")
        else:
            st.error("Account not found.")

elif menu == "Withdraw Amount":
    st.header("Withdraw Money")
    acno = st.text_input("Account Number")
    pin = st.number_input("PIN", min_value=1000, max_value=9999)
    amount = st.number_input("Amount", min_value=1)
    if st.button("Withdraw"):
        if bank.withdraw(acno, pin, amount):
            st.success("Withdrawal successful.")
        else:
            st.error("Account not found or insufficient funds.")

elif menu == "Check Balance":
    st.header("Check Account Balance")
    acno = st.text_input("Account Number")
    pin = st.number_input("PIN", min_value=1000, max_value=9999)
    if st.button("Check Balance"):
        balance = bank.check_balance(acno, pin)
        if balance is not None:
            st.info(f"Your Balance: ₹{balance}")
        else:
            st.error("Account not found.")

elif menu == "View All Accounts":
    st.header("All Accounts")
    accounts = bank.get_all_accounts()
    st.dataframe(accounts)
