


def format_name(fname, lname):
    '''takes the first name and last name and formats it into a title'''
    formated_f_name=fname.title()
    formated_lname=lname.title()
    return f"{formated_f_name} {formated_lname}"

first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
formatted_string=format_name(first_name,last_name)
print(formatted_string)