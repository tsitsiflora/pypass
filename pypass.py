import datetime
import os

name = str(input(">>>Name: "))
surname = str(input(">>>Surname: "))
nickname = str(input(">>>Nickname: "))

dob = str(input(">>>Date of Birth DDMMYYYY: "))
    
adds = str(input("\n\nWould you like to add more information about the target?: "))
if adds == 'yes' or 'y':
    sp_chars = str(input("Things like fav series/band, food or phrases: "))
elif adds == 'no' or 'n':
    pass

def clean_input(a):
    clean = a.lower()
    return ''.join(i for i in clean if i.isalnum())


def pypass(name, surname, dob, nickname, sp_chars):
    if name != 0 and surname != 0 and dob != 0:
        pass0 = clean_input(name + surname)
        pass1 = clean_input(name + surname + dob)
        pass2 = clean_input(name + surname + dob[4:])
        pass3 = clean_input(name + surname + dob[6:])
        pass4 = clean_input(name + surname + dob[:4])
        pass5 = clean_input(name + dob)
        pass6 = clean_input(surname + dob)
        pass7 = clean_input(name + dob[4:])
        pass8 = clean_input(name + dob[6:])
        pass9 = clean_input(name + dob[:4])
        pass10 = clean_input(name + surname + '@' + dob)
        pass11 = clean_input(name + surname + '@' + dob[4:])
        pass12 = clean_input(name + surname + '@' + dob[6:])
        pass13 = clean_input(name + surname + '@' + dob[:4])
        pass14 = clean_input(nickname + dob)
        pass15 = clean_input(nickname + dob[4:])
        pass16 = clean_input(nickname)+ dob[6:]
        pass17 = clean_input(nickname + dob[:4])
        pass18 = clean_input(nickname + '@' + dob)
        pass19 = clean_input(nickname + '@' + dob[4:])
        pass20 = clean_input(nickname + '@' + dob[6:])
        pass21 = clean_input(nickname + '@' + dob[:4])
        




        content = [pass1, pass2, pass3, pass4]

        with open(name + '.txt', 'w') as f:
            print(content , file=f)


        
if __name__ == '__main__':
    pypass(name, surname, dob, nickname, sp_chars)


