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


if __name__ == '__main__':
    pypass()
