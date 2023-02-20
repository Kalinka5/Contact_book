import tkinter as tk
from tkinter import ttk, messagebox
from Exceptions.name_exception import NameException
from Exceptions.number_exception import NumberException
from output_contacts import OutputContact
import re
import csv
import os
import pandas as pd


class Contact:
    def __init__(self, first_name, last_name, phone_number, department):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.department = department

    def __lt__(self, other):
        return self.first_name < other.first_name


class ContactBook(OutputContact):
    def __init__(self):
        self.contacts = []

    @property
    def get_contacts(self):
        return self.contacts

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, contact):
        self.contacts.pop(contact)

    def rename_contact(self, contact, new_name):
        contact.name = new_name


class ContactBookGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.df = None
        self.i = None
        self.tree = None
        self.btn = None
        self.departments = None
        self.text3 = None
        self.t3 = None
        self.lf = None
        self.b4 = None
        self.b3 = None
        self.b2 = None
        self.b1 = None
        self.selected_letter = None
        self.t1 = None
        self.t2 = None
        self.text1 = None
        self.text2 = None
        self.txt = None
        self.dict_departments = {'Work': "0", 'Classmates': "1", 'Friends': "2", 'Relatives': "3", 'Stars': "4"}

        self.title('Contact book')
        self.window_width = 430
        self.window_height = 320

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
        self.contact_book = ContactBook()
        self.tab_control = ttk.Notebook(self)

        self.create_tab1()
        self.create_tab2()
        self.create_tab3()
        self.create_tab4()

        self.df = pd.read_csv("Contact_book.csv")
        # generate sample data
        self.contacts = []
        if not self.df.empty:
            for row in self.reader:
                self.contacts.append((row['first_name'], row['last_name'], row['numbers']))
                self.contact_book.contacts.append(Contact(row['first_name'],
                                                          row['last_name'],
                                                          row['numbers'],
                                                          row['department']))
                self.tree.insert('',
                                 tk.END,
                                 text=f'{row["first_name"]} {row["last_name"]}',
                                 iid=str(self.i),
                                 open=False)
                self.tree.move(str(self.i), self.dict_departments[row["department"]], 0)
                self.i += 1

        # add data to the treeview
        for contact in self.contacts:
            self.txt.insert('', tk.END, values=contact)

        self.contact_book_r.close()
        self.tab_control.pack(expand=1, fill='both')

    def add_contact(self):
        try:
            first_name = self.text1.get().title()
            last_name = self.text2.get().title()
            number = self.text3.get().replace("-", "")
            pattern = r"(\d{3})(\d{3})([\d.]+)"
            if len(first_name) < 1 or len(first_name) > 10:
                raise NameException(first_name)
            elif number.isdigit():
                result = re.search(pattern, number)
                number = f"({result[1]})-{result[2]}-{result[3]}"
                if result:
                    self.txt.insert('',
                                    tk.END,
                                    values=(first_name, last_name, number))

                    department = self.departments.get()
                    self.tree.insert('', tk.END, text=f'{first_name} {last_name}', iid=str(self.i), open=False)
                    self.tree.move(str(self.i), self.dict_departments[department], 0)
                    self.i += 1

                    contact = Contact(first_name, last_name, number, department)
                    self.contact_book.add_contact(contact)

                    self.t1.delete(0, 'end')
                    self.t2.delete(0, 'end')
                    self.t3.delete(0, 'end')

                    tk.messagebox.showinfo(title='Update Contact Book',
                                           message=f"\"{first_name} {last_name}\" was successfully added.")
                    print(f"\"{first_name} {last_name}\" was successfully added to your Contact Book.\n")
            else:
                raise NumberException(number)

        except NameException as ne:
            print(ne)
            messagebox.showerror('Name error', 'Invalid value of contact name.\nName length should be from 1 to 10.\n')
        except NumberException as nue:
            print(nue)
            messagebox.showerror('Number error', 'Number should contain only integers and dashes.')

    def delete_contact(self):
        item = self.txt.item(self.txt.focus())['values']

        self.contact_book.delete_contact(f"{item[0]} {item[1]}")

        selected_item = self.txt.selection()[0]  # get selected item
        self.txt.delete(selected_item)

        tk.messagebox.showinfo(title='Update Contact Book',
                               message=f"\"{item[0]} {item[1]}\" was successfully deleted.")

        print(f"Deleting \"{item[0]} {item[1]}\" from your Contact Book was successfully.\n")

    def rename_contact(self):
        item = self.txt.item(self.txt.focus())['values']
        print(item)

    def add_to_favorites(self):
        item = self.txt.item(self.txt.focus())['values']
        print(item)

    def get_button_enable(self, department):
        # remove the disabled flag
        self.btn.state(['!disabled'])

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
        self.tab_control.add(tab2, text='Contacts')

        columns = ('first_name', 'last_name', 'number')
        self.txt = ttk.Treeview(tab2, columns=columns, show='headings')
        self.txt.heading('first_name', text='First Name')
        self.txt.heading('last_name', text='Second Name')
        self.txt.heading('number', text='Number')
        self.txt.column('first_name', width=100, anchor=tk.CENTER)
        self.txt.column('last_name', width=100, anchor=tk.CENTER)
        self.txt.column('number', width=200, anchor=tk.CENTER)

        self.txt.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(tab2, orient=tk.VERTICAL, command=self.txt.yview)
        self.txt.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # label frame
        self.lf = ttk.LabelFrame(tab2, text='Interaction')
        self.lf.grid(row=1, column=0, sticky='ns')

        self.b1 = ttk.Button(master=self.lf, text='Add contact', command=self.add_contact)
        self.b2 = ttk.Button(master=self.lf, text='Delete contact', command=self.delete_contact)
        self.b3 = ttk.Button(master=self.lf, text='Rename contact', command=self.rename_contact)
        self.b4 = ttk.Button(master=self.lf, text='Add to favorites', command=self.add_to_favorites)

        self.b2.grid(row=1, column=0, sticky='ns')
        self.b3.grid(row=1, column=1, sticky='ns')
        self.b4.grid(row=1, column=2, sticky='ns')

    def create_tab3(self):
        tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(tab3, text='Add contact')

        lbl3 = ttk.Label(master=tab3, text='First Name', font=("BOLD", 10))
        lbl3.grid(row=0, column=0)

        self.text1 = tk.StringVar()
        self.t1 = ttk.Entry(master=tab3, textvariable=self.text1)
        self.t1.focus()
        self.t1.grid(row=0, column=1)

        lbl4 = ttk.Label(master=tab3, text='Last Name', font=("BOLD", 10))
        lbl4.grid(row=1, column=0)

        self.text2 = tk.StringVar()
        self.t2 = ttk.Entry(master=tab3, textvariable=self.text2)
        self.t2.grid(row=1, column=1)

        lbl5 = ttk.Label(master=tab3, text='Number', font=("BOLD", 10))
        lbl5.grid(row=2, column=0)

        self.text3 = tk.StringVar()
        self.t3 = ttk.Entry(master=tab3, textvariable=self.text3)
        self.t3.grid(row=2, column=1)

        label = ttk.Label(master=tab3, text="Departments")
        label.grid(row=1, column=2)
        departments_str = tk.StringVar()
        self.departments = ttk.Combobox(master=tab3, textvariable=departments_str)
        headers = ('Work', 'Classmates', 'Friends', 'Relatives', 'Stars')
        self.departments['values'] = headers
        self.departments['state'] = 'readonly'
        self.departments.grid(row=2, column=2)
        self.departments.bind('<<ComboboxSelected>>', self.get_button_enable)

        self.btn = ttk.Button(master=tab3, text='Add contact', command=self.add_contact)
        self.btn.grid(row=3, column=1)
        self.btn.state(['disabled'])

    def create_tab4(self):
        tab4 = ttk.Frame(self.tab_control)
        self.tab_control.add(tab4, text='Departments')

        # create a treeview
        self.tree = ttk.Treeview(tab4)
        self.tree.heading('#0', text='Departments', anchor=tk.W)
        headers = ('Work', 'Classmates', 'Friends', 'Relatives', 'Stars')

        self.i = 0
        for head in headers:
            self.tree.insert('', tk.END, text=head, iid=str(self.i), open=False)
            self.i += 1

        # place the Treeview widget on the root window
        self.tree.pack()

    def save_csv_file(self):
        contact_book_w = open("Contact_book.csv", "w")
        writer = csv.DictWriter(contact_book_w, fieldnames=["first_name", "last_name", "numbers", "department"])
        writer.writeheader()

        peoples = []
        for contact in sorted(self.contact_book.contacts, key=lambda c: c.first_name):
            peoples.append({"first_name": contact.first_name,
                            "last_name": contact.last_name,
                            "numbers": contact.phone_number,
                            "department": contact.department})

        writer.writerows(peoples)

        contact_book_w.close()
