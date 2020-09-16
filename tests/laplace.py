import os, sys
sys.path.append(os.path.abspath('../.'))

import pytest
import numpy as np
import survey_of_distributions.distributions as ds

# get support

#log(uniform(0,1)/uniform(0,1)) ~ laplace(0,1)
