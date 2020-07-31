import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)
print(x)
plt.hist(x, 100)
plt.show()

# We specify that the mean value is 5.0, and the standard deviation is 1.0.

# Meaning that the values should be concentrated around 5.0,
# and rarely further away than 1.0 from the mean.

# And as you can see from the histogram, most values are between 4.0 and 6.0,
# with a top at approximately 5.0.