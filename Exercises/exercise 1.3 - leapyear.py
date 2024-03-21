user_input = input('Give a year: ')

year = int(user_input)

is_leapyear = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

print(year, is_leapyear)

if is_leapyear:
    print(f'{year} is a leapyear')

else:
    print(f'{year} is NOT a leapyear')
































# can_divide_by_4 = year % 4 == 0
# can_divide_by_100 = year % 100 == 0
# can_divide_by_400 = year % 400 == 0
#
# is_leapyear = can_divide_by_4 and \
#               not can_divide_by_100 or \
#               can_divide_by_400
#
# if is_leapyear:
#     print(year, 'is a leapyear')
# else:
#     print(year, 'is NOT a leapyear')
