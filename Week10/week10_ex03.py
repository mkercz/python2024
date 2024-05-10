# This script creates a pandas dataframe for ten first elements in the periodic
# table. The data are obtained from the periodictable library.

import periodictable
import itertools  # needed for slicing
import pandas as pd

elements = [(el.name, el.symbol, round(el.mass)) for el in
            itertools.islice(periodictable.elements, 1, 11)]

periodic_table = pd.DataFrame(elements, columns=["Name", "Symbol", "Weight"],
                              index=range(1, 11))

print(periodic_table)