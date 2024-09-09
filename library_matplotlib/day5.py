# stem plot

import matplotlib.pyplot as plt
#
# a = [1,2,3,4,5,6]
# b = [2,4,6,8,10,12]
#
# plt.stem(a,b,linefmt="-.", label="Information", orientation="vertical", markerfmt="*")
# plt.legend()
# plt.xlabel("value1")
# plt.ylabel("value2")
# plt.show()

# linefmt values
'''
    '_'  =====> solid
    '--' =====> dashed
    '-.' =====> dash-doted
    ':'  =====> dotted
'''

# numpy task

import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([11,22,33,44,55])

joined_arrays = np.concatenate((a,b))
print(joined_arrays)