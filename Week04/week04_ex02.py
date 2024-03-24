# This script creates a list of integers from 0 to 15, then creates a function
# that reverses a part of the list (from index 5 to 10), then uses this
# function and prints the result. Iterative and recursive methods are used.

def reverse_range_it(L, left, right):
    while left < right:
        temp_element = L[left]
        L[left] = L[right]
        L[right] = temp_element
        left += 1
        right -= 1


def reverse_range_rec(L, left, right):
    if left < right:
        temp_element = L[left]
        L[left] = L[right]
        L[right] = temp_element
        reverse_range_rec(L, left + 1, right - 1)


L1 = [x for x in range(16)]
L2 = L1[:]
reverse_range_it(L1, 5, 10)
print("Iterative method:", L1)
reverse_range_rec(L2, 5, 10)
print("Recursive method:", L2)