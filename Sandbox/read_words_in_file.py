
filename = r'data.txt'

f = open(filename)
text = f.read()
f.close()

print(text)

# text = text.lower().\
#            replace('.', '').\
#            replace(',', '').\
#            replace(':', '').\
#            replace(')', '').\
#            replace('(', '').\
#            replace('"', '').\
#            replace('\'', '')

text = text.lower().translate(str.maketrans('', '', '.,:()!?[]"'))

words = text.split()

unique_words = set(words)

d = dict()
for word in unique_words:
    n = words.count(word)
    d[word] = n

for k, v in sorted(d.items()):
    print(f'{k:30}: {v:4}')
