# SSPipeline Source Code

## [`__init__.py`](__init__.py#L1)

This file is very minor to the actual proccess of the analysis of sea levels, and is only needed to build the Python package. TODO

## [`__version__.py`](__version__.py#L1)

This file contains the version of the command line tool. Nothing too important! TODO

## [`acf.py`](acf.py#L1)

This code file implements the Auto Correlation Function, which was proposed by TODO.

This file includes one major function, used throughout the analysis, with some of it's helper functions. See the function declaration [here](acf.py#L51%23L95).

## [`cli.py`](cli.py#L1)

This code file implements the SSPipeline command line tool. It uses the [Click](http://click.pocoo.org/) Python package to achieve this.

## [`core.py`](core.py#L1)

TODO

## [`gelman_rubin.py`](gelman_rubin.py#L1)

This code file implements the Gelman & Rubin Diagnostic, which was proposed by Andrew Gelman and Donald B. Rubin in 1992  in their *Inference from Iterative Simulation Using Multiple Sequences* paper. TODO

This file includes one major function, used throughout the analysis, with some of it's helper functions. See the function declaration [here](gelman_rubin.py#L96%23L161).

## [`gev_utils.py`](gev_utils.py#L1)

TODO

## [`utils.py`](utils.py#L1)

This file contains three functions, each of which are important to SSPipeline. The first function, [`check_params`](utils.py#L30%23L94), takes in the settings found in the configuration file, and parses them to make sure required parameters were passed in and also inserts common settings to optional parameters, not were not included in the configuration file. The next function, [`read_and_clean`](utils.py#L97%23L187), TODO. Last, but not least, [`log`](utils.py#L190%23L211), TODO.