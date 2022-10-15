import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import binom
import numpy as np

X_GLOBAL = np.arange(-5,5,0.1)
X_GLOBAL_2 = np.linspace(0, 10, 11)
fig, (ax1, ax2) = plt.subplots(2)


def gaussian_probability_density(standard_deviation):
    return norm.pdf(X_GLOBAL, loc = 0, scale = standard_deviation)

def gaussian_cumulative_density(standard_deviation):
    return norm.cdf(X_GLOBAL, loc = 0, scale = standard_deviation)

def binomial_probability_mass_function(n,p):
    rv = binom(n, p)
    return rv.pmf(X_GLOBAL_2)


for standard_deviation in range(2,20,1):
    y_pdf = gaussian_probability_density(standard_deviation/10)
    y_cdf = gaussian_cumulative_density(standard_deviation/10)
    ax1.plot(X_GLOBAL,y_pdf, label=str(standard_deviation/10))
    ax1.legend()
    ax1.set_ylabel('gaussian_cumulative_density')
    ax2.plot(X_GLOBAL,y_cdf, label=str(standard_deviation/10))
    ax2.legend()
    ax2.set_ylabel('gaussian_probability_density')


plt.xlabel('X')
plt.show()


lst = [[[10,0.5], 'r'],[[10,0.1], 'g']]
fig, ax = plt.subplots(1)

for i in lst:
    y = binomial_probability_mass_function(i[0][0],i[0][1])
    ax.plot(X_GLOBAL_2,y)
    ax.vlines(X_GLOBAL_2, 0, y, colors=i[1])
    ax.scatter(X_GLOBAL_2, y, label=str(i[0]), color=i[1])
    ax.legend()

plt.xlabel('X')
plt.show()
