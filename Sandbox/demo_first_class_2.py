
s = """It is still a beautiful day outside 
Character or regex pattern to treat as the delimiter. If sep=None, the C engine cannot automatically detect the separator, but the Python parsing engine can, meaning the latter will be used and automatically detect the separator from only the first valid row of the file by Python’s builtin sniffer tool, csv.Sniffer. In addition, separators longer than 1 character and different from '\s+' will be interpreted as regular expressions and will also force the use of the Python parsing engine. Note that regex delimiters are prone to ignoring quoted data. Regex examp"""

words = s.split()

def number_of_vowels(s):
    n = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
    return n

lambda s: s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')


for word in sorted(words, key = lambda s: s.count('e')):
    print(word)