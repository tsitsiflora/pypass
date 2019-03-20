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
@click.option('interactive','/-i', help="Interactive shell for accepting input")
def interactive_shell(interactive):
    if interactive:
        main()






#interactive shell, accepting input from the user
@click.command()
def main():
    name = click.prompt('>>>Enter name ', type=str)
    surname = click.prompt('>>>Enter surname ', type=str)
    nickname = click.prompt('>>>Enter nickname ', type=str)
    dob = click.prompt('>>>Enter date of birth ', type=datetime.date)
    if click.confirm('>>>Any additional info ', default=True, abort=True):
        other = click.prompt('>>>Hobbies, favourites and obssessions ', type=list)
        click.echo('Password list ready!')

    return(name, surname, nickname, dob, other)


if __name__ == '__main__':
    main()


