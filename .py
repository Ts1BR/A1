# radius = int(input("Enter the radius of the circle: "))

# pi = 3.141592657

# # area = pi*(radius * radius)
# area = pi*(radius ** 2)

# print("The area of the cirlce is: ")
# print(area)

# width = int(input("Enter the width of the rectangle: "))
# length = int(input("Enter the length of the rectangle: "))

# area = width * length

# print("The area of the rectangle is: " + str(area))

# num = input("Enter a whole number: ")

# try:
#     num = int(num)
#     if num % 2 == 0:
#         print("The number is even")
#     else:
#         print("The number is odd")
# except ValueError:
#     print("That is not a integer")

# x = 1

# print(x)

# x_str = str(x)

# print("my fav num is", x, ".", "x =", x)
# print("my fav num is " + x_str + ". " + "x = " + x_str)

# x = input("Write something: ")

# if x != "sum" or x != "factorial":
#     print("thanks")
# if x == "sum":
#     n = int(input("Write an integer: "))
#     print(1+2+3+n)
# if x == "factorial":
#     n = int(input("Write an integer: "))
#     print(1*2*3*n)


# if x != "sum" or x != "factorial":
#     print("thanks")
# if x == "sum":
#     n = int(input("Write an integer: "))
#     sum = 0
#     for i in range(1, n+1):
#         sum = i + sum    # sum += i
#     print("Sum of operations: ", sum)
# elif x == "factorial":
#     n = int(input("Write an integer: "))
#     factorial = 1
#     for i in range(1, n+1):
#         factorial = i * factorial   # factorial *= i
#     print("factorial of operations: ", factorial)
# else:
#     print("thanks")


n = int(input("Write an integer: "))

# if n > 0:
#     i, sum = 1, 0
#     while i <= n:
#         sum = sum +i
#         i += 1
#     print("the number you entered is positiive.")
#     print("the sum from 1 to n is:", sum)

# elif n < 0:
#     i, sum = -1, 0
#     while i >= n:
#         sum = sum +i
#         i += -1
#     print("the number you entered is negative.")
#     print("the sum from -1 to n is:", sum)

# else:
#     print("You entered zero")

# if n > 0:
#     i, sum = 1, 0
#     for i in range (1, n):
#         sum = sum +i
#     print("the number you entered is positiive.")
#     print("the sum from 1 to n is:", sum)

# elif n < 0:
#     i, sum = -1, 0
#     for i in range (-1, n, -1):
#         sum = sum +i
#     print("the number you entered is negative.")
#     print("the sum from -1 to n is:", sum)

# else:
#     print("You entered zero")

''' CHECK IF THE NUMBER INPUT IS PRIME OR NOT '''

if n == 3 and n%2 == 0 or n%4 == 0:
    print("The number is not prime")
elif n == 2 and n%3 == 0 or n%4 == 0:
    print("The number is not prime")
elif n > 3 and n%2 == 0 or n%3 == 0 or n%4 == 0:
    print("The number is not prime")
else:
    print("The number is prime")

########### CHECK IF THE NUMBER INPUT IS PRIME OR NOT ###########
########### IF THE NUMBER IS DIVISIBLE BY 2 OR 3 OR 4 OR 5 IT IS NOT PRIME ###########
########### USE LOOP ###########