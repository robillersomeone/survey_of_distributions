import math
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# 'distribution' functions map the pdf of a numpy range for their respective ranges
# distribitions so far - gamma, beta, erlang, exponential, chi-squared, normal (apprx)
# to fix - f, t
# to add - cauchy, dirichlet

# gamma function
def gamma_function(k):
    ''' for integer random variables
    params
    ------
    k : int
        random variable
    returns
    -------
    gamma(k) : int
    '''
    return math.factorial((k-1))

# using quad function for real numbers
def intergrandt(t, k):
    return np.power(t, (k-1)) * np.exp(-t)
    
def integral_gamma_function(k):
    return quad(intergrandt, 0, np.inf, args=(k))[0]

# pdf of gamma distribution
def gamma_distribution(x, k, theta):
    '''two parameters -  shape k, scale theta, 
        x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    k : int (positive)
        shape paramter in gamma distribution
    theta : int
        scale parameter in gamma distribution

    returns
    -------
    value in gamma distr for random variable : float
    notes 
    -----
    will add case if rate parameter beta is used
    '''
    num = (x ** (k-1)) * (math.e ** (-x/theta))
    dem = gamma_function(k) * (theta**k)
    return num / dem

def int_gamma_distribution(x, k, theta):
    '''two parameters -  shape k, scale theta,
    x value is a random variable to pass in
    uses integer verion of gamma function
    params
    ------
    x : float
        random variable
    k : float (positive)
        shape parameter in gamma distribution
    theta : float
        scale parameter in gamma distribution

    returns
    -------
    value in gamma distr for random variable : float
    notes 
    -----
    will add case if rate parameter beta is used
    '''
    num = (x ** (k-1)) * (math.e ** (-x/theta))
    dem = integral_gamma_function(k) * (theta**k)
    return num / dem

# beta in relation to gamma

# beta_function in terms of the gamma function
def beta_function(x, y):
    num = gamma_function(x) * gamma_function(y)
    dem = gamma_function(x + y)
    return num / dem

def beta_distribution(x, alpha, beta):
    '''two parameters -  shape alpha, shape beta,
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    alpha : float (positive)
        shape paramter in  beta distribution
    beta : float
        scale parameter in beta distribution

    returns
    -------
    value in beta distr for random variable : float
    '''
    num = (x**(alpha -1)) * ((1-x)**(beta - 1))
    dem = beta_function(alpha, beta)
    return num / dem

# Erlang in relation to gamma
# built directly from the gammma distribution
def erlang_distribution(x, k, theta):
    # might have to account for 'scale' vs 'rate' parameterization
    # for right now, scale parameter is used
    '''two parameters -  shape k, scale mu,
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    k : int (positive)
        shape paramter in gamma distribution
    mu : float
        scale parameter in gamma distribution

    returns
    -------
    value in erlang distr for random variable : float
    '''
    if isinstance(k, int):
        return gamma_distribution(x, k, mu)
    else:
        return 'shape parameter is not an integer'

def exponential_distribution(x, lambda_, k=1):
    '''one parameter - rate (lambda)
    the lambda is converted to scale theta for the gamma_distribution function
    rate is a more common parameterization of the exp
    k (the shape param for gamma is set to one as a default)
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    lambda_ : int (positive)
        rate paramter in exponential distribution
        this function inverts lambda (the rate for expo) 
        to theta (the scale for gamma)
    k : 1 (int)
        known as shape parameter in gamma distribution,
        it is always =1 for the exponential distribution

    returns
    -------
    value in exponential distr for random variable : float
    '''
    theta = 1 / lambda_
    return gamma_distribution(x, k, theta)

def chi_squared_distribution(x, v, theta=2):
    '''one parameter -  shape v (known as degrees of freedom),
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    v : int (positive)
        shape paramter in chi-squared distribution
        'degrees of freedom' in chi-squared
    theta : 2 (int)
        known as shape parameter in gamma distribution,
        it is always =1 for the exponential distribution

    returns
    -------
    value in exponential distr for random variable : float
    '''
    return gamma_distribution(x, (v/2), theta)

def f_distribution(x, degree_1, degree_2, theta=2):
    '''two parameters -  degrees of freedoms degree_1, degree_2
    for the two chi_squared distributions
    x value is a random variable to pass in'''
    # x_1 = np.random.choice(x_gamma_values, 100)
    # x_2 = np.random.choice(x_gamma_values, 100)
    # num = int_gamma_distribution(x_1, (degree_1/2), theta) / degree_1
    # dem = int_gamma_distribution(x_2, (degree_2/2), theta) / degree_2
    num = int_gamma_distribution(x, (degree_1/2), theta) / degree_1
    dem = int_gamma_distribution(x, (degree_2/2), theta) / degree_2
    return num/dem
x_f_values = np.arange(0, 5, .05)[1:]
y_f_values = f_distribution(x_f_values, 20,2)
# right now, the num and dem are not independent
# instead, randomly sample from the x_gamma_values for each distribution
# x_1 = np.random.choice(x_gamma_values, 100)
# x_2 = np.random.choice(x_gamma_values, 100)
# x_f_distr = np.append(x_1, x_2)
# x_f_distr = x_1/x_2
# print(x_1)
# print(x_2)
# print(np.append(x_1, x_2))
# y_f_values = f_distribution(x_1, x_2, 10,1)
# print(len(x_1/x_2))
# print(len(y_f_values))
# y_f_values = f_distribution(x_gamma_values, 10,1)

# print(np.random.choice(x_gamma_values, 10))
# print(len(x_gamma_values))
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


# sampling for the t-distribution

def t_distribution(t, nu):
    '''one parameter -  shape nu (known as degrees of freedom)
    t value is a random variable to pass in
    from samples of a normally distributed population'''
    num = gamma_function((nu + 1)/2) * ((1 + ((t**2)/ nu))**(-((nu + 1)/2)))
    dem = ((nu * math.pi)**(1/2)) * gamma_function(nu/2)
    return num / dem


# revisit
# def beta_from_gamma(x, k_1, theta_1, k_2, theta_2):
#     '''four parameters -  shape k, scale theta for each gamma
#     value x a random variable to pass in
#
#     will add case if rate parameter beta is used'''
#     X_1 = gamma_distribution(x, k_1, theta_1)
#     X_2 = gamma_distribution(x, k_2, theta_2)
#     return X_1 / (X_1 + X_2)



