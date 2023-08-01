from tkinter import *


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.color1 = "black"
        self.color2 = "white"
        self.brush_size = 20
        self.setUI()

    def draw(self, event):
        self.canv.create_oval(event.x - 20, event.y - 20, event.x + 20,
                              event.y + 20,
                              fill=self.color1, outline=self.color1)
        self.canv.create_oval(event.x - 1, event.y - 1, event.x + 1,
                              event.y + 1,
                              fill=self.color2, outline=self.color2)

    def setUI(self):
        self.pack(fill=BOTH, expand=1)
        self.canv = Canvas(self, bg="white")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.canv.grid(padx=5, pady=5, sticky=E + W + S + N)
        self.canv.bind("<B1-Motion>", self.draw)


root = Tk()
root.geometry("850x500+300+300")
app = Paint(root)
root.mainloop()