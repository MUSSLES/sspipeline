# -*- coding: utf-8 -*-
"""

All of the implemented distribution functions

"""

from __future__ import (print_function, division, absolute_import,
                        unicode_literals)

# Tell module what it's allowed to import
__all__ = ["normal_logpost", "gev_logpost"]

import scipy.stats as stats
import numpy as np

# ===============================================================================
#         Normal Distribution
# ===============================================================================

def normal_loglikelihood(parameters, data):
    """
    Compute the log-likelihood of a Normal distribution

    Parameters
    ----------
    paramaters : array
    data : array

    Returns
    -------
    result : float
    """
    mu, sigma = parameters
    s = 0
    for i in range(len(data_meas)):
        logpdf = stats.norm.logpdf(x=data[i], loc=mu, scale=sigma)
        if logpdf == -np.inf:
            return -np.inf
        s += logpdf
    return s
# end function

def normal_logprior(parameters):
    """
    Compute the log-prior of a Normal distribution

    Parameters
    ----------
    paramaters : array

    Returns
    -------
    result : float
    """
    mu, sigma = parameters

    mu_logpdf = stats.norm.logpdf(x=mu, loc=0, scale=1000)

    if sigma <= 0 or sigma >= 1000:
        return -np.inf

    return mu_logpdf + np.log(1 / 1000)
# end function

def normal_logpost(parameters, data):
    """
    Compute the log-posterior (log-prior + log-likelihood) of a Normal
    distribution

    Parameters
    ----------
    paramaters : array
    data : array

    Returns
    -------
    result : float
    """
    pi = normal_logprior(parameters)
    if pi == -np.inf:
        return -np.inf
    LL = normal_loglikelihood(parameters, data)
    return LL + pi
# end function

# ===============================================================================
#         GEV Distribution
# ===============================================================================

def gev_loglikelihood(parameters, data):
    """
    Compute the log-likelihood of a GEV distribution

    Parameters
    ----------
    paramaters : array
    data : array

    Returns
    -------
    result : float
    """
    mu, sigma, shape = parameters
    s = 0
    for i in range(len(data_meas)):
        logpdf = stats.genextreme.logpdf(x=data_meas[i], loc=mu, scale=sigma, c=shape)
        if logpdf == -np.inf:
            return -np.inf
        s += logpdf
    return s
# end function

def gev_logprior(parameters):
    """
    Compute the log-prior of a GEV distribution

    Parameters
    ----------
    paramaters : array

    Returns
    -------
    result : float
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
    paramaters : array
    data : array

    Returns
    -------
    result : float
    """
    pi = gev_logprior(parameters)
    if pi == -np.inf:
        return -np.inf
    LL = gev_loglikelihood(parameters, data)
    return LL + pi
# end function