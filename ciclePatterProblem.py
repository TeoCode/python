# Place 2 or plus points on a circumference, calculate the amount of regions created by the lines created by the points.
# Knowing that the first 5 points create a number of regions which is a power of 2,
# find all the others numbers of points that give a number of regions which is a power of 2 too.
# Inspired by https://www.youtube.com/watch?v=YtkIWDE36qU&ab_channel=3Blue1Brown

import math


# Function to calculate the factorial of a number
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


# Alternative function to calculate the factorial of a number
def factorial2(n):
    fact = 1
    for j in range(1, n+1):
        fact = fact * j
    return fact


# Function to calculate all the combinations of n items over k slots
def choose(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))


# Alternative function of "choose"
def choose2(n, k):
    return int(factorial2(n) / (factorial2(k) * factorial2(n - k)))


# Function to calculate the number of faces
def faces(n):
    return 1 + choose(n, 2) + choose(n, 4)


# Alternative function of "faces"
def faces2(n):
    return 1 + choose2(n, 2) + choose2(n, 4)

# Testing arguments
# points = int(input("Insert the number of points: "))
# print(faces(points))


# Function to find all the numbers that are a power of 2
def find2powers(it):
    values = []
    for i in range(it):
        if math.log2(faces(i)) % 1 == 0:
            values.append((i, faces(i)))
    return values


# Alternative function of "find2powers"
def find2powers2(it):
    values = []
    for i in range(it):
        if math.log2(faces2(i)) % 1 == 0:
            values.append((i, faces2(i)))
    return values


# Main function WARNING: do not insert really high numbers!
it = int(input("Insert the number of iterations: "))

# Testing arguments
# f = int(input("Insert which function you want to use: "))
# if f == 1:
#     print(find2powers(it))  # For small numbers
# elif f == 2:
#     print(find2powers2(it))  # For medium numbers
# else:
#    print("Not a valid number!")

try:
    result = find2powers(it)
except:
    print("Error Found! Trying alternative calculation method...")
    result = find2powers2(it)
print(result)