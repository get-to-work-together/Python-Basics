
s = 'Summer is the hottest of the four temperate seasons, falling after spring and before autumn. At or around the summer solstice (about 3 days before Midsummer Day), the earliest sunrise and latest sunset occurs, the days are longest and the nights are shortest, with day length decreasing as the season progresses after the solstice. The date of the beginning of summer varies according to climate, tradition, and culture.'

s = s.lower().replace('.', '').replace(',', '').replace('(','').replace(')', '')

words = s.split()

unique_words = set(words)

d = dict()
for word in unique_words:
    d[word] = words.count(word)

for word, count in sorted(d.items()):
    print(f'{word:30} : {count:5}')
