import tkinter as tk
from tkinter import ttk, messagebox
from Exceptions.name_exception import NameException
from Exceptions.number_exception import NumberException
from contact_book import Contact
import re


class AddContactFrame(ttk.Frame):
    def __init__(self, container, tab_control, txt, tree, i, dict_departments, contact_book):
        super().__init__(container)
        
        self.tab_control = tab_control
        self.txt = txt
        self.tree = tree
        self.i = i
        self.dict_departments = dict_departments
        self.contact_book = contact_book

        self.__create_widgets()

    def __create_widgets(self):
        self.tab_control.add(self, text='Add contact')

        lbl1 = ttk.Label(master=self, text='First Name', font=("BOLD", 10))
        lbl1.grid(row=0, column=0)

        self.text1 = tk.StringVar()
        self.t1 = ttk.Entry(master=self, textvariable=self.text1)
        self.t1.focus()
        self.t1.grid(row=0, column=1)

        lbl2 = ttk.Label(master=self, text='Last Name', font=("BOLD", 10))
        lbl2.grid(row=1, column=0)

        self.text2 = tk.StringVar()
        self.t2 = ttk.Entry(master=self, textvariable=self.text2)
        self.t2.grid(row=1, column=1)

        lbl3 = ttk.Label(master=self, text='Number', font=("BOLD", 10))
        lbl3.grid(row=2, column=0)

        self.text3 = tk.StringVar()
        self.t3 = ttk.Entry(master=self, textvariable=self.text3)
        self.t3.grid(row=2, column=1)

        lbl4 = ttk.Label(master=self, text="Departments")
        lbl4.grid(row=1, column=2)
        departments_str = tk.StringVar()
        self.departments = ttk.Combobox(master=self, textvariable=departments_str)
        headers = ('Work', 'Classmates', 'Friends', 'Relatives', 'Stars')
        self.departments['values'] = headers
        self.departments['state'] = 'readonly'
        self.departments.grid(row=2, column=2)
        self.departments.bind('<<ComboboxSelected>>', self.get_button_enable)

        self.btn = ttk.Button(master=self, text='Add contact', command=self.add_contact, cursor='hand2')
        self.btn.grid(row=3, column=1)
        self.btn.state(['disabled'])

    def add_contact(self):
        try:
            first_name = self.text1.get().title()
            last_name = self.text2.get().title()
            number = self.text3.get().replace("-", "")
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
                    self.tree.move(str(self.i), self.dict_departments[department], 0)
                    self.i += 1

                    # Add contact to class Contacts
                    contact = Contact(first_name, last_name, number, department)
                    self.contact_book.add_contact(contact)

                    # Clear all fields with data
                    self.t1.delete(0, 'end')
                    self.t2.delete(0, 'end')
                    self.t3.delete(0, 'end')

                    # Show message box when add contact
                    tk.messagebox.showinfo(title='Update Contact Book',
                                           message=f"\"{first_name} {last_name}\" was successfully added.")
                    print(f"\"{first_name} {last_name}\" was successfully added to your Contact Book.\n")
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
