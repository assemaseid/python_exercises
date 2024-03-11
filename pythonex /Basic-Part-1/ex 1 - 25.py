
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
'''