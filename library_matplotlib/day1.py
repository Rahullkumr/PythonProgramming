import matplotlib.pyplot as plt
import numpy as np

# matplotlib: john d hunter

# LINE GRAPH
"""
x = np.array([10, 20, 30, 40])
y = x ** 2

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Normal line graph")
plt.plot(x,y,marker="*",ls="dashed",mfc="r",mec="b",ms=2,lw="1",color="m",label="Information")
plt.legend(loc="upper right")
# plt.legend(loc="center")
plt.show()
"""

"""
markers = point of intersection of x and y axis.
    "o",  # Circle              "s",  # Square                  "^",  # Triangle Up
    "v",  # Triangle Down       "<",  # Triangle Left           ">",  # Triangle Right
    "D",  # Diamond             "d",  # Thin Diamond            "p",  # Pentagon
    "h",  # Hexagon1            "H",  # Hexagon2                "*",  # Star
    "+",  # Plus                "x",  # Cross                   "X",  # Filled Cross
    "|",  # Vertical Line       "-",  # Horizontal Line         "_",  # Underscore (thin horizontal line)
    "1",  # Tri-down            "2",  # Tri-up                  "3",  # Tri-left
    "4",  # Tri-right           ".",  # Point (tiny dot)        ",",  # Pixel (smaller than a point)            
    "None",  # No marker        None,  # No marker              " "  # No marker

ls = line styles
    ("solid", "-"),            ("dashed", "--"),        ("dashdot", "-."),               
    ("dotted", ":"),           ("none", "None"),     


mfc     = marker face color (the inside of the square markers)
mec     = marker edge color (the border of the square markers)
ms      = marker size
lw      = line width
color   = line color
label   = label to be used in the legend
"""

# BAR GRAPH
# """
lang = ['Python', 'Java', 'C', 'C++', 'Js']
rating = [60, 30, 80, 15, 45]
c = ['w', 'w', 'w', 'w', 'w']

plt.ylabel("rating")
plt.xlabel("languages")
plt.title("Language info")
plt.bar(lang, rating, color=c, width=0.5, align="edge", label="language", edgecolor="olive", linewidth=2)
plt.legend()
plt.show()
# """
'''
colors = 
    ("blue", "b")               ("green", "g")                  ("red", "r")            ("cyan", "c")
    ("magenta", "m")            ("yellow", "y")                 ("black", "k")          ("white", "w")
    ("gray", "gray")            ("darkgray", "darkgray")        ("orange", "orange")    ("pink", "pink")
    ("purple", "purple")        ("brown", "brown")              ("lime", "lime")        ("olive", "olive"), etc
        
    also you can use:
        Hexadecimal strings like "#f500f5"
        RGB tuples like (255, 255, 1)
        RGBA tuples for transparency, like (0.1, 0.2, 0.5, 0.8) ()
        

'''


# hw
'''
l = ['Python', 'Java', 'C', 'C++', 'Js']
r = [60,30,80,15,45]
c = ['w', 'w', 'w', 'w', 'w']
cc = ['r', 'g', 'b','y', 'm']

rr = [30,15,40,7,22]
plt.ylabel("rating")
plt.xlabel("languages")
plt.title("Language info")
plt.bar(l,r,color=c,width=0.5, align="edge", label="language",edgecolor="b", linewidth=2)
plt.bar(l,rr,color=cc,width=0.5, align="edge", label="language",edgecolor="b", linewidth=2)
plt.legend()
plt.show()
'''
