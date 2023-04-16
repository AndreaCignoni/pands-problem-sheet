# Es program
# The text file is a plain text file and not a binary file
# This program rads in a text file and outputs
# the number of 'e' it contains
# Filename taken from an argument on the command line
# The program should count both uppercase and lower case,
# or as part of a word or string.


# Using sys.argv module to access command line arguments in a list
import sys
# Get the filename from the command line arguments
anneOfGG = sys.argv[1]

# Open the file for reading
with open(anneOfGG, 'r', encoding="utf-8") as f:
    # Initialize a counter for the number of e's found
    content = f.read()
    e_count = 0
    # Loop over each line in the file
    for line in f:
        # Loop over each character in the line
        for char in line:
            # Check if the character is 'e' (case-insensitive) and increment the counter if it is
            if char.lower() == 'e':
                e_count += 1

# Output the final count of e's found
print("E Count: ", e_count)