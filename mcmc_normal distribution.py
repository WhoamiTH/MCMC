import random
import math
import matplotlib.pyplot as plt
import numpy as np

def normal(x,mu,theta):
    return (1/math.sqrt(2*math.pi*theta))*np.exp(-(x-mu)**2/2*theta)

def normal_simplify(x,mu,theta):
    return np.exp(-(x-mu)**2/2*theta)

def normal_mcmc(n,mu,theta):
    states = []
    current = random.uniform(-3,3)
    for i in range(0,n):
        states.append(current)
        next = random.uniform(-3,3)
        alpha = min(normal(next,mu,theta)/normal(current,mu,theta),1)
        if random.uniform(0,1) < alpha:
            current = next
    return states[-10000:]


t = normal_mcmc(100000,0,1)
x = np.linspace(-3,3,1000)
y = normal(x,0,1)

plt.figure(num=1,figsize=(8,5))
plt.plot(x,y,color='red',linewidth=1.0,linestyle='--',label = 'normal distribution')
plt.hist(t, bins=30, normed=True,label='generated distribution')
plt.legend(loc='upper right')
plt.show()