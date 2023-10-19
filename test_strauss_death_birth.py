import numpy as np
from strauss_death_birth import *
def test_death_fn():
    # Test 1: Test if the returned indices are within the grid shape
    grid = np.zeros((10, 10))
    i, j = death_fn(grid)
    assert i >= 0 and i < grid.shape[0]
    assert j >= 0 and j < grid.shape[1]

    # Test 2: Test if the returned indices are integers
    assert isinstance(i, int)
    assert isinstance(j, int)

    # Test 3: Test if the returned indices are different for different calls
    i1, j1 = death_fn(grid)
    i2, j2 = death_fn(grid)
    assert (i1, j1) != (i2, j2)

    # Test 4: Test if the returned indices are random
    grid = np.ones((10, 10))
    i1, j1 = death_fn(grid)
    grid[i1, j1] = 0
    i2, j2 = death_fn(grid)
    assert (i1, j1) != (i2, j2)

def test_birth_fn():
    # Test 1: Test if the returned tuple has length 2
    assert len(birth_fn()) == 2

    # Test 2: Test if the returned tuple contains only numbers between 0 and 1
    x, y = birth_fn()
    assert 0 <= x <= 1
    assert 0 <= y <= 1

    # Test 3: Test if the returned tuples are different for different calls
    t1 = birth_fn()
    t2 = birth_fn()
    assert t1 != t2

def test_check_criteria():
    # Test 1: Test if the returned mask has the correct shape
    point_list = [[0, 0], [1, 1], [2, 2]]
    new_point = [1, 1]
    r0 = 1.5
    dist_mask = check_criteria(point_list, new_point, r0)
    assert dist_mask.shape == (3,), "test 1"

    # Test 2: Test if the returned mask is correct
    point_list = [[0, 0], [1, 1], [2, 2]]
    new_point = [1, 1]
    r0 = 1.5
    dist_mask = check_criteria(point_list, new_point, r0)
    assert np.array_equal(dist_mask, [True, True, False]), "test 2"

    # Test 3: Test if the function works with a different point list
    point_list = [[0, 0], [1, 1], [2, 2], [3, 3]]
    new_point = [1, 1]
    r0 = 1.5
    dist_mask = check_criteria(point_list, new_point, r0)
    assert np.array_equal(dist_mask, [True, True, False, False]), "test 3"

    # Test 4: Test if the function works with a different interaction radius
    point_list = [[0, 0], [1, 1], [2, 2]]
    new_point = [1, 1]
    r0 = 0.5
    dist_mask = check_criteria(point_list, new_point, r0)
    assert np.array_equal(dist_mask, [False, True, False]), "test 4"

def test_pair_potential_fn():
    # Test 1: Test if the returned value is between 0 and 1
    num_points_inside_r0 = 5
    beta = 0.5
    result = pair_potential_fn(num_points_inside_r0, beta)
    assert result >= 0 and result <= 1

    # Test 2: Test if the returned value is 1 when num_points_inside_r0 is 0
    num_points_inside_r0 = 0
    beta = 0.5
    result = pair_potential_fn(num_points_inside_r0, beta)
    assert result == 1

    # Test 3: Test if the returned value is 0 when beta is infinity
    num_points_inside_r0 = 5
    beta = float('inf')
    result = pair_potential_fn(num_points_inside_r0, beta)
    assert result == 0

    # Test 4: Test if the returned value is 1 when beta is 0
    num_points_inside_r0 = 5
    beta = 0
    result = pair_potential_fn(num_points_inside_r0, beta)
    assert result == 1