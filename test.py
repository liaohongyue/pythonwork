import re

str='/data/gpfs02/jliu/liaohy/RNA-seq/02.Alignment/01.sorted_bam/HZ.align.out.sorted.bam'

patern1=re.compile('\/')
patern2=re.compile('\.')

cutstr=patern1.split(str)

print(repr(cutstr[-1]))
fileName=patern2.split(repr(cutstr[-1]))
fileName=fileName[0]
fileName=fileName[1:]

print(fileName)