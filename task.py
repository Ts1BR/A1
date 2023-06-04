import random

n = random.randint(1,100)

print("Welcome to Number guessing game")

g = int(input("Guess a number from 1 to 100: "))

ng = 1

while g != n:
    if g < n:
        print("Too Low")
        g = int(input(""))
        ng += 1
    elif g> n:
        print("Too High")
        g = int(input(""))
        ng += 1

print("Correct guess,", ng, "trys")
print("The number was", n)