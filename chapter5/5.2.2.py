codon_table = {
    'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'CGU':'R', 'CGC':'R',   
    'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 'UCU':'S', 'UCC':'S',
    'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S', 'AUU':'I', 'AUC':'I',
    'AUA':'I', 'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L',
    'CUG':'L', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', 'GUU':'V',
    'GUC':'V', 'GUA':'V', 'GUG':'V', 'ACU':'T', 'ACC':'T', 'ACA':'T',
    'ACG':'T', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'AAU':'N',
    'AAC':'N', 'GAU':'D', 'GAC':'D', 'UGU':'C', 'UGC':'C', 'CAA':'Q',
    'CAG':'Q', 'GAA':'E', 'GAG':'E', 'CAU':'H', 'CAC':'H', 'AAA':'K',
    'AAG':'K', 'UUU':'F', 'UUC':'F', 'UAU':'Y', 'UAC':'Y', 'AUG':'M',
    'UGG':'W',
    'UAG':'STOP', 'UGA':'STOP', 'UAA':'STOP'
    }

# read the RNA sequence into a single string
rna=''
for line in open("chapter5/A06662-RNA.fasta"):
    if ">" not in line:
        rna=rna+line.strip()


# translate one frame at a time
for frame in range(3):
    prot=''
    for i in range(frame,len(rna),3):
        codon = rna[i:i+3]
        if codon in codon_table:
            if codon_table[codon]=="STOP":
                prot+="*"
            else:
                prot+=codon_table[codon]
        else:
                prot=prot+"-"
    print(prot)
