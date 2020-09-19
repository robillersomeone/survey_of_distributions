import os, sys
sys.path.append(os.path.abspath('../.'))

# import make_data as ds
# import distributions as ds
import matplotlib.pyplot as plt
# to run form main dir for now
import survey_of_distributions.make_data as ds


'''
plotting function
beta
erlang
exponential
chi-squared
normal
f
laplace
rayleigh
gumbel
fréchet
weibull
pareto
cauchy
lévy
'''

def plotting(title, x_values, y_values, color = 'blue', legend = None):
    plt.title(title)
    plt.plot(x_values, y_values, color)
    if legend != None:
        plt.legend(legend, loc='upper right')
    plt.show()

# beta

beta_title = 'beta distribution \n alpha=2, β=5'
beta_x_values, beta_y_values_2_5 = ds.x_beta_values, ds.y_beta_values_4_6
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


# laplace
# plt.title('laplace distribtuions')
# plt.plot(ds.x_laplace_values, ds.y_laplace_0_1)
# plt.plot(ds.x_laplace_values, ds.y_laplace_0_2)
# plt.plot(ds.x_laplace_values, ds.y_laplace_0_4)
# plt.plot(ds.x_laplace_values, ds.y_laplace_2_2)
# plt.legend(['μ=0 b=1','μ=0 b=2','μ=0 b=4','μ=2 b=2'], loc='upper right')

# rayleigh
# plt.title('rayleigh distribution')
# plt.plot(ds.x_rayleigh_values, ds.y_rayleigh_half)
# plt.plot(ds.x_rayleigh_values, ds.y_rayleigh_1)
# plt.plot(ds.x_rayleigh_values, ds.y_rayleigh_2)
# plt.plot(ds.x_rayleigh_values, ds.y_rayleigh_3)
# plt.plot(ds.x_rayleigh_values, ds.y_rayleigh_4)
# plt.legend(['σ=.5','σ=1','σ=2','σ=3', 'σ=4'], loc='upper right')


# gumbel
# plt.title('gumbel distribution')
# plt.plot(ds.x_gumbel_values, ds.y_gumbel_values_half_2)
# plt.plot(ds.x_gumbel_values, ds.y_gumbel_values_1_2)
# plt.plot(ds.x_gumbel_values, ds.y_gumbel_values_1_half_3)
# plt.plot(ds.x_gumbel_values, ds.y_gumbel_values_3_4)
# plt.legend(['μ=.5  β=2','μ=1 β=2','μ=1.5  β=3','μ=3  β=4'], loc='upper right')

# fréchet
# plt.title('fréchet distribution')
# plt.plot(ds.x_frechet_values, ds.y_frechet_values_1_1_0)
# plt.plot(ds.x_frechet_values, ds.y_frechet_values_2_1_0)
# plt.plot(ds.x_frechet_values, ds.y_frechet_values_3_1_0)
# plt.plot(ds.x_frechet_values, ds.y_frechet_values_1_2_0)
# plt.plot(ds.x_frechet_values, ds.y_frechet_values_2_2_0)
# plt.plot(ds.x_frechet_values, ds.y_frechet_values_3_2_0)
# plt.legend(['alpha=1 s=1 m=0','alpha=2 s=1 m=0','alpha=3 s=1 m=0','alpha=1 s=2 m=0', 'alpha=2 s=2 m=0', 'alpha=3 s=2 m=0'], loc='upper right')

# weibull
# plt.title('weibull distribution')
# plt.plot(ds.x_weibull_values, ds.y_weibull_values_1_half)
# plt.plot(ds.x_weibull_values, ds.y_weibull_values_1_1)
# plt.plot(ds.x_weibull_values, ds.y_weibull_values_1_1_half)
# plt.plot(ds.x_weibull_values, ds.y_weibull_values_1_5)
# plt.legend(['λ=1 k=.5','λ=1 k=1','λ=1 k=1.5','λ=1 k=5'], loc='upper right')

# pareto
# plt.title('pareto distribution')
# plt.plot(ds.x_pareto_values, ds.y_pareto_values_1_1)
# plt.plot(ds.x_pareto_values, ds.y_pareto_values_1_2)
# plt.plot(ds.x_pareto_values, ds.y_pareto_values_1_3)
# plt.legend(['x_min=1 alpha=1', 'x_min=1 alpha=2'], loc='upper right')
# plt.legend(['x_min=1 alpha=1', 'x_min=1 alpha=2', 'x_min=1 alpha=3'], loc='upper right')

# lomax
# plt.title('lomax distribution')
# plt.plot(ds.x_lomax_values, ds.y_lomax_values_1_2)
# plt.plot(ds.x_lomax_values, ds.y_lomax_values_2_2)
# plt.plot(ds.x_lomax_values, ds.y_lomax_values_4_2)
# plt.plot(ds.x_lomax_values, ds.y_lomax_values_6_1)
# plt.legend(['alpha=1 λ=2', 'alpha=2 λ=2', 'alpha=4 λ=2', 'alpha=6 λ=1'], loc='upper right')

# burr
# plt.title('burr distribution')
# plt.plot(ds.x_burr_values, ds.y_burr_values_1_1)
# plt.plot(ds.x_burr_values, ds.y_burr_values_1_2)
# plt.plot(ds.x_burr_values, ds.y_burr_values_1_3)
# plt.plot(ds.x_burr_values, ds.y_burr_values_2_1)
# plt.plot(ds.x_burr_values, ds.y_burr_values_3_1)
# plt.legend(['c=1 k=1', 'c=1 k=2', 'c=1 k=3','c=2 k=1', 'c=3 k=1'], loc='upper right')

# cauchy
# plt.title('cauchy distribution')
# plt.plot(ds.x_cauchy_values, ds.y_cauchy_values_0_half)
# plt.plot(ds.x_cauchy_values, ds.y_cauchy_values_0_1)
# plt.plot(ds.x_cauchy_values, ds.y_cauchy_values_0_2)
# plt.plot(ds.x_cauchy_values, ds.y_cauchy_values_neg_2_1)
# plt.legend(['x_knot=0 gamma=.5', 'x_knot=0 gamma=1', 'x_knot=0 gamma=2', 'x_knot=-2 gamma=1'], loc='upper right')

# levy
# plt.title('levy distribution')
# plt.plot(ds.x_levy_values, ds.y_levy_values_0_half)
# plt.plot(ds.x_levy_values, ds.y_levy_values_0_1)
# plt.plot(ds.x_levy_values, ds.y_levy_values_0_2)
# plt.plot(ds.x_levy_values, ds.y_levy_values_0_4)
# plt.plot(ds.x_levy_values, ds.y_levy_values_0_8)
# plt.legend(['μ=0 c=.5', 'μ=0 c=1', 'μ=0 c=2', 'μ=-2 c=4', 'μ=0 c=8'], loc='upper right')

# chi 
# plt.title('chi distribution')
# plt.plot(ds.x_chi_values, ds.y_chi_values_1)
# plt.plot(ds.x_chi_values, ds.y_chi_values_2)
# plt.plot(ds.x_chi_values, ds.y_chi_values_3)
# plt.plot(ds.x_chi_values, ds.y_chi_values_4)
# plt.plot(ds.x_chi_values, ds.y_chi_values_5)
# plt.legend(['k=1','k=2','k=3','k=4','k=5'], loc='upper right')

# kumaraswamy
# plt.title('kumaraswamy distribution')
# plt.plot(ds.x_kumaraswamy_values, ds.y_kumaraswamy_values_half_half)
# plt.plot(ds.x_kumaraswamy_values, ds.y_kumaraswamy_values_half_1)
# plt.plot(ds.x_kumaraswamy_values, ds.y_kumaraswamy_values_1_1)
# plt.plot(ds.x_kumaraswamy_values, ds.y_kumaraswamy_values_2_2)
# plt.plot(ds.x_kumaraswamy_values, ds.y_kumaraswamy_values_2_3)
# plt.plot(ds.x_kumaraswamy_values, ds.y_kumaraswamy_values_2_5)
# plt.legend(['alpha=.5 β=.5','alpha=2 β=2', 'alpha=2 β=3', 'alpha=2 β=5'], loc='upper right')

# nakagami
# plt.title('nakagami distribution')
# plt.plot(ds.x_nakagami_values, ds.y_nakagami_values_half_1)
# plt.plot(ds.x_nakagami_values, ds.y_nakagami_values_1_1)
# plt.plot(ds.x_nakagami_values, ds.y_nakagami_values_1_3)
# plt.plot(ds.x_nakagami_values, ds.y_nakagami_values_2_1)
# plt.plot(ds.x_nakagami_values, ds.y_nakagami_values_2_2)
# plt.legend(['μ=.5, omega=1', 'μ=1, omega=1', 'μ=.5, omega=3', 'μ=2, omega=1', 'μ=2, omega=2'], loc='upper right')

# logistic
# plt.title('logistic distribution')
# plt.plot(ds.x_logistic_values, ds.y_logistic_values_2_1)
# plt.plot(ds.x_logistic_values, ds.y_logistic_values_5_2)
# plt.plot(ds.x_logistic_values, ds.y_logistic_values_6_2)
# plt.plot(ds.x_logistic_values, ds.y_logistic_values_9_3)
# plt.plot(ds.x_logistic_values, ds.y_logistic_values_9_4)
# plt.legend(['μ=2, scale=1', 'μ=5, scale=2', 'μ=6, scale=2', 'μ=9, scale=3', 'μ=9, scale=4'], loc='upper right')

# logit normal
plt.title('logit-normal distribution')
plt.plot(ds.x_logit_normal_values, ds.y_logit_normal_values_point_3_0)
plt.plot(ds.x_logit_normal_values, ds.y_logit_normal_values_1_0)
plt.plot(ds.x_logit_normal_values, ds.y_logit_normal_values_3_0)
plt.plot(ds.x_logit_normal_values, ds.y_logit_normal_values_point_3_1)
plt.plot(ds.x_logit_normal_values, ds.y_logit_normal_values_1_1)
plt.plot(ds.x_logit_normal_values, ds.y_logit_normal_values_3_1)
plt.legend(['σ=.32 μ=0', 'σ=1 μ=0', 'σ=3.16 μ=0', 'σ=.32 μ=1', 'σ=1 μ=1', 'σ=3.16 μ=1'], loc='upper right')

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

# beta, params < 1
# plt.plot(ds.x_beta_values, ds.y_beta_values_frac_1_1)
# plt.plot(ds.x_beta_values, ds.y_beta_values_frac_1_25)
# plt.plot(ds.x_beta_values, ds.y_beta_values_frac_1_5)
# plt.plot(ds.x_beta_values, ds.y_beta_values_frac_1_75)
# plt.plot(ds.x_beta_values, ds.y_beta_values_frac_1_9)
# plt.legend(['alpha=β=.1','alpha=β=.25','alpha=β=.5','alpha=β=.75','alpha=β=.9'], loc='upper right')

# beta, alpha < beta
# plt.title('beta distribution \n alpha < β')
# plt.plot(ds.x_beta_values, ds.y_beta_values_1_2)
# plt.plot(ds.x_beta_values, ds.y_beta_values_1_3)
# plt.plot(ds.x_beta_values, ds.y_beta_values_2_3)
# plt.plot(ds.x_beta_values, ds.y_beta_values_1_4)
# plt.plot(ds.x_beta_values, ds.y_beta_values_2_4)
# plt.plot(ds.x_beta_values, ds.y_beta_values_4_6)
# plt.legend(['alpha=1 β=3','alpha=2 β=3', 'alpha=4 β=6'], loc='upper right')
# plt.legend(['alpha=1 β=2','alpha=2 β=3','alpha=1 β=3','alpha=1 β=4','alpha=2 β=4', 'alpha=4 β=6'], loc='upper right')

# beta, alpha > beta
# plt.title('beta distribution \n alpha > β')
# plt.plot(ds.x_beta_values, ds.y_beta_values_3_1)
# plt.plot(ds.x_beta_values, ds.y_beta_values_3_2)
# plt.plot(ds.x_beta_values, ds.y_beta_values_6_4)
# plt.legend(['alpha=2 β=1','alpha=3 β=2','alpha=6 β=4'], loc='upper right')


# arcsin
# plt.title('arcsin \n alpha=β=.5')
# plt.plot(ds.x_beta_values, ds.y_arcsin_values)

# uniform
# plt.title('uniform \n alpha=β=1')
# plt.plot(ds.x_beta_values, ds.y_arcsin_values)

# beta prime
# plt.title('beta prime distribution')
# plt.plot(ds.x_beta_prime_values, ds.y_beta_prime_values_1_1)
# plt.plot(ds.x_beta_prime_values, ds.y_beta_prime_values_1_2)
# plt.plot(ds.x_beta_prime_values, ds.y_beta_prime_values_2_1)
# plt.plot(ds.x_beta_prime_values, ds.y_beta_prime_values_2_3)
# plt.legend(['alpha=1 β=1','alpha=1 β=2','alpha=2 β=1','alpha=2 β=3'], loc='upper right')


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