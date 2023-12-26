
## Overview
This is a micro-project for demonstrating how to solve an optimal collision-free trajectory for a mobile robot using **SQP (Sequential Quadratic Programming)** Optimization.


## Model presentation

#### Trajectory
In this demo, the trajectory is modeled as a 2nd-order polynomial in 2D space:

  $$x(t) = a_2*t^2 + a_1*t + a_0$$
  $$y(t) = b_2*t^2 + b_1*t + b_0$$

**NOTE**: $t$ represents time which is zoomed to [0, 1] interval in this demo

We choose a polynomial model for robot trajectory so that we can guarantee the smoothness of the velocity even acceleration curves:
  $$x'(t) = 2*a_2*t + a_1$$
  $$y'(t) = 2*b_2*t + b_1$$
  $$x''(t) = 2*a_2$$
  $$y''(t) = 2*b_2$$

Of course, we could choose higher-order polynomials (or other types of parameterized curves such like B-Splines) for representing the trajectory, especially when there are more complexe constraints so that the solver would have more degrees of freedom to find the optimal solution.

### Obstacle
For sake of computaional efficiency, only one obstacle is defined in this demo which is represented by a circular region.

### Constraints
As in all the optimization problems, a series of **Equality** constraints and **Inequality** constraints should be defined. In this demo, the desired initial position/velocity and final position/velocity are defined with **Equality** constraints; and the avoidance of collision is defined as a series of **Inequality** constraints at some sampling instants to ensure the distance to obstacle is positive (sequential constraints).

### Objective
Various heuristics could be defined in the objective function (also called cost function). For example, the energy consumed throughout the motion, sequential jerk (derivative of acceleration) values, etc. When there are multiple costs defined, we should assgine a certain weight value to each cost.

### SQP problem to solve
Let $$\mathbf{q} = [ a_0, a_1, a_2, b_0, b_1, b_2]$$
Solve:  $$minimize( F_{obj}(\mathbf{q}) )$$  $$\text{ s.t.   }   g(\mathbf{q})=0 \text{  and   } H(\mathbf{q})>0$$
Once the SQP problem is solved, we find the optial solution $\mathbf{q}_{optim}$, the polynomial trajectory is then obtained.

## Run the demo
Run the demo with command:
```bash
python trajectory_sqp.py
```
