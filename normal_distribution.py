import math
import numpy as np
import distributions as ds
import matplotlib.pyplot as plt

# using the central limit theorem

# start with a distribution, in this case a gamma distribution with the shape and sclae both equal to 2
gamma_2_2 = ds.int_y_gamma_values_2_2

sampled_data = [sum(np.random.choice(gamma_2_2, 70))/70 for _ in range(2500)]

print(sampled_data[0], sampled_data[1], len(sampled_data))
print(np.random.choice(gamma_2_2, 30))

plt.hist(sampled_data)
plt.show()

# numpy normal distribution method
mu, sigma = 0, 1
standard_normal = np.random.normal(mu, sigma, 1000)


# this appraoches zero
# print(sum(standard_normal)/ len(standard_normal))

# chi-squared, as the sum of normals
# start with degree of freedom equal to one

chi_from_normal = [x**2 for x in standard_normal]

# t distribution
# from sampling a normal distribution