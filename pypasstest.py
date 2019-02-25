import datetime

name = str(input(">>>Name: "))
surname = str(input(">>>Surname: "))
nickname = str(input(">>>Nickname: "))
dob = str(input(">>>Date of birth: "))

def clean_input(a):
    clean = a.lower()
    return ''.join(i for i in clean if i.isalnum())

def validate(date_str):
    try:
        tdate = datetime.datetime.strptime(date_str, '%d%m%Y')
        return str(tdate)
    except ValueError:
        raise ValueError("Incorrect date format, should be DDMMYYYY")

if name != 0 and surname != 0 and nickname != 0 and dob != 0:
    pass0 = clean_input(name + surname)
    pass1 = clean_input(name + surname + nickname)
    pass3 = clean_input(name + validate(dob))

with open(name + '.txt', 'w') as f:
    content = [pass0, pass1, pass3]
    for i in content:
        print('{0}'.format(i), file=f)

