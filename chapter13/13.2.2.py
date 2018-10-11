import rpy2.robjects as robjects

r=robjects.r

pi=r.pi
x=r.c(1,2,3,4,5,6,7)
y=r.seq(1,10)
m=r.matrix(y,nrow=5)
f=r("read.table('Random.tsv',sep='\t')")