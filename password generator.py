import random
chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#*¥$€<>~"
length=int(input("enter the length of a password"))
password=""

for i in range(length):
    password+=random.choice(chars)
print(password)