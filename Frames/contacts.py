import tkinter as tk
import csv
import os
import re
import pandas as pd
from tkinter import ttk, messagebox
from Exceptions.name_exception import NameException
from Exceptions.number_exception import NumberException
from contact_book import Contact


class ContactsFrame(ttk.Frame):
    def __init__(self, container, tab_control, contact_book, tree, department, i):
        super().__init__(container)

        self.departments = None
        self.btn = None
        self.text5 = None
        self.text4 = None
        self.text3 = None
        self.text2 = None
        self.text1 = None
        self.tab_control = tab_control
        self.contact_book = contact_book
        self.tree = tree
        self.dict_department = department
        self.i = i

        self.__create_widgets()

    def __create_widgets(self):
        self.tab_control.add(self, text='Contacts')

        columns = ('first_name', 'last_name', 'number')
        self.txt = ttk.Treeview(self, columns=columns, show='headings')
        self.txt.heading('first_name', text='First Name')
        self.txt.heading('last_name', text='Second Name')
        self.txt.heading('number', text='Number')
        self.txt.column('first_name', width=100, anchor=tk.CENTER)
        self.txt.column('last_name', width=100, anchor=tk.CENTER)
        self.txt.column('number', width=200, anchor=tk.CENTER)

        # Read file to check is it empty
        df = pd.read_csv("Contact_book.csv")

        # Create contacts to store data for Contacts Treeview
        self.contacts = []

        # Append to Contacts Treeview all data from CSV file
        if os.path.exists("Contact_book.csv"):
            contact_book_r = open("Contact_book.csv")
            reader = csv.DictReader(contact_book_r)

            if not df.empty:
                for row in reader:
                    self.contacts.append((row['first_name'], row['last_name'], row['numbers']))

            # add data to the Contacts Treeview
            for contact in self.contacts:
                self.txt.insert('', tk.END, values=contact)

            contact_book_r.close()

        self.txt.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar to Contacts Treeview
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.txt.yview)
        self.txt.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        # Create Label Frame with 3 buttons
        self.lf = ttk.LabelFrame(self, text='Interaction')
        self.lf.grid(row=1, column=0, sticky='ns', pady=10)

        self.b1 = ttk.Button(master=self.lf, text='Add contact', command=self.add_contact, cursor='hand2')
        self.b2 = ttk.Button(master=self.lf, text='Delete contact', command=self.delete_contact, cursor='hand2')
        self.b3 = ttk.Button(master=self.lf, text='Rename contact', command=self.rename_contact, cursor='hand2')
        self.b4 = ttk.Button(master=self.lf, text='Add to favorites', command=self.add_to_favorites, cursor='hand2')

        self.b1.grid(row=1, column=0, sticky='ns')
        self.b2.grid(row=1, column=1, sticky='ns')
        self.b3.grid(row=1, column=2, sticky='ns')
        self.b4.grid(row=1, column=3, sticky='ns')

    def add_contact(self):
        add_frame = ttk.Frame(self)
        add_frame.grid(row=0, column=0, sticky='nsew')

        lf = ttk.LabelFrame(master=add_frame, text='Add Contact Window')
        lf.place(x=30, y=40)

        lbl1 = ttk.Label(master=lf, text='First Name', font=("BOLD", 10))
        lbl1.grid(row=0, column=0, padx=5)

        self.text3 = tk.StringVar()
        t1 = ttk.Entry(master=lf, textvariable=self.text3)
        t1.focus()
        t1.grid(row=0, column=1, padx=5)

        lbl2 = ttk.Label(master=lf, text='Last Name', font=("BOLD", 10))
        lbl2.grid(row=1, column=0, padx=5)

        self.text4 = tk.StringVar()
        t2 = ttk.Entry(master=lf, textvariable=self.text4)
        t2.grid(row=1, column=1, padx=5)

        lbl3 = ttk.Label(master=lf, text='Number', font=("BOLD", 10))
        lbl3.grid(row=2, column=0, padx=5, pady=10)

        self.text5 = tk.StringVar()
        t3 = ttk.Entry(master=lf, textvariable=self.text5)
        t3.grid(row=2, column=1, padx=5, pady=5)

        lbl4 = ttk.Label(master=lf, text="Departments")
        lbl4.grid(row=0, column=2, padx=5)
        departments_str = tk.StringVar()
        self.departments = ttk.Combobox(master=lf, textvariable=departments_str)
        headers = ('Work', 'Classmates', 'Friends', 'Relatives', 'Stars')
        self.departments['values'] = headers
        self.departments['state'] = 'readonly'
        self.departments.grid(row=1, column=2, padx=5)
        self.departments.bind('<<ComboboxSelected>>', self.get_button_enable)

        self.btn = ttk.Button(master=lf, text='Add contact', command=self.add, cursor='hand2')
        self.btn.grid(row=3, column=2, padx=5, pady=50)
        self.btn.state(['disabled'])

        add_frame.tkraise()
        self.scrollbar.grid_forget()
        self.lf.grid_forget()
        
    def add(self):
        try:
            first_name = self.text3.get().title()
            last_name = self.text4.get().title()
            number = self.text5.get().replace("-", "")
            pattern = r"(\d{3})(\d{3})([\d.]+)"

            # Get index of contact where he is in contact book by alphabet
            index = 0
            while index < len(self.txt.get_children()):
                if first_name.lower() < self.txt.item(self.txt.get_children()[index])['values'][0].lower():
                    break
                index += 1

            # Check name is it has less than 10 letters and more than 0
            if len(first_name) < 1 or len(first_name) > 10:
                raise NameException(first_name)

            # Check phone number is it has only digits
            elif number.isdigit():
                # convert phone number to (000)-000-0000
                result = re.search(pattern, number)
                number = f"({result[1]})-{result[2]}-{result[3]}"
                if result:

                    # Add new contact to ContactsFrame
                    self.txt.insert('',
                                    index,
                                    values=(first_name, last_name, number))

                    # Add contact to DepartmentsFrame
                    department = self.departments.get()
                    self.tree.insert('', tk.END, text=f'{first_name} {last_name}', iid=str(self.i), open=False)
                    self.tree.move(str(self.i), self.dict_department[department], 0)
                    self.i += 1

                    # Add contact to class Contacts
                    contact = Contact(first_name, last_name, number, department)
                    self.contact_book.add_contact(contact)

                    # Clear all fields with data
                    self.text3.set("")
                    self.text4.set("")
                    self.text5.set("")

                    # Show message box when add contact
                    tk.messagebox.showinfo(title='Update Contact Book',
                                           message=f"\"{first_name} {last_name}\" was successfully added.")
                    print(f"\"{first_name} {last_name}\" was successfully added to your Contact Book.\n")

                    # Open ContactsFrame again
                    self.txt.tkraise()
                    self.scrollbar.grid(row=0, column=1, sticky='ns')
                    self.lf.grid(row=1, column=0, sticky='ns')
            else:
                # If number contain not only digits, it raises exception
                raise NumberException(number)

        except NameException as ne:
            # When raise Name error, it shows message box with error text
            print(ne)
            messagebox.showerror('Name error', 'Invalid value of contact name.\nName length should be from 1 to 10.\n')
        except NumberException as nue:
            # When raise Number error, it shows message box with error text
            print(nue)
            messagebox.showerror('Number error', 'Number should contain only integers and dashes.')

    def get_button_enable(self, department):
        # remove the disabled flag
        self.btn.state(['!disabled'])

    def delete_contact(self):
        human = self.txt.item(self.txt.focus())['values']

        first_name = human[0]
        last_name = human[1]
        number = human[2]

        index_txt = None
        dep_user = None
        for n, user in enumerate(self.contact_book.contacts):
            if number == user.phone_number:
                index_txt = n
            if first_name == user.first_name:
                dep_user = user.department

        # Delete in class the Contact book
        contact = self.contact_book.contacts[index_txt]
        self.contact_book.delete_contact(contact)

        # Delete in ContactsFrame
        selected_item = self.txt.selection()[0]
        self.txt.delete(selected_item)

        # Delete in DepartmentsFrame
        found_id = None
        # Search for the row with contact name in the contact's department column
        for item in self.tree.get_children(self.dict_department[dep_user]):
            if self.tree.item(item, 'text') == f"{first_name} {last_name}":
                found_id = item
                break

        self.tree.delete(found_id)

        tk.messagebox.showinfo(title='Update Contact Book',
                               message=f"\"{human[0]} {human[1]}\" was successfully deleted.")

        print(f"Deleting \"{human[0]} {human[1]}\" from your Contact Book was successfully.\n")

    def rename_contact(self):
        item = self.txt.item(self.txt.focus())['values']

        renamer = ttk.Frame(self)
        renamer.grid(row=0, column=0, sticky='nsew')

        lf = ttk.LabelFrame(master=renamer, text='Rename Window')
        lf.place(x=85, y=60)

        lbl1 = ttk.Label(master=lf, text=f'You choose the contact \"{item[0]} {item[1]}\".', font=("BOLD", 10))
        lbl1.pack()

        btn = ttk.Button(master=lf, text='Rename contact', command=self.rename, cursor='hand2')
        btn.pack(side=tk.BOTTOM)

        self.text2 = tk.StringVar()
        t2 = ttk.Entry(master=lf, textvariable=self.text2)
        t2.pack(side=tk.BOTTOM)

        lbl2 = ttk.Label(master=lf, text='New last name', font=("BOLD", 10))
        lbl2.pack(side=tk.BOTTOM)

        self.text1 = tk.StringVar()
        t1 = ttk.Entry(master=lf, textvariable=self.text1)
        t1.focus()
        t1.pack(side=tk.BOTTOM)

        lbl1 = ttk.Label(master=lf, text='New first name', font=("BOLD", 10))
        lbl1.pack(side=tk.BOTTOM)

        renamer.tkraise()
        self.scrollbar.grid_forget()
        self.lf.grid_forget()

    def add_to_favorites(self):
        item = self.txt.item(self.txt.focus())['values']
        print(item)

    def rename(self):
        item = self.txt.item(self.txt.focus())['values']

        old_first_name = item[0]
        old_last_name = item[1]
        number = item[2]
        new_first_name = self.text1.get()
        new_last_name = self.text2.get()

        index_txt = None
        for n, user in enumerate(self.contact_book.contacts):
            if number == user.phone_number:
                index_txt = n

        # Rename contact in the class ContactsFrame
        selected_item = self.txt.selection()[0]
        self.txt.delete(selected_item)

        index = 0
        while index < len(self.txt.get_children()):
            if new_first_name.lower() < self.txt.item(self.txt.get_children()[index])['values'][0].lower():
                break
            index += 1

        self.txt.insert('',
                        index,
                        values=(new_first_name, new_last_name, number))

        # Rename contact in the class DepartmentsFrame
        dep_user = None
        for n, user in enumerate(self.contact_book.contacts):
            if old_first_name == user.first_name:
                dep_user = user.department

        found_id = None
        for item in self.tree.get_children(self.dict_department[dep_user]):
            if self.tree.item(item, 'text') == f"{old_first_name} {old_last_name}":
                found_id = item
                break

        self.tree.delete(found_id)

        self.tree.insert('', tk.END, text=f'{new_first_name} {new_last_name}', iid=str(self.i), open=False)
        self.tree.move(str(self.i), self.dict_department[dep_user], 0)
        self.i += 1

        # Rename contact in the class ContactBook
        contact = self.contact_book.contacts[index_txt]
        self.contact_book.rename_contact(contact, new_first_name, new_last_name)

        # Open ContactsFrame again
        self.txt.tkraise()
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.lf.grid(row=1, column=0, sticky='ns')
