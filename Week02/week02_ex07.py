# This script creates dictionaries with mapping of certain strings (Roman
# numerals) to Arabic numerals. First method is to define a list with keys
# and a list with values and then use zip to create a dictionary. Second
# method is to use dict comprehension.

dict_1_key = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM",
              "M"]
dict_1_val = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

dict_1 = dict(zip(dict_1_key, dict_1_val))

print("Items in the first dictionary:", dict_1.items())

dict_2 = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50,
          "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}

print("Items in the second dictionary:", dict_2.items())
