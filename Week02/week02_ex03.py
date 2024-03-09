# This script calculates the sum of 1*1 + 3*3 + 5*5 + ... + 2021*2021

my_sum = sum(x*x for x in range(1,2022,2))
print("Sum:", my_sum)
