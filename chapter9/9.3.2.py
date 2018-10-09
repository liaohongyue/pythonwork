import re

# compile a pattern and assign it to a variable
pattern = re.compile('R.[ST][^P]')

# define a string with three occurrences of regexp:
seq = 'RQSAMGSNKSKPKDASQRRRSLEPAENVHGAGGGAFPASQRPSKP'

# search for the pattern in the string
all=pattern.finditer(seq)

for s in all:
    print(s.group())
    print(s.span())
    print(s.start())
    print(s.end())

