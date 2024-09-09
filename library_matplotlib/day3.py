import matplotlib.pyplot as plt
import numpy as np

# a = [10,20,30,40,50]
# b = [11,25,35,33,55]
# size = [15,16,17,18,19]
#
# plt.xlabel('x value number',fontsize=15)
# plt.ylabel('y value number',fontsize=20)
# plt.title('Scatter Graph')
# plt.scatter(a,b,sizes=size,color=['r','g','y','c','m'],marker='*',edgecolors='green',label='Graph',alpha=0.2)
# plt.legend()
# plt.colorbar()
# plt.show()

# make a graph full of dots

# a = [1,6,4,8,3,8,2,0,4,8,4,7,4,6,6,3,9,2]
# b = [6,9,8,7,9,5,5,3,7,4,8,4,8,3,8,4,6,8]
# c = ['r','g','b','y','m','b','b','y','m','b','b','y','m','b','b','y','m','b']
# plt.xlabel('x',fontsize=15)
# plt.ylabel('y',fontsize=20)
# plt.title('Scatter Graph')
# plt.scatter(a,b,marker='+',color=c)
# plt.show()

# stack plot

s = [10,20,30,40]
x = [11,12,13,14]
y = [12,13,14,15]
z = [13,14,15,16]
q = ['area1','area2','area3']
plt.stackplot(s,x,y,z,labels=q,colors=['r','m','c'])
plt.legend()
plt.show()





























