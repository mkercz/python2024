import periodictable
import itertools  # needed for slicing

# The first part of the script creates a list of code points of the letters
# in "Monika". The second part prints a periodic table of elements (first 10
# elements), I decided to use the periodictable library to obtain the
# information about the elements rather than hardcode them myself.

code_points = [ord(x) for x in "Monika"]
print("Unicode code points for name Monika:", code_points)

periodic_table = [(el.number, el.name, el.symbol, round(el.mass)) for el in
                  itertools.islice(periodictable.elements, 1, 11)]

horizontal_line = "+---+--------------------+------+----------+"
row = "|{:>3}|{:<20}|{:^6}|{:>10}|"

print(horizontal_line)
print(row.format("No.", "Name (en)", "Symbol", "Weight (u)"))
print(horizontal_line)

for pt in periodic_table:
    print(row.format(pt[0], pt[1], pt[2], pt[3]))

print(horizontal_line)
