import numpy as np
import scipy as scp
import matplotlib.pyplot as plt
from scipy.optimize import linprog

Z = np.array([5,7,12]) #objective function

A = np.array([[-1,-1,-1],[-1,2,0],[0,0,-1]])
B = np.array([-500,0,-340])

x_low = 0
x_upper = None

result = linprog(Z,A,B,method="revised simplex",bounds=[x_low,x_upper])
print("Maximum value of the objective function is = ", result.fun)
print("The values of x1, x2 and x3 are = ", result.x)