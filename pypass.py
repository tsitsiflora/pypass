import datetime

name = str(input(">>>Name: "))
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
        datetime.datetime.strptime(date_str, '%d%m%Y')
    except ValueError:
        raise ValueError("Incorrect date format, should be DDMMYYYY")

def organise(info):
    


def main():
    if name != 0 and surname != 0 and dob != 0:
        pass0 = clean_input(name + surname)
        pass1 = clean_input(name + surname + validate(dob))
        pass2 = clean_input(name + surname + validate(dob[4:]))
        pass3 = clean_input(name + surname + validate(dob[6:]))
        pass4 = clean_input(name + surname + validate(dob[:4]))
        pass5 = clean_input(name + validate(dob))
        pass6 = clean_input(surname + validate(dob))
        pass7 = clean_input(name + validate(dob[4:]))
        pass8 = clean_input(name + validate(dob[6:]))
        pass9 = clean_input(name + validate(dob[:4]))
        pass10 = clean_input(name + surname + '@' + validate(dob))
        pass11 = clean_input(name + surname + '@' + validate(dob[4:]))
        pass12 = clean_input(name + surname + '@' + validate(dob[6:]))
        pass13 = clean_input(name + surname + '@' + validate(dob[:4]))
        pass14 = clean_input(nickname + validate(dob))
        pass15 = clean_input(nickname + validate(dob[4:]))
        pass16 = clean_input(nickname + validate(dob[6:]))
        pass17 = clean_input(nickname + validate(dob[:4]))
        pass18 = clean_input(nickname + '@' + validate(dob))
        pass19 = clean_input(nickname + '@' + validate(dob[4:]))
        pass20 = clean_input(nickname + '@' + validate(dob[6:]))
        pass21 = clean_input(nickname + '@' + validate(dob[:4]))
        pass22 = clean_input(surname + name)
        pass23 = clean_input(name + nickname)
        pass24 = clean_input(nickname + surname)
        pass25 = clean_input(surname + name + validate(dob))
        pass26 = clean_input(surname + validate(dob[4:]))
        pass27 = clean_input(surname + validate(dob[6:]))
        pass28 = clean_input(surname + validate(dob[:4]))
        pass29 = clean_input(nickname + surname + validate(dob))
        pass30 = clean_input(nickname + surname + validate(dob[4:]))
        pass31 = clean_input(nickname + surname + validate(dob[6:]))
        pass26 = clean_input(nickname + surname + validate(dob[:4]))


        with open(name + '.txt', 'w') as f:
            content = [pass0, pass1, pass2, pass3, pass4, pass5, pass6, pass7, pass8, pass9, pass10, pass11,
                    pass12, pass13, pass14, pass15, pass16, pass17, pass18, pass19, pass20, pass21, pass22, pass23, pass24 ]
            for i in content:
                print('{0}'.format(i), file=f)
           
        
if __name__ == '__main__':
    main()


