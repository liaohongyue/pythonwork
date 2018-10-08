transcripts_file=open("chapter6/transcripts.tracking","r")
trans_out_file=open("chapter6/transcripts-filter","w")

for tran in transcripts_file:
    columns=tran.strip().split("\t")
    wildtype=columns[4:7].count('-')
    treatment=columns[7:10].count('-')
    if wildtype<2 and treatment<2:
        trans_out_file.write(tran)

transcripts_file.close()
trans_out_file.close()