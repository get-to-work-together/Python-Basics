from calendar_functions import is_leapyear

year = int(input('Which year? : '))

if is_leapyear(year):
    print(f'{year} is a leapyear.')
else:
    print(f'{year} is NOT a leapyear.')
