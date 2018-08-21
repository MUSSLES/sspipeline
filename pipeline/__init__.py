# -*- coding: utf-8 -*-
"""

Copyright (C) 2018 MUSSLES

This file is part of MUSSLES (Modeling and Uncertainty in Storm and Sea
LEvelS). MUSSLES is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option)
any later version.

@author: John Letey, University of Colorado, Boulder

"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

# ===============================================================================
#         Version
# ===============================================================================
from .__version__ import __version__
# ===============================================================================
#         Author + Copyright
# ===============================================================================
__author__ = "John Letey (john.letey@colorado.edu)"
__copyright__ = "Copyright 2018, MUSSLES"
# ===============================================================================
#         Command Line
# ===============================================================================
from pipeline.cli import cli_main
# ===============================================================================
#         Distributions
# ===============================================================================
from pipeline.distributions import normal_logpost
from pipeline.distributions import gev_logpost
