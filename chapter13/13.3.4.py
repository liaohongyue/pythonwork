import rpy2.robjects as robjects

r=robjects.r

y=r.seq(1,10)
print(r.matrix(y,nrow=5))