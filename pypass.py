import datetime

name = str(input(">>>Name: "))
if name == 0:
    print("You have to enter at least the name")

surname = str(input(">>>Surname: "))
nickname = str(input(">>>Nickname: "))
dob = str(input(">>>Date of Birth DDMMYYYY: "))
    
adds = str(input("\n\nWould you like to add more information about the target?[Y/N]: "))
if adds == 'Y':
    other = str(input("Things like fav series/band, food or phrases separated by commas: "))
elif adds == 'N':
    print('Password list ready!')
else :
    print("Invalid input!")

def clean_input(a):
    clean = a.lower()
    return ''.join(i for i in clean if i.isalnum())

def validate(date_str):
    try:
        tdate = datetime.datetime.strptime(date_str, '%d%m%Y')
        return str(tdate)
    except ValueError:
        raise ValueError("Incorrect date format, should be DDMMYYYY")

def parse_other(info):
    ls = info.split(',')
    return ls

def basic():
    if name != 0 and surname != 0:
        pass0 = clean_input(name + surname)
        pass1 = clean_input(surname + name)

    with open(name + '.txt', 'w') as f:
        content = [pass0, pass1]
        for i in content:
            print('{0}'.format(i), file=f)
                    
