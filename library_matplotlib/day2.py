import matplotlib.pyplot as plt
import numpy as np

# x = ['java', 'python', 'c++', 'JS']
# y = [50,60,70,80]
# ex = [0.0,0.1,0.0,0.0]
# col = ['g','r','c','m']
# plt.pie(y,labels=x,autopct="%1.0f%%",explode=ex,shadow=True,radius=1.0, counterclock=False, labeldistance=1.5,startangle=180, colors=col)
# plt.show()

# statewise rainfall

states = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]

rain_percentage = [
    85.0,
    92.5,
    88.7,
    75.4,
    80.2,
    95.3,
    70.6,
    60.1,
    83.9,
    78.5,
    90.4,
    97.2,
    74.8,
    76.5,
    85.7,
    92.1,
    89.9,
    87.3,
    82.4,
    65.2,
    55.7,
    93.8,
    60.3,
    77.6,
    88.9,
    68.5,
    79.2,
    81.7
]




# y = [50,60,70,80]
# ex = [0.0,0.1,0.0,0.0]
# col = ['g','r','c','m']
# plt.pie(rain_percentage,labels=states,autopct="%1.0f%%",shadow=True,radius=1.0, counterclock=False, labeldistance=1.2,startangle=90)
# plt.legend(loc="best")
# plt.show()



# grid
x = [10,20,30,40]
y = [10,20,30,40]
plt.plot(x,y)
plt.grid(axis='x') # x-axis pe giro
plt.show()

