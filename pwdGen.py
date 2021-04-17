import string
import random

pwdUpper = string.ascii_uppercase #Upper letters ABC...
pwdLower = string.ascii_lowercase #Lower letters abc...
pwdDigits = string.digits #Numbers 0123456789
pwdPunc = string.punctuation #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

print('###########################')
print('#   Password Generator    #')
print('#-------------------------#')
print('#    Choose complexity    #')
print('#-------------------------#')
print('# (1) Upper Letters       #')
print('# ABCDEFGHIJKLMNOPQRS...  #')
print('# (2) Lowe Letters        #')
print('# abcdefghijklmnopqrs...  #')
print('# (3) Numbers             #')
print('# 0123456789              #')
print('# (4) Punctuation         #')
print('# !#$%&''()*+,-./:;<=...    #')
print('###########################')

choice = input('Enter with complexity (12 or 124): ')
size = int(input('Size: '))

pwdChars = ''
pwd = []
if '1' in choice:
    pwdChars = pwdChars + pwdUpper
if '2' in choice:
    pwdChars = pwdChars + pwdLower
if '3' in choice:
    pwdChars = pwdChars + pwdDigits
if '4' in choice:
    pwdChars = pwdChars + pwdPunc

for i in range(size):
      pwd.append(random.choice(pwdChars))
print(''.join(pwd))

