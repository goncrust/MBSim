import tkinter as tk
import i_event_handler
from scenarios import *
from tkcalendar import Calendar, DateEntry
import time

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

        # set first scenario and run it
        self.current_scenario = Scenario.LOGIN
        self.update_scenario()

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

    # create canvas function
    def create_canvas(self):
        self.canvas = tk.Canvas(self.window, width=WIDTH,
                                height=HEIGHT, bg=BACKGROUND_CLR, highlightthickness=0)
        self.canvas.pack()

    # update onscreen scenario
    def update_scenario(self):
        self.scenario(Scenario.get_scenario_active(
            self.current_scenario), Scenario.get_scenario_text(self.current_scenario))

        if self.current_scenario == Scenario.LOGIN:
            self.login()
        elif self.current_scenario == Scenario.REGISTER:
            self.register()

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
            if i < 4:
                image_loader.place_text(self, image_loader.B_LEFT, label[i])
            else:
                image_loader.place_text(self, image_loader.B_RIGHT, label[i])

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

        # place entry objects
        self.username_field.place(
            x=(WIDTH/2)-100, y=(HEIGHT/2)-20-42-20, width=200, height=40)
        self.pin_field.place(
            x=(WIDTH/2)-100, y=(HEIGHT/2)-20-20, width=200, height=40)

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

    def focusin_pin_login(self, pos):
        if self.pin_field.cget("fg") == "grey":
            self.pin_field.config(fg="black", show="*")
            self.pin_field.delete(0, tk.END)

    def destroy_login(self):
        # destroy fields
        self.username_field.destroy()
        self.pin_field.destroy()

        # reset variables
        self.login_username_text.set("")
        self.login_pin_text.set("")

    # for register scenario
    def register(self):
        # variables to store fields data
        self.register_username_text = tk.StringVar()
        self.register_pin_text = tk.StringVar()
        self.register_bank_text = tk.StringVar(self.canvas)
        self.register_bank_text.set("Caixa Geral de Depóstios")

        # create entry objects
        self.register_username_field = tk.Entry(
            self.canvas, textvariable=self.register_username_text, font=("default", 23))
        self.register_pin_field = tk.Entry(
            self.canvas, textvariable=self.register_pin_text, show='*', font=("default", 23))
        self.register_calendar_field = Calendar(
            self.canvas, font=("default", 9), selectmode='day')
        self.register_bank_field = tk.OptionMenu(
            self.canvas, self.register_bank_text, "Caixa Geral de Depóstios", "Santander Totta", "Millennium BCP",
            "BPI", "Novo Banco", "Bankinter", "EuroBIC", "Popular", "Montepio", "Banco CTT", "BBVA")
        self.register_info_field = tk.Label(
            self.canvas, text=Scenario.register_info_pt, font=("default", 18), justify=tk.LEFT, bg=BACKGROUND_CLR)
        self.register_warning_field = tk.Label(
            self.canvas, font=("default", 18), justify=tk.LEFT, bg=BACKGROUND_CLR, fg="red")
        self.register_calendar_label = tk.Label(self.canvas, font=(
            "default", 16), justify=tk.LEFT, bg=BACKGROUND_CLR, text=Scenario.register_calendar_field_pt)

        # place entry objects
        self.register_username_field.place(x=10, y=10, width=200, height=40)
        self.register_pin_field.place(x=10, y=52, width=200, height=40)
        self.register_calendar_field.place(x=10, y=208, height=150, width=200)
        self.register_bank_field.place(x=10, y=115, height=50, width=200)
        self.register_info_field.place(x=280, y=10)
        self.register_warning_field.place(x=450, y=475)
        self.register_calendar_label.place(x=10, y=178)

        # greyed out default text
        self.register_username_field.config(fg="grey")
        self.register_pin_field.config(fg="grey")
        self.register_pin_field.config(show="")

        self.register_username_field.insert(0, Scenario.register_username_pt)
        self.register_pin_field.insert(0, Scenario.register_pin_pt)

        self.register_username_field.bind(
            "<FocusIn>", self.focusin_username_register)
        self.register_pin_field.bind(
            "<FocusIn>", self.focusin_pin_register)

    def focusin_username_register(self, pos):
        if self.register_username_field.cget("fg") == "grey":
            self.register_username_field.config(fg="black")
            self.register_username_field.delete(0, tk.END)

    def focusin_pin_register(self, pos):
        if self.register_pin_field.cget("fg") == "grey":
            self.register_pin_field.config(fg="black")
            self.register_pin_field.delete(0, tk.END)

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

    def blink_info_register(self):
        self.register_info_field.config(fg="red")

    def destroy_register(self):
        # destroy fields
        self.register_username_field.destroy()
        self.register_pin_field.destroy()
        self.register_calendar_field.destroy()
        self.register_bank_field.destroy()
        self.register_info_field.destroy()
        self.register_warning_field.destroy()
        self.register_bank_field.destroy()

        # reset variables
        self.register_username_text.set("")
        self.register_pin_text.set("")
        self.register_bank_text.set("Caixa Geral de Depóstios")
