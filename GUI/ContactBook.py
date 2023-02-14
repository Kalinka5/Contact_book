from tkinter import *
from PIL import Image, ImageTk


class MyWindow:
    def __init__(self, win):
        self.frame_1 = Frame(master=window, relief=RIDGE, borderwidth=5, width=150, height=150)
        self.frame_1.grid(row=0, column=1, sticky="n")

        self.lbl1 = Label(master=self.frame_1, text="Your Contact book", fg='red', font=("Helvetica", 16))
        self.lbl1.pack()

        self.frame_2 = Frame(master=window, relief=FLAT, borderwidth=5, width=150, height=150)
        self.frame_2.grid(row=1, column=1, sticky="n")

        image1 = Image.open("telephone2.png")
        test = ImageTk.PhotoImage(image1)
        label1 = Label(master=self.frame_2, image=test)
        label1.image = test
        label1.pack()

        self.frame_3 = Frame(master=window, relief=SUNKEN, borderwidth=5, width=150, height=150)
        self.frame_3.grid(row=3, column=2, sticky="nsew")

        self.lbl2 = Label(master=self.frame_3, text='All contacts', fg='purple', font="BOLD")
        self.lbl2.pack()

        self.data = ["Eldar (099)-346-7773", "Katya (066)-234-5866", "Elena (056)-445-9878", "Roma (050)-234-1854",
                     "Dania (093)-884-6390", "Gleb (095)-006-3828", "Anya (099)-775-9887"]
        self.lb = Listbox(master=self.frame_3, width=30, height=6, selectmode='multiple')
        for num in self.data:
            self.lb.insert(END, num)
        self.lb.pack()
        self.lb.bind('<Double-Button-1>', self.open_menu)
        self.lb.bind('<Button-2>', self.close_menu)

        self.frame_4 = Frame(master=window, relief=SUNKEN, borderwidth=5)
        self.frame_4.grid(row=3, column=1)

        self.lbl3 = Label(master=self.frame_4, text='Name', font='BOLD')
        self.lbl3.pack()

        self.t1 = Entry(master=self.frame_4, bd=3)
        self.t1.pack()

        self.lbl4 = Label(master=self.frame_4, text='Number', font='BOLD')
        self.lbl4.pack()

        self.t2 = Entry(master=self.frame_4, bd=3)
        self.t2.pack()

        self.b1 = Button(master=self.frame_4, text='Add contact', command=self.add_contact)
        self.b1.pack()

        self.data = ["Delete contact", "Add contact", "Rename contact"]
        self.lb2 = Listbox(window, height=3)
        for num in self.data:
            self.lb2.insert(END, num)

    def add_contact(self):
        name = str(self.t1.get())
        number = str(self.t2.get())
        result = f"{name} {number}"
        if result != " ":
            self.lb.insert(END, str(result))
            self.t1.delete(0, 'end')
            self.t2.delete(0, 'end')

    def open_menu(self, name):
        pass
        # self.lb2.pack()
        # self.data = ["Delete contact", "Add contact", "Rename contact"]
        # self.lb2 = Listbox(window, height=3)
        # for num in self.data:
        #     self.lb2.insert(END, num)
        # self.lb2.place(x=450, y=260)

    def close_menu(self, name):
        pass
        # self.lb2.pack_forget()
        # self.lb2.destroy()


window = Tk()
mywin = MyWindow(window)
window.title('Contact book')
window.columnconfigure([0, 1, 2], minsize=250)
window.rowconfigure([0, 1, 2, 3, 4], minsize=100)
window.mainloop()
