list_a=[]
for line in open(file='chapter4/cell_cycle_proteins.txt'):
    list_a.append(line.strip())
list_b=[]
for line in open("chapter4/cancer_cell_proteins.txt"):
    list_b.append(line.strip())

for proteins in list_a:
    if proteins in list_b:
        print("protein:",proteins," is in the cancer cell!")
    else:
        print("protein:",proteins," is observed!")
