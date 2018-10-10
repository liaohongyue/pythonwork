import re

p=re.compile('(a(b)c)d')

m=p.match('abcd')

print(m.groups())