import tkinter as tk


class Interface:

    def __init__(self, title):
        self.title = title
        self.create(700, 450)

        self.window.mainloop()

    def create(self, width, height):
        self.window = tk.Tk()
        self.window.title(self.title)
        self.window.geometry(str(width) + "x" + str(height) + "+400+200")
