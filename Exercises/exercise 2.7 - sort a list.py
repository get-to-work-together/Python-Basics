sentence = 'abacadabra this is a story about a couple of kids walking through the woods'

words = sentence.split()

def how_many_vowels(word):
    return sum([word.count(v) for v in 'aeiou']), word

print( sorted(words, key = how_many_vowels) )

print( sorted(words, key = lambda word: (sum(word.count(v) for v in 'aeiou'), word) ))


