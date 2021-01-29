import string
import random

print('Hello, please enter the length of the password, a minimum of 6 characters')
length = int(input())

print('How many letters?')
letters = int(input())

print('How many numbers?')
digits = int(input())

punc = length - (letters + digits)
password_letters = string.ascii_letters
password_symbols = string.punctuation
password_digits = string.digits

sample = ''.join((random.choice(password_letters)for i in range(letters)))
sample += ''.join((random.choice(password_digits)for i in range(digits)))
sample += ''.join((random.choice(password_symbols)for i in range(punc)))

sample_list = list(sample)
random.shuffle(sample_list)
password = ''.join(sample_list)

print(password)
