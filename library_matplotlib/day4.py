import matplotlib.pyplot as plt

# Matplotlib interview question

# 1. what is the purpose of matplotlib library?
"""
the purpose of it is to generate graphs, it is a py package that provides many functionalities for
    2d plotting in various forms.
"""



# 2. Name the fn you will use to create line chart, bar chart bar(), horizontal bar chart barh(), barv().
"""
plot()
bar()
barh()
"""



# 3. write a py program to display a bar chart of the no of students in the class
"""
class = [6,7,8,9,10,11,12,13]
strength = [42,44,50,37,48,40,35]
"""



# 4. The comment used to give heading of the paragraph is?
"""
plt.title()
"""



# 5. Using py matplotlib, ______ can be used to count how many values fall into each interval.
"""
histograph
"""



# 6. out of the following which fn can't be used for the customization of chart in py
"""
a. xlabel
b. color ✅
c. title
d. legend
"""



# 7. WAPP to plot a line chart based on given data to depict the changing weekly average temprature in Delhi for four weeks
# week = [1,2,3,4]
# avg_tem = [40,42,50,44]
"""
week = [1,2,3,4]
avg_tem = [40,42,50,44]
plt.plot(week,avg_tem)
plt.show()
"""



# 8. How does Python supports data visualization?
"""
using matplotlib
using seaborn
"""



# 9. The score of four cricket team isn four matches is available to you.
# Write program to plot horizontal bar chart with followings:
#   legend at bottom right corner
#   category axis label as 'match'
#   value axis label as 'runs'
"""
matches = [1,2,3,4]
runs = [40,60,30,100]
plt.xlabel('runs')
plt.ylabel('match')
plt.barh(matches,runs)
plt.legend(loc='lower right')
plt.show()
"""