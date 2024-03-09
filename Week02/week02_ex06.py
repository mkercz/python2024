# Find and explain the results.

t = (2, 4) # type(t) returns "<class 'tuple'>" which means that t is a tuple
print(t[2]) # it returns "tuple index out of range" because indices start at 0
# print(t[0]) returns 2 and print(t[1]) returns 4
t.append(6) # it returns "'tuple' object has no attribute 'append'" because
# size of a tuple is fixed when we create it, so we can't add more elements
a, b = t ; print(a, b) # it creates a tuple in which the first element is a
# and the second element is b, so print(a,b) returns (2,4)
