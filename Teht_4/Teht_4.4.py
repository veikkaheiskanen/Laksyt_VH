import random

cor_num = random.randint(1, 10)

guess = 0

while guess != cor_num:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < cor_num:
        print("Liian pieni arvaus")
    elif guess > cor_num:
        print("Liian suuri arvaus")
    else:
        print("Oikein")
