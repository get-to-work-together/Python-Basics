s = 'en eeeen endgh dsfkjhfg kldgfkjhjkl ewter uytu tuy'

words = s.split()

count_e = lambda word: word.lower().count('e')

print(sorted(words, key = lambda word: word.lower().count('k')))
