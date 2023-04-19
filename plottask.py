# Plot Task
# This diagram should show 1000 values drawn from a normal distribution
# with a mean of 5 and standard deviation of 2.
# It also plots the function h(x) = x^3.
# Author: Andrea Cignoni

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics

# Set random seed for reproducibility
np.random.seed(42)
# Generating 1000 values with mean 5 and standard deviation 2
values = np.random.normal(loc=5, scale=2, size=1000)

# Plot the histogram of generated values
plt.hist(values, bins=30, density=True, edgecolor='black')
plt.title('Normal Distribution with Mean 5 and Standard Deviation 2')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Create a new figure to plot the function h(x) = x^3
def h(x):
    return x**3
 
# Generate x values in the range [0, 10]
x = np.linspace (0, 10, num=100)

# Plot the function h(x) = x^3 in normal distribution
plt.plot(norm.pdf(x, h(x)))
plt.title('Function h(x)=x^3')
plt.xlabel('x')

# Show the plots
plt.show()