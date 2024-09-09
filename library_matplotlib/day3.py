import matplotlib.pyplot as plt
import numpy as np

# SCATTER GRAPH
"""
a               = [10,20,30,40,50]
b               = [11,25,35,33,55]
marker_size     = [50,60,70,80,90]

plt.xlabel('x value number',fontsize=15)
plt.ylabel('y value number',fontsize=20)
plt.title('Scatter Graph')
plt.scatter(
    a,b,
    sizes=marker_size,
    color=['r','g','y','c','m'],
    marker='*',
    edgecolors='green',
    label='Scatter Graph',
    alpha=0.2
)
plt.legend()
plt.colorbar()
plt.show()
"""


# make a graph full of dots
"""
a = [1,6,4,8,3,8,2,0,4,8,4,7,4,6,6,3,9,2]
b = [6,9,8,7,9,5,5,3,7,4,8,4,8,3,8,4,6,8]
c = ['r','g','b','y','m','b','b','y','m','b','b','y','m','b','b','y','m','b']
plt.xlabel('x',fontsize=15)
plt.ylabel('y',fontsize=20)
plt.title('Scatter Graph')
plt.scatter(a,b,marker='+',color=c)
plt.show()
"""




# STACK PLOT
# """
x_axis = [1,2,3,4]
y1 = [150, 200, 250, 300]
y2 = [100, 150, 200, 250]
y3 = [50, 100, 150, 200]
label_names = ['area1','area2','area3']
plt.grid(axis="y")
plt.stackplot(x_axis,y1,y2,y3, labels=label_names,colors=['r','m','c'])
plt.legend()
plt.show()
# """
