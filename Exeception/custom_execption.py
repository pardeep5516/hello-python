
class NameToSortError(ValueError):
    pass
def validate(name):
    if len(name) <8:
        raise NameToSortError("name is too short")
    return name


user_name = input("enter your Name ")
print(validate(user_name))