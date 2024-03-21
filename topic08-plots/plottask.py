# plottask.py
# Plot a histogram of a normal distribution of 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.
# Author: Finbar Dennehy

import numpy as np
import matplotlib.pyplot as plt

# ensure random generator produces same numbers each time (for comparison)
np.random.seed(1) 
# create normal distribution of 1000 values with a mean of 5 and standard deviation of 2
norm_data = np.random.normal(loc=5,scale=2,size=1000)
# print data for testing purposes
# print(norm_data) 

# plot data in a histogram
plt.hist(norm_data)

# add x cubed
# create x values from 1 to 10
xpoints = np.array(range(1, 11))
# create y values = x cubed
ypoints = xpoints * xpoints * xpoints

# Plot x,y co-ordinates in red line with legend 'x cubed'
plt.plot(xpoints, ypoints, color= 'red', label="x cubed")
# Add title, x-axis label, y-axis label and legend to the plot
plt.title("normally distributed histogram and x cubed")
plt.xlabel("x")
plt.ylabel("x cubed")
plt.legend()
# Finally, show plot
plt.show()