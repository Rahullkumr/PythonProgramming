import matplotlib.pyplot as plt
import numpy as np

# matplotlib: john d hunter

# line graph
# """
x = np.array([10,20,30,40])
y = x ** 2

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Normal line graph")
plt.plot(x,y,marker="s",ls="dashdot",mfc="r", mec="b", ms=20, lw="15", color="m", label="Information")
plt.legend(loc="upper right")
plt.legend(loc="center")
plt.show()
# """

# bar graph
"""
l = ['Python', 'Java', 'C', 'C++', 'Js']
r = [60,30,80,15,45]
c = ['w', 'w', 'w', 'w', 'w']
plt.ylabel("rating")
plt.xlabel("languages")
plt.title("Language info")
plt.bar(l,r,color=c,width=0.5, align="edge", label="language",edgecolor="b", linewidth=2)
plt.legend()
plt.show()
"""
# hw

# l = ['Python', 'Java', 'C', 'C++', 'Js']
# r = [60,30,80,15,45]
# c = ['w', 'w', 'w', 'w', 'w']
# cc = ['r', 'g', 'b','y', 'm']
#
# rr = [30,15,40,7,22]
# plt.ylabel("rating")
# plt.xlabel("languages")
# plt.title("Language info")
# plt.bar(l,r,color=c,width=0.5, align="edge", label="language",edgecolor="b", linewidth=2)
# plt.bar(l,rr,color=cc,width=0.5, align="edge", label="language",edgecolor="b", linewidth=2)
# plt.legend()
# plt.show()























