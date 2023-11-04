import numpy as np
from point_process.poisson_point_process import gen_poisson_pp

def test_gen_poisson_pp():
    # Test 1: Check if the number of points generated is correct
    xx, yy = gen_poisson_pp(10, 100, 100)
    assert len(xx) == len(yy)

    # Test 2: Check if all points are within the bounds of the rectangle
    xx, yy = gen_poisson_pp(5, 50, 50)
    assert all(0 <= x <= 50 for x in xx)
    assert all(0 <= y <= 50 for y in yy)

    # Test 3: Check if the function returns empty arrays when lambda0 is 0
    xx, yy = gen_poisson_pp(0, 10, 10)
    assert len(xx) == len(yy) == 0

    # Test 4: Check if the function returns arrays of the same length
    xx, yy = gen_poisson_pp(2, 20, 30)
    assert len(xx) == len(yy)