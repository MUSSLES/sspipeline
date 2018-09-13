# SSPipeline Code

### [`__init__.py`](__init__.py)

This file is very minor to the actual proccess of the analysis of sea levels, and is only needed to build the Python package. TODO

### [`__version__.py`](__version__.py)

This file contains the version of the command line tool. Nothing too important! TODO

### [`acf.py`](acf.py)

This code file implements the Auto Correlation Function, which was proposed by TODO.

This file includes one major function, used throughout the analysis, with some of it's helper functions. See the function declaration [here](https://github.com/MUSSLES/sspipeline/blob/master/sspipeline/acf.py#L51%23L95).

### [`cli.py`](cli.py)

This code file implements the `sspipeline` command line tool. It uses the [click](http://click.pocoo.org/) Python package to achieve this.

### [`core.py`](core.py)

TODO

### [`gelman_rubin.py`](gelman_rubin.py)

This code file implements the Gelman & Rubin Diagnostic, which was proposed by Andrew Gelman and Donald B. Rubin in 1992  in their *Inference from Iterative Simulation Using Multiple Sequences* paper. TODO

This file includes one major function, used throughout the analysis, with some of it's helper functions. See the function declaration [here](https://github.com/MUSSLES/sspipeline/blob/master/sspipeline/gelman_rubin.py#L96%23L161).

### [`gev_utils.py`](gev_utils.py)

TODO

### [`utils.py`](utils.py)

TODO