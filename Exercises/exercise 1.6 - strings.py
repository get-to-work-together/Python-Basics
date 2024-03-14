s = input('Give me some text please: ')

print('Original:', s)

print('Upper:', s.upper())
print('Lower:', s.lower())
print('Capitalize:', s.capitalize())
print('Title:', s.title())

print('First three characters:', s[:3])

print('Ends with a ?:', s.endswith('?'))
print('Ends with a ?:', s[-1] == '?')
print('Has a ?:', '?' in s)

print('Snake case:', s.lower().replace(' ', '_'))

print('Kebab case:', s.lower().replace(' ', '-'))
print('Pascal case:', s.title().replace(' ', ''))
print('Camel case:', s[0].lower() + s.title().replace(' ', '')[1:])
print('Screaming case:', s.upper().replace(' ', '_'))
