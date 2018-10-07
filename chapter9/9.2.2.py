import re

seq = 'VSVLTMFRYAGWLDRLYMLVGTQLAAIIHGVALPLMMLI'

pattern=re.compile('[ST]Q')

match=pattern.search(seq)

if match:
    print('%10s' % (seq[match.start() - 4:match.end() + 4]))
    print('%6s' % match.group())
else:
    print('no match')