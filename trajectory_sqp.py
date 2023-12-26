import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

class Obstable:
    """ Obstacle class, an circular object """
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.rad = radius
    
def func(q):
    """ Objective function """
    return (2*q[2]*0.25 + q[1])**2 + (2*q[5]*0.25 + q[4])**2 +(2*q[2]*0.5 + q[1])**2 + (2*q[5]*0.5 + q[4])**2 +(2*q[2]*0.75 + q[1])**2 + (2*q[5]*0.75 + q[4])**2 


def dist_constraint(t:float, o:Obstable, c:float):
    """ constraint function on bot-obstacle distance """
    return lambda q: (q[0] + q[1]*t + q[2]*t*t - o.x)**2 + (q[3] + q[4]*t + q[5]*t*t - o.y)**2 - (o.rad + c)**2

def make_sequential_ineq_constaints(obs:Obstable, tol:float):
    """ generate a tuple containing sequential constraint functions on bot-obstacle distance """
    return ({'type': 'ineq', 'fun': dist_constraint(0.1, obs, tol)},
            {'type': 'ineq', 'fun': dist_constraint(0.2, obs, tol)},
            {'type': 'ineq', 'fun': dist_constraint(0.3, obs, tol)},
            {'type': 'ineq', 'fun': dist_constraint(0.4, obs, tol)},
            {'type': 'ineq', 'fun': dist_constraint(0.5, obs, tol)},
            {'type': 'ineq', 'fun': dist_constraint(0.6, obs, tol)},
            {'type': 'ineq', 'fun': dist_constraint(0.7, obs, tol)},
            {'type': 'ineq', 'fun': dist_constraint(0.8, obs, tol)},
            {'type': 'ineq', 'fun': dist_constraint(0.9, obs, tol)})

obs1 = Obstable(3.0, 4.0, 1.8) ## circular obstacle at (4.0, 4.0) with radius 1.8
# obs2 = Obstable(4.0, 8.0, 1.0) ## circular obstacle at (7.0, 5.0) with radius 1.0
tol = 0.2

cons = ({'type': 'eq', 'fun': lambda q: q[0] - 0},
        {'type': 'eq', 'fun': lambda q: q[3] - 0},
        {'type': 'eq', 'fun': lambda q: q[0] + q[1] + q[2] - 9.0},
        {'type': 'eq', 'fun': lambda q: q[3] + q[4] + q[5] - 10.0})

cons_obs1 = make_sequential_ineq_constaints(obs1, tol)
# cons_obs2 = make_sequential_ineq_constaints(obs2, tol)

cons = cons + cons_obs1
#cons = cons + cons_obs2

### Solve now the optimization problem and print the solution
res = minimize(func, [0.1, 0.1, 1.0, 1.0, 1.0, 1.0], constraints=cons, method='SLSQP', options={'disp': True})
print(res.x)


############## below, we plot the trajectory ##############
t = np.arange(0.0, 1.05, 0.05)
fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
circle1 = plt.Circle((3, 4), 1.8, color='g')
#circle2 = plt.Circle((4, 8), 1.0, color='g')
ax = plt.gca()
ax.cla() 
plt.grid()
# change default range
ax.set_xlim((-0.1, 10.2))
ax.set_ylim((-0.1, 10.2))

# key data point that we are encircling
ax.plot((0), (0), 'o', color='b')
ax.plot((9), (10), 'o', color='y')

ax.add_artist(circle1)
#ax.add_artist(circle2)

ax.plot(res.x[0] + res.x[1]*t + res.x[2]*t*t, res.x[3] + res.x[4]*t + res.x[5]*t*t, 'r')
plt.axis('equal')
plt.show()