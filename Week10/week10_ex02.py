# This scripts reads a JSON file containing days of a current month and
# temperatures at noon, then it creates a pandas series where the dates are
# the indices and the temperatures are the data.

import pandas as pd
import json
import numpy as np

with open("temperatures.json", "r") as file:  # no need to close the file
    data_from_file = json.load(file)

index_str = [item["date"] for item in data_from_file["data"]]
temp = [item["temperature"] for item in data_from_file["data"]]

index_date = np.array(index_str, dtype="datetime64")  # converting to np.array
# containing np.datetime64 (the dates are read from the JSON file as strings)

temperature_series = pd.Series(temp, index_date, name="Temperatures at noon in "
                                                      "May 2024")

print(temperature_series)

# just a check to be sure that index_date contains np.datetime64
print("Type of elements in index:", type(index_date[0]))
