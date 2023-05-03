from tkinter.messagebox import askyesno


def confirmation_messagebox(first_name: str, last_name: str) -> askyesno:
    """Print confirmation messagebox to delete contact from the Favorites"""

    if last_name == "":
        answer = askyesno(
            title='Confirmation',
            message=f'Are you sure that you want to delete \"{first_name}\" from the Favorites?')
    else:
        answer = askyesno(
            title='Confirmation',
            message=f'Are you sure that you want to delete \"{first_name} {last_name}\" from the Favorites?')

    return answer
