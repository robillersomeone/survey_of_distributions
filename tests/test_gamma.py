import os, sys
sys.path.append(os.path.abspath('../.'))

import numpy as np
import pytest
import survey_of_distributions.distributions as ds

# x values for support in distributions
x = np.arange(0, 20, .05)[1:]

def test_gamma_function():
    assert ds.gamma_function(3) == ds.integral_gamma_function(3)
    assert ds.gamma_function(5) == ds.integral_gamma_function(5)
    assert ds.gamma_function(15) == ds.integral_gamma_function(15)


def test_gamma_distribution():
    assert ds.gamma_distribution(x,1,2).all() == ds.int_gamma_distribution(x,1,2).all()
    assert ds.gamma_distribution(x,2,2).all() == ds.int_gamma_distribution(x,2,2).all()
