from tkinter import messagebox

from Exceptions.exist_contact import ContactExistInFavoritesException, NameExistException, NumberExistException
from Exceptions.invalid_contact import InvalidLengthNumberException, InvalidNameException, InvalidNameQuotesException,\
    InvalidNumberException
from Exceptions.no_changes import ContactHasNoChanged
from Exceptions.not_ukrainian_code import NotUkrainianCode


# decorator to catch exception in Add frame and Edit frame
def try_exceptions(func):
    def _wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except InvalidNameException as ine:
            print(ine)
            messagebox.showerror(title='Name error',
                                 message=ine)
        except InvalidNameQuotesException as inqe:
            print(inqe)
            messagebox.showerror(title='Name error',
                                 message=inqe)
        except InvalidNumberException as inue:
            print(inue)
            messagebox.showerror(title='Number error',
                                 message=inue)
        except NumberExistException as cee:
            print(cee)
            messagebox.showwarning(title='Exist warning',
                                   message="A contact with this number is already in the Contact book!")
        except NameExistException as nee:
            print(nee)
            messagebox.showwarning(title='Exist warning',
                                   message="A contact with this name is already in the Contact Book!")
        except NotUkrainianCode as nuc:
            print(nuc)
            messagebox.showwarning(title='Update Contact Book',
                                   message=nuc)
        except InvalidLengthNumberException as ilne:
            print(ilne)
            messagebox.showerror(title='Number error',
                                 message=ilne)
        except ContactExistInFavoritesException as ceife:
            print(ceife)
            messagebox.showwarning(title='Exist warning',
                                   message=ceife)
        except ContactHasNoChanged as chnc:
            print(chnc)
            messagebox.showwarning(title='No change warning',
                                   message=chnc)

    return _wrapper
