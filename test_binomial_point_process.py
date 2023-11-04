import numpy as np
from binomial_point_process import gen_binomial_pp

def test_gen_binomial_pp():
    N = 100
    h = 10
    w = 5
    x, y = gen_binomial_pp(N, h, w)
    assert len(x) == N
    assert len(y) == N
    assert np.all(x >= 0) and np.all(x <= w)
    assert np.all(y >= 0) and np.all(y <= h)