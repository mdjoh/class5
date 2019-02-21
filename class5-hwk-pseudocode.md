Class 5 Homework

####

# Loading, organizing dataset and computing summary stats
Load diabetes data set
Import pandas library
Read dataset from file using pandas.read function passing in file name of dataset
Import numpy library
Ensure dataset is in a numpy array form so that data rows and columns can be indexed and extracted 

Compute summary stats of dataset using numpy.mean and numpy.std

# Visualization
Import matplotlib library for plotting purposes (import matplotlib.pyplot as plt) and pylab
Make a loop to go through all variables in dataset
Plot each variable on its own for exploratory purposes using plt.plot or plt.hist
Save figure to file using pylab.savefig
To plot two variables as y vs. x, use a scatter plot in matplotlib (plt.scatter)
Save figure to file using pylab.savefig

# Intermediate: Adding header names to table
Figure out what the dataset headers will be (ie. column names)
Put those header names of string type into a list of its own
Pass said list as the name argument in read_csv function from pandas library

# Reach
A 3D plot can be of use to visualize 2 or more features at one time
Import matplotlib and Axes3D from mpl_toolkits.mplot3d
Plot line plots using Axes3D.plot where arguments include x,y,z coordinates (ie. 3 features)
Show plot using show() from matplotlib or save figure
