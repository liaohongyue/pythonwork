import rpy2.robjects as robjects
import time
from rpy2.robjects.packages import importr

grdevices=importr("grDevices")
grdevices.png(file='plot.png',width=512,height=512)
r=robjects.r
r.plot(r.rnorm(100),xlab="y",ylab="Y")
grdevices.dev_off()
