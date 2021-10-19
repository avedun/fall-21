# A year in the modern Gregorian Calendar consists of 365 days. In reality, the earth
# takes longer to rotate around the sun. To account for the difference in time, every 4 years,
# a leap year takes place. A leap year is when a year has 366 days: An extra day, February 29th.
# The requirements for a given year to be a leap year are:

# 1) The year must be divisible by 4
# 2) If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400

# Some example leap years are 1600, 1712, and 2016.
# 1900 is NOT a leap year (not evenly divisible by 400)
# Write a program that takes in a year and determines whether that year is a leap year.

is_leap_year = False
year_input = int(input())

print(year_input, end='')

if year_input % 100 == 0:
    if year_input % 400 == 0:
        is_leap_year = True
elif year_input % 4 == 0:
    is_leap_year = True

if is_leap_year == True:
    print(' - leap year')
else: #False
    print(' - not a leap year')