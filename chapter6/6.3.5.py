line_file=open("chapter6/test.txt","r")
out_file=open("chapter6/out.txt","w")
unique=[]
out_data=“”
for line in line_file:
    if line not in unique:
        out_data+=line
        unique.append(line)
    
print(out_data)
        