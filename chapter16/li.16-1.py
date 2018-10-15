from pylab import figure, plot, text, axis, savefig,legend

import math
figure()

xdata=[0.1 * i for i in  range(100)]

ydata=[math.sin(j) for j in xdata]

plot(xdata,ydata,'kd',linewidth=1)

axis([0, 3 * math.pi, -1.2, 1.2])

legend()
savefig('chapter16/sinfunc.png')