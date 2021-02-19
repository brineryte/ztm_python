from getpass import getpass

print('Login')
print()
user = input('Please enter user name')
password = getpass(prompt='Please enter password', stream=None)

print(f'{user}, your password {password} is {len(password)} letters long')
