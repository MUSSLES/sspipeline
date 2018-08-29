#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 The MUSSLES Developers
#
# This file is part of MUSSLES.
#
# MUSSLES is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MUSSLES is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MUSSLES.  If not, see <http://www.gnu.org/licenses/>.

# Tell module what it's allowed to import
__all__ = ["gev_logpost"]

import scipy.stats as stats
import numpy as np

# ===============================================================================
#         GEV Distribution
# ===============================================================================


def gev_loglikelihood(parameters, data):
    """
    Compute the log-likelihood of a GEV distribution

    Parameters
    ----------
    parameters : tuple
        :math:`\mu`, :math:`\sigma`, and :math:`\\xi` parameters for a GEV
        distribution
    data : :class:`numpy.ndarray`
        the data you're fitting

    Returns
    -------
    log_likelihood : float
    """
    mu, sigma, shape = parameters
    log_likelihood = 0
    for i in range(len(data)):
        logpdf = stats.genextreme.logpdf(
            x=data[i], loc=mu, scale=sigma, c=shape
        )
        if logpdf == -np.inf:
            return -np.inf
        log_likelihood += logpdf
    return log_likelihood


# end function


def gev_logprior(parameters):
    """
    Compute the log-prior of a GEV distribution

    Parameters
    ----------
    parameters : tuple
        :math:`\mu`, :math:`\sigma`, and :math:`\\xi` parameters for a GEV
        distribution

    Returns
    -------
    log_prior : float
    """
    mu, sigma, shape = parameters
    mu_logpdf = stats.norm.logpdf(x=mu, loc=0, scale=1000)
    shape_logpdf = stats.norm.logpdf(x=shape, loc=0, scale=1000)
    if sigma >= 10000 or sigma <= 0:
        return -np.inf
    else:
        return mu_logpdf + np.log(1 / 10000) + shape_logpdf


# end function


def gev_logpost(parameters, data):
    """
    Compute the log-posterior (log-prior + log-likelihood) of a GEV
    distribution

    Parameters
    ----------
    parameters : tuple
        :math:`\mu`, :math:`\sigma`, and :math:`\\xi` parameters for a GEV
        distribution
    data : :class:`numpy.ndarray`
        the data you're fitting

    Returns
    -------
    log_post : float

    Examples
    --------
    >>> from pipeline.distributions import gev_logpost
    >>> import scipy.stats as stats
    >>> params = (410, 100, -1)
    >>> real_params = (400, 100, -0.4)
    >>> data = stats.genextreme.rvs(loc=real_params[0],
    ...                             scale=real_params[1],
    ...                             c=real_params[2],
    ...                             size=10)
    >>> gev_logpost(params, data)
    -inf
    """
    pi = gev_logprior(parameters)
    if pi == -np.inf:
        return -np.inf
    LL = gev_loglikelihood(parameters, data)
    return LL + pi


# end function
