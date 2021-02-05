import string
import random

pwdUpper = string.ascii_uppercase #Letras maiusculas ABC...
pwdLower = string.ascii_lowercase #Letras minusculas abc...
pwdDigits = string.digits #Numeros 0123456789
pwdPunc = string.punctuation #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
pwdTest = []
print('##########################')
print('#   Gerador de senhas    #')
print('#------------------------#')
print('#    Escolha os tipo     #')
print('#------------------------#')
print('# (1) Letras maiusculas  #')
print('# ABCDEFGHIJKLMNOPQR...  #')
print('# (2) Letras minusculas  #')
print('# abcdefghijklmnopqr...  #')
print('# (3) Números            #')
print('# 0123456789             #')
print('# (4) Pontuação          #')
print('# !#$%&''()*+,-./:;<=....  #')
print('##########################')

pwdEscolha = input('Digite sua escolha (ex 123 ou 124):\n')
tam = int(input('Qual o tamanho da senha? \n'))

pwdChars = ''
pwd = []
escPwd = []
if '1' in pwdEscolha:
    pwdChars = pwdChars + pwdUpper
if '2' in pwdEscolha:
    pwdChars = pwdChars + pwdLower
if '3' in pwdEscolha:
    pwdChars = pwdChars + pwdDigits
if '4' in pwdEscolha:
    pwdChars = pwdChars + pwdPunc

for i in range(tam):
      pwd.append(random.choice(pwdChars))
print(''.join(pwd))
