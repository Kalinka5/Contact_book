from tkinter import *
from PIL import Image, ImageTk


class MyWindow:
    def __init__(self, win):
        self.frame_1 = Frame(master=window, relief=SUNKEN, borderwidth=5)
        self.frame_1.pack()
        self.lbl1 = Label(master=self.frame_1, text="Your Contact book", fg='red', font=("Helvetica", 16))
        self.lbl1.pack()
        # self.lbl1.place(x=200, y=20)

        self.frame_2 = Frame(master=window, relief=SUNKEN, borderwidth=5)
        self.frame_2.pack(side=LEFT)
        self.lbl2 = Label(master=self.frame_2, text='All contacts', fg='purple', font=("Helvetica", 12))
        self.lbl2.pack()
        # self.lbl2.place(x=440, y=230)

        self.frame_3 = Frame()
        self.lbl3 = Label(win, text='Name', fg='orange')
        self.lbl3.pack()
        # self.lbl3.place(x=90, y=260)

        self.frame_4 = Frame()
        self.lbl4 = Label(win, text='Number', fg='orange')
        self.lbl4.pack()
        # self.lbl4.place(x=90, y=300)

        self.frame_5 = Frame()
        self.data = ["Eldar (099)-346-7773", "Katya (066)-234-5866", "Elena (056)-445-9878", "Roma (050)-234-1854",
                     "Dania (093)-884-6390", "Gleb (095)-006-3828", "Anya (099)-775-9887"]
        self.lb = Listbox(window, height=5, selectmode='multiple')
        for num in self.data:
            self.lb.insert(END, num)
        self.lb.pack()
        # self.lb.place(x=400, y=260)
        self.lb.bind('<Double-Button-1>', self.open_menu)
        self.lb.bind('<Button-2>', self.close_menu)

        self.data = ["Delete contact", "Add contact", "Rename contact"]
        self.lb2 = Listbox(window, height=3)
        for num in self.data:
            self.lb2.insert(END, num)

        self.b1 = Button(win, text='Add contact', command=self.add_contact)
        self.b1.pack()
        # self.b1.place(x=150, y=340)

        self.t1 = Entry(bd=3)
        self.t1.pack()
        # self.t1.place(x=150, y=260)

        self.t2 = Entry(bd=3)
        self.t2.pack()
        # self.t2.place(x=150, y=300)

        image1 = Image.open("telephone2.png")
        test = ImageTk.PhotoImage(image1)
        label1 = Label(image=test)
        label1.image = test
        label1.pack()
        # label1.place(x=125, y=60)

    def add_contact(self):
        name = str(self.t1.get())
        number = str(self.t2.get())
        result = f"{name} {number}"
        if result != " ":
            self.lb.insert(END, str(result))
            self.t1.delete(0, 'end')
            self.t2.delete(0, 'end')

    def open_menu(self, name):
        self.lb2.pack()
        # self.data = ["Delete contact", "Add contact", "Rename contact"]
        # self.lb2 = Listbox(window, height=3)
        # for num in self.data:
        #     self.lb2.insert(END, num)
        # self.lb2.place(x=450, y=260)

    def close_menu(self, name):
        self.lb2.pack_forget()
        # self.lb2.destroy()


window = Tk()
mywin = MyWindow(window)
window.title('Contact book')
window.geometry("600x400+450+200")
window.mainloop()
