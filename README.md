# Point Processes
This repository contains code for simulating and analyzing point processes. Point processes are stochastic models used to describe the occurrence of events in time or space. They have applications in a variety of fields, including neuroscience, ecology, and finance.

## Contents
- [uniform_point_process.py](./uniform_point_process.py): Python code for generating a random point using a uniform point process.
- [binomial_point_process.py](./binomial_point_process.py): In this script we generate a point pattern with fixed number of points with uniform probability
- [poisson_point_process.py](./poisson_point_process.py): The generated point pattern is one realisation of poisson point process with intensity &lambda; = 100
- [matern_point_process.py](./matern_point_process.py): Here we generate a point pattern based on the matern I point process. I changed the code in a wonderfull overview of Point Processes by Paul Keeler that you can find [here](https://hpaulkeeler.com/simulating-matern-hard-core-point-processes/). It now contains only the type-I Matern PP.
- 