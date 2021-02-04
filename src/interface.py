import tkinter as tk
import i_event_handler
from scenarios import *
from tkcalendar import Calendar, DateEntry
import time
import random
import admin

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

        # admin
        self.admin = admin.Admin(self)

        # languages image
        self.pt_image = None
        self.en_image = None

        self.pt_button = None
        self.en_button = None

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

        self.focusedin = False

    # place buttons and assign events
    def scenario(self, active, label):

        import image_loader

        if self.current_scenario == Scenario.LOGIN:
            if self.pt_image == None:
                image_loader.get_language_button_images(self)
            self.login()
        elif self.current_scenario == Scenario.REGISTER:
            self.register()

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
        # language selection
        self.language_selection()

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

        self.username_field.insert(0, Scenario.get_label("login_username"))
        self.pin_field.insert(0, Scenario.get_label("login_pin"))

        self.username_field.bind("<FocusIn>", self.focusin_username_login)
        self.pin_field.bind("<FocusIn>", self.focusin_pin_login)

    # language selection
    def language_selection(self):

        if self.pt_button != None:
            self.pt_button.destroy()
        if self.en_button != None:
            self.en_button.destroy()

        if Scenario.get_current_language() == Scenario.PORTUGUESE:
            self.pt_button = tk.Button(
                self.canvas, image=self.pt_image[1], borderwidth=0, highlightthickness=0)
            self.en_button = tk.Button(
                self.canvas, image=self.en_image[0], borderwidth=0, highlightthickness=0)
        elif Scenario.get_current_language() == Scenario.ENGLISH:
            self.pt_button = tk.Button(
                self.canvas, image=self.pt_image[0], borderwidth=0, highlightthickness=0)
            self.en_button = tk.Button(
                self.canvas, image=self.en_image[1], borderwidth=0, highlightthickness=0)

        self.pt_button.place(x=20, y=20)
        self.en_button.place(x=140, y=20)

        self.pt_button.bind("<Button-1>", self.select_pt_button)
        self.en_button.bind("<Button-1>", self.select_en_button)

    def select_pt_button(self, pos):
        Scenario.set_current_language(Scenario.PORTUGUESE)
        # self.language_selection()
        self.destroy_login()
        self.update_scenario()

    def select_en_button(self, pos):
        Scenario.set_current_language(Scenario.ENGLISH)
        # self.language_selection()
        self.destroy_login()
        self.update_scenario()

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
        self.login_warning_label.config(
            text=Scenario.get_label("login_warning"))

    def destroy_login(self):
        # destroy fields
        self.username_field.destroy()
        self.pin_field.destroy()
        self.login_warning_label.destroy()
        self.pt_button.destroy()
        self.en_button.destroy()

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
            self.canvas, text=Scenario.get_label("register_info"), font=(
                "default", 18), justify=tk.LEFT, bg=BACKGROUND_CLR)
        self.register_warning_field = tk.Label(
            self.canvas, font=("default", 18), justify=tk.LEFT, bg=BACKGROUND_CLR, fg="red")
        self.register_calendar_label = tk.Label(self.canvas, font=(
            "default", 16), justify=tk.LEFT, bg=BACKGROUND_CLR, text=Scenario.get_label("register_calendar_field"))
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

        self.register_username_field.insert(
            0, Scenario.get_label("register_username"))
        self.register_pin_field.insert(0, Scenario.get_label("register_pin"))
        self.register_pin_confirm_field.insert(
            0, Scenario.get_label("register_pin_confirm"))

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
                text=Scenario.get_label("register_only_letters"))
        elif message == 1:
            self.register_warning_field.config(
                text=Scenario.get_label("register_short_username"))
        elif message == 2:
            self.register_warning_field.config(
                text=Scenario.get_label("register_only_numbers"))
        elif message == 3:
            self.register_warning_field.config(
                text=Scenario.get_label("register_pin_size"))
        elif message == 4:
            self.register_warning_field.config(
                text=Scenario.get_label("register_username_exists"))
        elif message == 5:
            self.register_warning_field.config(
                text=Scenario.get_label("register_pin_match"))
        elif message == 6:
            self.register_warning_field.config(
                text=Scenario.get_label("register_age"))

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
            label_text = Scenario.get_label("withdraw_current_balance") + ": " + str(current_balance) + " €\n" + Scenario.get_label("withdraw_amount") + ": " + str(
                amount) + " €\n" + Scenario.get_label("withdraw_insufficient_balance")
        else:
            label_text = Scenario.get_label("withdraw_current_balance") + ": " + str(current_balance) + " €\n" + Scenario.get_label("withdraw_amount") + ": " + str(
                amount) + " €\n" + Scenario.get_label("withdraw_final_balance") + ": " + str(self.final_balance) + " €"

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
            0, Scenario.get_label("withdraw_other_default_text"))

        self.custom_withdraw_field.bind(
            "<FocusIn>", self.focusin_withdraw_custom)

        self.withdraw_warning_field = tk.Label(
            self.canvas, font=("default", 18), justify=tk.LEFT, bg=BACKGROUND_CLR, fg="red")

        self.withdraw_warning_field.place(x=450, y=475)

    def withdraw_warning(self):
        self.withdraw_warning_field.config(
            text=Scenario.withdraw_error_pt)

    def focusin_withdraw_custom(self, pos):
        if self.custom_withdraw_field.cget("fg") == "grey":
            self.custom_withdraw_field.config(fg="black")
            self.custom_withdraw_field.delete(0, tk.END)

        self.focusedin = True

    def withdraw_custom_destroy(self):
        self.custom_withdraw_text.set("")
        self.withdraw_warning_field.destroy()
        self.custom_withdraw_field.destroy()

    # balance
    def balance(self, current_balance):
        label_text = Scenario.get_label("withdraw_current_balance") + \
            ": " + str(current_balance) + " €"

        self.balance_label = tk.Label(self.canvas, font=(
            "default", 18), text=label_text, justify=tk.LEFT, bg=BACKGROUND_CLR)
        self.balance_label.place(x=270, y=200)

    def destroy_balance(self):
        self.current_balance = None
        self.balance_label.destroy()

    # mbway
    def mbway(self):
        label_text = Scenario.get_label("mbway_error")

        self.mbway_label = tk.Label(self.canvas, font=(
            "default", 18), text=label_text, justify=tk.LEFT, bg=BACKGROUND_CLR)
        self.mbway_label.place(x=285, y=200)

    def destroy_mbway(self):
        self.mbway_label.destroy()

    # vouchers
    def vouchers(self, amount, final_balance):
        self.voucher_type = self.event_handler.voucher

        self.voucher_type_text = None
        if self.event_handler.voucher == "Music":
            self.voucher_type_text = Scenario.get_label("voucher_music")
        elif self.event_handler.voucher == "Movies":
            self.voucher_type_text = Scenario.get_label("voucher_movies")
        elif self.event_handler.voucher == "Games":
            self.voucher_type_text = Scenario.get_label("voucher_games")

        self.voucher_amount = amount

        self.voucher_type_label = tk.Label(self.canvas, font=(
            "default", 18), text=self.voucher_type_text, justify=tk.CENTER, bg=BACKGROUND_CLR)
        self.voucher_type_label.place(x=285, y=150)

        label_text = Scenario.get_label(
            "voucher_checkout") + ": " + str(amount) + " €"

        self.vouchers_label = tk.Label(self.canvas, font=(
            "default", 18), text=label_text, justify=tk.CENTER, bg=BACKGROUND_CLR)
        self.vouchers_label.place(x=285, y=200)

        self.voucher_code = ""
        self.voucher_digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

        if final_balance >= 0:
            for i in range(0, 3):
                for i in range(0, 4):
                    self.voucher_code = self.voucher_code + \
                        str(random.choice(self.voucher_digits))
                self.voucher_code = self.voucher_code + "-"
            for i in range(0, 4):
                self.voucher_code = self.voucher_code + \
                    str(random.choice(self.voucher_digits))

            label_text2 = Scenario.get_label(
                "voucher_code") + ": " + self.voucher_code

            self.vouchers_code_label = tk.Label(self.canvas, font=(
                "default", 18), text=label_text2, justify=tk.CENTER, bg=BACKGROUND_CLR)
            self.vouchers_code_label.place(x=285, y=250)

            label_text3 = Scenario.get_label("voucher_warning")
            
            self.vouchers_warning_label = tk.Label(self.canvas, font=(
                "default", 18), text=label_text3, justify=tk.CENTER, bg=BACKGROUND_CLR, fg="red")

            if Scenario.get_current_language() == Scenario.PORTUGUESE:
                self.vouchers_warning_label.place(x=120, y=300)
            elif Scenario.get_current_language() == Scenario.ENGLISH:
                 self.vouchers_warning_label.place(x=180, y=300)
           
        else:
            label_text3 = Scenario.get_label("withdraw_insufficient_balance")

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
        label_text = Scenario.get_label("transfers_iban")
        label2_text = Scenario.get_label("transfers_amount")

        self.tranfers_label = tk.Label(self.canvas, font=(
            "default", 18), text=label_text, justify=tk.LEFT, bg=BACKGROUND_CLR)
        self.tranfers_label.place(x=220, y=100)

        self.tranfers2_label = tk.Label(self.canvas, font=(
            "default", 18), text=label2_text, justify=tk.LEFT, bg=BACKGROUND_CLR)
        
        if Scenario.get_current_language() == Scenario.PORTUGUESE:
            self.tranfers2_label.place(x=190, y=200)
        elif Scenario.get_current_language() == Scenario.ENGLISH:
            self.tranfers2_label.place(x=235, y=200)
        
        self.iban_text = tk.StringVar()

        self.iban_field = tk.Entry(
            self.canvas, textvariable=self.iban_text, font=("default", 21))

        if Scenario.get_current_language() == Scenario.PORTUGUESE:
            self.iban_field.place(x=(WIDTH/2)-100, y=(HEIGHT)-600, width=200, height=40)
        elif Scenario.get_current_language() == Scenario.ENGLISH:
            self.iban_field.place(x=(WIDTH/2)-100, y=(HEIGHT)-600, width=200, height=40)

    
        self.iban_field.config(fg="grey")

        self.iban_field.insert(
            0, Scenario.get_label("iban_default_text"))

        self.iban_field.bind("<FocusIn>", self.focusin_iban)

        self.amount_text = tk.StringVar()

        self.amount_field = tk.Entry(
            self.canvas, textvariable=self.amount_text, font=("default", 21))

        if Scenario.get_current_language() == Scenario.PORTUGUESE:
            self.amount_field.place(x=(WIDTH/2)-100, y=(HEIGHT)-500, width=200, height=40)
        elif Scenario.get_current_language() == Scenario.ENGLISH:
            self.amount_field.place(x=(WIDTH/2)-100, y=(HEIGHT)-500, width=200, height=40)
        

        self.amount_field.config(fg="grey")

        self.amount_field.insert(
            0, Scenario.get_label("amount_default_text"))

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
            text=Scenario.get_label("tranfers_warning_message"))

    def transfers_zero_warning(self):
        self.transfers_warning_field.config(
            text=Scenario.transfers_zero_warning_pt)

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
        label_text = Scenario.get_label("payments_entity")
        label2_text = Scenario.get_label("payments_reference")
        label3_text = Scenario.get_label("payments_amount")

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

    def payments_warning(self, error_code):
        if error_code == 0:
            # only numbers
            self.payments_warning_field.config(
                text=Scenario.get_label("payments_warning_message"))
        elif error_code == 1:
            # entity size
            self.payments_warning_field.config(
                text=Scenario.get_label("payments_entity_size"))
        elif error_code == 2:
            # reference size
            self.payments_warning_field.config(
                text=Scenario.get_label("payments_reference_size"))
        elif error_code == 3:
            # not enough money
            self.payments_warning_field.config(
                text=Scenario.get_label("withdraw_insufficient_balance"))
        elif error_code == 4:
            # paying zero
            self.payments_warning_field.config(
                text=Scenario.payments_zero_warning_pt)

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

    # movements
    def movements_menu(self, data, current_user_account_number):

        self.widthdraw_data, self.transfers_data, self.payments_data, self.vouchers_data = data

        self.widthdraw_text = ""
        for w in self.widthdraw_data:
            if w[1] < 9999:
                self.widthdraw_text = self.widthdraw_text + \
                    str(w[1]) + " €\t\t\t\t\t" + w[2] + "\n"
            else:
                self.widthdraw_text = self.widthdraw_text + \
                    str(w[1]) + " €\t\t\t\t" + w[2] + "\n"

        self.first_frame = tk.Frame(self.canvas)
        self.first_frame.place(x=20, y=20)
        self.ff_label = tk.Label(
            self.first_frame, text=Scenario.get_label("movements_withdraws")).pack()
        self.f_scrollable = Scrollable(self.first_frame)
        self.ff_label = tk.Label(
            self.f_scrollable, text=self.widthdraw_text).grid()
        self.f_scrollable.update()

        self.transfers_text = ""
        for t in self.transfers_data:
            if t[0] == current_user_account_number:
                if t[2] < 9999:
                    self.transfers_text = self.transfers_text + \
                        t[1] + "\t-" + str(t[2]) + " €\t" + t[3] + "\n"
                else:
                    self.transfers_text = self.transfers_text + \
                        t[1] + "  -" + str(t[2]) + " €\t" + t[3] + "\n"
            elif t[1] == current_user_account_number:
                if t[2] < 9999:
                    self.transfers_text = self.transfers_text + \
                        t[0] + "\t+" + str(t[2]) + " €\t" + t[3] + "\n"
                else:
                    self.transfers_text = self.transfers_text + \
                        t[0] + "  +" + str(t[2]) + " €\t" + t[3] + "\n"

        self.second_frame = tk.Frame(self.canvas)
        self.second_frame.place(x=(WIDTH/2) + 10, y=20)
        self.sf_label = tk.Label(
            self.second_frame, text=Scenario.get_label("movements_transfers")).pack()
        self.s_scrollable = Scrollable(self.second_frame)
        self.sf_label = tk.Label(
            self.s_scrollable, text=self.transfers_text).grid()
        self.s_scrollable.update()

        self.payments_text = ""
        for p in self.payments_data:
            if p[3] < 9999:
                self.payments_text = self.payments_text + \
                    p[1] + "\t" + p[2] + "\t" + \
                    str(p[3]) + " €\t\t" + p[4] + "\n"
            else:
                self.payments_text = self.payments_text + \
                    p[1] + "\t" + p[2] + "\t" + \
                    str(p[3]) + " €\t" + p[4] + "\n"

        self.third_frame = tk.Frame(self.canvas)
        self.third_frame.place(x=20, y=(HEIGHT/2) + 10 - 100)
        self.tf_label = tk.Label(
            self.third_frame, text=Scenario.get_label("movements_payments")).pack()
        self.t_scrollable = Scrollable(self.third_frame)
        self.tf_label = tk.Label(
            self.t_scrollable, text=self.payments_text).grid()
        self.t_scrollable.update()

        self.vouchers_text = ""
        for v in self.vouchers_data:

            # voucher type translation
            type_v = ""
            if v[1] == "Games":
                type_v = Scenario.get_label("voucher_games")
            elif v[1] == "Movies":
                type_v = Scenario.get_label("voucher_movies")
            elif v[1] == "Music":
                type_v = Scenario.get_label("voucher_music")

            self.vouchers_text = self.vouchers_text + \
                type_v + "\t" + v[2] + "\t" + \
                str(v[3]) + " €\t" + v[4] + "\n"

        self.fourth_frame = tk.Frame(self.canvas)
        self.fourth_frame.place(x=(WIDTH/2) + 10, y=(HEIGHT/2) + 10 - 100)
        self.fof_label = tk.Label(
            self.fourth_frame, text=Scenario.get_label("movements_vouchers")).pack()
        self.fo_scrollable = Scrollable(self.fourth_frame)
        self.fof_label = tk.Label(
            self.fo_scrollable, text=self.vouchers_text).grid()
        self.fo_scrollable.update()

    def movements_menu_destroy(self):
        self.widthdraw_data, self.transfers_data, self.transfers_data, self.vouchers_data = None, None, None, None
        self.widthdraw_text, self.transfers_text, self.payments_text, self.vouchers_text = "", "", "", ""

        self.first_frame.destroy()
        # self.ff_label.destroy()
        self.f_scrollable.destroy()

        self.second_frame.destroy()
        # self.sf_label.destroy()
        self.s_scrollable.destroy()

        self.third_frame.destroy()
        # self.tf_label.destroy()
        self.t_scrollable.destroy()

        self.fourth_frame.destroy()
        # self.fof_label.destroy()
        self.fo_scrollable.destroy()

    # IBAN
    def iban(self, user_iban):
        label_text = Scenario.get_label("iban") + \
            ": " + str(user_iban)

        self.iban_label = tk.Label(self.canvas, font=(
            "default", 18), text=label_text, justify=tk.LEFT, bg=BACKGROUND_CLR)
        self.iban_label.place(x=200, y=200)

    def destroy_iban(self):
        self.iban_label.destroy()

    # admin
    def admin_menu(self, code):
        if code == 0:
            self.admin.generate_menu_search(
                Scenario.get_label("login_username"))
        elif code == 1:
            return self.admin.generate_menu_user(Scenario.get_label("admin_new_pin"))
        elif code == 2:
            return self.admin.return_user_modification()
        elif code == 3:
            return self.admin.return_user_to_delete()

    def username_exists(self, username):
        return self.event_handler.username_exists(username)

    def get_account_number_from_username(self, username):
        return self.event_handler.get_account_number_from_name(username)

    def get_bank_from_username(self, username):
        return self.event_handler.get_bank_from_user(username)

    def get_birthday_from_username(self, username):
        return self.event_handler.get_birthday_from_user(username)

    def get_balance_from_username(self, username):
        return self.event_handler.get_balance_from_user(username)


# movements scrolling sections
# credits: https://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter
class Scrollable(tk.Frame):
    """
       Make a frame scrollable with scrollbar on the right.
       After adding or removing widgets to the scrollable frame,
       call the update() method to refresh the scrollable area.
    """

    def __init__(self, frame, width=16, canvas_width=(WIDTH/2)-16-10-20, canvas_height=(HEIGHT/2)-140-10):

        scrollbar = tk.Scrollbar(frame, width=width)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)

        self.canvas = tk.Canvas(
            frame, yscrollcommand=scrollbar.set, width=canvas_width, height=canvas_height)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.canvas.yview)

        self.canvas.bind('<Configure>', self.__fill_canvas)

        # base class initialization
        tk.Frame.__init__(self, frame)

        # assign this obj (the inner frame) to the windows item of the canvas
        self.windows_item = self.canvas.create_window(
            0, 0, window=self, anchor=tk.NW)

    def __fill_canvas(self, event):
        # Enlarge the windows item to the canvas width

        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width=canvas_width)

    def update(self):
        # Update the canvas and the scrollregion

        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))
