from tkinter.messagebox import askyesno


def confirmation_favorites(first_name: str, last_name: str) -> askyesno:
    """Print confirmation messagebox to add contact to Favorites"""

    if last_name == "":
        answer = askyesno(
            title='Confirmation',
            message=f'Are you sure that you want to add \"{first_name}\" to the Favorites?')
    else:
        answer = askyesno(
            title='Confirmation',
            message=f'Are you sure that you want to add \"{first_name} {last_name}\" to the Favorites?')

    return answer
