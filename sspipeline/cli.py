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
__all__ = ["main"]

import json
import logging

import click
import matplotlib.pyplot as plt
import pandas as pd

from .core import output_parameters
from .core import diagnostic_plots
from .core import final_params_pool
from .core import history_plots
from .core import max_ls_parameters
from .core import runner

from .gelman_rubin import GR_result

from .acf import acf_result

from .gev_utils import logpost

from .utils import check_params
from .utils import read_and_clean
from .utils import log

from .__version__ import __version__


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(version=__version__)
@click.option(
    "--config",
    type=click.Path(
        exists=False, file_okay=True, dir_okay=False, readable=True, allow_dash=False
    ),
    default="config.json",
    show_default=1,
    help="Read configuration from PATH.",
)
@click.pass_context
def main(ctx, config):
    """A pipeline for estimating and characterizing uncertainty in coastal storm surge levels"""

    # Read in the config file
    with open(config) as f:
        config_data = json.load(f)
    config_data = check_params(config_data)
    # Start up the logger
    logging.basicConfig(
        filename=config_data["output_dir"] + "/sspipeline.log",
        format="%(asctime)s %(message)s",
        filemode="w",
    )
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # Log where the configuration file is at
    logger = log(
        logger, "the config file is located at " + config, config_data["verbose"]
    )
    # Put the config file into the log file
    logger.info("==> CONFIG FILE PARAMETERS")
    for key, value in sorted(config_data.items()):
        logger.info("==> \t {:>10} : ".format(key) + str(value))
    # Clean up the data
    data_meas, logger = read_and_clean(
        config_data["data"],
        config_data["percentage"],
        config_data["output_dir"],
        logger,
        config_data["verbose"],
        config_data["plot"],
    )
    # Run the Adaptive Metropolis-Hastings Algorithm on the chains
    mcmc_chains, ar, ls = runner(
        m=config_data["sequences"],
        n_iter=config_data["iterations"],
        t=config_data["adaption"],
        logpost=logpost,
        data_meas=data_meas,
        stepsize=config_data["transition"],
    )
    # Plot the history plots for the chains
    if config_data["plot"]:
        history_plots(mcmc_chains=mcmc_chains, output_dir=config_data["output_dir"])
    # Log the acceptance rates
    logger = log(
        logger,
        "the acceptance rates for these Markov chains are: " + str(ar),
        config_data["verbose"],
    )
    # Burnin the chains!
    burnin = GR_result(
        mcmc_chains=mcmc_chains,
        params=[r"$\mu$", r"$\sigma$", r"$\xi$"],
        t=config_data["adaption"],
        threshold=config_data["gr_threshold"],
        output_dir=config_data["output_dir"],
        plot=config_data["plot"],
    )
    # Thin the chains!
    lags = acf_result(
        mcmc_chains,
        [r"$\mu$", r"$\sigma$", r"$\xi$"],
        burnin,
        config_data["acf_threshold"],
        config_data["output_dir"],
        config_data["plot"],
    )
    # Calculate the final parameter pool
    params_analysis = final_params_pool(
        mcmc_chains=mcmc_chains,
        burnin=burnin,
        lags=lags,
        output_dir=config_data["output_dir"],
        plot=config_data["plot"],
    )
    # Find the maximum parameters
    max_params = max_ls_parameters(ls, mcmc_chains, logger, config_data["verbose"])
    # Diagnostic Plots
    (
        percentile_05,
        percentile_1,
        percentile_2,
        percentile_5,
        percentile_95,
        percentile_98,
        percentile_99,
        percentile_995,
    ) = diagnostic_plots(
        data_meas,
        max_params,
        params_analysis,
        config_data["output_dir"],
        config_data["plot"],
    )
    # Output return levels
    df = pd.DataFrame(
        data={
            ".5": percentile_05,
            "1": percentile_1,
            "2": percentile_2,
            "5": percentile_5,
            "95": percentile_95,
            "98": percentile_98,
            "99": percentile_99,
            "99.5": percentile_995,
        }
    )
    df = df.reindex([0, 3, 8, 18, 48, 98, 198, 498])
    # print(df.index)
    df.rename(
        index={0: 2, 3: 5, 8: 10, 18: 20, 48: 50, 98: 100, 198: 200, 498: 500},
        inplace=True,
    )
    df.to_csv(config_data["output_dir"] + "/return_levels.csv")
    # Output the parameters
    output_parameters(
        mcmc_chains=mcmc_chains,
        burnin=burnin,
        lags=lags,
        output_dir=config_data["output_dir"],
    )
    # Log "All done!"
    logger = log(logger, "All done!", True)
