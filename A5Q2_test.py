import numpy as np
from A5Q2 import *
small = 5e-7
d = 2.446197e-01
def test_poly_err():
    assert np.abs(err - d) < small
