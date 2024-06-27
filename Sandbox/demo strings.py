s = input('Give me some text please: ')

print('Original:', s)
print('Upper:', s.upper())  
print('Lower:', s.lower())
print('Capitalize:', s.capitalize())
print('Title:', s.title())

print('Ends with a ?', s.endswith('?'))
print('Ends with a ?', s[-1] == '?')

print('Snake case:', s.lower().replace(' ', '_'))
