# This script creates variables, saves them to a text file and prints them.

import math

n = 2022
x = round(math.pi, 5)
word = "Python"
polish = "książka"

with open('vars.txt', 'w') as outfile: # w for writing
    outfile.write("{}\n{}\n{}\n{}".format(n, x, word, polish))

with open('vars.txt', 'r') as infile: # r for reading
    text = infile.read()

print(text)