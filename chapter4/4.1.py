fasta_file=open("chapter4/SwissProt.fasta","r")
#out_file=open("chapter4/SwissProt.head","w")
ac_list=[]
for line in fasta_file:
    if line[0]==">":
        fields=line.split('|')
        ac_list.append(fields[1])

print(ac_list)
#out_file.close()