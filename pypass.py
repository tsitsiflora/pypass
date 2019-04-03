#!/usr/bin/env python

import click
import datetime

#function lower-cases the provided string
#strips the string off all special characters and spaces
def clean_input(a):
    clean = a.lower()
    return ''.join(i for i in clean if i.isalnum())

#function uses slicing to return a reverse of the string provided
def reverser(a):
    return a[::-1]

def takeother(other):
    return other.split(',')

   

@click.command()
@click.option('--about', is_flag=True, help='Information about the program and its usage.')
#@click.option('--full', is_flag=True, help='Option to get an almost exhaustive list of passwords. Requires more information about the target.')
#interactive shell, accepting input from the user
def main(about):

    profile = {}
    pass_list = []
    if about:
        click.echo("Welcome to pypass Version0.1!           pypass --help for more options")
    name = click.prompt('>>>Enter name ', type=str)
    surname = click.prompt('>>>Enter surname ', type=str)
    nickname = click.prompt('>>>Enter nickname ', type=str)
    dob = click.prompt('>>>Enter date of birth(DDMMYYY) ', type=click.DateTime(formats=['%d%m%Y']))

    profile['name'] = name
    profile['surname'] = surname
    profile['nickname'] = nickname
    profile['dob'] = dob

    #print(profile)

    pass0 = reverser(profile['name'])
    pass1 = profile['name'] + profile['surname']
    pass2 = profile['name'] + profile['nickname']
    pass3 = profile['nickname'] + profile['surname']
    pass4 = reverser(profile['surname'])
    pass5 = profile['surname'] + profile['name']
    pass6 = profile['surname'] + profile['nickname']

    pass_list = [pass0, pass1, pass2, pass3, pass4, pass5, pass6]

    for i in pass_list:
        with open('passwords.txt', 'w+' ) as passfile:
            passfile.write(i)


if __name__ == "__main__":
    main()




