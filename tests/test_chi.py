import os, sys
sys.path.append(os.path.abspath('../.'))

import pytest
import numpy as np
import survey_of_distributions.distributions as ds
import survey_of_distributions.normal_distribution as nd


# x values for support in distributions
x = np.arange(0, 20, .05)[1:]

# test chi from gammma and from normal
def test_chi_distribution():
    assert ds.chi_squared_distribution(x, 4).all() == ds.chi_from_normal.all()