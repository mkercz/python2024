# Explain the results.

x = 5
x == 5 and 3 + 8   # 11 -- it returns 3+8 because "and" works in the
# following way: if the left part is true, then the right part is returned
x == 4 and 3 + 8   # False -- now the left part is false, so it returns false,
# right part is not even checked
3 + 8 and x == 5   # True -- left part is true (because it is not equal to 0)
# so the right part is returned (it's true)
3 + 8 and x == 4   # False -- left part is true so the right part is returned
# (it's false)

isinstance(True, int)    # True -- True is of a bool type, which in python is
# a subclass of int
isinstance(True, bool)   # True -- True is of a bool type
