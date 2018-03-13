# importing the required module
import matplotlib.pyplot as plt
 
# x axis values
x = [2014,2015,2016,2017,2018]
# corresponding y axis values
y = [100,220,300,550,10]
 
# plotting the points 
plt.plot(x, y)
 
# naming the x axis
plt.xlabel('year')
# naming the y axis
plt.ylabel('number of students')
 
# giving a title to my graph
plt.title('My first graph!')
 
# function to show the plot
plt.show()

