import click
allpass = []

def other_info_callback(ctx, param, value):
    pass

#function lower-cases the provided string
#strips the string off all special characters and spaces
def clean_input(a):
    clean = a.lower()
    return ''.join(i for i in clean if i.isalnum())

#function uses slicing to return a reverse of the string provided
def reverser(a):
    return a[::-1]

#@click.command()
@click.option('--firstname', prompt='Enter target\'s firstname: ',
              help='Target\'s firstname ')
@click.option('--surname', prompt='Enter target\'s surname: ',
              help='Target\'s surname'  )
@click.option('--nickname', prompt='Enter target\'s nickname: ',
              help='Target\'s nickname')
@click.option('--date_of_birth',
              prompt='Enter target\'s date of birth in this format dd-mm-yyyy',
              help='Target\'s date of birth',
              type=click.DateTime(formats=['%d-%m-%Y']))
@click.option('--other',
              prompt="Do you have other info about the target? ",
              help='Other useful info about the target ie hobbies, likes, etc',
              type=click.Choice(['yes', 'no']), callback=other_info_callback)


def tooobv(firstname):
    pass0 = clean_input(firstname)
    pass1 = clean_input(firstname.title())
    pass2 = clean_input(firstname.upper())
    return allpass.append(pass0, pass1, pass2)

def lvl1(firstname, surname):
    pass3 = clean_input(firstname + surname)
    pass4 = clean_input(surname + firstname)
    pass5 = clean_input(firstname.title() + surname.title())
    pass6 = clean_input(surname.title() + firstname.title())
    pass7 = clean_input((firstname + surname).upper())
    pass8 = clean_input((surname + firstname).upper())



def pypass(firstname,surname, nickname, date_of_birth, other, output_file):
    '''
    Command line password profiler based on user provided information
    '''

    if firstname and surname and nickname and date_of_birth:
        # if all the information about the target has been provided
        with open(output_file, 'w+') as _file:
            if not other == 'no':
                # so we have other information provided
                _file.write('{}\t {}\t {}'.format(
                                firstname, nickname, date_of_birth))
            # else other is none
            _file.write('{}\t {}\t {}'.format(
                                firstname, nickname, date_of_birth))


if __name__ == '__main__':
    pypass()
