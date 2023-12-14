gender = 'm'
age = 43

if gender == 'm':
    if age < 21:
        print('boy')
    else:
        print('man')
elif gender == 'f':
    if age < 21:
        print('girl')
    else:
        print('woman')
else:
    print('other')

print('done')


# print( 'sir' if gender.lower() == 'm' else 'madam' )
