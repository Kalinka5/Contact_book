from tkinter.messagebox import askyesno


def confirmation_messagebox(old_first_name, old_last_name, new_first_name, new_last_name):
    if old_last_name == "" and new_last_name == "":
        answer = askyesno(title='Confirmation',
                          message='Are you sure that you want to rename '
                                  f'\"{old_first_name}\" to \"{new_first_name}\"?')
    elif old_last_name == "":
        answer = askyesno(title='Confirmation',
                          message='Are you sure that you want to rename '
                                  f'\"{old_first_name}\" to \"{new_first_name} {new_last_name}\"?')
    elif new_last_name == "":
        answer = askyesno(title='Confirmation',
                          message='Are you sure that you want to rename '
                                  f'\"{old_first_name} {old_last_name}\" to \"{new_first_name}\"?')
    else:
        answer = askyesno(title='Confirmation',
                          message='Are you sure that you want to rename '
                                  f'\"{old_first_name} {old_last_name}\" to \"{new_first_name} {new_last_name}\"?')

    return answer
