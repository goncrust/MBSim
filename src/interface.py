import tkinter as tk
import i_event_handler

WIDTH = 750
HEIGHT = 750


class Interface:

    def __init__(self, title):
        self.title = title

        self.buttons = [None, None, None, None, None, None, None, None]

        self.event_handler = i_event_handler.IEventHandler(self)

        self.create_window(WIDTH, HEIGHT)
        self.create_canvas()

        self.cenario([True, True, True, True, True, True, True, True], "")

        self.window.mainloop()

    def create_window(self, width, height):
        self.window = tk.Tk()
        self.window.title(self.title)
        self.window.geometry(str(width) + "x" + str(height) + "+500+100")

    def create_canvas(self):
        self.canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

    def cenario(self, active, label):

        import image_loader

        for x in range(len(self.buttons)):
            if self.buttons[x] != None:
                self.buttons[x].destroy()
                self.buttons[x] = None

        for z in range(len(active)):
            if active[z]:
                if z < 4:
                    self.buttons[z] = tk.Button(
                        self.canvas, image=image_loader.button_left, borderwidth=0)
                else:
                    self.buttons[z] = tk.Button(
                        self.canvas, image=image_loader.button_right, borderwidth=0)

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



                self.buttons[z].bind('<Button-1>', self.event_handler.click)
