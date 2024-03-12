
'''
#ex1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#ex2   Write a Python program to find out what version of Python you are using.
import sys
print(f"Python version: {sys.version}")

#ex3 current date and time
import datetime

print(f"Current date and time :{datetime.datetime.now()}")

#ex4
import math
radius = float(input("Enter a radius:"))
area = math.pi * (radius**2)
print(f"r = {radius}")
print(f"Area: {area}")

#ex5
f_name =input("enter first name:")
l_name =input("enter last name:")

print(f_name[::-1], l_name[::-1],sep=" ")
#print( l_name[::-1])

#ex 6
numbers =input("enter numbers:")

#first method
t = numbers.replace(',',' ').replace(' ', '')
list = list(t)
print(list)

tuple = tuple(t)
print(tuple)

#2nd method
#list = numbers.split(", ")
#print(list)
#tuple = tuple(t)
#print(tuple)

#ex 7
file_name = input("Enter file name:")
extention = file_name.split(".")
print(f"Extention:{extention[1]}")

#ex 8
color_list = ["Red","Green","White" ,"Black"]
print("%s, %s" %(color_list[0],color_list[-1]))

#ex 9 Write a Python program to display the examination schedule. (extract the date from exam_st_date).

exam_st_date = (11, 12, 2014)

newlist = []
for x in exam_st_date:
    srtt = str(x)
    newlist.append(srtt)
    
print(newlist)
sting = "/".join(newlist)
print(sting)

#2nd method
print("The examination will start from : %i / %i / %i" % exam_st_date)


#ex 10
n = int(input("Enter a number: "))
nn = (n * 10)+n
nnn = (nn * 10)+n
sum = n + nn + nnn
print(sum)

#ex 11. Write a  Python program to print the documents (syntax, description etc.) of Python built-in function(s).

print(sum.__doc__)


#ex12
import calendar
yy = 2024
mm = 1
print(calendar.month(yy, mm)) 


#ex13

#1st method
import datetime

def convert_to_string(date):
    date_str = []
    for x in date:
        date_str.append(str(x))
    return "-".join(date_str)
    
def date_difference_in_days(date_str1, date_str2, date_format='%Y-%m-%d'):

    date1 = datetime.datetime.strptime(date_str1,date_format)
    date2 = datetime.datetime.strptime(date_str2,date_format)
    time_difference = abs((date1 - date2).days)
    return time_difference


date_str1 = convert_to_string((2014, 7, 2))
date_str2 = convert_to_string((2014, 7, 11))

difference_days = date_difference_in_days(date_str1, date_str2)
print(f"Date difference in days: {difference_days}")

#2nd method
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)

delta = l_date - f_date
print(delta.days)


#ex 15
import math
radius = 6
volume = (4/3) * math.pi * radius**3
print(volume)

#ex 16
s_number = 17
g_numder = 5

if g_numder > s_number:
    diff = 2 * abs(s_number - g_numder)
else:
    diff = s_number - g_numder

print(diff)

#ex 17
x = 100
if 100 >= abs(x -1000) or 100 >= abs(x - 2000):
    print("yes")
else:
    print("no")

#ex 19
str = "it snow?"

if str.startswith("Is"):
    print(str)
else:
    new_string = "Is" +" " + str
    print(new_string)

#ex 20
n = 3    
print(n * str)

#ex 21

def even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

number = int(input("Enter a number:"))
even_odd(number)

#ex 22

count = 0
list = [4,4,5,6,4,5,4,4]
str = "".join(map(str, list))

for i in str:
    if i == "4" in str:
        count += 1
    else:
        continue
print(count)

 
#ex 23


def copy(n,str):
    if n >= 0 and len(str) < 2:
        make_copy = str * n
        print(make_copy)
    else:
        make_copy = str[:2] * n
        print(make_copy)
 

word = "Hellp"
copy(4, word)
       
#ex 24
 
vowel_letters = ["a","e",'i','0','u']
letter = input("Enter a letter:")
if letter in vowel_letters:
    print(f"{letter} is a vowel")
        
else:
    print(f"{letter} is not  a vowel")
        
'''
#ex 25
    
def check(group, value):
    for i in group:
        if value == i:
            return True
    return False
            

print(check([1, 5, 8, 3], 5))
