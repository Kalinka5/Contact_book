import tkinter as tk
import re
from Exceptions.name_exception import NameException
from Exceptions.number_exception import NumberException
from Exceptions.contact_exist_exception import ContactExistException
from tkinter import ttk, messagebox
from contact_book import Contact


class AddFrame(ttk.Frame):

    def __init__(self, container, contacts_txt, contacts_lf, contacts_scrollbar,
                 contact_book, tree, department, favorites):
        super().__init__(container)

        self.contacts_txt = contacts_txt
        self.contacts_lf = contacts_lf
        self.contacts_scrollbar = contacts_scrollbar
        self.contact_book = contact_book
        self.tree = tree
        self.dict_department = department
        self.favorites = favorites

        self.__create_widgets()

    def __create_widgets(self):
        self.grid(row=0, column=0, sticky='nsew')

        lf = ttk.LabelFrame(master=self, text='Add Contact Window')
        lf.place(x=30, y=30)

        lbl1 = ttk.Label(master=lf, text='First Name', font=("BOLD", 10))
        lbl1.grid(row=1, column=0, padx=5)

        self.text3 = tk.StringVar()
        t1 = ttk.Entry(master=lf, textvariable=self.text3)
        t1.focus()
        t1.grid(row=1, column=1, padx=5)

        lbl2 = ttk.Label(master=lf, text='Last Name', font=("BOLD", 10))
        lbl2.grid(row=2, column=0, padx=5)

        self.text4 = tk.StringVar()
        t2 = ttk.Entry(master=lf, textvariable=self.text4)
        t2.grid(row=2, column=1, padx=5)

        lbl3 = ttk.Label(master=lf, text='Number', font=("BOLD", 10))
        lbl3.grid(row=3, column=0, padx=5, pady=10)

        self.text5 = tk.StringVar()
        t3 = ttk.Entry(master=lf, textvariable=self.text5)
        t3.grid(row=3, column=1, padx=5, pady=5)

        lbl4 = ttk.Label(master=lf, text="Departments")
        lbl4.grid(row=1, column=2, padx=5)
        departments_str = tk.StringVar()
        self.departments = ttk.Combobox(master=lf, textvariable=departments_str)
        headers = ('Work', 'Classmates', 'Friends', 'Relatives', 'Stars')
        self.departments['values'] = headers
        self.departments['state'] = 'readonly'
        self.departments.grid(row=2, column=2, padx=5)
        self.departments.bind('<<ComboboxSelected>>', self.get_button_enable)

        self.btn = ttk.Button(master=lf, text='Add contact', command=self.add, cursor='hand2')
        self.btn.grid(row=4, column=2, padx=5, pady=50)
        self.btn.state(['disabled'])

        download_icon = tk.PhotoImage(file='images/close.png')
        download_button = ttk.Button(
            lf,
            image=download_icon,
            command=self.close_clicked
        )
        download_button.image = download_icon
        download_button.grid(row=0, column=2, sticky='e')

        self.tkraise()
        self.contacts_scrollbar.grid_forget()
        self.contacts_lf.grid_forget()

    def get_button_enable(self, department):
        # remove the disabled flag
        self.btn.state(['!disabled'])

    def close_clicked(self):
        self.contacts_txt.tkraise()
        self.contacts_scrollbar.grid(row=0, column=1, sticky='ns')
        self.contacts_lf.grid(row=1, column=0, sticky='ns')

    def add(self):
        try:
            first_name = self.text3.get().title()
            last_name = self.text4.get().title()
            digits = self.text5.get().replace("-", "")
            pattern = r"(\d{3})(\d{3})([\d.]+)"
            # convert phone number to (000)-000-0000
            result = re.search(pattern, digits)
            number = f"({result[1]})-{result[2]}-{result[3]}"

            # Get index of contact where he is in contact book by alphabet
            index = 0
            while index < len(self.contacts_txt.get_children()):
                if first_name.lower() < self.contacts_txt.item(self.contacts_txt.get_children()[index])['values'][0].lower():
                    break
                index += 1

            for contact in self.contact_book:
                if number == contact.phone_number:
                    raise ContactExistException()

            # Check name is it has less than 10 letters and more than 0
            if len(first_name) < 1 or len(first_name) > 10:
                raise NameException(first_name)

            # Check phone number is it has only digits
            elif digits.isdigit():
                if result:
                    # Add contact to class Contacts
                    department = self.departments.get()
                    contact = Contact(first_name, last_name, number, department)
                    self.contact_book.add_contact(contact)

                    # Add new contact to ContactsFrame
                    self.contacts_txt.insert('',
                                             index,
                                             values=(first_name, last_name, number))

                    # Add contact to DepartmentsFrame
                    children = self.tree.get_children(self.dict_department[department])
                    self.tree.delete(*children)

                    amount_all_contacts = len(self.contact_book)
                    for human in self.contact_book:
                        if human.department == department:
                            self.tree.insert('',
                                             tk.END,
                                             text=f'{human.first_name} {human.last_name}',
                                             iid=str(Contact.iid),
                                             open=False)
                            self.tree.move(str(Contact.iid),
                                           self.dict_department[department],
                                           amount_all_contacts)
                            Contact.iid += 1

                    # Clear all fields with data
                    self.text3.set("")
                    self.text4.set("")
                    self.text5.set("")

                    if last_name == "":
                        tk.messagebox.showinfo(title='Update Contact Book',
                                               message=f"\"{first_name}\" was successfully added.")
                        print(f"\"{first_name}\" was successfully added to your Contact Book.\n")
                    else:
                        # Show message box when add contact
                        tk.messagebox.showinfo(title='Update Contact Book',
                                               message=f"\"{first_name} {last_name}\" was successfully added.")
                        print(f"\"{first_name} {last_name}\" was successfully added to your Contact Book.\n")

                    # Open ContactsFrame again
                    self.contacts_txt.tkraise()
                    self.contacts_scrollbar.grid(row=0, column=1, sticky='ns')
                    self.contacts_lf.grid(row=1, column=0, sticky='ns')
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
        except ContactExistException as cee:
            print(cee)
            tk.messagebox.showwarning(title='Update Contact Book',
                                      message="A contact with this number is already in the phone book!")
