import re

s = '1,4,3.7.8,9'
print(re.split(r',\.', s))


s = 'jdshkf ksdjhf, sdfkh. peter@tip.nl dkfhsdkjfhsdkfjh, peter@asml.cm sdfsdfsdfwefsd'

regex = r'(\w+@\w+\.\w{2,3})'

matches = re.findall(regex, s)

if matches:
    print(matches)
else:
    print('Nothing found.')