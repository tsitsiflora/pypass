import click


def other_info_callback(ctx, param, value):
    pass


@click.command()
@click.option('--fullname', prompt='Enter target\'s fullname',
              help='Target\'s fullname ')
@click.option('--nickname', prompt='Enter target\'s nickname',
              help='Target\'s nickname')
@click.option('--date_of_birth',
              prompt='Enter target\'s date of birth in this format dd-mm-yyyy',
              help='Target\'s date of birth',
              type=click.DateTime(formats=['%d-%m-%Y']))
@click.option('--other',
              prompt="Do you have other info about the target? ",
              help='Other useful info about the target ie hobbies, likes, etc',
              type=click.Choice(['yes', 'no']), callback=other_info_callback)
@click.option('--output_file',
              help='The file to write information about the target',
              default='password.txt', show_default=True)
def pypass(fullname, nickname, date_of_birth, other, output_file):
    '''
    Command line password cracker based on user provided information
    '''

    if fullname and nickname and date_of_birth:
        # if all the information about the target has been provided
        with open(output_file, 'w+') as _file:
            if not other == 'no':
                # so we have other information provided
                _file.write('{}\t {}\t {}'.format(
                                fullname, nickname, date_of_birth))
            # else other is none
            _file.write('{}\t {}\t {}'.format(
                                fullname, nickname, date_of_birth))

<<<<<<< HEAD
def console_i():
    name = str(input(">>>Name: "))
    if name == "":
        name = str(input("You have to enter at least the name: "))

    surname = str(input(">>>Surname: "))
    nickname = str(input(">>>Nickname: "))
    dob = str(input(">>>Date of Birth [YYYY-MM-DD]: "))
        
    adds = str(input("\n\n>>>Would you like to add more information about the target?[y/n]: "))
    if adds == 'y':
        extra = str(input(">>>Things like fav series/band, food or phrases [separated by commas]: "))
    elif adds == 'n':
        print('Password list ready!')
    else :
        print("Invalid input!")
    return name, surname, nickname, dob, extra

def clean_input(a):
    clean = a.lower()
    return ''.join(i for i in clean if i.isalnum())


def validate(date_text):
    try:
        if date_text != datetime.datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        return False    

def parse_other(info):
    ls = info.split(',')
    return ls

def fstlevel(name):
    pass0 = name
    pass1 = name.title()
    print(pass0, pass1)

def basic(name, surname):
    if name != 0 and surname != 0:
        pass0 = clean_input(name + surname)
        pass1 = clean_input(surname + name)

    with open(name + '.txt', 'w') as f:
        content = [pass0, pass1]
        for i in content:
            print('{0}'.format(i), file=f)
                    
def main():
    console_i()
    fstlevel(name)



if __name__ == "__main__":
    main()
=======

if __name__ == '__main__':
    pypass()
>>>>>>> 015a0a9bbfe1d44b036058c701d121cc12833cc9
