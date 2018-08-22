#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 The MUSSLES developers
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
    parameters : array_like
        :math:`\mu` and :math:`\sigma` parameters for a Normal distribution
    data : array_like
        the data you're fitting

    Returns
    -------
    log_likelihood : float
    """
    mu, sigma = parameters
    log_likelihood = 0
    for i in range(len(data)):
        logpdf = stats.norm.logpdf(x=data[i], loc=mu, scale=sigma)
        if logpdf == -np.inf:
            return -np.inf
        log_likelihood += logpdf
    return log_likelihood


# end function


def normal_logprior(parameters):
    """
    Compute the log-prior of a Normal distribution

    Parameters
    ----------
    parameters : array_like
        :math:`\mu` and :math:`\sigma` parameters for a Normal distribution

    Returns
    -------
    log_prior : float
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
    parameters : array_like
        :math:`\mu` and :math:`\sigma` parameters for a Normal distribution
    data : array_like
        the data you're fitting

    Returns
    -------
    log_post : float

    Examples
    --------
    >>> from pipeline.distributions import normal_logpost
    >>> import scipy.stats as stats
    >>> params = [8, 1]
    >>> real_params = [10, 2]
    >>> data = stats.norm.rvs(loc=real_params[0],
    ...                       scale=real_params[1],
    ...                       size=10)
    >>> normal_logpost(params, data)
    -87.09445386092345
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
    parameters : array_like
        :math:`\mu`, :math:`\sigma`, and :math:`\\xi` parameters for a GEV
        distribution
    data : array_like
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
    parameters : array_like
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
    parameters : array_like
        :math:`\mu`, :math:`\sigma`, and :math:`\\xi` parameters for a GEV
        distribution
    data : array_like
        the data you're fitting

    Returns
    -------
    log_post : float

    Examples
    --------
    >>> from pipeline.distributions import gev_logpost
    >>> import scipy.stats as stats
    >>> params = [410, 100, -1]
    >>> real_params = [400, 100, -0.4]
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
