inputFile=open("chapter4/AY810830.gb")
out_file=open("chapter4/AY810830.fasta","w")
flag=0

for line in inputFile:
    if line[0:9]=='ACCESSION':
        AC=line.split()[1].strip()
        out_file.write(">"+AC+"\n")
    elif line[0:6]=="ORIGIN":
        flag=1
    elif flag==1:
        fields=line.split()
        if fields!=[]:
            seq="".join(fields[1:])
            out_file.write(seq.upper()+"\n")

inputFile.close()
out_file.close()
