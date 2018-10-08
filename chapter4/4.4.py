fasta_file=open("chapter4/SwissProt.fasta","r")
out_file=open("chapter4/SwissProtHuman.fasta","w")
seq=''

for line in fasta_file:
    if line[0]==">" and seq=='':
        header=line
    elif line[0]!='>':
        seq=header+line
    elif line[0]==">" and seq!='':
        if "Homo sapiens" in header:
            out_file.write(header+seq)
            seq=''
            header=line
