from tkinter import ttk
import tkinter as tk


class ImageFrame(ttk.Frame):
    def __init__(self, container: tk.Tk, tab_control: ttk.Notebook):
        super().__init__(container)
        self.tab_control = tab_control
        self.__create_widgets()

    def __create_widgets(self):
        self.tab_control.add(self, text='Contact Book')

        test = tk.PhotoImage(name='telephone', file="Images/telephone2.png")
        label1 = ttk.Label(master=self, image=test)
        label1.image = test
        label1.place(x=60, y=40)

        lbl1 = ttk.Label(master=self, text="Your Contact book", foreground='red', font=("Helvetica", 20))
        lbl1.place(x=110, y=230)
