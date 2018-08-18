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

from .__version__ import __version__

__author__ = "John Letey (john.letey@colorado.edu)"
__copyright__ = "Copyright 2018 MUSSLES"

import json
import logging

import click
import matplotlib.pyplot as plt
import pandas as pd

from pipeline.core import acf_result
from pipeline.core import diagnostic_plots
from pipeline.core import final_params_pool
from pipeline.core import GR_result
from pipeline.core import history_plots
from pipeline.core import logpost
from pipeline.core import max_ls_parameters
from pipeline.core import runner

from pipeline.utils import check_params
from pipeline.utils import read_and_clean
from pipeline.utils import log

plt.style.use("fivethirtyeight")
COLORS = ["skyblue", "steelblue", "gray"]
ALPHAS = [1.0, 1.0, 0.45]


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(version=__version__)
@click.option(
    "--config",
    type=click.Path(
        exists=False,
        file_okay=True,
        dir_okay=False,
        readable=True,
        allow_dash=False,
    ),
    default="config.json",
    show_default=1,
    help="Read configuration from PATH.",
)
@click.pass_context
def main(ctx, config):
    """A pipeline that takes in data from UHSLC and analyzes it using MCMC."""

    # Start up the logger
    logging.basicConfig(
        filename="pipeline.log", format="%(asctime)s %(message)s", filemode="w"
    )
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # Read in the config file
    with open(config) as f:
        config_data = json.load(f)
    config_data = check_params(config_data, logger)
    logger = log(
        logger,
        "info",
        "The config file is located at " + config,
        config_data["verbose"],
    )
    # Put the config file into the log file
    logger.info("==> CONFIG PARAMETERS")
    for key in config_data.keys():
        logger.info("==> \t {:>10} : ".format(key) + str(config_data[key]))
    # Clean up the data
    data_meas, logger = read_and_clean(
        config_data["data"],
        config_data["percentage"],
        config_data["output"],
        logger,
        config_data["verbose"],
        config_data["plot"],
    )
    # Run the Adaptive Metropolis-Hastings Algorithm on the chains
    mcmc_chains, ar, ls = runner(
        m=config_data["sequences"],
        n_iter=config_data["iterations"],
        t=config_data["adaption"],
        d=3,
        logpost=logpost,
        data_meas=data_meas,
        stepsize=config_data["transition"],
    )
    # Plot the history plots for the chains
    if config_data["plot"]:
        history_plots(
            mcmc_chains,
            config_data["output"],
            [r"$\mu$", r"$\sigma$", r"$\xi$"],
        )
    # Log the acceptance rates
    logger = log(
        logger,
        "info",
        "The acceptance rates for these Markov chains are: " + str(ar),
        config_data["verbose"],
    )
    # Burnin the chains!
    burnin = GR_result(
        mcmc_chains,
        config_data["output"],
        [r"$\mu$", r"$\sigma$", r"$\xi$"],
        config_data["adaption"],
        config_data["plot"],
    )
    # Thin the chains!
    lags = acf_result(
        mcmc_chains,
        config_data["output"],
        [r"$\mu$", r"$\sigma$", r"$\xi$"],
        burnin,
        config_data["plot"],
    )
    # Calculate the final parameter pool
    params_analysis = final_params_pool(
        mcmc_chains,
        config_data["output"],
        burnin,
        lags,
        [r"$\mu$", r"$\sigma$", r"$\xi$"],
        config_data["plot"],
    )
    # Find the maximum parameters
    max_params = max_ls_parameters(
        ls, mcmc_chains, logger, config_data["verbose"]
    )
    # Diagnostic Plots
    (
        percentile_05,
        percentile_5,
        percentile_95,
        percentile_995
    ) = diagnostic_plots(
        data_meas,
        max_params,
        params_analysis,
        config_data["output"],
        config_data["plot"],
    )
    # Output return levels
    df = pd.DataFrame(
        data={
            ".05%": percentile_05,
            "5%": percentile_5,
            "95%": percentile_95,
            "99.5%": percentile_995,
        }
    )
    df = df.loc[[1, 2, 5, 10, 50, 100, 200]]
    df.to_csv(config_data["output"] + "/return_levels.csv")
    # Log "All done!"
    logger = log(logger, "info", "All done!", True)
