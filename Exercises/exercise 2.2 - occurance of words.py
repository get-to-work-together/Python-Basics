import string

s = r"""Microchips go by many names: integrated circuits, semiconductor chips, 
computer chips or, most simply, chips. Whatever you call them, these tiny pieces of 
silicon are the foundation of the digital world. They make our smartphones, cars, 
medical equipment and so many other now-common devices possible – and the tinier they get, 
the more advanced technology we realize in the everyday world. 
They may be small, but their impact is tremendous."""

s = s.lower().translate(str.maketrans('áäâàéëêèíïìîóöôòúüûù',
                                      'aaaaeeeeiiiioooouuuu',
                                      string.punctuation))

print(s)

words = s.split()
print(words)

unique_words = set(words)
print(unique_words)

d = dict()
for word in unique_words:
    d[word] = words.count(word)
print(d)

for word, n in sorted(d.items()):
    print(f'{word:25}: {n:3} {"*" * n}')













# for word, n in sorted(d.items(), key = lambda item: item[1], reverse=True):
#    print(f'{word:20}: {n:3} {"*" * n}')








# # or with a dict comprehension
# d = {word: words.count(word) for word in set(words)}

# for word, n in sorted(d.items()):
#     print(f'{word:20}: {n:3} {"*" * n}')

# from operator import itemgetter
# for word, n in sorted(d.items(), key = itemgetter(1, 0), reverse = True):
#    print(f'{word:20}: {n:3}')

# for word, n in sorted(d.items(), key = lambda item: item[1], reverse=True):
#    print(f'{word:20}: {n:3} {"*" * n}')

# def get_values(item):
#     return item[1]
#
# for word, n in sorted(d.items(), key=get_values, reverse=True):
#     # print(word, n)
#     # print('%-25s: %3d' % (word, n))
#     print(f'{word:<25}: {n:3}')
#     # or
#     print('%-15s: %3d %s' % (word, n, '*' * n))



# # or with collection.Counter
# from collections import Counter
# d = Counter(s.lower().translate(str.maketrans('', '', string.punctuation)).split())
# print(d)
