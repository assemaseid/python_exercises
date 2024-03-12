
'''
#ex 26 Write a  Python program to create a histogram from a given list of integers.

intrgers = [4,5,2,9]
symbol = "*"
for i in intrgers:
    print(symbol*i)

#ex 27 Write a Python program that concatenates all elements in a list into a string and returns it.
def to_string(list_1):
    string = ''
    for i in list_1:
        string += str(i)
    print(string)


to_string(["apple", "banana", "cherry"])
to_string([1, 5, 7, 9, 3])

#ex 28
#Write a Python program to print all even
#numbers from a given list of numbers in the same order
#and stop printing any after 237 in the sequence.
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
even_numbers = []
for i in numbers:
    if i == 248:
        break
    elif i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)

#ex 29
# Write a  Python program that prints out all colors from color_list_1 that are not present in color_list_2.

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1 - color_list_2)


#ex 31

import math
print(math.gcd(6,3))
print(math.lcm(5,6))

#33
a = 10
b = 5
c = 5

sum = a+b+c
if a == b or b == c or a == c:
    sum = 0

print(sum)

#34
a = 10
b = 11

sum = a+b
if sum in range(15,20):
    sum = 20
print(sum)

#35

a = 5
b = 10
if a == b or a+b == 5 or abs(a-b) == 5:
    print(True) 
else:
    print(False)

#36

a = 5
b = 10.3

if a == int(a) and b == int(b):
#methos 2
#def add_numbers(a, b):
#    if not (isinstance(a, int) and isinstance(b, int)):
       # return "Inputs must be integers!"
#    return a + b
    sum = a+b
    print(sum)
else:
    print(False)

#38
    
x = 4
y = 3
sq = (x + y) **2
print(f"({x} + {y}) ^ 2 = {sq}")

#39
# Write a  Python program to compute the future value of
# a specified principal amount, rate of interest, and number of years.
amt = 10000
int = 3.5
years = 7
for i in range(1,8):
    future = (amt * 103.5) / 100
    #2nd method
    #  future = amt * (1 + int/100)
    amt = future
print(future)

#40Write a  Python program to calculate the distance between the points (x1, y1) and (x2, y2).

(x1, y1) = (4 , 0)
(x2, y2) = (6 , 6)

d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(d)

#41
import os
if os.path.exists("//Users//assemseidkarim//Desktop//python_exercises//pythonex //Basic-Part-1//ex 50-75.py"):
    print("Exists" )
else:
    print("does not Exist" )

#2nd method
    # Import the os.path module to work with file and directory paths.
import os.path

# Check if 'main.txt' is a file and print the result.
print(os.path.isfile('main.txt'))

# Check if 'main.py' is a file and print the result.
print(os.path.isfile('main.py'))

#43
# Import the 'site' module.
import site

# Use the 'site.getsitepackages()' function to retrieve site packages' paths.
# 'site.getsitepackages()' returns a list of paths where site packages are installed.
print(site.getsitepackages())
'''
#48
str = "28303"
fl = float(str)
intr = int(str)
print(fl)
print(intr)

#49
import os 
path = "//Users/assemseidkarim//Desktop//PP_2//Practice//lab 6"
os.chdir(path)
print(os.listdir(path))

#50 Write a Python program to print without a newline or space.
# Iterate through a range of numbers from 0 to 9 (inclusive).
for i in range(0, 10):
    # Print an asterisk '*' character on the same line using the 'end' parameter.
    print('*', end="")
# Print a newline character to move to the next line.
print("\n")
