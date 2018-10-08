table = [
    ['protein', 'ext1', 'ext2', 'ext3'],
    [0.16, 0.038, 0.044, 0.040],
    [0.33, 0.089, 0.095, 0.091],
    [0.66, 0.184, 0.191, 0.191],
    [1.00, 0.280, 0.292, 0.283],
    [1.32, 0.365, 0.367, 0.365],
    [1.66, 0.441, 0.443, 0.444]
    ]

nested_dict={}

key=table[0]
j=0
for row in table[1:]:
    entryrow={}
    i=0
    for col in row:
        entryrow[str(key[i])]=col
        i=i+1
    nested_dict['row'+str(j)]=entryrow
    j=j+1



myTable=[]
for row in nested_dict:
    r=[]
    for col in nested_dict[row]:
        r.append(nested_dict[row][col])
    myTable.append(r)

print(myTable)