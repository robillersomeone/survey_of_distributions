import math
import numpy as np
import matplotlib.pyplot as plt

# using the central limit theorem

# numpy normal distribution method
mu, sigma = 0, 1
standard_normal = np.random.normal(mu, sigma, 1000)


# this appraoches zero
# print(sum(standard_normal)/ len(standard_normal))

# chi-squared, as the sum of normals
# start with degree of freedom equal to one

chi_from_normal = [x**2 for x in standard_normal]


# gamma function
def gamma_function(k):
    return math.factorial((k-1))

# print(gamma_function(4))


# pdf of gamma distribution
def gamma_distribution(x, k, theta):
    '''two parameters -  shape k, scale theta
    value x a random variable to pass in

    will add case if rate parameter beta is used'''
    num = (x ** (k-1)) * (math.e ** (-x/theta))
    dem = gamma_function(k) * (theta**k)
    return num / dem

# check the gamma
# print(gamma_distribution(1.4, 3, 1))

# get values (0,20) to plot
x_gamma_values = np.arange(0, 20, .1)[1:]

y_gamma_values = gamma_distribution(x_gamma_values, 2, 2)

plt.title('gamma with k=2, θ=2')
plt.plot(x_gamma_values, y_gamma_values)
plt.show()
plt.savefig('gamma_2_2.png')
# print(len(np.arange(0, 20, .1)))
# print(x_gamma_values)


# beta in relation to gamma

# Erlang in relation to gamma
