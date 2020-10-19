import random
import time
chars1='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chars2 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


print('Welcome to the random password generator')
length = input('How much characters would you like your password to be? ')
length = int(length)
number = input ('How many passwords would you like to generate? ')
number = int(number)

xe = input('Would you like to have numbers in your password? yes/no ').lower()
print('Here is a list of passwords generated')
if xe == 'yes':
  for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars1)
    print(password)
elif xe == 'no':
    for p in range(number):
       password = ''
       for c in range(length):
           password += random.choice(chars2)
       print(password)

time.sleep(20)


