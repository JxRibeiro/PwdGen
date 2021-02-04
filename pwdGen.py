import string
import random


pwdUpper = string.ascii_uppercase #Letras maiusculas ABC...
pwdLower = string.ascii_lowercase #Letras minusculas abc...
pwdDigits = string.digits #Numeros 0123456789
pwdPunc = string.punctuation #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


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
pwdChars = pwdEscolha
#pwdChars = string.ascii_letters + string.digits + string.punctuation
pwd = []
if pwdEscolha == '1':
    pwdChars = pwdUpper
if pwdEscolha == '2':
    pwdChars = pwdLower
if pwdEscolha == '3':
    pwdChars = pwdDigits
if pwdEscolha == '4':
    pwdChars = pwdPunc

if pwdEscolha == '12':
    pwdChars = pwdUpper + pwdLower
if pwdEscolha == '123':
    pwdChars = pwdLower + pwdUpper + pwdDigits
if pwdEscolha == '1234': 
    pwdChars = pwdDigits + pwdLower + pwdUpper + pwdPunc
if pwdEscolha == '134': 
    pwdChars = pwdDigits + pwdLower + pwdPunc
if pwdEscolha == '13': 
    pwdChars = pwdDigits + pwdUpper
if pwdEscolha == '14': 
    pwdChars = ppwdUpper + pwdPunc
if pwdEscolha == '234': 
    pwdChars = pwdDigits + pwdLower  + pwdPunc
if pwdEscolha == '23': 
    pwdChars = pwdDigits + pwdLower
if pwdEscolha == '24': 
    pwdChars = pwdLower + pwdPunc
if pwdEscolha == '34': 
    pwdChars = pwdDigits + pwdPunc









for i in range(tam):
    pwd.append(random.choice(pwdChars))
print(''.join(pwd))


