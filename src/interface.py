import tkinter as tk
import i_event_handler
from scenarios import *

# window dimensions
WIDTH = 750
HEIGHT = 750


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

        import image_loader
        self.window.iconphoto(False, image_loader.icon)

    # create canvas function
    def create_canvas(self):
        self.canvas = tk.Canvas(self.window, width=WIDTH,
                                height=HEIGHT, bg="#32a84e", highlightthickness=0)
        self.canvas.pack()

    # update onscreen scenario
    def update_scenario(self):
        self.scenario(Scenario.get_scenario_active(
            self.current_scenario), Scenario.get_scenario_text(self.current_scenario))

        if self.current_scenario == Scenario.LOGIN:
            self.login()

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
        self.login_username_text = None
        self.login_password_text = None

        # create entry objects
        self.username_field = tk.Entry(
            self.canvas, textvariable=self.login_username_text, font=("default", 23))
        self.password_field = tk.Entry(
            self.canvas, textvariable=self.login_password_text, show='*', font=("default", 23))

        # place entry objects
        self.username_field.place(
            x=(WIDTH/2)-100, y=(HEIGHT/2)-20-42-20, width=200, height=40)
        self.password_field.place(
            x=(WIDTH/2)-100, y=(HEIGHT/2)-20-20, width=200, height=40)

        # greyed out default text
        self.username_field.config(fg="grey")
        self.password_field.config(fg="grey")
        self.password_field.config(show="")

        self.username_field.insert(0, Scenario.login_username_pt)
        self.password_field.insert(0, Scenario.login_pin_pt)

        self.username_field.bind("<FocusIn>", self.focusin_username_login)
        self.password_field.bind("<FocusIn>", self.focusin_password_login)

    def focusin_username_login(self, pos):
        if self.username_field.cget("fg") == "grey":
            self.username_field.config(fg="black")
            self.username_field.delete(0, tk.END)

    def focusin_password_login(self, pos):
        if self.password_field.cget("fg") == "grey":
            self.password_field.config(fg="black", show="*")
            self.password_field.delete(0, tk.END)

    def destroy_login(self):
        self.username_field.destroy()
        self.password_field.destroy()
        self.login_username_text = None
        self.login_password_text = None
