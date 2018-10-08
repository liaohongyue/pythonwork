fasta_file=open("chapter5/SwissProt.fasta")
issulin_ac='P61981'
result=None
while result==None:
    line=str(fasta_file.readline())
    if line.startswith(">"):
        ac=line.split('|')[1]
        if ac==issulin_ac:
            result=ac.strip()
        

print(result)