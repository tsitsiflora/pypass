#!/usr/bin/env python
import click
import pyfiglet


# banner
def pypass_banner():
    ascii_banner = pyfiglet.figlet_format("pypass")
    print(ascii_banner)

# function lower-cases the provided string
# strips the string off all special characters and spaces


def clean_input(text):
    clean = text.lower()
    return ''.join(i for i in clean if i.isalnum())

# function uses slicing to return a reverse of the string provided


def reverser(text):
    return text[::-1]

# function to convert datetime to string


def convert_date(date_input):
    date_string = date_input.strftime('%d%m%Y')
    return date_string


def takeother(other):
    return other.split(',')


@click.command()
@click.option('--about', is_flag=True, help='Information about the program and its usage.')
@click.option('--i', is_flag=True, help='Interactive shell to accept information about the target.')
def main(about, i):

    if about:
        pypass_banner()
        click.echo(
            "Welcome to pypass Version1.0!                     pypass --help for more options")
    else:
        pypass()


def pypass():

    profile = {}
    pass_list = []

    name = click.prompt('>>>Enter name ', type=str)
    surname = click.prompt('>>>Enter surname ', type=str)
    nickname = click.prompt('>>>Enter nickname ', type=str)
    dob = click.prompt('>>>Enter date of birth(DDMMYYY) ',
                       type=click.DateTime(formats=['%d%m%Y']))

    profile['name'] = name
    profile['surname'] = surname
    profile['nickname'] = nickname
    profile['dob'] = dob

    # print(profile)

    pass0 = reverser(profile['name'])
    pass1 = profile['name'] + profile['surname']
    pass2 = profile['name'] + profile['nickname']
    pass3 = profile['nickname'] + profile['surname']
    pass4 = reverser(profile['surname'])
    pass5 = profile['surname'] + profile['name']
    pass6 = profile['surname'] + profile['nickname']
    pass7 = profile['name'] + convert_date(profile['dob'])
    pass8 = profile['name'] + convert_date(profile['dob'])[:5]
    pass9 = profile['name'] + convert_date(profile['dob'])[4:]
    pass10 = profile['surname'] + convert_date(profile['dob'])
    pass11 = profile['surname'] + convert_date(profile['dob'])[:5]
    pass12 = profile['surname'] + convert_date(profile['dob'])[4:]
    pass13 = profile['nickname'] + convert_date(profile['dob'])
    pass14 = profile['nickname'] + convert_date(profile['dob'])[:5]
    pass15 = profile['nickname'] + convert_date(profile['dob'])[4:]

    pass_list = [pass0, pass1, pass2, pass3,
                 pass4, pass5, pass6, pass7, pass8, pass9, pass10, pass11, pass12, pass13, pass14, pass15]

    with open('passwords.txt', 'w+') as passfile:
        for i in pass_list:
            passfile.write("\n" + i)


if __name__ == "__main__":
    main()
