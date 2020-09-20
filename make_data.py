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

# beta prime
x_beta_prime_values = np.arange(0, 5, .02)[1:]

y_beta_prime_values_1_1 = ds.beta_prime_distribution(x_beta_prime_values, 1, 1)
y_beta_prime_values_1_2 = ds.beta_prime_distribution(x_beta_prime_values, 1, 2)
y_beta_prime_values_2_1 = ds.beta_prime_distribution(x_beta_prime_values, 2, 1)
y_beta_prime_values_2_3 = ds.beta_prime_distribution(x_beta_prime_values, 2, 3)

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

# lomax
x_lomax_values = np.arange(1, 5, .05)[:]

y_lomax_values_1_2 = ds.lomax_distribution(x_lomax_values, 1, 2)
y_lomax_values_2_2 = ds.lomax_distribution(x_lomax_values, 2, 2)
y_lomax_values_4_2 = ds.lomax_distribution(x_lomax_values, 4, 2)
y_lomax_values_6_1 = ds.lomax_distribution(x_lomax_values, 6, 1)

# burr
x_burr_values = np.arange(0, 5, .05)[1:]

y_burr_values_1_1 = ds.burr_distribution(x_burr_values, 1, 1)
y_burr_values_1_2 = ds.burr_distribution(x_burr_values, 1, 2)
y_burr_values_1_3 = ds.burr_distribution(x_burr_values, 1, 3)
y_burr_values_2_1 = ds.burr_distribution(x_burr_values, 2, 1)
y_burr_values_3_1 = ds.burr_distribution(x_burr_values, 3, 1)

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

# chi

x_chi_values = np.arange(0, 4, .01)[1:]
# x_chi_values = np.arange(0, 20, .05)[1:]

y_chi_values_1 = ds.chi_distribution(x_chi_values, 1)
y_chi_values_2 = ds.chi_distribution(x_chi_values, 2)
y_chi_values_3 = ds.chi_distribution(x_chi_values, 3)
y_chi_values_4 = ds.chi_distribution(x_chi_values, 4)
y_chi_values_5 = ds.chi_distribution(x_chi_values, 5)
y_chi_values_6 = ds.chi_distribution(x_chi_values, 6)



# kumaraswamy
x_kumaraswamy_values = x_beta_values = np.arange(0, 1, .01)[1:]

y_kumaraswamy_values_half_half = ds.kumaraswamy_distribution(x_kumaraswamy_values, .5, .5)
y_kumaraswamy_values_half_1 = ds.kumaraswamy_distribution(x_kumaraswamy_values, .5, 1)
y_kumaraswamy_values_1_1 = ds.kumaraswamy_distribution(x_kumaraswamy_values, 1, 1)
y_kumaraswamy_values_2_2 = ds.kumaraswamy_distribution(x_kumaraswamy_values, 2, 2)
y_kumaraswamy_values_2_3 = ds.kumaraswamy_distribution(x_kumaraswamy_values, 2, 3)
y_kumaraswamy_values_2_5 = ds.kumaraswamy_distribution(x_kumaraswamy_values, 2, 5)


# nakagami
x_nakagami_values = np.arange(0, 4, .01)[1:]

y_nakagami_values_half_1 = ds.nakagami_distribution(x_nakagami_values, .5, 1)
y_nakagami_values_1_1 = ds.nakagami_distribution(x_nakagami_values, 1, 1)
y_nakagami_values_1_3 = ds.nakagami_distribution(x_nakagami_values, 1, 3)
y_nakagami_values_2_1 = ds.nakagami_distribution(x_nakagami_values, 2, 1)
y_nakagami_values_2_2 = ds.nakagami_distribution(x_nakagami_values, 2, 2)

# logistic
x_logistic_values = np.arange(-5, 20, .1)[1:]

y_logistic_values_2_1 = ds.logistic_distribution(x_logistic_values, 2, 1)
y_logistic_values_5_2 = ds.logistic_distribution(x_logistic_values, 5, 2)
y_logistic_values_6_2 = ds.logistic_distribution(x_logistic_values, 6, 2)
y_logistic_values_9_3 = ds.logistic_distribution(x_logistic_values, 9, 3)
y_logistic_values_9_4 = ds.logistic_distribution(x_logistic_values, 9, 4)

# logit normal
x_logit_normal_values = np.arange(0, 1, .01)[1:]

y_logit_normal_values_point_3_0 = ds.logit_normal_distribution(x_logit_normal_values, .32, 0)
y_logit_normal_values_1_0 = ds.logit_normal_distribution(x_logit_normal_values, 1, 0)
y_logit_normal_values_3_0 = ds.logit_normal_distribution(x_logit_normal_values, 3.16, 0)
y_logit_normal_values_point_3_1 = ds.logit_normal_distribution(x_logit_normal_values, .32, 1)
y_logit_normal_values_1_1 = ds.logit_normal_distribution(x_logit_normal_values, 1, 1)
y_logit_normal_values_3_1 = ds.logit_normal_distribution(x_logit_normal_values, 3.16, 1)

# exponential-logarithmic
x_exponential_logarthmic_values = np.arange(0, 3, .01)[1:]

y_exponential_logarthmic_values_half_1 = ds.exponential_logarithmic_distribution(x_exponential_logarthmic_values, .5, 1)
y_exponential_logarthmic_values_half_2 = ds.exponential_logarithmic_distribution(x_exponential_logarthmic_values, .5, 2)
y_exponential_logarthmic_values_half_3 = ds.exponential_logarithmic_distribution(x_exponential_logarthmic_values, .5, 3)

# gompertz
x_gompertz_values = np.arange(0, 5, .01)[:]

# y_gompertz_values_point_1_1 = ds.gompertz_distribution(x_gompertz_values, .1, 1)
# y_gompertz_values_2_1 = ds.gompertz_distribution(x_gompertz_values, 2.0, 1)
# y_gompertz_values_3_1 = ds.gompertz_distribution(x_gompertz_values, 3, 1)
y_gompertz_values_1_2 = ds.gompertz_distribution(x_gompertz_values, 1, 2)
y_gompertz_values_point_1_2 = ds.gompertz_distribution(x_gompertz_values, .1, 2)
y_gompertz_values_half_3 = ds.gompertz_distribution(x_gompertz_values, .5, 3)

# inverse-gamma 
x_inverse_gamma_values = np.arange(0, 3, .01)[1:]

y_inverse_gamma_values_1_1 = ds.inverse_gamma_distribution(x_inverse_gamma_values, 1, 1)
y_inverse_gamma_values_2_1 = ds.inverse_gamma_distribution(x_inverse_gamma_values, 2, 1)
y_inverse_gamma_values_3_1 = ds.inverse_gamma_distribution(x_inverse_gamma_values, 3, 1)
y_inverse_gamma_values_3_half = ds.inverse_gamma_distribution(x_inverse_gamma_values, 3, .5)

# inverse-chi-squared
x_inverse_chi_squared_values = np.arange(0, 1, .01)[1:]

y_inverse_chi_squared_values_1 = ds.inverse_chi_squared_distribution(x_inverse_chi_squared_values, 1)
y_inverse_chi_squared_values_2 = ds.inverse_chi_squared_distribution(x_inverse_chi_squared_values, 2)
y_inverse_chi_squared_values_3 = ds.inverse_chi_squared_distribution(x_inverse_chi_squared_values, 3)
y_inverse_chi_squared_values_4 = ds.inverse_chi_squared_distribution(x_inverse_chi_squared_values, 4)
y_inverse_chi_squared_values_5 = ds.inverse_chi_squared_distribution(x_inverse_chi_squared_values, 5)
y_inverse_chi_squared_values_6 = ds.inverse_chi_squared_distribution(x_inverse_chi_squared_values, 6)

# log-cauchy
x_log_cauchy_values = np.arange(0, 3, .01)[1:]

y_log_cauchy_values_0_half = ds.log_cauchy_distribution(x_log_cauchy_values, 0, .5)
y_log_cauchy_values_0_1 = ds.log_cauchy_distribution(x_log_cauchy_values, 0, 1)
y_log_cauchy_values_0_2 = ds.log_cauchy_distribution(x_log_cauchy_values, 0, 2)
y_log_cauchy_values_1_half = ds.log_cauchy_distribution(x_log_cauchy_values, 1, .5)
y_log_cauchy_values_1_1 = ds.log_cauchy_distribution(x_log_cauchy_values, 1, 1)

# log-logistic
x_log_logistic_values = np.arange(0, 3, .01)[1:]

y_log_logistic_values_1_half = ds.log_logistic_distribution(x_log_logistic_values, 1, .5)
y_log_logistic_values_1_1 = ds.log_logistic_distribution(x_log_logistic_values, 1, 1)
y_log_logistic_values_1_2 = ds.log_logistic_distribution(x_log_logistic_values, 1, 2)
y_log_logistic_values_1_4 = ds.log_logistic_distribution(x_log_logistic_values, 1, 4)
y_log_logistic_values_1_8 = ds.log_logistic_distribution(x_log_logistic_values, 1, 8)

# log-normal
x_log_normal_values = np.arange(0, 3, .01)[1:]

y_log_normal_values_0_quarter = ds.log_normal_distribution(x_log_normal_values, 0, .25)
y_log_normal_values_0_half = ds.log_normal_distribution(x_log_normal_values, 0, .5)
y_log_normal_values_0_1 = ds.log_normal_distribution(x_log_normal_values, 0, 1)

# maxwell-boltzmann
x_maxwell_boltzmann_values = np.arange(0, 20, .05)[1:]

y_maxwell_boltzmann_values_1 = ds.maxwell_boltzmann_distribution(x_maxwell_boltzmann_values, 1)
y_maxwell_boltzmann_values_2 = ds.maxwell_boltzmann_distribution(x_maxwell_boltzmann_values, 2)
y_maxwell_boltzmann_values_5 = ds.maxwell_boltzmann_distribution(x_maxwell_boltzmann_values, 5)

# generalized normal
x_generalized_normal_values = np.arange(-3, 3, .01)[:]

y_generalized_normal_values_0_1_half = ds.generalized_normal_distribution(x_generalized_normal_values, 0, 1, .5)
y_generalized_normal_values_0_1_1 = ds.generalized_normal_distribution(x_generalized_normal_values, 0, 1, 1)
y_generalized_normal_values_0_1_1_half = ds.generalized_normal_distribution(x_generalized_normal_values, 0, 1, 1.5)
y_generalized_normal_values_0_1_3 = ds.generalized_normal_distribution(x_generalized_normal_values, 0, 1, 3)
y_generalized_normal_values_0_1_8 = ds.generalized_normal_distribution(x_generalized_normal_values, 0, 1, 8)

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

