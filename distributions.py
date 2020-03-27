import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma
import matplotlib.pyplot as plt

# 'distribution' functions map the pdf of a numpy range for their respective ranges
# distribitions so far
# gamma, beta, erlang, exponential, chi-squared
# need to fix - f, normal, t


# gamma function
def gamma_function(k):
    # only works fot integers
    return math.factorial((k-1))
# implement the integral function
# may use quad function for real numbers
# using the scipy gamma function for integral implementation for now

# print(gamma_function(4))

# pdf of gamma distribution
def gamma_distribution(x, k, theta):
    '''two parameters -  shape k, scale theta
    x value is a random variable to pass in

    will add case if rate parameter beta is used'''
    num = (x ** (k-1)) * (math.e ** (-x/theta))
    dem = gamma_function(k) * (theta**k)
    return num / dem

# check the gamma
# print(gamma_distribution(1.4, 3, 1))

def gamma_distribution_scipy(x, k ,theta):
    '''two parameters -  shape k, scale theta
    x value is a random variable to pass in

    will add case if rate parameter beta is used'''
    num = (x ** (k-1)) * (math.e ** (-x/theta))
    dem = gamma(k) * (theta**k)
    return num / dem

# get values (0,20) to plot
x_gamma_values = np.arange(0, 20, .1)[1:]
y_gamma_values = gamma_distribution(x_gamma_values, 2, 2)

# beta in relation to gamma

# beta_function in terms of the gamma function
def beta_function(x, y):
    num = gamma_function(x) * gamma_function(y)
    dem = gamma_function(x + y)
    return num / dem

def beta_distribution(x, alpha, beta):
    '''two parameters -  shape alpha, shape beta

    x value is a random variable to pass in'''
    num = (x**(alpha -1)) * ((1-x)**(beta - 1))
    dem = beta_function(alpha, beta)
    return num / dem

# this is the support for beta
x_beta_values = np.arange(0, 1, .01)[1:]
# print(x_beta_values)
y_beta_values = beta_distribution(x_beta_values, 2, 5)

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

# Erlang in relation to gamma
# built directly from the gammma distribution
def erlang_distribution(x, k, theta):
    # might have to account for 'scale' vs 'rate' parameterization
    # for right now, rate parameter is used
    '''two parameters -  shape k, scale theta
    where k is an integer
    x value is a random variable to pass in'''
    if isinstance(k, int):
        return gamma_distribution(x, k, theta)
    else:
        return 'shape parameter is not an integer'

def exponential_distribution(x, lambda_, k=1):
    '''one parameter - rate lambda
    the lambda is converted to scale theta for the gamma_distribution function
    rate is a more common parameterization of the exp
    k (the shape param for gamma is set to one as a default)
    x value is a random variable to pass in'''
    theta = 1 / lambda_
    return gamma_distribution(x, k, theta)



def chi_squared_distribution(x, k, theta=2):
    '''one parameter -  shape k (known as degrees of freedom)
    x value is a random variable to pass in'''
    return gamma_distribution(x, (k/2), theta)

# just takes x_gamma_values, chi-squared and gamma have the same support
# y_chi_squared_values = chi_squared_distribution(x_gamma_values, 2)


def f_distribution(x, degree_1, degree_2, theta=2):
    '''two parameters -  degrees of freedoms degree_1, degree_2
    for the two chi_squared distributions
    x value is a random variable to pass in'''
    num = gamma_distribution(x, (degree_1/2), theta) / degree_1
    dem = gamma_distribution(x, (degree_2/2), theta) / degree_2
    return num/dem

# right now, the num and dem are not independent
# instead, randomly sample from the x_gamma_values for each distribution
# y_f_values = f_distribution(x_gamma_values, 10,1)

# getting to normal
# at first, increase k as a parameter
# may implement a limit

def normal_distribution(x, k, theta):
    '''two parameters -  shape k, scale theta
    scale theta refers to a theta = standard deviation of the normal
    updated_x and updated_theta are to keep the distribution stationary (updated_x, for stationary) and
    keep the standard deviation (updated_theta, scale param)
    x value is a random variable to pass in'''
    updated_x = (k-1) * (((1/k)**(1/2)) * theta) + x
    updated_theta = ((1/k)**(1/2)) * theta
    return gamma_distribution(updated_x, k, updated_theta)

# for now the normal distribution is approximated using the central limit theorem

x_gamma_values_getting_normal = np.arange(0, 2, .01)[1:]
y_gamma_values_int = gamma_distribution_scipy(x_gamma_values_getting_normal, 25, 1/25)

# x_gamma_values = np.arange(-4, 4, .01)[1:]
# y_gamma_values = gamma_distribution(x_gamma_values, 2, 2)

# y_normal_values = normal_distribution(x_gamma_values_getting_normal, 50, 1/50 )

# sampling for the t-distribution

def t_distribution(t, nu):
    '''one parameter -  shape nu (known as degrees of freedom)
    t value is a random variable to pass in
    from samples of a normally distributed population'''
    num = gamma_function((nu + 1)/2) * ((1 + ((t**2)/ nu))**(-((nu + 1)/2)))
    dem = ((nu * math.pi)**(1/2)) * gamma_function(nu/2)
    return num / dem

# may use quad function for real numbers
def intergrandt(k, t):
    return np.power(t, (k-1)) * np.exp(-t)
    # return (t **(k-1)) * np.exp(-t)
def integral_gamma_function(k):
    return quad(intergrandt, 0, np.inf, args=(k))[0]

# vec_integral_gamma_function = np.vectorize(integral_gamma_function)
# print(gamma_function(4))
# print(integral_gamma_function(2))

def int_gamma_distribution(x, k, theta):
    '''two parameters -  shape k, scale theta
    x value is a random variable to pass in

    will add case if rate parameter beta is used'''
    num = (x ** (k-1)) * (math.e ** (-x/theta))
    dem = integral_gamma_function(k) * (theta**k)
    return num / dem
