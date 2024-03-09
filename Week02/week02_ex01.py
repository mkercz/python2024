# This script creates a long int number, converts it to a string and counts
# zeros.

number = 25368503460523064863043
str_number = str(number)

print(f"Number of zeros in {number}:", str_number.count('0'))
