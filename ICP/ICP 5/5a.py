import numpy as np
import matplotlib.pyplot as plt

#Take two arrays
x=np.array([2.9, 6.7, 4.9, 7.9, 9.8, 6.9, 6.1, 6.2, 6, 5.1, 4.7, 4.4, 5.8])
y=np.array([4, 7.4, 5, 7.2, 7.9, 6.1, 6, 5.8, 5.2, 4.2, 4, 4.4, 5.2])

#Calculate the means of two arrays
meanx=np.mean(x)
meany=np.mean(y)

#Calculate the distance between the points  from mean and add them
num=np.sum((x-meanx)*(y-meany))
den=np.sum(pow((x-meanx),2))
m=num/den

#Calculate the intercept of the line
intercept=meany-(m*meanx)

#Write the line equation and plot the graph
val=(m*x)+intercept
plt.scatter(x,y)
plt.plot(x,val)
plt.show()