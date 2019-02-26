import datetime
import click


@click.command()
@click.option('--fullname', prompt='Enter target\'s fullname',
              help='Target\'s fullname ',
              type=click.STRING)
@click.option('--nickname', prompt='Enter target\'s nickname',
              help='Target\'s nickname')
@click.option('--date_of_birth',
              prompt='Enter target\'s date of birth in this format DDMMYYYY',
              help='Target\'s date of birth')
@click.option('--other',
              prompt="Do you have other info about the target? If 'yes'"
              "provide them. If 'not' just type 'no' ",
              help='Other useful info about the target ie hobbies, likes, etc')
@click.option('--output_file',
              help='The file to write information about the target',
              default='reconnoisance.txt')
def pypass(fullname, nickname, date_of_birth, other, output_file):
    '''
    Command line password cracker based on user provided information
    '''

    try:
        # validate date of birth here
        date_of_birth = datetime.datetime.strptime(date_of_birth, '%d%m%Y')
    except Exception:
        click.echo("Incorrect date of birth format, date should be DDMMYYYY")

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


if __name__ == '__main__':
    pypass()
