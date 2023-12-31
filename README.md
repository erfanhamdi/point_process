[![codecov](https://codecov.io/gh/erfanhamdi/point_process/branch/main/graph/badge.svg)](https://codecov.io/gh/erfanhamdi/point_process)
# Point Processes
This repository contains code for simulating and analyzing point processes. Point processes are stochastic models used to describe the occurrence of events in time or space. They have applications in a variety of fields, including neuroscience, ecology, and finance.

## Contents

### Uniform Point Process
- [uniform_point_process.py](./uniform_point_process.py): Python code for generating a random point using a uniform point process.

### Binomial Point Process
- [binomial_point_process.py](./binomial_point_process.py): In this script we generate a point pattern with fixed number of points with uniform probability

### Poisson Point Process
- [poisson_point_process.py](./poisson_point_process.py): The generated point pattern is one realisation of poisson point process with intensity &lambda; = 100

### Strauss Point Process
- [strauss_point_process.py](./strauss_death_birth.py): In this script, I simulated a point pattern based on [Strauss Point Process](https://academic.oup.com/biomet/article-abstract/62/2/467/337198) using birth and death algorithm. The pair potential function used for generating it is:
$$\phi(x) = exp(-\beta\Sigma^{n}_{j=1, j\neq k}\mathbf{1}(0<||x-x_j||\leq r_i))$$
taken from a great book by Illian

```yaml
Illian, Janine, Antti Penttinen, Helga Stoyan, and Dietrich Stoyan. Statistical Analysis and Modelling of Spatial Point Patterns. 1st ed. Wiley, 2007. https://doi.org/10.1002/9780470725160.
```



| Point Process Name | Final Result |
| --- | --- |
| Uniform Point Process | ![Uniform Point Process](figs/uniform_pp.png) |
| Binomial Point Process | ![Binomial Point Process](figs/binomial.png) |
| Poisson Point Process | ![Poisson Point Process](figs/poisson_pp2.png) |
| Strauss Point Process | ![Strauss Point Process](figs/output.gif) |
