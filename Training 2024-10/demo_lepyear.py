
def leapyear(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0



year = int(input('Which year? : '))
print(year, leapyear(year))


import calendar

print(year, calendar.isleap(year))
