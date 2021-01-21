import tkinter as tk
import i_event_handler

WIDTH = 750
HEIGHT = 750


class Interface:

    def __init__(self, title):
        self.title = title

        self.event_handler = i_event_handler.IEventHandler()

        self.create_window(WIDTH, HEIGHT)
        self.create_canvas()
        import image_loader

        # test buttons
        b1 = tk.Button(self.canvas, image=image_loader.botao)
        b1.pack()
        b1.bind('<Button-1>', self.event_handler.click)

        self.window.mainloop()

    def create_window(self, width, height):
        self.window = tk.Tk()
        self.window.title(self.title)
        self.window.geometry(str(width) + "x" + str(height) + "+500+100")

    def create_canvas(self):
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack()

    def test(self, event):
        print("test1")
