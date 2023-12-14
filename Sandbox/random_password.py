import random
import string

upper = random.choices([c for c in string.ascii_uppercase if c not in 'O'], k = random.randint(2, 5))
lower = random.choices([c for c in string.ascii_lowercase if c not in 'l'], k = random.randint(2, 5))
digits = random.choices(string.digits, k = random.randint(2, 5))
special = random.choices([c for c in string.punctuation if c not in '`\'"()[]'], k = 1)

# print(upper)
# print(lower)
# print(digits)
# print(special)

all_characters = upper + lower + digits + special

random.shuffle(all_characters)

# print(all_characters)

password = ''.join(all_characters)

print('Your new password is', password)