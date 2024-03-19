#82

tuple = (1,2,3,4,4,5)
list = list(tuple)
set = set(tuple)

thisdict = {
  "a": 5,
  "b": 4,
  "c": 1
}
sum = 0
for i in tuple:
    sum += i
print(sum)

num_sum = 0

for i in thisdict:
    num_sum  += thisdict[i]
print(num_sum)

#86 Write a Python program to get the ASCII value of a character
# Print a newline character for spacing.
print()

# Print the Unicode code point of the character 'a'.
print(ord('a'))

# Print the Unicode code point of the character 'A'.
print(ord('A'))

# Print the Unicode code point of the character '1'.
print(ord('1'))

# Print the Unicode code point of the character '@'.
print(ord('@'))

# Print a newline character for spacing.
print()

#87 Write a Python program to get the size of a file.
# Import the os module for file operations.
import os
# Get the size of the file "abc.txt".
file_size = os.path.getsize("abc.txt")
# Print the size of the file "abc.txt" in bytes.
print("\nThe size of abc.txt is:", file_size, "Bytes")
# Print a newline character for spacing.
print()

#98 Write a  Python program to get system time.

#Note : The system time is important for debugging, 
#network information, random number seeds, 
#or something as simple as program performance.

# Import the 'time' module to work with time-related functions.
import time

# Print an empty line for formatting.
print()

# Get and print the current time using 'time.ctime()'.
print(time.ctime())

# Print an empty line for formatting.
print()
