import distributions as ds
import matplotlib.pyplot as plt


plt.title('gamma with k=2, θ=2')
plt.plot(ds.x_gamma_values_getting_normal, ds.y_gamma_values_int)
# plt.savefig('gamma_2_2.png', format="png")
plt.show()
# print(len(np.arange(0, 20, .1)))
print(ds.x_gamma_values_getting_normal)
print(ds.y_gamma_values_int)

 
