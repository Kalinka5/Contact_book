from tkinter import ttk
import tkinter as tk


class ImageFrame(ttk.Frame):
    def __init__(self, container, tab_control):
        super().__init__(container)
        self.tab_control = tab_control
        self.__create_widgets()

    def __create_widgets(self):
        self.tab_control.add(self, text='Contact Book')

        lbl1 = ttk.Label(master=self, text="Your Contact book", foreground='red', font=("Helvetica", 16))
        lbl1.pack()

        test = tk.PhotoImage(name='telephone', file="images/telephone2.png")
        label1 = ttk.Label(master=self, image=test)
        label1.image = test
        label1.pack()
