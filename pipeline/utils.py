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
    print_function,
    division,
    absolute_import,
    unicode_literals,
)

# Tell module what it's allowed to import
__all__ = ["check_params", "read_and_clean", "log"]

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===============================================================================
#         Config Functions
# ===============================================================================


def check_params(params, logger=None):
    """
    Fixes & cleans up the config file parameters

    Parameters
    ----------
    params : dictionary
        list of parameters in dictionary form from config file
    logger : logging.RootLogger
        logger that the command line tool uses

    Returns
    -------
    new_params : dictionary
        fixed and cleaned up config file parameters
    logger : logging.RootLogger
        updated logger for the command line
    """
    new_params = {}
    # Check for the verbose parameter
    if "verbose" in params:
        new_params["verbose"] = bool(params["verbose"])
    else:
        new_params["verbose"] = False
    # Check for the data parameter
    if "data" in params:
        new_params["data"] = params["data"]
    else:
        # TODO: switch to command line error
        logger.error("You need a data parameter")
    # Check for the output parameter
    if "output" in params:
        new_params["output"] = params["output"]
    else:
        new_params["output"] = "output"
    # Check for the percentage of data in good years parameter
    if "percentage" in params:
        if params["percentage"] <= 1.0:
            new_params["percentage"] = params["percentage"]
        else:
            new_params["percentage"] = params["percentage"] / 100
    else:
        new_params["percentage"] = 0.9
    # Check for the number of iterations parameter
    if "iterations" in params:
        new_params["iterations"] = params["iterations"]
    else:
        new_params["iterations"] = 10000
    # Check for the number of sequences parameter
    if "sequences" in params:
        new_params["sequences"] = params["sequences"]
    else:
        new_params["sequences"] = 3
    # Check for when to start adaption parameter
    if "adaption" in params:
        new_params["adaption"] = params["adaption"]
    else:
        new_params["adaption"] = round(0.1 * new_params["iterations"])
    # Check for the transition covariance matrix
    if "transition" in params:
        new_params["transition"] = params["transition"]
    else:
        # TODO: switch to command line error
        logger.error("You need a transition covariance matrix")
    # Check to see if the user wants to plot
    if "plot" in params:
        new_params["plot"] = bool(params["plot"])
    else:
        new_params["plot"] = True
    # Return
    return new_params


# ===============================================================================
#         Data Functions
# ===============================================================================


def read_and_clean(
    datafile,
    percentage,
    output_dir="output/",
    logger=None,
    verbose=False,
    plot=False,
):
    """
    Reads & cleans the dataset

    Parameters
    ----------
    datafile : string
        where the dataset file is located
    percentage : float
        how much data to use in good years
    output_dir : string
        where to put the output from the function
    logger : logging.RootLogger
        logger that the command line uses
    verbose : bool
        whether or not to be verbose
    verbose : bool
        whether or not to plot

    Returns
    -------
    data : array_like
        cleaned data
    logger : logging.RootLogger
        updated logger for the command line
    """
    dfSL = pd.read_csv(datafile, header=None)
    dfSL.rename(
        columns={0: "year", 1: "month", 2: "day", 3: "hour", 4: "sealevel"},
        inplace=True,
    )
    num_years = len(list(set(dfSL["year"])))

    if plot:
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.plot(dfSL["sealevel"], color="steelblue")
        ax.set_xlabel("Time (in hours)", fontsize=16)
        ax.set_ylabel("Sea level (in MM)", fontsize=16)
        fig.savefig(output_dir + "/plots/original_data.png")

    fill_in = dfSL.loc[dfSL["sealevel"] < -5000, "sealevel"].mode()
    logger = log(
        logger, "The fill in value is {0}".format(float(fill_in)), verbose
    )

    dfSL["sealevel"].replace(fill_in, np.nan, inplace=True)
    dfSL.dropna(inplace=True)

    if plot:
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.plot(dfSL["sealevel"], color="steelblue")
        ax.set_title("Data Set", fontsize=20)
        ax.set_xlabel("Time (in hours)", fontsize=16)
        ax.set_ylabel("Sea Level (in MM)", fontsize=16)
        fig.savefig(output_dir + "/plots/cleaned_data.png")

    n_hours = 365 * 24
    sl_year = {}

    for index, row in dfSL.iterrows():
        year = row["year"]
        sl = row["sealevel"]
        if year in sl_year:
            sl_year[year].append(sl)
        else:
            sl_year[year] = []
            sl_year[year].append(sl)

    max_sl = {}

    for year, sealevel in sl_year.items():
        if len(sealevel) / n_hours >= percentage:
            max_sl[year] = max(np.array(sealevel) - np.mean(sealevel))

    data = list(max_sl.values())

    logger = log(
        logger,
        "The percentage of years that had enough data to use is {}%".format(
            100 * len(data) / num_years
        ),
        verbose,
    )

    return data, logger


# ===============================================================================
#         Logging Functions
# ===============================================================================


def log(logger, message, verbose):
    """
    A logging function (only to be used by the command line tool)

    Parameters
    ----------
    logger : logging.RootLogger
        logger that the command line uses
    message : string
        your message you want to log
    verbose : bool
        whether or not to be verbose

    Returns
    -------
    logger : logging.RootLogger
        updated logger for the command line
    """
    logger.info(message)
    if verbose:
        print("INFO :", message)
    return logger
