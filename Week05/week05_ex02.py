# This script firstly takes two dates from a user (as strings) and parses
# them into datetime objects. Then a function called print_working_days takes
# the dates and checks how many working days are between them (the second
# date is excluded). Finally, the function is executed in main and the result is
# printed.

import datetime
import sys

date1_str = input("Enter the first date (YYYY-MM-DD): ")
date2_str = input("Enter the second date (YYYY-MM-DD): ")

date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")

if date1 >= date2:
    print("The second date needs to be larger than the first date!")
    sys.exit()


def print_working_days(d1, d2):
    date_range = d2 - d1
    delta = datetime.timedelta(days=1)

    workingdays_count = 0

    while d1 < d2:
        if d1.weekday() < 5:
            workingdays_count += 1
        d1 += delta

    return workingdays_count


result = print_working_days(date1, date2)

print("The number of working days between {} and {} is {}".format(date1,
                                                                  date2,
                                                                  result))
