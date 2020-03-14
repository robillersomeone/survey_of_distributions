import math
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# 'distribution' functions map the pdf of a numpy range for their respective ranges


# gamma function
def gamma_function(k):
    # only works fot integers
    return math.factorial((k-1))
# implement the integral function
# may use quad function for real numbers

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
# print(x_gamma_values)

y_gamma_values = gamma_distribution(x_gamma_values, 2, 2)

# plt.title('gamma with k=2, θ=2')
# plt.plot(x_gamma_values, y_gamma_values)
# plt.savefig('gamma_2_2.png', format="png")
# plt.show()
# print(len(np.arange(0, 20, .1)))
# print(x_gamma_values)


# beta in relation to gamma

# beta_function in terms of the gamma function
def beta_function(x, y):
    num = gamma_function(x) * gamma_function(y)
    dem = gamma_function(x + y)
    return num / dem

def beta_distribution(x, alpha, beta):
    num = (x**(alpha -1)) * ((1-x)**(beta - 1))
    dem = beta_function(alpha, beta)
    return num / dem

x_beta_values = np.arange(0, 1, .01)[1:]
# print(x_beta_values)

y_beta_values = beta_distribution(x_beta_values, 2, 5)

plt.plot(x_beta_values, y_beta_values)
plt.show()

# revisit
# def beta_from_gamma(x, k_1, theta_1, k_2, theta_2):
#     '''four parameters -  shape k, scale theta for each gamma
#     value x a random variable to pass in
#
#     will add case if rate parameter beta is used'''
#     X_1 = gamma_distribution(x, k_1, theta_1)
#     X_2 = gamma_distribution(x, k_2, theta_2)
#     return X_1 / (X_1 + X_2)

# need to generate numbers to pass into the beta


# y_gamma_values = beta_from_gamma(x_gamma_values,1,1,3,1)

# Erlang in relation to gamma
erlang_distribution = gamma_distribution()
