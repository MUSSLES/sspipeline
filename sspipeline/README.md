<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD032 -->
<!-- markdownlint-disable MD022 -->

# SSPipeline Source Code

<details><summary><a href="__init__.py#L1">__init__.py</a> (click to expand)</summary>

This file is where Python goes whenever you want to run the pipeline. The pipeline wouldn't work without this!

</details>

<details><summary><a href="__version__.py#L1">__version__.py</a> (click to expand)</summary>

This file contains the version of the command line tool. Nothing too important!

</details>

<details><summary><a href="acf.py#L1">acf.py</a> (click to expand)</summary>

This file contains the following functions:

- [`ACF`](acf.py#L30%23L48)

Helper function for `acf_result`

- [`acf_result`](acf.py#L51%23L96)

Obtains the lags for each parameter

</details>

<details><summary><a href="cli.py#L1">cli.py</a> (click to expand)</summary>

This file contains the function [`main`](cli.py#L62%23L170), which implements the pipeline's command line tool. It uses the [Click](http://click.pocoo.org/) Python package to do this.

</details>

<details><summary><a href="core.py#L1">core.py</a> (click to expand)</summary>

This file contains the following functions:

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
  </details>

<details><summary><a href="gelman_rubin.py#L1">gelman_rubin.py</a> (click to expand)</summary>

This file contains the following functions:

- [`GR_diag`](gelman_rubin.py#L30%23L47)

Helper function to `GR_result`

- [`psrf`](gelman_rubin.py#L50%23L93)

Helper function to `GR_result`

- [`GR_result`](gelman_rubin.py#L96%23L161)

Obtains the maximum burnin for the chains

</details>

<details><summary><a href="gev_utils.py#L1">gev_utils.py</a> (click to expand)</summary>

This file contains the following functions:

- [`loglikelihood`](gev_utils.py#L27%23L52)

This function implements the log-likelihood.

- [`logprior`](gev_utils.py#L55%23L75)

This function implements the prior distribution.

- [`logpost`](gev_utils.py#L78%23L112)

In this function, we add the the log-prior and log-likelihood together to obtain the log-posterior score.

</details>

<details><summary><a href="utils.py#L1">utils.py</a> (click to expand)</summary>

This file contains the following functions:

- [`check_params`](utils.py#L30%23L94)

This function takes in the settings found in the configuration file, and parses them to make sure required parameters were passed in and also inserts common settings to optional parameters, not were not included in the configuration file.

- [`read_and_clean`](utils.py#L97%23L187)

- [`log`](utils.py#L190%23L211)
  </details>