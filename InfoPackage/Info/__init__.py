class id():
    number = 12345
    name = 'Prince'
    birthday = '05/09/1990'
    password = 'Prince08*'


#print(f'id: {id.number}')
#print(f'id: {id.name}')
#print(f'id: {id.birthday}')
#print(f'id: {id.password}')


def login():
    User = input('Name: ')
    Password = input('Password: ')

    if User == id.name.lower() and Password == str(id.password):
        print('Your in!')
    else:
        print('That is incorrect!')
        return login()

__version__ = 'dev'
 name = “Zinfo”
