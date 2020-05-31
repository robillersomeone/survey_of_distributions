import numpy as np
# import survey_of_distributions.distributions as ds
import distributions as ds
np.set_printoptions(suppress=True)


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
    stacked = np.stack((x, y_chi), axis=1)
    # get a subset of the data
    subset = np.round(stacked[[0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 390]], 5)

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
y_beta_values = ds.beta_distribution(x_beta_values, 2, 5)

# support for f 
x_f_values = np.arange(0, 5, .02)[1:]
y_f_values_1_1 = ds.f_distribution(x_f_values, 1, 1)
y_f_values_2_1 = ds.f_distribution(x_f_values, 2, 1)
y_f_values_5_2 = ds.f_distribution(x_f_values, 5, 2)
y_f_values_10_1 = ds.f_distribution(x_f_values, 10, 1)

# for now the normal distribution is approximated using the central limit theorem

x_gamma_values_getting_normal = np.arange(0, 2, .01)[1:]
y_gamma_values_getting_normal = ds.int_gamma_distribution(x_gamma_values_getting_normal, 25, 1/25)

