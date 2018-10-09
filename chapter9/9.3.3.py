import re

seq = 'QSAMGSNKSKPKDASQRRRSLEPAENVHGAGGGAFPASQRPSKP'

pattern1=re.compile('R(.)[ST][^P]')

match1=pattern1.search(seq)
print(match1.group())
print(match1.group(1))

pattern2=re.compile('R(.{0,3})[ST][^p]')

match2=pattern2.search(seq)
print(match2.group())
print(match2.group(1))