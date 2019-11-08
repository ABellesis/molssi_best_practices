'''
Unit testing for the measure module
'''
import numpy as np
import molecool

def test_calculate_distance():
    r1 = np.array([0, 0, 0])
    r2 = np.array([0.1, 0, 0])

    expected_distance = 0.1
    calculated_distance = molecool.calculate_distance(r1, r2) 
    assert expected_distance == calculated_distance #For an assert statement: If it is true, nothing happens. If it is falwe, there is an assertion error. 
