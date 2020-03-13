import math
import numpy as np

# using the central limit theorem

# numpy normal distribution method
mu, sigma = 0, 1
standard_normal = np.random.normal(mu, sigma, 1000)


# this appraoches zero
# print(sum(standard_normal)/ len(standard_normal))

# chi-squared, as the sum of normals
# start with degree of freedom equal to one

chi_from_normal = [x**2 for x in standard_normal]
