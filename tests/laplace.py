import os, sys
sys.path.append(os.path.abspath('../.'))

import pytest
import numpy as np
import survey_of_distributions.distributions as ds

# x values for support in distributions
x = np.arange(0, 20, .05)[1:]



def test_laplace_distribution():
    # might need the decimal for float types
    scale = 1. 
    loc = 0.
    assert ds.laplace_distribution(x, 0, 1).all() == np.exp(-abs(x-loc)/scale)/(2.*scale).all()


#log(uniform(0,1)/uniform(0,1)) ~ laplace(0,1)