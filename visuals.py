import distributions as ds
import matplotlib.pyplot as plt

def plotting(title, x_values, y_values, color = 'blue', legend = None):
    plt.title(title)
    plt.plot(x_values, y_values, color)
    if legend != None:
        plt.legend(legend, loc='upper right')
    plt.show()

# gamma
# ds.int_y_gamma_values_1_2
# ds.int_y_gamma_values_2_2
# ds.int_y_gamma_values_3_2
# ds.int_y_gamma_values_5_1
# ds.int_y_gamma_values_9_1

# plt.title('gamma distributions')
# plt.plot(ds.x_gamma_values, ds.int_y_gamma_values_1_2)
# plt.plot(ds.x_gamma_values, ds.int_y_gamma_values_2_2)
# plt.plot(ds.x_gamma_values, ds.int_y_gamma_values_3_2)
# plt.plot(ds.x_gamma_values, ds.int_y_gamma_values_5_1)
# plt.plot(ds.x_gamma_values, ds.int_y_gamma_values_9_1)
# plt.legend(['alpha=1 β=2', 'alpha=2 β=2', 'alpha=3 β=2', 'alpha=5 β=1', 'alpha=9 β=1'], loc='upper right')
# plt.savefig('imgs/gamma_distributions.png', format="png")
# plt.show()
# plt.savefig('imgs/gamma_distributions.png', format="png")

# beta

beta_title = 'beta distribution \n alpha=2, β=5'
beta_x_values, beta_y_values = ds.x_beta_values, ds.y_beta_values
beta_color='blue'
# # plt.savefig('imgs/beta_distribution_2_5.png', format="png")

# erlang

erlang_title = 'erlang distribution \n k=9, θ=1'
erlang_x_values, erlang_y_values = ds.x_gamma_values, ds.y_erlang_values
erlang_color='purple'
# plt.savefig('imgs/erlang_distribution_9_1.png', format="png")

# exponential

exp_title = 'exponential distribution \n λ=1'
exp_x_values, exp_y_values = ds.x_gamma_values, ds.y_exponential_values
# plt.savefig('imgs/exponential_distribution_1.png', format="png")

# chi-squared

chi_title = 'chi-squared distribution \n k=3'
chi_x_values, chi_y_values = ds.x_gamma_values, ds.y_chi_squared_values
# plt.savefig('imgs/approximated normal distribution_25.png', format="png")

# normal

normal_title = 'approximated normal distribution \n k=25, θ=1/25'
# normal_x_values, normal_y_values = ds.x_gamma_values_getting_normal, ds.y_gamma_values_int
# # plt.savefig('imgs/approximated normal distribution_25.png', format="png")

# f

f_title = 'f distribution \n k=??, θ=1?'
f_x_values, f_y_values = ds.x_f_values, ds.y_f_values
# # plt.savefig('imgs/approximated normal distribution_25.png', format="png")

plotting(erlang_title, erlang_x_values, erlang_y_values, erlang_color)
plt.savefig('imgs/erlang_distribution_9_1.png', format="png")
