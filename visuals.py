import distributions as ds
import matplotlib.pyplot as plt


plt.title('approximated normal distribution \n k=25, θ=1/25')
plt.plot(ds.x_gamma_values_getting_normal, ds.y_gamma_values_int)
plt.savefig('imgs/approximated normal distribution_25.png', format="png")
plt.show()
# print(len(np.arange(0, 20, .1)))
print(ds.x_gamma_values_getting_normal)
print(ds.y_gamma_values_int)
