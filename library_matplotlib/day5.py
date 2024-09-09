import matplotlib.pyplot as plt


# STEM PLOT

a = [1,2,3,4,5,6]
b = [2,4,6,8,10,12]

plt.stem(
a,b,
     linefmt="-.",
     label="Information",
     orientation="vertical",
     markerfmt="*"
)
plt.legend()
plt.xlabel("value1")
plt.ylabel("value2")
plt.show()

# linefmt values
'''
("solid", "-"), ("dashed", "--"), ("dashdot", "-."), ("dotted", ":"), ("none", "None"), 
'''
