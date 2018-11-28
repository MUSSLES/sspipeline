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
__all__ = ["logpost"]

import scipy.stats as stats
import numpy as np


def loglikelihood(parameters, data):
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
    s = 0
    for i in range(len(data)):
        logpdf = stats.genextreme.logpdf(x=data[i], loc=mu, scale=sigma, c=-shape)
        if logpdf == -np.inf:
            return -np.inf
        s += logpdf
    return s


def logprior(parameters):
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
    mu_logpdf = stats.uniform.logpdf(x=mu, loc=0, scale=10000)
    sigma_logpdf = stats.uniform.logpdf(x=sigma, loc=0, scale=10000)
    shape_logpdf = stats.norm.logpdf(x=shape, loc=0, scale=1000)
    return mu_logpdf + sigma_logpdf+ shape_logpdf


def logpost(parameters, data):
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
    """
    pi = logprior(parameters)
    if pi == -np.inf:
        return -np.inf
    LL = loglikelihood(parameters, data)
    return LL + pi
