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
__all__ = ["acf_result"]

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")
COLORS = ["#34495e", "#95a5a6", "#a76c6e"]


def ACF(X, threshold, end=200):
    """
    Calculate the autocorrelation function (ACF) for input vector `X`,
    considering lags from 0 to `end`. Checks to find where the ACF < `threshold`, which
    is used as the threshold for independence among samples.
    """
    N = len(X)
    acf = []
    for a in range(0, end):
        acf.append(np.corrcoef(X[a:], X[: N - a])[0][1])

    lag = -1
    for i in range(len(acf)):
        if acf[i] <= threshold:
            lag = i
            break
    if lag == -1:
        print("Please increase the value of the end parameter for this function")
    return lag, acf


def acf_result(mcmc_chains, params, burnin, threshold, output_dir="output", plot=False):
    """
    Compute the autocorrelation function (above) for each model parameter in the
    input `mcmc_chains`, and return the lag that satisfies independence for all
    parameters. Also, plot the ACF?
    """
    lag_params, acf_params = [], []
    m, d = len(mcmc_chains), len(mcmc_chains[0])
    end = 100
    for i in range(d):
        lag_params.append([])
        acf_params.append([])
        for j in range(m):
            lag, acf = ACF(mcmc_chains[j][i][burnin:], threshold, end)
            lag_params[i].append(lag)
            acf_params[i].append(acf)
    lags = [max(np.array(lag_params)[:, i]) for i in range(m)]
    if plot:
        if m==1:
            fig, ax = plt.subplots(nrows=1, ncols=m, figsize=(12, 6))
            for j in range(d):
                ax.scatter(
                    np.arange(0, end),
                    acf_params[j][0],
                    label=params[j],
                    color=COLORS[j % 3],
                )
                ax.fill_between(
                    x=np.arange(0, end),
                    y2=np.zeros_like(acf_params[j][0]),
                    y1=acf_params[j][0],
                    alpha=0.3,
                    facecolor="black",
                )
            ax.plot(
                [max(lags), max(lags)],
                ax.get_ylim(),
                color="black",
                label="lag = {0}".format(max(lags)),
            )
            ax.set_xlabel("Lag")
            ax.set_ylabel("ACF")
            ax.set_title("Sequence {0}".format(1))
            ax.legend(loc="best")
            ax.grid(alpha=0.5)
            fig.savefig(output_dir + "/plots/acf.png")
        else:
            fig, ax = plt.subplots(nrows=1, ncols=m, figsize=(25, 6))
            for i in range(m):
                for j in range(d):
                    ax[i].scatter(
                        np.arange(0, end),
                        acf_params[j][i],
                        label=params[j],
                        color=COLORS[j % 3],
                    )
                    ax[i].fill_between(
                        x=np.arange(0, end),
                        y2=np.zeros_like(acf_params[j][i]),
                        y1=acf_params[j][i],
                        alpha=0.3,
                        facecolor="black",
                    )
                ax[i].plot(
                    [lags[i], lags[i]],
                    ax[i].get_ylim(),
                    color="black",
                    label="lag = {0}".format(lags[i]),
                )
                ax[i].set_xlabel("Lag")
                ax[i].set_ylabel("ACF")
                ax[i].set_title("Sequence {0}".format(i + 1))
                ax[i].legend(loc="best")
                ax[i].grid(alpha=0.5)
            fig.savefig(output_dir + "/plots/acf.png")
    return lags
