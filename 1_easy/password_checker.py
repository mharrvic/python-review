username = input('what is your username? ')
password = input('what is your password? ')

secret = len(password) * '*'
print(f'{username}, your password {secret}, is {len(password)} letters long ')
