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
__all__ = ["GR_result"]

import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")
COLORS = ["#34495e", "#95a5a6", "#a76c6e"]


def GR_diag(parameter, threshold, interval=100, start=100):
    """
    Computes the potential scale reduction factor for MCMC output array
    `parameter`, starting with iteration `start` at intervals of `interval`
    until the end of the parameter list.
    """
    end = len(parameter[0])
    GR_result_out = []
    for n in range(start, end, interval):
        sequences = []
        for i in range(len(parameter)):
            sequences.append(parameter[i][:n])
        GR_result_out.append(psrf(sequences))
    burnin = 0
    for i in range(len(GR_result_out)):
        if max(GR_result_out[i:]) < threshold:
            burnin = i + 1
            break
    return GR_result_out, burnin * interval


def psrf(sequences):
    """
    Function to calculate the Potential Scale Reduction Factor (PSRF) for MCMC
    chains

    Parameters
    ----------
    sequences : :class:`numpy.ndarray`
        MCMC chains that you want to calculate the PSRF of

    Returns
    -------
    psrf : float
        .. math:: \hat{R} = \sqrt{\\frac{\hat{V}}{\sigma^2} \cdot \\frac{
                  \\text{df}}{\\text{df}-2}}

        where:

        .. math:: \hat{V} = \hat{\sigma}^2 + \\frac{B}{mn} \quad\\text{and}
                  \quad \hat{\sigma}^2 = \\frac{n-1}{n}W + \\frac{1}{n}B

        and also:

        .. math:: m = \\text{number of sequences} \\\ n = \\text{length of each
                  chain} \\\ B = \\frac{n}{(m - 1)}.\sum{(\mu_i - \\bar{\mu})^2
                  }, ~~ \\text{where $\mu_i$ is the average of each chain and $
                  \\bar{\mu}$ is the global} \\\ \\text{mean of all estimated
                  variables} \\\ W = \\frac{1}{m}.\sum{\\textrm{Var}_i}, ~~
                  \\text{where }\\textrm{Var}_i\\text{ is the variance of
                  sequence $i$}
    """
    u = [np.mean(sequence) for sequence in sequences]
    s = [np.var(sequence, ddof=1) for sequence in sequences]
    m = len(sequences)
    n = len(sequences[0])
    U = np.mean(u)
    B, W = 0, 0
    for i in range(m):
        B += (u[i] - U) ** 2
        W += s[i]
    B = (B * n) / (m - 1)
    W = W / m
    Var = (1 - (1 / n)) * W + (B / n)
    return np.sqrt(Var / W)


def GR_result(
    mcmc_chains,
    params,
    t,
    threshold,
    output_dir="output",
    plot=False,
    start=100,
    interval=100,
):
    """
    Run the Gelman and Rubin (1992) diagnostic on the tails of the `mcmc_chains`
    output object. Start by considering tails of length [start:], and reduce the
    length by moving the initial point considered `interval` closer to the end
    of the chain. Once the potential scale reduction factor is below 1.1 (by
    default; can be adjusted in the config file), the chains are considered to
    be burned-in/warmed-up, and converged to the posterior distribution.
    """
    m, d, n = len(mcmc_chains), len(mcmc_chains[0]), len(mcmc_chains[0][0])
    if m==1:
        return int(0.5*n)
    params_raw, GR_params, burnin_params = [], [], []
    start, interval, end = start, interval, n
    for i in range(d):
        params_raw.append([])
        for j in range(m):
            params_raw[i].append(mcmc_chains[j][i])
    for i in range(d):
        GR, burnin = GR_diag(params_raw[i], threshold, interval, start)
        GR_params.append(GR)
        burnin_params.append(burnin)
    burnin = max(max(burnin_params), t)
    if plot:
        fig, ax = plt.subplots(figsize=(14, 6))
        for i in range(d):
            ax.scatter(
                x=np.arange(start, end, interval),
                y=GR_params[i],
                label=params[i],
                color=COLORS[i % 3],
            )
        ax.plot(
            [burnin, burnin],
            plt.ylim(),
            label="burn in = {0}".format(burnin),
            color="black",
        )
        ax.set_xlabel("Iteration", fontsize=14)
        ax.set_ylabel("Potential Scale Reduction Fator", fontsize=14)
        ax.set_title("Gelman & Rubin Diagnostic", fontsize=14)
        ax.legend(loc="best")
        fig.savefig(output_dir + "/plots/gr_diagnostic.png")
    return burnin
