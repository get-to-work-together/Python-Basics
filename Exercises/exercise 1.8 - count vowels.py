s = input('Give some text: ')

number_of_a = s.lower().count('a')
number_of_e = s.lower().count('e')
number_of_i = s.lower().count('i')
number_of_o = s.lower().count('o')
number_of_u = s.lower().count('u')
number_of_y = s.lower().count('y')

number_of_vowels = (number_of_a +
                    number_of_e +
                    number_of_i +
                    number_of_o +
                    number_of_u +
                    number_of_y)

print("Found the vowel 'a' %d times" % number_of_a)
print("Found the vowel 'e' %d times" % number_of_e)
print("Found the vowel 'i' %d times" % number_of_i)
print("Found the vowel 'o' %d times" % number_of_o)
print("Found the vowel 'u' %d times" % number_of_u)
print("Found the vowel 'y' %d times" % number_of_y)

print("Total number of characters: %d" % len(s))

print("Total number of non-whitespace characters: %d" % len(s.replace(' ', '')))

print("Total number of vowels: %d" % number_of_vowels)











# number_of_vowels = 0
#
# for vowel in 'aeiouy':
#   n = s.count(vowel)
#   number_of_vowels += n
#
#   print(f'The vowel {vowel} occurs {n} times.')
#
# print(f"Total number of characters: {len(s)}")
# print(f"Total number of vowels: {number_of_vowels}")
