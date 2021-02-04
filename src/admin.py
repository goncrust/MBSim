import tkinter as tk
from tkcalendar import Calendar, DateEntry


class Admin:

    def __init__(self, interface):
        self.interface = interface

    def generate_menu_search(self, label):
        self.admin_user_search_text = tk.StringVar()

        self.admin_user_search_entry = tk.Entry(
            self.interface.canvas, textvariable=self.admin_user_search_text, font=("default", 21))

        self.admin_user_search_entry.config(fg="grey")
        self.admin_user_search_entry.insert(0, label)

        self.admin_user_search_entry.place(
            x=(750/2)-100, y=(750/2)-20-200, width=200, height=40)

        self.admin_user_search_entry.bind(
            "<Button-1>", self.focusin_admin_user_search_entry)

    def focusin_admin_user_search_entry(self, event):
        if self.admin_user_search_entry.cget("fg") == "grey":
            self.admin_user_search_entry.config(fg="black")
            self.admin_user_search_entry.delete(0, tk.END)

        self.interface.focusedin = True

    def destroy_menu_search(self):
        self.admin_user_search_text = None
        self.admin_user_search_entry.destroy()

    def generate_menu_user(self, label):
        self.username = self.admin_user_search_entry.get()

        if not self.interface.username_exists(self.username):
            return False
        else:
            self.admin_username_text = tk.StringVar()
            self.admin_username_text.set(self.username)

            self.admin_account_number_text = tk.StringVar()
            self.admin_account_number_text.set(
                self.interface.get_account_number_from_username(self.username))

            self.admin_bank_text = tk.StringVar()
            self.admin_bank_text.set(
                self.interface.get_bank_from_username(self.username))

            self.admin_pin_text = tk.StringVar()

            birthday = self.interface.get_birthday_from_username(self.username)

            self.admin_balance_text = tk.StringVar()
            self.admin_balance_text.set(
                self.interface.get_balance_from_username(self.username))

            self.admin_username_entry = tk.Entry(
                self.interface.canvas, textvariable=self.admin_username_text, font=("default", 21))
            self.admin_account_number_entry = tk.Entry(
                self.interface.canvas, textvariable=self.admin_account_number_text, font=("default", 21))
            self.admin_bank_entry = tk.Entry(
                self.interface.canvas, textvariable=self.admin_bank_text, font=("default", 21))
            self.admin_pin_entry = tk.Entry(
                self.interface.canvas, textvariable=self.admin_pin_text, font=("default", 21))
            self.admin_calendar_field = Calendar(
                self.interface.canvas, font=("default", 9), selectmode="day", day=int(birthday[0:2]), month=int(birthday[3:5]), year=int(birthday[6:10]))
            self.admin_balance_entry = tk.Entry(
                self.interface.canvas, textvariable=self.admin_balance_text, font=("default", 21))

            self.admin_username_entry.place(x=10, y=10, width=200, height=40)
            self.admin_account_number_entry.place(
                x=10, y=52, width=450, height=40)
            self.admin_bank_entry.place(x=10, y=94, width=200, height=40)
            self.admin_pin_entry.place(x=10, y=136, width=200, height=40)
            self.admin_calendar_field.place(
                x=10, y=178, height=150, width=200)
            self.admin_balance_entry.place(x=10, y=330, width=200, height=40)

            self.admin_pin_entry.config(fg="grey")
            self.admin_pin_entry.insert(0, label)

            self.admin_username_entry.bind(
                "<Button-1>", self.focusin_admin_username_entry)
            self.admin_account_number_entry.bind(
                "<Button-1>", self.focusin_admin_account_number_entry)
            self.admin_bank_entry.bind(
                "<Button-1>", self.focusin_admin_bank_entry)
            self.admin_pin_entry.bind(
                "<Button-1>", self.focusin_admin_pin_entry)
            self.admin_balance_entry.bind(
                "<Button-1>", self.focusin_admin_balance_entry)

            return True

    def focusin_admin_username_entry(self, event):
        self.interface.focusedin = True

    def focusin_admin_account_number_entry(self, event):
        self.interface.focusedin = True

    def focusin_admin_bank_entry(self, event):
        self.interface.focusedin = True

    def focusin_admin_pin_entry(self, event):
        if self.admin_pin_entry.cget("fg") == "grey":
            self.admin_pin_entry.config(fg="black")
            self.admin_pin_entry.delete(0, tk.END)

        self.interface.focusedin = True

    def focusin_admin_balance_entry(self, event):
        self.interface.focusedin = True

    def destroy_menu_user(self):
        self.username = None
        self.admin_username_text = None
        self.admin_account_number_text = None
        self.admin_bank_text = None
        self.admin_pin_text = None
        self.admin_balance_text = None

        self.admin_username_entry.destroy()
        self.admin_account_number_entry.destroy()
        self.admin_bank_entry.destroy()
        self.admin_pin_entry.destroy()
        self.admin_calendar_field.destroy()
        self.admin_balance_entry.destroy()

    def return_user_modification(self):
        return self.admin_username_text.get(), self.admin_account_number_text.get(), self.admin_bank_text.get(), self.admin_pin_text.get(), self.admin_calendar_field.selection_get(), self.admin_balance_entry.get()

    def return_user_to_delete(self):
        return self.username
