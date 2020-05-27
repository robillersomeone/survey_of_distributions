import numpy as np
import distributions as ds
np.set_printoptions(suppress=True)

# get values for support (0,20] to plot
x_gamma_values = np.arange(0, 20, .05)[1:]

# pass x values to gamma distribution
y_gamma_values = ds.gamma_distribution(x_gamma_values, 2, 2)
# with the integral implementation
int_y_gamma_values_1_2 = ds.int_gamma_distribution(x_gamma_values, 1, 2)
int_y_gamma_values_2_2 = ds.int_gamma_distribution(x_gamma_values, 2, 2)
int_y_gamma_values_3_2 = ds.int_gamma_distribution(x_gamma_values, 3, 2)
int_y_gamma_values_5_1 = ds.int_gamma_distribution(x_gamma_values, 5, 1)
int_y_gamma_values_9_1 = ds.int_gamma_distribution(x_gamma_values, 9, 1)

# check for different gamma function implementations
# if y_gamma_values.all() == int_y_gamma_values.all():
#     print('cool')

# rename 'em
x =  x_gamma_values
y1 = int_y_gamma_values_1_2
y2 = int_y_gamma_values_2_2
y3 = int_y_gamma_values_3_2

# stack, pair down, and export as json for graphing

# stack
# gamma_data = np.stack((x, y1 = int_y_gamma_values_1_2, int_y_gamma_values_2_2, int_y_gamma_values_3_2), axis =1)
#  pair down this is done to have a light weight approximation the distribution for the site
# gamma_paired_down = np.round(gamma_paired_down[[0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 390]], 5)
# # list of dictionaries for json
# [{'x':x[0], 'y':x[1]} for x in gamma_paired_down[:]]




# # need to generate numbers to pass into the beta

# # this is the support for beta
x_beta_values = np.arange(0, 1, .01)[1:]
# # print(x_beta_values)
y_beta_values = ds.beta_distribution(x_beta_values, 2, 5)


y_erlang_values = ds.erlang_distribution(x_gamma_values, 9, 1)

y_exponential_values = ds.exponential_distribution(x_gamma_values, 1)
# # print(y_exponential_values)

# # just takes x_gamma_values, chi-squared and gamma have the same support
y_chi_squared_values = ds.chi_squared_distribution(x_gamma_values, 6)





# # for now the normal distribution is approximated using the central limit theorem

x_gamma_values_getting_normal = np.arange(0, 2, .01)[1:]
y_gamma_values_int = ds.int_gamma_distribution(x_gamma_values_getting_normal, 25, 1/25)





# # # np.savetxt('data/baseline_x.csv', x_gamma_values, delimiter=',') 
# # np.savetxt('data/int_y_gamma_values_1_2.csv', int_y_gamma_values_1_2, delimiter=',') 
# # np.savetxt('data/int_y_gamma_values_2_2.csv', int_y_gamma_values_2_2, delimiter=',') 
# # np.savetxt('data/int_y_gamma_values_3_2.csv', int_y_gamma_values_3_2, delimiter=',') 
# # np.savetxt('data/int_y_gamma_values_5_1.csv', int_y_gamma_values_5_1, delimiter=',') 
# # np.savetxt('data/int_y_gamma_values_9_1.csv', int_y_gamma_values_9_1, delimiter=',') 

# # saving in column wise format
# # test_x = np.column_stack((x_gamma_values, int_y_gamma_values_1_2), int_y_gamma_values_2_2)
# # test_x =  np.stack((x_gamma_values, int_y_gamma_values_1_2), int_y_gamma_values_2_2),axis=1)
# # np.savetxt('data/test.csv', test_x, delimiter=',') 
# # print(type(x_gamma_values))