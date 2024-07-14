import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self, account_number, balance=0, passkey=0):
        self.account_number = account_number
        self.balance = balance
        self.passkey = passkey

    def deposit(self, amount, passkey):
        if passkey == self.passkey:
            if amount > 0:
                self.balance += amount
                return True
            else:
                return False
        else:
            return False

    def withdraw(self, amount, passkey):
        if passkey == self.passkey:
            if 0 < amount <= self.balance:
                self.balance -= amount
                return True
            else:
                return False
        else:
            return False

    def get_balance(self):
        return self.balance

class ATM:
    def __init__(self, master, account):
        self.master = master
        self.account = account
        self.balance_label = tk.Label(master, text="Balance: $0.00")
        self.balance_label.pack()
        self.account_number_label = tk.Label(master, text=f"Account Number: {account.account_number}")
        self.account_number_label.pack()
        self.passkey_label = tk.Label(master, text="Enter Passkey:")
        self.passkey_label.pack()
        self.passkey_entry = tk.Entry(master, show="*")
        self.passkey_entry.pack()
        self.amount_label = tk.Label(master, text="Enter Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(master)
        self.amount_entry.pack()
        self.deposit_button = tk.Button(master, text="Deposit", command=self.deposit)
        self.deposit_button.pack()
        self.withdraw_button = tk.Button(master, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()
        self.check_balance_button = tk.Button(master, text="Check Balance", command=self.check_balance)
        self.check_balance_button.pack()

    def deposit(self):
        passkey = int(self.passkey_entry.get())
        amount = float(self.amount_entry.get())
        if self.account.deposit(amount, passkey):
            self.balance_label.config(text=f"Balance: ${self.account.get_balance():.2f}")
            messagebox.showinfo("Success", "Deposit successful")
        else:
            messagebox.showerror("Error", "Invalid passkey or amount")

    def withdraw(self):
        passkey = int(self.passkey_entry.get())
        amount = float(self.amount_entry.get())
        if self.account.withdraw(amount, passkey):
            self.balance_label.config(text=f"Balance: ${self.account.get_balance():.2f}")
            messagebox.showinfo("Success", "Withdrawal successful")
        else:
            messagebox.showerror("Error", "Invalid passkey or amount")

    def check_balance(self):
        passkey = int(self.passkey_entry.get())
        if self.account.passkey == passkey:
            messagebox.showinfo("Balance", f"Your balance is: ${self.account.get_balance():.2f}")
        else:
            messagebox.showerror("Error", "Invalid passkey")

root = tk.Tk()
account = BankAccount("1234", 1000, 1111)
atm = ATM(root, account)
root.mainloop()