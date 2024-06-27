import random
import string

minimum_length = 8
n_lowercase = 3
n_uppercase = 3
n_numbers = 2
n_special = 1
n_extra = max(0, minimum_length - n_lowercase - n_uppercase - n_numbers - n_special)

# LOWERCASE_CHARACTERS = string.ascii_uppercase
# UPPERCASE_CHARACTERS = string.ascii_lowercase
# NUMBER_CHARACTERS = string.digits
# SPECIAL_CHARACTERS = string.punctuation

# or

LOWERCASE_CHARACTERS = 'abcdefghijkmnopqrstuvwxyz'  # removed l
UPPERCASE_CHARACTERS = 'ABCDEFGHJKLMNPQRSTUVWXYZ'  # removed I and O
NUMBER_CHARACTERS = '0123456789'
SPECIAL_CHARACTERS = '@#$%&*+?!{}'

EXTRA_CHARACTERS = LOWERCASE_CHARACTERS + UPPERCASE_CHARACTERS + NUMBER_CHARACTERS

lowercase = random.choices(LOWERCASE_CHARACTERS, k = n_lowercase)
uppercase = random.choices(UPPERCASE_CHARACTERS, k = n_uppercase)
numbers = random.choices(NUMBER_CHARACTERS, k = n_numbers)
special = random.choices(SPECIAL_CHARACTERS, k = n_special)
extra = random.choices(EXTRA_CHARACTERS, k = n_extra)

all_characters = lowercase + uppercase + numbers + special + extra

random.shuffle(all_characters)

password = ''.join(all_characters)

# or

# shuffled = random.sample(all_characters, k = len(all_characters))
#
# password = ''.join(shuffled)

print('New password:', password)





# import secrets
#
# lowercase = ''.join(secrets.choice(LOWERCASE_CHARACTERS) for _ in range(n_lowercase))
# uppercase = ''.join(secrets.choice(UPPERCASE_CHARACTERS) for _ in range(n_uppercase))
# numbers = ''.join(secrets.choice(NUMBER_CHARACTERS) for _ in range(n_numbers))
# special = ''.join(secrets.choice(SPECIAL_CHARACTERS) for _ in range(n_special))
# extra = ''.join(secrets.choice(EXTRA_CHARACTERS) for _ in range(n_extra))
#
# all_characters = lowercase + uppercase + numbers + special + extra
#
# random.shuffle(all_characters)
#
# password = ''.join(all_characters)
#
# print('New password: ', password)
