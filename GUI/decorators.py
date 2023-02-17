def check_name(func):
    def _wrapper(*args, **kwargs):
        self, name = args[:2]
        result = func(*args, **kwargs)
        if result == 1:
            if name.title() in self.changed_names:
                print(f"There is no \"{name}\" in your Contact book.\n"
                      f"Maybe you mean \"{self.changed_names[name.title()]}\"?\n")
            else:
                print(f"There is no \"{name}\" in your Contact book.\n")
    return _wrapper
