from operator import itemgetter

table=[]
for line in open("chapter8/random_distribution.tsv"):
    columns=line.split()
    columns=[float(x) for x in columns]
    table.append(columns)

column=1
table_sorted=sorted(table,key=itemgetter(column))
for row in table_sorted:
    row=[str(x) for x in row]
    print("\t".join(row))
