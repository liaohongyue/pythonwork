table=[]
for line in open("chapter7/lowry_data.txt"):
    table.append(line.strip().split("\t"))

out=""

for row in table:
    line=[str(cell) for cell in row]
    out=out + "\t".join(line) + "\n"
open("chapter7/out.file.txt","w").write(out)