import os, sys
sys.path.append(os.path.abspath('../.'))

# import make_data as ds
# import distributions as ds
import matplotlib.pyplot as plt
# to run form main dir for now
import survey_of_distributions.make_data as ds

def plotting(title, x_values, y_values, color = 'blue', legend = None):
    plt.title(title)
    plt.plot(x_values, y_values, color)
    if legend != None:
        plt.legend(legend, loc='upper right')
    plt.show()

# beta

beta_title = 'beta distribution \n alpha=2, β=5'
beta_x_values, beta_y_values_2_5 = ds.x_beta_values, ds.y_beta_values_2_5
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
# chi_x_values, chi_y_values = ds.x_gamma_values, ds.y_chi_squared_values
# plt.savefig('imgs/chi_squared_distribution_3.png', format="png")

# normal

normal_title = 'approximated normal distribution \n k=25, θ=1/25'
normal_x_values, normal_y_values = ds.x_gamma_values_getting_normal, ds.y_gamma_values_getting_normal
# # plt.savefig('imgs/approximated normal distribution_25.png', format="png")

# f

f_title = 'f distribution \n k=??, θ=1?'
f_x_values, f_y_values = ds.x_gamma_values, ds.y_f_values_5_2
f_color = 'red'
# # plt.savefig('imgs/f_distribution_.png', format="png")

# plotting(f_title, f_x_values, f_y_values, f_color)

# plt.title('f distributions')
# plt.plot(ds.x_f_values, ds.y_f_values_1_1)
# plt.plot(ds.x_f_values, ds.y_f_values_2_1)
# plt.plot(ds.x_f_values, ds.y_f_values_5_2)
# plt.plot(ds.x_f_values, ds.y_f_values_10_1)
# plt.legend(['d1=1 d2=1', 'd1=2 d2=1', 'd1=5 d2=2', 'd1=10 d2=1'], loc='upper right')



# plot for exp, erlang, chi, beta

# plotting(erlang_title, erlang_x_values, erlang_y_values, erlang_color)
# plt.savefig('imgs/erlang_distribution_9_1.pngerlang_distribution_9_1.pnsaf', format="png")

# beta
# plt.title('beta \n alpha=β')
# plt.plot(ds.x_beta_values, ds.y_beta_values_1_1)
# plt.plot(ds.x_beta_values, ds.y_beta_values_2_2)
# plt.plot(ds.x_beta_values, ds.y_beta_values_3_3)
# plt.plot(ds.x_beta_values, ds.y_beta_values_4_4)
# plt.plot(ds.x_beta_values, ds.y_beta_values_5_5)
# plt.plot(ds.x_beta_values, ds.y_beta_values_6_6)
# plt.legend(['alpha=β=2','alpha=β=3','alpha=β=4','alpha=β=5','alpha=β=6'], loc='upper right')

# plt.plot(ds.x_beta_values, ds.y_beta_values_frac_1_1)
# plt.plot(ds.x_beta_values, ds.y_beta_values_frac_1_25)
# plt.plot(ds.x_beta_values, ds.y_beta_values_frac_1_5)
# plt.plot(ds.x_beta_values, ds.y_beta_values_frac_1_75)
# plt.plot(ds.x_beta_values, ds.y_beta_values_frac_1_9)
# plt.legend(['alpha=β=.1','alpha=β=.25','alpha=β=.5','alpha=β=.75','alpha=β=.9'], loc='upper right')

# arcsin
plt.title('arcsin \n alpha=β=.5')
plt.plot(ds.x_beta_values, ds.y_arcsin_values)

# gamma

# plt.title('gamma distributions')
# plt.plot(ds.x_gamma_values, ds.int_y_gamma_values_1_2)
# plt.plot(ds.x_gamma_values, ds.int_y_gamma_values_2_2)
# plt.plot(ds.x_gamma_values, ds.int_y_gamma_values_3_2)
# plt.plot(ds.x_gamma_values, ds.int_y_gamma_values_5_1)
# plt.plot(ds.x_gamma_values, ds.int_y_gamma_values_9_1)
# plt.legend(['alpha=1 θ=2', 'alpha=2 θ=2', 'alpha=3 θ=2', 'alpha=5 θ=1', 'alpha=9 θ=1'], loc='upper right')
# plt.savefig('../imgs/gamma_distributions.png', format="png")
plt.show()
# plt.savefig('imgs/gamma_distributions.png', format="png")

# updated location to save
# plt.savefig('./imgs/beta_distributions_alpha_equals_beta.png', format="png")