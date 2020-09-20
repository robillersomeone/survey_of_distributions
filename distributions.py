import math
import numpy as np
from scipy.integrate import quad
from scipy.special import logit
# bessel function for rice distribution
# import scipy.special.jv

# 'distribution' functions map the pdf of a numpy range for their respective ranges
# distribitions so far - gamma, beta, erlang, exponential, chi-squared, f, normal (apprx), laplace, rayleigh, gumbel, fréchet, weibull
# pareto, levy, cauchy, chi, kumaraswamy, nakagami, lomax, burr, beta prime, logit-normal, exponential-logarithmic
# gompertz, inverse-gamma, inverse-chi-squared, log-cauchy, log-logistic, log-normal, maxwell-boltzmann
# generalized normal distribution, fishers z-distribution
# to fix - t
# to add - laplace from exp, log-cauchy from cauchy, dirichlet, negative binomial, zeta,
# rice, q-exponential, q-normal, q-weibull

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
        shape parameter in beta distribution

    returns
    -------
    value in beta distr for random variable : float
    '''
    num = (x**(alpha -1)) * ((1-x)**(beta - 1))
    dem = beta_function(alpha, beta)
    return num / dem

def beta_prime_distribution(x, alpha, beta):
    '''
    two parameters -  shape alpha, shape beta,
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    alpha : float (positive)
        shape paramter in  beta prime distribution
    beta : float
        shape parameter in beta prime distribution

    returns
    -------
    value in beta prime distr for random variable : float
    '''
    num = (x**(alpha -1)) * ((1+x)**(-alpha - beta))
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

def chi_distribution(x, v):
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

    returns
    -------
    value in exponential distr for random variable : float
    '''
    num = (2 ** (1 - (v/2 ))) * (x ** (v-1)) * np.exp( -(x * x) / 2)
    den = integral_gamma_function(v /2)
    return num / den
    
def chi_distribution_from_squared(x, v, theta=2):
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
    # return [n ** .5 for n in int_gamma_distribution(x, (v/2), theta)]
    return int_gamma_distribution(x, (v/2), theta) ** .5

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

def logit_normal_distribution(x, sigma, mu):
    '''
    two parameters - squared scale, location
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    sigma : float
        squared scale parameter for logit-normal distribution
    mu : float (positive)
        location parameter for logit-normal distribution

    returns
    -------
    value in logit-normal distr for random variable : float
    '''
    coef_1 = (1 / (sigma * (2 * np.pi)** .5))
    random_var_1 = (1 / (x * (1 - x) ) )
    # logit = math.log(np.abs(x)) - math.log(1 - np.abs(x))
    exponent = ((logit(x) - mu) ** 2) / (2 * sigma ** 2)
    return coef_1 * random_var_1 * np.exp(-exponent)

def generalized_normal_distribution(x, mu, alpha, beta):
    '''
    three parameters - location, scale, shape
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    mu : float
        squared scale parameter for generalized normal distribution
    alpha : float (positive)
        location parameter for generalized normal distribution
    beta : float (positive)
        location parameter for generalized normal distribution

    returns
    -------
    value in generalized normal distr for random variable : float
    '''
    coef = beta / (2 * alpha * integral_gamma_function(1/beta))
    exponent = (np.abs(x - mu) / alpha) ** beta
    return coef * np.exp(- exponent)

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

def lomax_distribution(x, alpha, lambda_):
    '''
    two parameters - shape, scale
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    alpha : float (positive)
        shape parameter for lomax distribution
    lambda_ : float (positive)
        scale parameter for lomax distribution

    returns
    -------
    value in lomax distr for random variable : float
    '''
    return (alpha * lambda_) * ( (1 + (x / lambda_)) ** (- (alpha + 1)) )


def burr_distribution(x, c, k):
    '''
    two parameters - shape, scale
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    c : float (positive)
        shape parameter for burr distribution
    k : float (positive)
        scale parameter for burr distribution

    returns
    -------
    value in burr distr for random variable : float
    '''
    top_exp = (c-1)
    bottom_exp = (k+1)
    num = (x**top_exp)
    den = (1 + x ** c)
    random_var = num / den
    const = c * k
    return const* random_var

def inverse_gamma_distribution(x, alpha, beta):
    '''
    two parameters -  shape k, scale beta, 
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    alpha : int (positive)
        shape paramter in inverse-gamma distribution
    beta : int (positive)
        scale parameter in inverse-gamma distribution

    returns
    -------
    value in inverse-gamma distr for random variable : float
    
    '''
    coef = (beta ** alpha) / integral_gamma_function(alpha)
    return coef * (x **(-alpha -1)) * np.exp(- beta /  x)

def inverse_chi_squared_distribution(x, v, beta=.5):
    '''
    one parameter -  shape v (known as degrees of freedom),
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    v : int (positive)
        shape paramter in invers-chi-squared distribution
        'degrees of freedom' in inverse-chi-squared
    beta : .5 (int)
        known as scale parameter in inverse-gamma distribution,
        it is always =.5 for the inverse-chi-squared distribution

    returns
    -------
    value in inverse-chi-squared distr for random variable : float
    '''
    return inverse_gamma_distribution(x, (v/2), beta) 

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

def kumaraswamy_distribution(x, a, b):
    '''
    two parameters -  shape alpha, shape beta,
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    alpha : float (positive)
        shape paramter in  kumaraswamy distribution
    beta : float (positive)
        shape parameter in kumaraswamy distribution

    returns
    -------
    value in kumaraswamy distr for random variable : float
    '''
    return a * b * (x ** (a - 1)) * ( (1 - x ** a) ** (b - 1))

def nakagami_distribution(x, mu, omega):
    '''
    two parameters -  shape mu, spread omega,
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    mu : float (positive)
        shape paramter in  nakagami distribution
    omega : float (positive)
        spread parameter in nakagami distribution

    returns
    -------
    value in nakagami distr for random variable : float
    '''
    coef_1 = 2 / integral_gamma_function(mu)
    coef_2 = (mu / omega) ** mu
    return coef_1 * coef_2 * (x ** ((2 * mu) - 1) ) * np.exp( - (mu / omega) * x ** 2)

def logistic_distribution(x, mu, scale):
    '''
    two parameters -  shape mu, spread omega,
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    mu : float 
        location paramter in  logistic distribution
    scale : float (positive)
        scale parameter in logistic distribution

    returns
    -------
    value in logistic distr for random variable : float
    '''
    expo = -((x - mu) / scale)
    num = np.exp(expo)
    den = scale * (1 + np.exp(expo)) ** 2
    return num / den

def exponential_logarithmic_distribution(x, p, beta):
    '''
    two parameters - probability, rate
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    p : float 
        probability paramter in  exponential-logarithmic distribution
    beta : float (positive)
        rate parameter in exponential-logarithmic distribution

    returns
    -------
    value in exponential-logarithmic distr for random variable : float
    '''
    return (beta* (1-p) * np.exp(-beta * x)) / ((1 - (1-p) * np.exp(-beta * x)) * (- np.log(p)))

def gompertz_distribution(x, eta, beta):
    '''
    two parameters - shape, scale
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    eta : float (positive)
        shape paramter in  gompertz distribution
    beta : float (positive)
        scale parameter in gompertz distribution

    returns
    -------
    value in gompertz distr for random variable : float
    '''
    # coef = beta * eta
    # exponent_2= np.exp(beta * x)
    # exponent = eta + (beta * x) - (eta * exponent_2)
    # return coef * np.exp(exponent)
    # return   np.exp(eta + (beta * x) - (eta * np.exp(beta * x)))
    #  second version 
    # return eta * (np.exp(beta * x)) * np.exp((- (eta / beta))* ((np.exp(beta * x)) - 1))
    # third version
    return eta * (beta ** x) * np.exp( - eta * ( ((beta ** x) -1) / (np.log(beta)) ))

def log_cauchy_distribution(x, mu, sigma):
    '''
    two parameters

    params
    ------
    x : float
        random variable
    mu : float
        location parameter for log-cauchy distribution
    sigma : float (positive)
        scale parameter for log-cauchy distribution    

    returns 
    -------
    value in log-cauchy distr for random variable : float
    '''
    coef = (1 / (x * np.pi))
    return coef * (sigma / ( ((np.log(x) - mu) **2) + sigma ** 2) )

def log_cauchy_distribution_from_cauchy(x, mu, sigma):
    '''
    two parameters

    params
    ------
    x : float
        random variable
    mu : float
        location parameter for log-cauchy distribution
    sigma : float (positive)
        scale parameter for log-cauchy distribution    

    returns 
    -------
    value in log-cauchy distr for random variable : float
    '''
    return np.exp(cauchy_distribution(x, mu, sigma))

def log_logistic_distribution(x,alpha, beta):
    '''
    two parameters -  scale mu, shape omega,
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    alpha : float 
        scale paramter in  log-logistic distribution
    beta : float (positive)
        shape parameter in log-logistic distribution

    returns
    -------
    value in log-logistic distr for random variable : float
    '''
    num = (beta / alpha) * ((x / alpha) ** (beta - 1))
    den = (1 + ((x / alpha)** beta) ) ** 2
    return num / den

def log_normal_distribution(x, mu, sigma):
    '''
    two parameters -  shape mu, scale sigma,
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    mu : float 
        shape paramter in  log-normal distribution
    sigma : float (positive)
        scale parameter in log-normal distribution

    returns
    -------
    value in log-normal distr for random variable : float
    '''
    exponent = (((np.log(x)) - mu) ** 2 ) / (2 *sigma ** 2)
    coef = 1 / (x * sigma * ( (sigma * np.pi) ** .5 ))
    return coef * np.exp(- exponent)

def maxwell_boltzmann_distribution(x, a):
    '''
    one parameter - scale
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    a : float 
        scale paramter in  maxwell-boltzmann distribution
    
    returns
    -------
    value in maxwell-boltzmann distr for random variable : float
    '''
    coef = (2 / np.pi) ** .5
    exponent = (- (x ** 2)) / (2 * a ** 2)
    return coef * ( ((x **2) * np.exp(exponent) ) / a ** 3)

def fishers_z_distribution(x, degree_1, degree_2):
    '''
    two parameters - both degrees of freedom
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    degree_1 : float 
        scale paramter in  fishers z-distribution 
    degree_2 : float 
        scale paramter in  fishers z-distribution 

    returns
    -------
    value in fishers z distr for random variable : float
    '''
    coef = (2 * (degree_1 ** (degree_1 /2)) *  (degree_2 ** (degree_2 /2))) / beta_function((degree_1/2), (degree_2 / 2))
    return coef * (np.exp(degree_1 * x) / ((degree_1 * np.exp(2 * x) + degree_2) ** ((degree_1 + degree_2) / 2)) )


def continuous_bernoulli_distribution(x, lambda_):
    '''
    one parameters - lambda
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    lambda_ : float 
        shape paramter in  continuous bernoulli distribution

    returns
    -------
    value in fishers continuous bernoulli distr for random variable : float
    '''
    if lambda_ == .5:
        c = 2
    else:
        c = (2 * np.arctanh(1 - (2 * lambda_))) / (1 - (2 * lambda_))
    return c * (lambda_ ** x) * ((1 - lambda_) ** (1-x))

def dagum_distribution(x, p, a, b):
    '''
    three parameters - shape, shape, and scale
    x value is a random variable to pass in
    params
    ------
    x : float
        random variable
    p : float 
        shape paramter in  dagum distribution
    a : float 
        shape paramter in  dagum distribution
    b : float 
        scale paramter in  dagum distribution
    returns
    -------
    value in dagum distr for random variable : float
    '''
    coef = (a * p) / x
    num = (x / b) ** (a * p)
    den = (( (x/b) ** a) + 1) ** (p + 1)
    return coef * (num / den)

def q_exponential_distribution(x, q, lambda_):
    '''
    '''
    pass

def q_gaussian_distribution(x, q, beta):
    '''
    '''
    pass

def q_weibull_distribution(x, q, lambda_, k):
    '''
    '''
    pass

def slash_distribution(x):
    # if x == 0:
    # return generalized_normal_distribution(x, 0, 1, 2)
    # return beta_distribution(x, 1, 1)
    # return generalized_normal_distribution(x, 0, 1, 2) / beta_distribution(x, 1, 1)
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