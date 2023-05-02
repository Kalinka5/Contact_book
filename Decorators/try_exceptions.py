from tkinter import messagebox

from Exceptions.invalid_contact import InvalidNameException, InvalidNumberException, InvalidLengthNumberException
from Exceptions.exist_contact import NumberExistException, NameExistException
from Exceptions.not_ukrainian_code import NotUkrainianCode


def try_exceptions(func):
    def _wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except InvalidNameException as ine:
            print(ine)
            messagebox.showerror(title='Name error',
                                 message=ine)
        except InvalidNumberException as inue:
            print(inue)
            messagebox.showerror(title='Number error',
                                 message=inue)
        except NumberExistException as cee:
            print(cee)
            messagebox.showwarning(title='Update Contact Book',
                                   message="A contact with this number is already in the Contact book!")
        except NameExistException as nee:
            print(nee)
            messagebox.showwarning(title='Update Contact Book',
                                   message="A contact with this name is already in the Contact Book!")
        except NotUkrainianCode as nuc:
            print(nuc)
            messagebox.showwarning(title='Update Contact Book',
                                   message=nuc)
        except InvalidLengthNumberException as ilne:
            print(ilne)
            messagebox.showerror(title='Update Contact Book',
                                 message=ilne)
    return _wrapper
