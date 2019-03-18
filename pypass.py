import click

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


#interactive shell, accepting input from the user
name = str(input('>>>Enter name: '))
surname = str(input('>>>Enter surname: '))
nickname = str(input('>>>Enter nickname: '))
#dob = datetime.datetime(format, '%d%m%Y')
other = str(input('Enter additional info: '))


l = []

pass1 = clean_input(name)
pass2 = clean_input(reverser(name))
l.append(pass1)
l.append(pass2)
    
with open(name + '.txt', 'w+') as passfile:
    for i in l:
        print(i, file=passfile)
print("You file is ready.")



