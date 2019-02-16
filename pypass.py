name = str(input(">>>Name: "))
surname = str(input(">>>Surname: "))
dob = str(input(">>>Date of Birth DDMMYYYY: "))
nickname = str(input(">>>Nickname: "))

adds = str(input("\n\nWould you like to add more information about the target?: "))
if adds == 'yes' or 'y':
    sp_chars = str(input("Things like fav series/band, food or phrases: "))
else:
    pass

def clean_input(a):
    clean = a.lower()
    return ''.join(i for i in clean if i.isalnum())


def pypass(name, surname, dob, nickname, sp_chars):
    if name != 0 and surname != 0 and dob != 0:
        pass1 = clean_input(name + surname + dob)
        pass2 = clean_input(name + surname + dob[4:])
        pass3 = clean_input(name + surname + dob[6:])
        pass4 = clean_input(name + surname + dob[:4])

        with open(name + '.txt', 'w') as f:
            print(pass1, pass2, pass3, pass4, file=f)


        
if __name__ == '__main__':
    pypass(name, surname, dob, nickname, sp_chars)


