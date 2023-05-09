from tkinter.messagebox import askyesno


def confirmation_messagebox(new_first_name: str, new_last_name: str) -> askyesno:
    """Print confirmation messagebox to rename contact"""

    if new_last_name:
        answer = askyesno(title='Confirmation',
                          message=f'Are you sure that you want to edit contact \"{new_first_name} {new_last_name}\"?')
        print(f'Are you sure that you want to edit contact \"{new_first_name} {new_last_name}\"?')
    else:
        answer = askyesno(title='Confirmation',
                          message=f'Are you sure that you want to edit contact \"{new_first_name}\"?')
        print(f'Are you sure that you want to edit contact \"{new_first_name}\"?')

    return answer
