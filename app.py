from tkinter import *
from bankapi import BankAPI
from bankdb import Database
from tkinter import messagebox


class BankingApp:
    def __init__(self):
        self.dbo = Database()
        self.api = BankAPI()
        self.root = Tk()  # Initalizing Tkinter window for the app
        self.root.title("Indian Net Banking System")
        self.root.geometry("350x600")  # Setting the window size
        self.root.configure(bg="#D6EAE8")

        self.login_gui()  # Displaying the login GUI initially
        self.root.mainloop()  # Running the tkinter event loop to keep app running

    def login_gui(self):
        self.clear()
        Label(
            self.root,
            text="Internet Banking",
            bg="#D6EAE8",
            fg="black",
            font=("Helvetica", 24, "bold"),
        ).pack(pady=(32, 32))

        # Email Input
        Label(
            self.root,
            text="Enter your Email",
            bg="#D6EAE8",
            fg="black",
            font=("Helvetica", 10, "bold"),
        ).pack(pady=(12, 35))
        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(ipady=5, pady=(1, 10))

        # Password Input
        Label(
            self.root,
            text="Enter your Password",
            bg="#D6EAE8",
            fg="black",
            font=("Helvetica", 10, "bold"),
        ).pack(pady=(12, 35))
        self.password_input = Entry(self.root, width=30, show="*")
        self.password_input.pack(ipady=5, pady=(1, 10))

        # Login Button
        Button(self.root, text="Login", width=20, command=self.perform_login).pack(
            pady=(20, 10)
        )

        Label(self.root, text="Not a member?", bg="#D6EAE8", fg="black").pack(
            pady=(10, 5)
        )

        # Register Button
        Button(
            self.root,
            text="Not Register yet? Signup",
            width=20,
            command=self.register_gui,
        ).pack(pady=(20, 10))

        # Register Button
        Button(self.root, text="Back to login", width=20).pack(pady=(20, 10))

    def register_gui(self):
        self.clear()
        Label(
            self.root,
            text="Internet Banking",
            bg="#D6EAE8",
            fg="black",
            font=("Helvetica", 24, "bold"),
        ).pack(pady=(32, 32))

        # Name Input
        Label(
            self.root,
            text="Enter your Name",
            bg="#D6EAE8",
            fg="black",
            font=("Helvetica", 10, "bold"),
        ).pack(pady=(12, 35))
        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(ipady=5, pady=(1, 10))

        # Email Input
        Label(
            self.root,
            text="Enter your Email",
            bg="#D6EAE8",
            fg="black",
            font=("Helvetica", 10, "bold"),
        ).pack(pady=(12, 35))
        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(ipady=5, pady=(1, 10))

        # Password Input
        Label(
            self.root,
            text="Enter your Password",
            bg="#D6EAE8",
            fg="black",
            font=("Helvetica", 10, "bold"),
        ).pack(pady=(12, 35))
        self.password_input = Entry(self.root, width=30, show="*")
        self.password_input.pack(ipady=5, pady=(1, 10))

        Button(
            self.root, text="Register", width=20, command=self.perform_registration
        ).pack(pady=(20, 10))

        Button(self.root, text="Back to login", width=20, command=self.login_gui).pack(
            pady=(20, 10)
        )

    def clear(self):
        for widget in self.root.pack_slaves():
            widget.destroy()

    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        if self.dbo.add_user(name, email, password):
            messagebox.showinfo("Success", "Registration Successful!")
        else:
            messagebox.showinfo("Error", "Email Already Exists")

        print(name, email, password)

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        if self.dbo.authenticate_user(email, password):
            messagebox.showinfo("Success", "Login Successfull, Welcome to Bank")
            self.dashboard_gui(email)
        else:
            messagebox.showerror("Error", "Invalid EMail/Password, you are a thief")

    def dashboard_gui(self, email):
        self.clear()

        Label(
            self.root,
            text="Dashboard",
            bg="#D6EAE8",
            fg="black",
            font=("Helvetica", 10, "bold"),
        ).pack(pady=(30, 5))

        Button(
            self.root,
            text="View Balance",
            width=20,
            command=lambda: self.view_balance(email),
        ).pack(pady=(20, 10))

        Button(
            self.root,
            text="Deposite Money",
            width=20,
            command=lambda: self.view_balance(email, "deposite"),
        ).pack(pady=(20, 10))

        Button(
            self.root,
            text="Withdraw Money",
            width=20,
            command=lambda: self.view_balance(email, "withdraw"),
        ).pack(pady=(20, 10))

        Button(
            self.root,
            text="Transfer Funds",
            width=20,
            command=lambda: self.view_balance(email, "transfer"),
        ).pack(pady=(20, 10))

        Button(self.root, text="Logout", width=20, command=self.login_gui).pack(
            pady=(20, 10)
        )

    def view_balance(self, email):
        balance = self.dbo.get_balance(email)
        messagebox.showinfo("Balance", f"Your current balance is {balance}")

    def transaction_gui(self, email, transaction_type):
        pass


BankingApp()
