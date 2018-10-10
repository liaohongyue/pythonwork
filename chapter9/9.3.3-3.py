import re

seq = 'QSAMGSNKSKPKDASQRRRSLEPAENVHGAGGGAFPASQRPSKP'
pattern=re.compile('R(?P<w1>.{0,3})[ST](?P<w2>[^P])')
match=pattern.search(seq)

print(match.group('w1'))

print(match.group('w2'))