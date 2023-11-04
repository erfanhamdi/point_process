import numpy as np
from point_process.uniform_point_process import gen_uniform_pp

def test_gen_uniform_pp():
    # Test with N = 0
    x, y = gen_uniform_pp(0, 10, 10)
    assert len(x) == 0
    assert len(y) == 0
    
    # Test with N = 1
    x, y = gen_uniform_pp(1, 10, 10)
    assert len(x) == 1
    assert len(y) == 1
    assert 0 <= x[0] <= 10
    assert 0 <= y[0] <= 10
    
    # Test with N = 10
    x, y = gen_uniform_pp(10, 10, 10)
    assert len(x) == 10
    assert len(y) == 10
    assert all(0 <= xi <= 10 for xi in x)
    assert all(0 <= yi <= 10 for yi in y)
    
    # Test with N = 100
    x, y = gen_uniform_pp(100, 10, 10)
    assert len(x) == 100
    assert len(y) == 100
    assert all(0 <= xi <= 10 for xi in x)
    assert all(0 <= yi <= 10 for yi in y)