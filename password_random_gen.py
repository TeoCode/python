import random

print('''
Generatore Di Password Casuali
==============================
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('Numero di password da generare: ')
number = int(number)

length = input('Lunghezza di ogni password: ')
length = int(length)

print('\nEcco le tue password:')
print(" ")

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)

print(" ")
wait = input("Premi un tasto per uscire")
print("Closing...")