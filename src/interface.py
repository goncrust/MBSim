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

    # create canvas function
    def create_canvas(self):
        self.canvas = tk.Canvas(self.window, width=WIDTH,
                                height=HEIGHT, bg="#32a84e", highlightthickness=0)
        self.canvas.pack()

    # update onscreen scenario
    def update_scenario(self):
        self.scenario(Scenario.get_scenario_active(
            self.current_scenario), Scenario.get_scenario_text(self.current_scenario))

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
                    self.buttons[z].place(x=-1, y=50)
                elif z == 1:
                    self.buttons[z].place(x=-1, y=200)
                elif z == 2:
                    self.buttons[z].place(x=-1, y=350)
                elif z == 3:
                    self.buttons[z].place(x=-1, y=500)
                elif z == 4:
                    self.buttons[z].place(x=WIDTH-320, y=50)
                elif z == 5:
                    self.buttons[z].place(x=WIDTH-320, y=200)
                elif z == 6:
                    self.buttons[z].place(x=WIDTH-320, y=350)
                elif z == 7:
                    self.buttons[z].place(x=WIDTH-320, y=500)

                # assign events to button
                self.buttons[z].bind(
                    '<Button-1>', eval("self.event_handler.click_" + str(z)))
