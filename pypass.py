name = str(input("Enter the name of the target: "))
surname = str(input("Enter the surname of the target: "))
dob = str(input("Enter the date of birth of the target DDMMYYYY: "))

def pypass(name, surname, dob):
    if name != 0 and surname != 0 and dob != 0:
        password = name + surname + dob
        with open(name + '.txt', 'w') as f:
            print(password, file=f)
        
if __name__ == '__main__':
    pypass(name, surname, dob)


