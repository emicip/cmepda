""" Create a ProbabilityDensityFunction class that is capable of throwing
preudo-random number with an arbitrary distribution.
"""


import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

class ProbabilityDensityFunction(InterpolatedUnivariateSpline):
    def __init__(self, x, y):
        InterpolatedUnivariateSpline.__init__(self, x, y) 

    def cdf (self, x):
        return np.array([self.integral(x[0], t) for t in x])

    def ppf(self, x):
        ycdf = self.cdf(x) 
        k = InterpolatedUnivariateSpline(ycdf,x)
        return np.array(k(ycdf)) 

    def rnd(self,size):
        return self.ppf(np.random.uniform(size=size))


if __name__ == "__main__":
    x = np.linspace(0, 3, 50)
    y = 2 * x
    p = ProbabilityDensityFunction(x, y)
    plt.plot(x, p(x))

    plt.figure()
    plt.plot(x, p.cdf(x))

    plt.figure()
    q = np.linspace(0., 1., 250)
    plt.plot(q, p.ppf(q))

   #plt.hist(p.rnd(1000),bins=100)
    #plt.plot(p.ppf(x))
    plt.show()