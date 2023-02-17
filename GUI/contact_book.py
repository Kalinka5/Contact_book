import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from Exceptions.name_exception import NameException
from Exceptions.number_exception import NumberException
from output_contacts import OutputContact
import re
import csv
import os
import pandas as pd


class ContactBook(OutputContact, tk.Tk):
    def __init__(self):
        super().__init__()

        self.lf = None
        self.b4 = None
        self.b3 = None
        self.b2 = None
        self.b1 = None
        self.selected_letter = None
        self.searching = None
        self.t1 = None
        self.t2 = None
        self.text1 = None
        self.text2 = None
        self.txt = None

        self.title('Contact book')
        self.window_width = 500
        self.window_height = 300

        # get the screen dimension
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        # find the center point
        self.center_x = int(self.screen_width / 2 - self.window_width / 2)
        self.center_y = int(self.screen_height / 2 - self.window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')
        self.resizable(True, True)

        self.iconbitmap('images/receiver.ico')

        # create a folder where templates will be downloaded.
        if os.path.exists("Contact_book.csv"):
            self.contact_book_r = open("Contact_book.csv")
            self.reader = csv.DictReader(self.contact_book_r)
            print("Open Contact book.")

        self.data = []
        self.__favorites = {}
        self.__all_contacts = {}
        self.pattern = r"^(\w+) (\d{3})(\d{3})([\d.]+)$"
        self.tab_control = ttk.Notebook(self)

        self.create_tab1()
        self.create_tab3()
        self.create_tab2()
        self.create_tab4()
        self.tab_control.pack(expand=1, fill='both')

    @property
    def favorites(self):
        return self.__favorites

    @property
    def all_contacts(self):
        return self.__all_contacts

    def create_tab4(self):
        tab4 = ttk.Frame(self.tab_control)
        self.tab_control.add(tab4, text='Add contact')
        lbl3 = ttk.Label(master=tab4, text='Name', font=("BOLD", 10))
        lbl3.pack(padx=5, pady=5)

        self.text1 = tk.StringVar()
        self.t1 = ttk.Entry(master=tab4, textvariable=self.text1)
        self.t1.focus()
        self.t1.pack(padx=5, pady=5)

        lbl4 = ttk.Label(master=tab4, text='Number', font=("BOLD", 10))
        lbl4.pack(padx=5, pady=5)

        self.text2 = tk.StringVar()
        self.t2 = ttk.Entry(master=tab4, textvariable=self.text2)
        self.t2.pack(padx=5, pady=5)

        btn = ttk.Button(master=tab4, text='Add contact', command=self.add_contact)
        btn.pack(padx=5, pady=5)

    def create_tab1(self):
        tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(tab1, text='Contact Book')

        lbl1 = ttk.Label(master=tab1, text="Your Contact book", foreground='red', font=("Helvetica", 16))
        lbl1.pack()

        test = tk.PhotoImage(name='telephone', file="images/telephone2.png")
        label1 = ttk.Label(master=tab1, image=test)
        label1.image = test
        label1.pack()

    def create_tab2(self):
        tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(tab2, text='Edit')

        # create a combobox all contacts
        self.selected_letter = tk.StringVar()
        self.searching = ttk.Combobox(tab2, textvariable=self.selected_letter)
        data = [f"{name.ljust(10)} {number}" for name, number in self.__all_contacts.items()]
        data.append("New contact")
        self.searching['values'] = data
        self.searching['state'] = 'readonly'
        self.searching.pack(fill=tk.X, padx=5, pady=5)
        self.searching.bind('<<ComboboxSelected>>', self.create_buttons)

        # label frame
        self.lf = ttk.LabelFrame(tab2, text='Interaction')
        self.lf.pack(ipadx=20, ipady=20, side=tk.LEFT, expand=True)

        self.b1 = ttk.Button(master=self.lf, text='Add contact', command=self.add_contact)
        self.b2 = ttk.Button(master=self.lf, text='Delete contact', command=self.delete_contact)
        self.b3 = ttk.Button(master=self.lf, text='Rename contact', command=self.rename_contact)
        self.b4 = ttk.Button(master=self.lf, text='Add to favorites', command=self.add_to_favorites)

        self.searching.set(data[0])
        self.b2.pack(ipadx=20, ipady=20, side=tk.LEFT, expand=True)
        self.b3.pack(ipadx=20, ipady=20, side=tk.LEFT, expand=True)
        self.b4.pack(ipadx=20, ipady=20, side=tk.LEFT, expand=True)

    def create_buttons(self, contact):
        if self.searching.get() == "New contact":
            self.b1.pack(ipadx=20, ipady=20, side=tk.LEFT, expand=True)
            self.b2.pack_forget()
            self.b3.pack_forget()
            self.b4.pack_forget()
        else:
            self.b1.pack_forget()
            self.b2.pack(ipadx=20, ipady=20, side=tk.LEFT, expand=True)
            self.b3.pack(ipadx=20, ipady=20, side=tk.LEFT, expand=True)
            self.b4.pack(ipadx=20, ipady=20, side=tk.LEFT, expand=True)

    def add_contact(self):
        try:
            name = self.text1.get().title()
            number = self.text2.get().replace("-", "")
            text = f"{name} {number}"
            if len(name) < 1 or len(name) > 10:
                raise NameException(name)
            elif number.isdigit():
                result = re.search(self.pattern, text)
                if result:
                    self.txt.insert('', tk.END, values=(name, f"({result[2]})-{result[3]}-{result[4]}"))
                    self.__all_contacts[name] = f"({result[2]})-{result[3]}-{result[4]}"
                    self.t1.delete(0, 'end')
                    self.t2.delete(0, 'end')
                    tk.messagebox.showinfo(title='Update Contact Book',
                                           message=f"\"{name}\" was successfully added.")
                    print(f"\"{name}\" was successfully added to your Contact Book.\n")
            else:
                raise NumberException(number)

        except NameException as ne:
            print(ne)
            messagebox.showerror('Name error', f'Invalid value of contact name.\n'
                                               'Name length should be from 1 to 10.\n')
        except NumberException as nue:
            print(nue)
            messagebox.showerror('Number error', 'Number should contain only integers and dashes.')

    def delete_contact(self):
        pattern = r"^(\w+)"
        deleted_name = re.search(pattern, self.searching.get())
        self.__all_contacts.pop(deleted_name[1])

        self.txt.delete('1.0', tk.END)
        self.txt.insert(tk.END, f"{'Names'.ljust(10)} Numbers\n\n")
        for name, number in self.__all_contacts.items():
            self.txt.insert(tk.END, f"{name.ljust(10)} {number}\n")

        data = [f"{name.ljust(10)} {number}" for name, number in self.__all_contacts.items()]
        data.append("New contact")
        self.searching['values'] = data

        self.searching.set('')

        print(f"Deleting \"{deleted_name[1]}\" from your Contact Book was successfully.\n")

    def rename_contact(self):
        pattern = r"^(\w+)"
        renamed_name = re.search(pattern, self.searching.get())
        print(renamed_name[1])

    def add_to_favorites(self):
        pattern = r"^(\w+)"
        renamed_name = re.search(pattern, self.searching.get())
        print(renamed_name[1])

    def create_tab3(self):
        tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(tab3, text='Contacts')

        columns = ('name', 'number')
        self.txt = ttk.Treeview(tab3, columns=columns, show='headings')
        self.txt.heading('name', text='Name')
        self.txt.heading('number', text='Number')
        df = pd.read_csv("Contact_book.csv")  # or pd.read_excel(filename) for xls file
        # generate sample data
        contacts = []
        if not df.empty:
            for row in self.reader:
                contacts.append((row['names'], row['numbers']))
                self.__all_contacts[row['names']] = row['numbers']

        # add data to the treeview
        for contact in contacts:
            self.txt.insert('', tk.END, values=contact)

        self.txt.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(tab3, orient=tk.VERTICAL, command=self.txt.yview)
        self.txt.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # self.txt = scrolledtext.ScrolledText(master=tab3, width=60, height=20)
        # df = pd.read_csv("Contact_book.csv")  # or pd.read_excel(filename) for xls file
        # self.txt.insert(tk.END, f"{'Names'.ljust(10)} Numbers\n\n")
        # if not df.empty:
        #     for row in self.reader:
        #         self.txt.insert(tk.END, f"{row['names'].ljust(10)} {row['numbers']}\n")
        #         self.__all_contacts[row['names']] = row['numbers']
        # self.txt.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.contact_book_r.close()

    def save_csv_file(self):
        contact_book_w = open("Contact_book.csv", "w")
        writer = csv.DictWriter(contact_book_w, fieldnames=["names", "numbers"])
        writer.writeheader()

        peoples = []
        for name, number in sorted(self.__all_contacts.items()):
            peoples.append({"names": name, "numbers": number})

        writer.writerows(peoples)

        contact_book_w.close()
