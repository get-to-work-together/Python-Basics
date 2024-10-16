
words = 'the brown fox jumped over the lazy dog looping and scooping'.split()

print(words)
print(sorted(words))
print(sorted(words, reverse=True))

print(sorted(words, key=len))
print(sorted(words, key=len, reverse=True))

print(sorted(words, key=lambda word: word.count('e'), reverse=True))

print(sorted(words, key=lambda word: sum(word.count(v) for v in 'aeiou'), reverse=True))
