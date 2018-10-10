import re

gemmome_seq=open(file="chapter9/genome.txt",mode='r').read()

sites=[]
for line in open(file="chapter9/TFBS.txt",mode='r'):
    fields=line.split()
    tf=fields[0]
    site=fields[1]
    sites.append((tf,site))

for tf,site in sites:
    tfbs_re=re.compile(site)
    all_matchs=tfbs_re.findall(gemmome_seq)
    matchs=tfbs_re.finditer(gemmome_seq)
    if all_matchs:
        print(tf,':')
        for tfbs in matchs:
            print("\t",tfbs.group(),tfbs.start(),tfbs.end())
