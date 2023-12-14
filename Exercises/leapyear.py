
def is_leapyear(year):
    """Determine if a year is a leapyear"""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# -----------------------------------------------------------------

year = int(input('Which year? : '))
print(year, is_leapyear(year))

##for year in range(year, year + 101):
##    print(year, is_leapyear(year))

from calendar import isleap
print(year, isleap(year))



