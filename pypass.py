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
#interactive shell, accepting input from the user
def main(about):
    profile = {}
    if about:
        click.echo("Welcome to pypass Version0.1!      pypass --help for more options")
    name = click.prompt('>>>Enter name ', type=str)
    surname = click.prompt('>>>Enter surname ', type=str)
    nickname = click.prompt('>>>Enter nickname ', type=str)

    profile['name'] = name
    profile['surname'] = surname
    profile['nickname'] = nickname

    print(profile)


if __name__ == "__main__":
    main()




