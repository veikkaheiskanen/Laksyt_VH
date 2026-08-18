import random

first_code = random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)
second_code = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)

print(f"{first_code[0]}{first_code[1]}{first_code[2]}")
print(f"{second_code[0]}{second_code[1]}{second_code[2]}{second_code[3]}")