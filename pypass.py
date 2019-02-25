import datetime

def console_i():
    name = str(input(">>>Name: "))
    if name == "":
        name = str(input("You have to enter at least the name: "))

    surname = str(input(">>>Surname: "))
    nickname = str(input(">>>Nickname: "))
    dob = str(input(">>>Date of Birth [DDMMYYYY]: "))
        
    adds = str(input("\n\n>>>Would you like to add more information about the target?[Y/N]: "))
    if adds == 'y' or 'Y':
        other = str(input(">>>Things like fav series/band, food or phrases [separated by commas]: "))
    elif adds == 'N' or 'n':
        print('Password list ready!')
    else :
        print("Invalid input!")
    return name, surname, nickname, dob, other

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

def fstlevel(name):
    pass0 = name
    pass1 = name.title()

def basic(name, surname):
    if name != 0 and surname != 0:
        pass0 = clean_input(name + surname)
        pass1 = clean_input(surname + name)

    with open(name + '.txt', 'w') as f:
        content = [pass0, pass1]
        for i in content:
            print('{0}'.format(i), file=f)
                    
def main():



if __name__ == "__main__":
    main()
