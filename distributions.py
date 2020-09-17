import math
import numpy as np
from scipy.integrate import quad
# bessel function for rice distribution
import scipy.special.jv

# 'distribution' functions map the pdf of a numpy range for their respective ranges
# distribitions so far - gamma, beta, erlang, exponential, chi-squared, f, normal (apprx), laplace, rayleigh, gumbel, fréchet, weibull
# pareto, levy, cauchy
# to fix - t
# to add - laplace from exp, dirichlet, negative binomial, zeta, rice

# gamma function
def gamma_function(k):
    ''' 
    for integer random variables
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
    '''
    two parameters -  shape k, scale theta, 
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
    '''
    two parameters -  shape k, scale theta,
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
    num = integral_gamma_function(x) * integral_gamma_function(y)
    dem = integral_gamma_function(x + y)
    return num / dem

def beta_distribution(x, alpha, beta):
    '''
    two parameters -  shape alpha, shape beta,
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
    '''
    two parameters -  shape k, scale mu,
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
    # might have to account for 'scale' vs 'rate' parameterization
    # for right now, scale parameter is used
    if isinstance(k, int):
        return gamma_distribution(x, k, theta)
    else:
        return 'shape parameter is not an integer'

def exponential_distribution(x, lambda_, k=1):
    '''
    one parameter - rate (lambda)
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
    '''
    one parameter -  shape v (known as degrees of freedom),
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

def f_distribution(x, degree_1, degree_2):
    '''
    two parameters -  degrees of freedoms degree_1, degree_2
    for the two chi_squared distributions
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    degree_1 : int (positive)
        shape paramter in chi-squared distribution
        'degrees of freedom' in chi-squared
    degree_2 : int (positive)
        shape paramter in chi-squared distribution
        'degrees of freedom' in chi-squared

    returns
    -------
    value in f distr for random variable : float
    '''
    num = integral_gamma_function((degree_1 + degree_2)/2) * (degree_1 ** (degree_1/2)) * (degree_2**(degree_2/2)) * (x **((degree_1/2)-1))
    dem = integral_gamma_function(degree_1/2) * integral_gamma_function(degree_2/2)  * ((degree_2 + (degree_1*x))**((degree_1 + degree_2)/2))
    return num / dem


# getting to normal
# at first, increase k as a parameter
# may implement a limit
def normal_distribution(x, k, theta):
    '''two parameters -  shape k, scale theta
    scale theta refers to a theta = standard deviation of the normal
    updated_x - keep the distribution stationary (updated_x, for stationary) 
    updated_theta - keep the standard deviation (updated_theta, scale param)
    x value is a random variable to pass in'''
    updated_x = (k-1) * (((1/k)**(1/2)) * theta) + x
    updated_theta = ((1/k)**(1/2)) * theta
    return gamma_distribution(updated_x, k, updated_theta)


# sampling for the t-distribution
# pdf uses gamma function... add integral version
def t_distribution(t, nu):
    '''one parameter -  shape nu (known as degrees of freedom)
    t value is a random variable to pass in
    from samples of a normally distributed population'''
    num = integral_gamma_function((nu + 1)/2) * ((1 + ((t**2)/ nu))**(-((nu + 1)/2)))
    dem = ((nu * math.pi)**(1/2)) * integral_gamma_function(nu/2)
    return num / dem

def laplace_distribution(x, mu, beta):
    '''
    two parameters - shape , scale
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    mu : float
        shape parameter for laplace distribution
    beta : float (positive)
        scale parameter for laplace distribution

    returns
    -------
    value in laplace distr for random variable : float
    '''
    return (1 / (2 * beta)) * np.exp( - abs(x - mu) / beta)

def laplace_from_exponential_distribution(x, mu, beta):
    '''
    '''
    pass

def rayleigh_distribution(x, sigma):
    '''
    one parameter - scale
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    sigma : float (positive)
        scale parameter for rayleigh distribution

    returns
    -------
    value in rayleigh distr for random variable : float
    '''
    exponent = -(x ** 2) / (2 * (sigma ** 2))
    return (x / (sigma ** 2)) * np.exp(exponent)

def gumbel_distribution(x, mu, beta):
    '''
    two parameters
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    mu : float
        location parameter for gumbel distribution
    beta : float (positive)
        scale parameter for gumbel distribution

    returns
    -------
    value in gumbel distr for random variable : float

    '''
    z = (x - mu) / beta
    coeff = 1 / beta 
    return coeff * np.exp(- (z + np.exp(-z)))

def frechet_distribution(x, alpha, s=1, m=0):
    '''
    three parameters
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    alpha : float (positive)
        shape parameter for frechet distribution
    s : float (positive), default=1
        scale parameter for frechet distribution
    m : float, default=0
        location of minimum for frechet distribution

    returns
    -------
    value in frechet distr for random variable : float
    '''
    standardized = ( (x - m) / s)
    return (alpha / s) * ( standardized ** (-1 - alpha) ) * np.exp( -(standardized ** (-alpha) ) )

def weibull_distribution(x, lambda_, k):
    '''
    two parameters
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    lambda_ : float (positive)
        shape parameter for weibull distribution
    k : float (positive)
        scale parameter for weibull distribution

    returns
    -------
    value in weibull distr for random variable : float
    '''
    return (k / lambda_) * ( (x/ lambda_) ** (k - 1)) * np.exp( - ((x / lambda_) ** k))


def pareto_distribution(x, x_min, alpha):
    '''
    two parameters - scale, shape
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    x_min : float (positive)
        scale parameter for pareto distribution
    alpha : float (positive)
        shape parameter for pareto distribution

    returns
    -------
    value in pareto distr for random variable : float
    '''
    # add check for x < x_min
    return (alpha * (x_min ** alpha)) / (x ** (alpha + 1))

def levy_distribution(x, mu, c):
    '''
    two parameters _ location, scale
        scale has to be greater than 0
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    mu : float (positive)
        location parameter for levy distribution
    c : float
        scale parameter for levy distribution
        
    returns
    -------
    value in levy distr for random variable : float
    '''
    coef = (c / (2 * np.pi)) ** (1/2)
    exponent = - (c / (2 * (x - mu) ) )
    denom = (x - mu) ** (3/2)
    return coef * (np.exp(exponent) / denom)


def cauchy_distribution(x, x_knot, gamma):
    '''
    two parameters

    params
    ------
    x : float
        random variable
    x_knot : float
        location parameter for cauchy distribution
    gamma : float (positive)
        scale parameter for cauchy distribution    

    returns 
    -------
    value in cauchy distr for random variable : float
    '''
    coef = np.pi * gamma
    return 1 / (coef * (1 + ( ( (x - x_knot) / gamma) ** 2 ) ) )

def rice_distribution(x):
    '''
    scipy.special.jv for bessel function
    '''
    pass

def rice_distribution_from_poisson(x):
    '''
    generate data with poisson
    generate a chi-squared distribution with data
    rice = sigma * square root of chi squared
    '''
    pass

# revisit beta
# def beta_from_gamma(x, k_1, theta_1, k_2, theta_2):
#     '''four parameters -  shape k, scale theta for each gamma
#     value x a random variable to pass in
#
#     will add case if rate parameter beta is used'''
#     X_1 = gamma_distribution(x, k_1, theta_1)
#     X_2 = gamma_distribution(x, k_2, theta_2)
#     return X_1 / (X_1 + X_2)

# revisit f
# dividing two chi-squares is tricky
# watch out for independence... 
# f- distr is 2 random samples from 2 different populations
# def f_distribution(x, degree_1, degree_2, theta=2):
    # '''two parameters -  degrees of freedoms degree_1, degree_2
    # for the two chi_squared distributions
    # x value is a random variable to pass in'''
    # x_1 = np.random.choice(x_gamma_values, 100)
    # x_2 = np.random.choice(x_gamma_values, 100)
    # num = int_gamma_distribution(x_1, (degree_1/2), theta) / degree_1
    # dem = int_gamma_distribution(x_2, (degree_2/2), theta) / degree_2
#     num = int_gamma_distribution(x, (degree_1/2), theta) / degree_1
#     dem = int_gamma_distribution(x, (degree_2/2), theta) / degree_2
#     return num/dem
# x_f_values = np.arange(0, 5, .05)[1:]
# y_f_values = f_distribution(x_f_values, 20,2)
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