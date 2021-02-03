import tkinter as tk
import i_event_handler
from scenarios import *
from tkcalendar import Calendar, DateEntry
import time
import random

# window dimensions
WIDTH = 750
HEIGHT = 750

BACKGROUND_CLR = "#32a84e"


class Interface:

    def __init__(self, title):
        # title as constructur argument
        self.title = title

        # initialize 8 buttons as null
        self.buttons = [None, None, None, None, None, None, None, None]

        # create event handler
        self.event_handler = i_event_handler.IEventHandler(self)

        # create window and canvas
        self.create_window(WIDTH, HEIGHT)
        self.create_canvas()

        # user
        self.current_user = None

        # set first scenario and run it
        self.current_scenario = Scenario.LOGIN
        self.update_scenario()

        # focusin something
        self.focusedin = False

        # bind keys
        self.bind_keys()

        # tkinter mainloop
        self.window.mainloop()

    # create window function
    def create_window(self, width, height):
        self.window = tk.Tk()
        self.window.title(self.title)
        self.window.geometry(str(width) + "x" + str(height) + "+500+100")
        self.window.resizable(False, False)

        import image_loader
        self.window.iconphoto(False, image_loader.icon)

    # bind numpad keys
    def bind_keys(self):
        self.window.bind("7", lambda x=None: self.bind_keys_connector(7))
        self.window.bind("4", lambda x=None: self.bind_keys_connector(4))
        self.window.bind("1", lambda x=None: self.bind_keys_connector(1))
        self.window.bind("0", lambda x=None: self.bind_keys_connector(0))
        self.window.bind("9", lambda x=None: self.bind_keys_connector(9))
        self.window.bind("6", lambda x=None: self.bind_keys_connector(6))
        self.window.bind("3", lambda x=None: self.bind_keys_connector(3))
        self.window.bind(".", lambda x=None: self.bind_keys_connector("."))

    def bind_keys_connector(self, button):
        if not self.focusedin:
            if button == 7:
                self.event_handler.click_0("")
            elif button == 4:
                self.event_handler.click_1("")
            elif button == 1:
                self.event_handler.click_2("")
            elif button == 0:
                self.event_handler.click_3("")
            elif button == 9:
                self.event_handler.click_4("")
            elif button == 6:
                self.event_handler.click_5("")
            elif button == 3:
                self.event_handler.click_6("")
            elif button == ".":
                self.event_handler.click_7("")

    # create canvas function
    def create_canvas(self):
        self.canvas = tk.Canvas(self.window, width=WIDTH,
                                height=HEIGHT, bg=BACKGROUND_CLR, highlightthickness=0)
        self.canvas.pack()

    # update onscreen scenario
    def update_scenario(self):
        if self.current_user == "admin":
            self.scenario(Scenario.get_scenario_active(
                self.current_scenario, True), Scenario.get_scenario_text(self.current_scenario))
        else:
            self.scenario(Scenario.get_scenario_active(
                self.current_scenario, False), Scenario.get_scenario_text(self.current_scenario))

        if self.current_scenario == Scenario.LOGIN:
            self.login()
        elif self.current_scenario == Scenario.REGISTER:
            self.register()

        self.focusedin = False

    # place buttons and assign events
    def scenario(self, active, label):

        import image_loader

        # clear current buttons
        for x in range(len(self.buttons)):
            if self.buttons[x] != None:
                self.buttons[x].destroy()
                self.buttons[x] = None

        self.b_label = []
        for i in range(len(label)):
            image_loader.place_text(self, i, label[i])

        for z in range(len(active)):
            if active[z]:

                # create button
                self.buttons[z] = tk.Button(
                    self.canvas, image=self.b_label[z], borderwidth=0, highlightthickness=0)

                # place button
                if z == 0:
                    self.buttons[z].place(x=-1, y=105)
                elif z == 1:
                    self.buttons[z].place(x=-1, y=255)
                elif z == 2:
                    self.buttons[z].place(x=-1, y=405)
                elif z == 3:
                    self.buttons[z].place(x=-1, y=555)
                elif z == 4:
                    self.buttons[z].place(x=WIDTH-320, y=105)
                elif z == 5:
                    self.buttons[z].place(x=WIDTH-320, y=255)
                elif z == 6:
                    self.buttons[z].place(x=WIDTH-320, y=405)
                elif z == 7:
                    self.buttons[z].place(x=WIDTH-320, y=555)

                # assign events to button
                self.buttons[z].bind(
                    '<Button-1>', eval("self.event_handler.click_" + str(z)))

    # for login scenario
    def login(self):
        # variables to store fields data
        self.login_username_text = tk.StringVar()
        self.login_pin_text = tk.StringVar()

        # create entry objects
        self.username_field = tk.Entry(
            self.canvas, textvariable=self.login_username_text, font=("default", 23))
        self.pin_field = tk.Entry(
            self.canvas, textvariable=self.login_pin_text, show='*', font=("default", 23))
        self.login_warning_label = tk.Label(self.canvas, font=(
            "default", 18), justify=tk.LEFT, bg=BACKGROUND_CLR, fg="red")

        # place entry objects
        self.username_field.place(
            x=(WIDTH/2)-100, y=(HEIGHT/2)-20-42-20, width=200, height=40)
        self.pin_field.place(
            x=(WIDTH/2)-100, y=(HEIGHT/2)-20-20, width=200, height=40)
        self.login_warning_label.place(x=133, y=400)

        # greyed out default text
        self.username_field.config(fg="grey")
        self.pin_field.config(fg="grey")
        self.pin_field.config(show="")

        self.username_field.insert(0, Scenario.login_username_pt)
        self.pin_field.insert(0, Scenario.login_pin_pt)

        self.username_field.bind("<FocusIn>", self.focusin_username_login)
        self.pin_field.bind("<FocusIn>", self.focusin_pin_login)

    def focusin_username_login(self, pos):
        if self.username_field.cget("fg") == "grey":
            self.username_field.config(fg="black")
            self.username_field.delete(0, tk.END)

        self.focusedin = True

    def focusin_pin_login(self, pos):
        if self.pin_field.cget("fg") == "grey":
            self.pin_field.config(fg="black", show="*")
            self.pin_field.delete(0, tk.END)

        self.focusedin = True

    def login_warning(self):
        self.login_warning_label.config(text=Scenario.login_warning_pt)

    def destroy_login(self):
        # destroy fields
        self.username_field.destroy()
        self.pin_field.destroy()
        self.login_warning_label.destroy()

        # reset variables
        self.login_username_text.set("")
        self.login_pin_text.set("")

    # for register scenario
    def register(self):
        # variables to store fields data
        self.register_username_text = tk.StringVar()
        self.register_pin_text = tk.StringVar()
        self.register_pin_confirm_text = tk.StringVar()
        self.register_bank_text = tk.StringVar(self.canvas)
        self.register_bank_text.set("Caixa Geral de Depóstios")
        self.register_account_number = None

        self.register_bank_abb = None

        # create entry objects
        self.register_username_field = tk.Entry(
            self.canvas, textvariable=self.register_username_text, font=("default", 21))
        self.register_pin_field = tk.Entry(
            self.canvas, textvariable=self.register_pin_text, show='*', font=("default", 21))
        self.register_pin_confirm_field = tk.Entry(
            self.canvas, textvariable=self.register_pin_confirm_text, show='*', font=("default", 21))
        self.register_calendar_field = Calendar(
            self.canvas, font=("default", 9), selectmode="day", year=2000, month=1, day=1)
        self.register_bank_field = tk.OptionMenu(
            self.canvas, self.register_bank_text, "Caixa Geral de Depóstios", "Santander Totta", "Millennium BCP",
            "BPI", "Novo Banco", "Bankinter", "EuroBIC", "Popular", "Montepio", "Banco CTT", "BBVA", command=self.change_bank_register)
        self.register_info_field = tk.Label(
            self.canvas, text=Scenario.register_info_pt, font=("default", 18), justify=tk.LEFT, bg=BACKGROUND_CLR)
        self.register_warning_field = tk.Label(
            self.canvas, font=("default", 18), justify=tk.LEFT, bg=BACKGROUND_CLR, fg="red")
        self.register_calendar_label = tk.Label(self.canvas, font=(
            "default", 16), justify=tk.LEFT, bg=BACKGROUND_CLR, text=Scenario.register_calendar_field_pt)
        self.register_account_number_label = tk.Label(
            self.canvas, font=("default", 9), justify=tk.LEFT, fg="grey")

        # place entry objects
        self.register_username_field.place(x=10, y=10, width=200, height=40)
        self.register_pin_field.place(x=10, y=52, width=200, height=40)
        self.register_pin_confirm_field.place(x=10, y=94, width=200, height=40)
        self.register_calendar_field.place(x=10, y=250, height=150, width=200)
        self.register_bank_field.place(x=10, y=157, height=50, width=200)
        self.register_info_field.place(x=280, y=10)
        self.register_warning_field.place(x=450, y=475)
        self.register_calendar_label.place(x=10, y=220)
        self.register_account_number_label.place(x=220, y=170)

        # greyed out default text
        self.register_username_field.config(fg="grey")
        self.register_pin_field.config(fg="grey", show="")
        self.register_pin_confirm_field.config(fg="grey", show="")

        self.register_username_field.insert(0, Scenario.register_username_pt)
        self.register_pin_field.insert(0, Scenario.register_pin_pt)
        self.register_pin_confirm_field.insert(
            0, Scenario.register_pin_confirm_pt)

        self.register_username_field.bind(
            "<FocusIn>", self.focusin_username_register)
        self.register_pin_field.bind(
            "<FocusIn>", self.focusin_pin_register)
        self.register_pin_confirm_field.bind(
            "<FocusIn>", self.focusin_pin_confirm_register)

    def focusin_username_register(self, pos):
        if self.register_username_field.cget("fg") == "grey":
            self.register_username_field.config(fg="black")
            self.register_username_field.delete(0, tk.END)

        self.focusedin = True

    def focusin_pin_register(self, pos):
        if self.register_pin_field.cget("fg") == "grey":
            self.register_pin_field.config(fg="black", show="*")
            self.register_pin_field.delete(0, tk.END)

        self.focusedin = True

    def focusin_pin_confirm_register(self, pos):
        if self.register_pin_confirm_field.cget("fg") == "grey":
            self.register_pin_confirm_field.config(fg="black", show="*")
            self.register_pin_confirm_field.delete(0, tk.END)

        self.focusedin = True

    def set_warning_message_register(self, message):
        if message == 0:
            self.register_warning_field.config(
                text=Scenario.register_only_letters_pt)
        elif message == 1:
            self.register_warning_field.config(
                text=Scenario.register_short_username_pt)
        elif message == 2:
            self.register_warning_field.config(
                text=Scenario.register_only_numbers_pt)
        elif message == 3:
            self.register_warning_field.config(
                text=Scenario.register_pin_size_pt)
        elif message == 4:
            self.register_warning_field.config(
                text=Scenario.register_username_exists_pt)
        elif message == 5:
            self.register_warning_field.config(
                text=Scenario.register_pin_match_pt)
        elif message == 6:
            self.register_warning_field.config(text=Scenario.register_age_pt)

    def blink_info_register(self):
        self.register_info_field.config(fg="red")

    def change_bank_register(self, event):
        self.event_handler.update_interface_bank_numbers_abb()
        self.register_account_number_label.config(
            text=self.register_account_number)

    def destroy_register(self):
        # destroy fields
        self.register_username_field.destroy()
        self.register_pin_field.destroy()
        self.register_pin_confirm_field.destroy()
        self.register_calendar_field.destroy()
        self.register_bank_field.destroy()
        self.register_info_field.destroy()
        self.register_warning_field.destroy()
        self.register_bank_field.destroy()
        self.register_calendar_label.destroy()
        self.register_account_number_label.destroy()

        # reset variables
        self.register_username_text.set("")
        self.register_pin_text.set("")
        self.register_pin_confirm_text.set("")
        self.register_bank_text.set("Caixa Geral de Depóstios")
        self.register_account_number = None
        self.register_bank_abb = None

    # withdraw
    def withdraw(self, amount, current_balance):
        self.amount_withdraw = amount
        self.final_balance = current_balance - self.amount_withdraw

        if self.final_balance < 0:
            label_text = Scenario.withdraw_current_balance_pt + ": " + str(current_balance) + " €\n" + Scenario.withdraw_amount_pt + ": " + str(
                amount) + " €\n" + Scenario.withdraw_insufficient_balance_pt
        else:
            label_text = Scenario.withdraw_current_balance_pt + ": " + str(current_balance) + " €\n" + Scenario.withdraw_amount_pt + ": " + str(
                amount) + " €\n" + Scenario.withdraw_final_balance_pt + ": " + str(self.final_balance) + " €"

        self.withdraw_label = tk.Label(self.canvas, font=(
            "default", 18), text=label_text, justify=tk.LEFT, bg=BACKGROUND_CLR)
        self.withdraw_label.place(x=270, y=200)

    def destroy_withdraw(self):
        self.final_balance = None
        self.withdraw_label.destroy()

    # withdraw custom amount
    def withdraw_custom(self):
        self.custom_withdraw_text = tk.StringVar()

        self.custom_withdraw_field = tk.Entry(
            self.canvas, textvariable=self.custom_withdraw_text, font=("default", 21))

        self.custom_withdraw_field.place(
            x=(WIDTH/2)-100, y=(HEIGHT/2)-20-200, width=200, height=40)

        self.custom_withdraw_field.config(fg="grey")

        self.custom_withdraw_field.insert(
            0, Scenario.withdraw_other_default_text_pt)

        self.custom_withdraw_field.bind(
            "<FocusIn>", self.focusin_withdraw_custom)

    def focusin_withdraw_custom(self, pos):
        if self.custom_withdraw_field.cget("fg") == "grey":
            self.custom_withdraw_field.config(fg="black")
            self.custom_withdraw_field.delete(0, tk.END)

        self.focusedin = True

    def withdraw_custom_destroy(self):
        self.custom_withdraw_text.set("")
        self.custom_withdraw_field.destroy()

    # balance
    def balance(self, current_balance):
        label_text = Scenario.withdraw_current_balance_pt + \
            ": " + str(current_balance) + " €"

        self.balance_label = tk.Label(self.canvas, font=(
            "default", 18), text=label_text, justify=tk.LEFT, bg=BACKGROUND_CLR)
        self.balance_label.place(x=270, y=200)

    def destroy_balance(self):
        self.current_balance = None
        self.balance_label.destroy()

    # mbway
    def mbway(self):
        label_text = Scenario.mbway_error_pt

        self.mbway_label = tk.Label(self.canvas, font=(
            "default", 18), text=label_text, justify=tk.LEFT, bg=BACKGROUND_CLR)
        self.mbway_label.place(x=285, y=200)

    def destroy_mbway(self):
        self.mbway_label.destroy()

    # vouchers
    def vouchers(self, amount, final_balance):
        self.voucher_type_text = self.event_handler.voucher
        self.voucher_amount = amount

        self.voucher_type_label = tk.Label(self.canvas, font=(
            "default", 18), text=self.voucher_type_text, justify=tk.CENTER, bg=BACKGROUND_CLR)
        self.voucher_type_label.place(x=285, y=150)

        label_text = Scenario.voucher_checkout_pt + ": " + str(amount) + " €"

        self.vouchers_label = tk.Label(self.canvas, font=(
            "default", 18), text=label_text, justify=tk.CENTER, bg=BACKGROUND_CLR)
        self.vouchers_label.place(x=285, y=200)

        self.voucher_code = None

        if final_balance >= 0:
            self.voucher_code = str(random.randint(0, 9999999999))

            label_text2 = Scenario.voucher_code_pt + ": " + self.voucher_code

            self.vouchers_code_label = tk.Label(self.canvas, font=(
                "default", 18), text=label_text2, justify=tk.CENTER, bg=BACKGROUND_CLR)
            self.vouchers_code_label.place(x=285, y=250)

            label_text3 = Scenario.voucher_warning_pt

            self.vouchers_warning_label = tk.Label(self.canvas, font=(
                "default", 18), text=label_text3, justify=tk.CENTER, bg=BACKGROUND_CLR, fg="red")
            self.vouchers_warning_label.place(x=120, y=300)
        else:
            label_text3 = Scenario.withdraw_insufficient_balance_pt

            self.vouchers_warning_label = tk.Label(self.canvas, font=(
                "default", 18), text=label_text3, justify=tk.CENTER, bg=BACKGROUND_CLR, fg="red")
            self.vouchers_warning_label.place(x=250, y=300)

    def destroy_vouchers(self):
        try:
            self.voucher_type_label.destroy()
            self.vouchers_label.destroy()
            self.vouchers_warning_label.destroy()
            self.vouchers_code_label.destroy()
        except:
            pass

    # transfers
    def transfers(self):
        label_text = Scenario.tranfers_iban_pt
        label2_text = Scenario.transfers_amount_pt

        self.tranfers_label = tk.Label(self.canvas, font=(
            "default", 18), text=label_text, justify=tk.LEFT, bg=BACKGROUND_CLR)
        self.tranfers_label.place(x=220, y=100)

        self.tranfers2_label = tk.Label(self.canvas, font=(
            "default", 18), text=label2_text, justify=tk.LEFT, bg=BACKGROUND_CLR)
        self.tranfers2_label.place(x=190, y=200)

        self.iban_text = tk.StringVar()

        self.iban_field = tk.Entry(
            self.canvas, textvariable=self.iban_text, font=("default", 21))

        self.iban_field.place(
            x=(WIDTH/2)-100, y=(HEIGHT)-600, width=200, height=40)

        self.iban_field.config(fg="grey")

        self.iban_field.insert(
            0, Scenario.iban_default_text_pt)

        self.iban_field.bind("<FocusIn>", self.focusin_iban)

        self.amount_text = tk.StringVar()

        self.amount_field = tk.Entry(
            self.canvas, textvariable=self.amount_text, font=("default", 21))

        self.amount_field.place(
            x=(WIDTH/2)-100, y=(HEIGHT)-500, width=200, height=40)

        self.amount_field.config(fg="grey")

        self.amount_field.insert(
            0, Scenario.amount_default_text_pt)

        self.amount_field.bind("<FocusIn>", self.focusin_amount)

        self.transfers_warning_field = tk.Label(
            self.canvas, font=("default", 18), justify=tk.LEFT, bg=BACKGROUND_CLR, fg="red")

        self.transfers_warning_field.place(x=450, y=475)

    def focusin_iban(self, pos):
        if self.iban_field.cget("fg") == "grey":
            self.iban_field.config(fg="black")
            self.iban_field.delete(0, tk.END)

        self.focusedin = True

    def focusin_amount(self, pos):
        if self.amount_field.cget("fg") == "grey":
            self.amount_field.config(fg="black")
            self.amount_field.delete(0, tk.END)

        self.focusedin = True

    def transfers_warning(self):
        self.transfers_warning_field.config(
            text=Scenario.tranfers_warning_message_pt)

    def transfers_destroy(self):
        self.iban_text.set("")
        self.amount_text.set("")
        self.iban_field.destroy()
        self.amount_field.destroy()
        self.tranfers_label.destroy()
        self.tranfers2_label.destroy()
        self.transfers_warning_field.destroy()

    # payments
    def payments(self):
        label_text = Scenario.payments_entity_pt
        label2_text = Scenario.payments_reference_pt
        label3_text = Scenario.payments_amount_pt

        self.payments_label = tk.Label(self.canvas, font=(
            "default", 18), text=label_text, justify=tk.LEFT, bg=BACKGROUND_CLR)
        self.payments_label.place(x=150, y=150)

        self.payments2_label = tk.Label(self.canvas, font=(
            "default", 18), text=label2_text, justify=tk.LEFT, bg=BACKGROUND_CLR)
        self.payments2_label.place(x=150, y=200)

        self.payments3_label = tk.Label(self.canvas, font=(
            "default", 18), text=label3_text, justify=tk.LEFT, bg=BACKGROUND_CLR)
        self.payments3_label.place(x=150, y=250)

        self.entity_text = tk.StringVar()

        self.entity_field = tk.Entry(
            self.canvas, textvariable=self.entity_text, font=("default", 21))

        self.entity_field.place(
            x=300, y=150, width=200, height=40)

        self.entity_field.bind("<FocusIn>", self.focusin_entity)

        self.reference_text = tk.StringVar()

        self.reference_field = tk.Entry(
            self.canvas, textvariable=self.reference_text, font=("default", 21))

        self.reference_field.place(
            x=300, y=200, width=200, height=40)

        self.reference_field.bind("<FocusIn>", self.focusin_reference)

        self.payments_amount_text = tk.StringVar()

        self.payments_amount_field = tk.Entry(
            self.canvas, textvariable=self.payments_amount_text, font=("default", 21))

        self.payments_amount_field.place(
            x=300, y=250, width=200, height=40)

        self.payments_amount_field.bind(
            "<FocusIn>", self.focusin_payments_amount)

        self.payments_warning_field = tk.Label(
            self.canvas, font=("default", 18), justify=tk.LEFT, bg=BACKGROUND_CLR, fg="red")

        self.payments_warning_field.place(x=450, y=475)

    def payments_warning(self):
        self.payments_warning_field.config(
            text=Scenario.payments_warning_message_pt)

    def focusin_entity(self, pos):
        self.focusedin = True

    def focusin_reference(self, pos):
        self.focusedin = True

    def focusin_payments_amount(self, pos):
        self.focusedin = True

    def payments_destroy(self):
        self.entity_text.set("")
        self.payments_amount_text.set("")
        self.reference_text.set("")
        self.entity_field.destroy()
        self.payments_amount_field.destroy()
        self.reference_field.destroy()
        self.payments_label.destroy()
        self.payments2_label.destroy()
        self.payments3_label.destroy()
        self.payments_warning_field.destroy()
