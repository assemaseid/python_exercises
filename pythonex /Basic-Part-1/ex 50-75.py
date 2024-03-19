'''
#57
import time

def sum_of_n_numbers(n):
    start_time = time.time()

    s = 0
    for i in range(1, n + 1):
        s = s + i

    end_time = time.time()

    return s, end_time - start_time

n = 5
print("\nTime to sum of 1 to", n, "and required time to calculate is:", sum_of_n_numbers(n))

#58

def sum_of_n_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i


    return sum

n = 3
print(f"sum_of_n_numbers {sum_of_n_numbers(n)}")
'''
#68
def sum_of_digits(n):
    string = str(n)
    sum = 0
    for i in range(0,len(string)):
        nol = 10 ** i
        s = n // nol

        num = s % 10
        print(num)
        sum += num

    return sum

n = 3468
print(f"sum_of_digits {sum_of_digits(n)}")

#ex 70 Write a Python program to sort files by date.


# Import the necessary libraries to work with file operations and globbing.
import glob
import os

# Use the glob module to find all files in the current directory with a ".txt" extension.
files = glob.glob("*.py")

# Sort the list of file names based on the modification time (getmtime) of each file.
files.sort(key=os.path.getmtime)

# Print the sorted list of file names, one per line.
print("\n".join(files))

#73
# Create a list that maps characters to their Soundex codes.
soundex = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]

# Prompt the user to input the word to be hashed.
word = input("Input the word to be hashed: ")

# Convert the input word to uppercase.
word = word.upper()

# Initialize the coded word with the first character of the input word.
coded = word[0]

# Iterate over the remaining characters in the word to calculate the Soundex code.
for a in word[1:len(word)]:
    # Calculate the index for the Soundex list based on the character's ASCII code.
    i = 65 - ord(a)
    coded = coded + str(soundex[i])

# Print a blank line.
print()

# Display the coded word.
print("The coded word is: " + coded)

# Print a blank line.
print()
