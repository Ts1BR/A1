import random
# math.abs()
# math.pow(10, -5)
x = float(input("Write a number: "))
g = random.randint(1, x-1)

while abs(x - g*g) > 1e-5:
    g = (g + x/g) /2

print(g)