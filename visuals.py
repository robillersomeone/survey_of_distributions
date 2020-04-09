import distributions as ds
import matplotlib.pyplot as plt

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

# print(ds.x_beta_values)
# print(ds.y_beta_values)


# beta

# plt.title('beta distribution \n alpha=2, β=5')
# plt.plot(ds.x_beta_values, ds.y_beta_values)
# plt.savefig('imgs/beta_distribution_2_5.png', format="png")
# plt.show()
# print(ds.x_beta_values)
# print(ds.y_beta_values)

# erlang

plt.title('erlang distribution \n k=9, θ=1')
# make it purple
plt.plot(ds.x_gamma_values, ds.y_erlang_values, color='purple')
plt.show()
plt.savefig('imgs/erlang_distribution_9_1.png', format="png")
# plt.savefig('imgs/gamma_distributions.png', format="png")

# print(ds.x_gamma_values)
# print(ds.y_erlang_values)

# exponential

# plt.title('exponential distribution \n λ=1')
# plt.plot(ds.x_gamma_values, ds.y_exponential_values)
# plt.savefig('imgs/exponential_distribution_1.png', format="png")
# plt.show()
# print(ds.x_gamma_values)
# print(ds.y_exponential_values)

# chi-squared

# plt.title('chi-squared distribution \n k=3')
# plt.plot(ds.x_gamma_values, ds.y_chi_squared_values)
# plt.savefig('imgs/chi_squared_distribution_3.png', format="png")
# plt.show()
# print(ds.x_gamma_values)
# print(ds.y_chi_squared_values)


# normal

# plt.title('approximated normal distribution \n k=25, θ=1/25')
# plt.plot(ds.x_gamma_values_getting_normal, ds.y_gamma_values_int)
# plt.savefig('imgs/approximated normal distribution_25.png', format="png")
# plt.show()
# print(ds.x_gamma_values_getting_normal)
# print(ds.y_gamma_values_int)

# f

# plt.title('f distribution \n k=??, θ=1?')
# plt.plot(ds.x_f_values, ds.y_f_values)
# # plt.savefig('imgs/approximated normal distribution_25.png', format="png")
# plt.show()
# # print(ds.x_gamma_values_getting_normal)
# print(ds.y_f_values)
