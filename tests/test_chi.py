import os, sys
sys.path.append(os.path.abspath('../.'))

import pytest
import numpy as np
import survey_of_distributions.distributions as ds
import survey_of_distributions.normal_distribution as nd


# x values for support in distributions
x = np.arange(0, 20, .05)[1:]

def test_chi_distribution():
    pass