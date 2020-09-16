import numpy as np
import survey_of_distributions.distributions as ds
# import distributions as ds
np.set_printoptions(suppress=True)


'''
use import survey_of_distributions.distributions as ds when calling from viz directory
d3 function
support for gamma
gamma and special cases
support for beta
beta and special cases
support for f
f 
support for laplace
laplace
rayleigh
normal via CLT
'''

def data_for_d3(x, y):
    """
    function for data used in website,
    very small subset to keep website light

    params
    ------
    x : numpy array
        support for the distribution
    y : numpy array
        values the pdf takes for the given distribution
    returns
    -------
    """
    # stack into numpy array
    stacked = np.stack((x, y), axis=1)
    # get a subset of the data
    if len(stacked)>101:
        # gamma support (0,20)
        subset = np.round(stacked[[0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 390]], 5)
    else:
         # beta support (0,``)
        subset = np.round(stacked[[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 98]], 5)

    # put subset in json format
    subset_json = [{'x':x[0], 'y':x[1]} for x in subset[:]]

    # save json data... not implemented
    # np.savetxt('data/int_y_gamma_values_1_2.csv', subset_json, delimiter=',') 

    return subset_json


# get values for support (0,20] to plot
x_gamma_values = np.arange(0, 20, .05)[1:]

# pass x values to gamma distribution
y_gamma_values_2_2 = ds.gamma_distribution(x_gamma_values, 2, 2)
# with the integral implementation
int_y_gamma_values_1_2 = ds.int_gamma_distribution(x_gamma_values, 1, 2)
int_y_gamma_values_2_2 = ds.int_gamma_distribution(x_gamma_values, 2, 2)
int_y_gamma_values_3_2 = ds.int_gamma_distribution(x_gamma_values, 3, 2)
int_y_gamma_values_5_1 = ds.int_gamma_distribution(x_gamma_values, 5, 1)
int_y_gamma_values_9_1 = ds.int_gamma_distribution(x_gamma_values, 9, 1)

# these three are special cases of the gamma distribution
y_erlang_values = ds.erlang_distribution(x_gamma_values, 9, 1)

y_exponential_values = ds.exponential_distribution(x_gamma_values, 1)

y_chi_6 = ds.chi_squared_distribution(x_gamma_values, 6)
y_chi_8 = ds.chi_squared_distribution(x_gamma_values,8)
 
# this is the support for beta
x_beta_values = np.arange(0, 1, .01)[1:]
# where alpha=beta for positive integers
y_beta_values_1_1 = ds.beta_distribution(x_beta_values, 1, 1)
y_beta_values_2_2 = ds.beta_distribution(x_beta_values, 2, 2)
y_beta_values_3_3 = ds.beta_distribution(x_beta_values, 3, 3)
y_beta_values_4_4 = ds.beta_distribution(x_beta_values, 4, 4)
y_beta_values_5_5 = ds.beta_distribution(x_beta_values, 5, 5)
y_beta_values_6_6 = ds.beta_distribution(x_beta_values, 6, 6)

# where alpha=beta for positive real numbers < 1
y_beta_values_frac_1_1 = ds.beta_distribution(x_beta_values, .1, .1)
y_beta_values_frac_1_25 = ds.beta_distribution(x_beta_values, .25, .25)
y_beta_values_frac_1_5 = ds.beta_distribution(x_beta_values, .5, .5)
y_beta_values_frac_1_75 = ds.beta_distribution(x_beta_values, .75, .75)
y_beta_values_frac_1_9 = ds.beta_distribution(x_beta_values, .9, .9)

y_beta_values_1_2 = ds.beta_distribution(x_beta_values, 1, 2)
y_beta_values_2_1 = ds.beta_distribution(x_beta_values, 2, 1)
y_beta_values_1_3 = ds.beta_distribution(x_beta_values, 1, 3)
y_beta_values_3_1 = ds.beta_distribution(x_beta_values, 3, 1)
y_beta_values_1_4 = ds.beta_distribution(x_beta_values, 1, 4)
y_beta_values_4_1 = ds.beta_distribution(x_beta_values, 4, 1)
y_beta_values_2_3 = ds.beta_distribution(x_beta_values, 2, 3)
y_beta_values_3_2 = ds.beta_distribution(x_beta_values, 3, 2)
y_beta_values_2_4 = ds.beta_distribution(x_beta_values, 2, 4)
y_beta_values_4_2 = ds.beta_distribution(x_beta_values, 4, 2)

y_beta_values_4_6 = ds.beta_distribution(x_beta_values, 4, 6)
y_beta_values_6_4 = ds.beta_distribution(x_beta_values, 6, 4)


y_beta_values_frac_1_4_6 = ds.beta_distribution(x_beta_values, .4, .6)
y_beta_values_frac_1_6_4 = ds.beta_distribution(x_beta_values, .6, .4)

y_arcsin_values = ds.beta_distribution(x_beta_values, .5, .5)

# support for f 
x_f_values = np.arange(0, 5, .02)[1:]

# f
y_f_values_1_1 = ds.f_distribution(x_f_values, 1, 1)
y_f_values_2_1 = ds.f_distribution(x_f_values, 2, 1)
y_f_values_5_2 = ds.f_distribution(x_f_values, 5, 2)
y_f_values_10_1 = ds.f_distribution(x_f_values, 10, 1)

x_f_values_d3 = np.arange(0, 5, .05)[1:]
y_f_values_2_2_d3 = ds.f_distribution(x_f_values_d3, 2, 2)

# support for laplace
x_laplace_values = np.arange(-10, 10, .05)[1:]

y_laplace_values_0_1 = ds.laplace_distribution(x_laplace_values, 0, 1)
y_laplace_values_0_2 = ds.laplace_distribution(x_laplace_values, 0, 2)
y_laplace_values_0_4 = ds.laplace_distribution(x_laplace_values, 0, 4)
y_laplace_values_2_2 = ds.laplace_distribution(x_laplace_values, 2, 2)

x_laplace_values_d3 = np.arange(0, 20, .05)[1:]
y_laplace_values_10_1_d3 = ds.laplace_distribution(x_laplace_values_d3, 10, 1)

# rayleigh
x_rayleigh_values = np.arange(0, 10, .025)[1:]

y_rayleigh_values_half = ds.rayleigh_distribution(x_rayleigh_values, .5)
y_rayleigh_values_1 = ds.rayleigh_distribution(x_rayleigh_values, 1)
y_rayleigh_values_2 = ds.rayleigh_distribution(x_rayleigh_values, 2)
y_rayleigh_values_3 = ds.rayleigh_distribution(x_rayleigh_values, 3)
y_rayleigh_values_4 = ds.rayleigh_distribution(x_rayleigh_values, 4)

x_rayleigh_values_d3 = np.arange(0, 5, .05)[1:]
y_rayleigh_values_1_d3 = ds.rayleigh_distribution(x_rayleigh_values_d3, 1)

# gumbel
x_gumbel_values = np.arange(-5, 20, .5)[1:]

y_gumbel_values_half_2 = ds.gumbel_distribution(x_gumbel_values, .5, 2)
y_gumbel_values_1_2 = ds.gumbel_distribution(x_gumbel_values, 1, 2)
y_gumbel_values_1_half_3 = ds.gumbel_distribution(x_gumbel_values, 1.5, 3)
y_gumbel_values_3_4 = ds.gumbel_distribution(x_gumbel_values, 3, 4)

y_gumbel_values_1_2_d3 = ds.gumbel_distribution(x_gamma_values, 1, 2)

# fréchet
x_frechet_values = np.arange(0, 4, .01)[1:]

y_frechet_values_1_1_0 = ds.frechet_distribution(x_frechet_values, 1, 1, 0)
y_frechet_values_2_1_0 = ds.frechet_distribution(x_frechet_values, 2, 1, 0)
y_frechet_values_3_1_0 = ds.frechet_distribution(x_frechet_values, 3, 1, 0)
y_frechet_values_1_2_0 = ds.frechet_distribution(x_frechet_values, 1, 2, 0)
y_frechet_values_2_2_0 = ds.frechet_distribution(x_frechet_values, 2, 2, 0)
y_frechet_values_3_2_0 = ds.frechet_distribution(x_frechet_values, 3, 2, 0)

x_frechet_values_d3 = np.arange(0, 5, .05)[1:]
y_frechet_values_2_1_0_d3 = ds.frechet_distribution(x_frechet_values_d3, 2, 1, 0)
# weibull
x_weibull_values = np.arange(0, 3, .01)[1:]

y_weibull_values_1_half = ds.weibull_distribution(x_weibull_values, 1, .5)
y_weibull_values_1_1 = ds.weibull_distribution(x_weibull_values, 1, 1)
y_weibull_values_1_1_half = ds.weibull_distribution(x_weibull_values, 1, 1.5)
y_weibull_values_1_5 = ds.weibull_distribution(x_weibull_values, 1, 5)

y_weibull_values_1_2 = ds.weibull_distribution(x_weibull_values, 1, 2)

x_weibull_values_d3 = np.arange(0, 5, .05)[1:]
y_weibull_values_1_1_d3 = ds.weibull_distribution(x_weibull_values_d3, 1, 1)
y_weibull_values_1_2_d3 = ds.weibull_distribution(x_weibull_values_d3, 1, 2)


# pareto
x_pareto_values = np.arange(1, 5, .05)[:]

y_pareto_values_1_1 = ds.pareto_distribution(x_pareto_values, 1, 1)
y_pareto_values_1_2 = ds.pareto_distribution(x_pareto_values, 1, 2)
y_pareto_values_1_3 = ds.pareto_distribution(x_pareto_values, 1, 3)

# cauchy
x_cauchy_values = np.arange(-4, 4, .05)[1:]

y_cauchy_values_0_half = ds.cauchy_distribution(x_cauchy_values, 0, .5)
y_cauchy_values_0_1 = ds.cauchy_distribution(x_cauchy_values, 0, 1)
y_cauchy_values_0_2 = ds.cauchy_distribution(x_cauchy_values, 0, 2)
y_cauchy_values_neg_2_1 = ds.cauchy_distribution(x_cauchy_values, -2, 1)

# levy
x_levy_values = np.arange(0, 5, .05)[1:]

y_levy_values_0_half = ds.levy_distribution(x_levy_values, 0, .5)
y_levy_values_0_1 = ds.levy_distribution(x_levy_values, 0, 1)
y_levy_values_0_2 = ds.levy_distribution(x_levy_values, 0, 2)
y_levy_values_0_4 = ds.levy_distribution(x_levy_values, 0, 4)
y_levy_values_0_8 = ds.levy_distribution(x_levy_values, 0, 8)


# for now the normal distribution is approximated using the central limit theorem

x_gamma_values_getting_normal = np.arange(0, 2, .01)[1:]
y_gamma_values_getting_normal = ds.int_gamma_distribution(x_gamma_values_getting_normal, 25, 1/25)

# data for d3

# print(data_for_d3(x_beta_values,y_beta_values_4_6))



# print(data_for_d3(x_f_values_d3,y_f_values_2_2_d3))

# print(data_for_d3(x_laplace_values_d3, y_laplace_values_10_1_d3))

# might have to put in gamma support x values ...
# print(data_for_d3(x_rayleigh_values_d3, y_rayleigh_values_1_d3))

# print(data_for_d3(x_gamma_values, y_gumbel_values_1_2_d3))
# print(data_for_d3(x_gumbel_values, y_gumbel_values_1_2))

# print(data_for_d3(x_frechet_values, y_frechet_values_2_1_0))
# print(data_for_d3(x_frechet_values_d3, y_frechet_values_2_1_0_d3))

# print(data_for_d3(x_weibull_values, y_weibull_values_1_1))
# print(data_for_d3(x_weibull_values_d3, y_weibull_values_1_1_d3))

# print(data_for_d3(x_weibull_values, y_weibull_values_1_2))
# print(data_for_d3(x_weibull_values_d3, y_weibull_values_1_2_d3))

