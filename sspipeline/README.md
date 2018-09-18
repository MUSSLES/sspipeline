# SSPipeline Source Code

## [`__init__.py`](__init__.py#L1)

This file is very minor to the actual proccess of the analysis of sea levels, and is only needed to build the Python package. TODO

## [`__version__.py`](__version__.py#L1)

This file contains the version of the command line tool. Nothing too important! TODO

## [`acf.py`](acf.py#L1)

- [`ACF`](acf.py#L30%23L48)

Helper function for `acf_result`

- [`acf_result`](acf.py#L51%23L96)

Obtains the lags for each parameter

## [`cli.py`](cli.py#L1)

- [`main`](cli.py#L62%23L170)

This function implements the SSPipeline command line tool. It uses the [Click](http://click.pocoo.org/) Python package to achieve this.

## [`core.py`](core.py#L1)

- [`update_mean`](core.py#L40%23L48)

- [`update_cov`](core.py#L51%23L65)

- [`random_move`](core.py#L68%23L87)

- [`adaptivemcmc`](core.py#L90%23L148)

- [`runner`](core.py#L151%23L177)

- [`history_plots`](core.py#L180%23L206)

- [`final_params_pool`](core.py#L209%23L232)

- [`max_ls_parameters`](core.py#L235%23L257)

- [`diagnostic_plots`](core.py#L260%23L437)

- [`output_parameters`](core.py#L440%23L452)

## [`gelman_rubin.py`](gelman_rubin.py#L1)

- [`GR_diag`](gelman_rubin.py#L30%23L47)

Helper function to `GR_result`

- [`psrf`](gelman_rubin.py#L50%23L93)

Helper function to `GR_result`

- [`GR_result`](gelman_rubin.py#L96%23L161)

Obtains the maximum burnin for the chains

## [`gev_utils.py`](gev_utils.py#L1)

- [`loglikelihood`](gev_utils.py#L27%23L52)

This function implements the log-likelihood.

- [`logprior`](gev_utils.py#L55%23L75)

This function implements the prior distribution.

- [`logpost`](gev_utils.py#L78%23L112)

In this function, we add the the log-prior and log-likelihood together to obtain the log-posterior score.

## [`utils.py`](utils.py#L1)

- [`check_params`](utils.py#L30%23L94)

This function takes in the settings found in the configuration file, and parses them to make sure required parameters were passed in and also inserts common settings to optional parameters, not were not included in the configuration file.

-  [`read_and_clean`](utils.py#L97%23L187)

- [`log`](utils.py#L190%23L211)