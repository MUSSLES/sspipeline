# SSPipeline v0.1.dev0 [![Travis CI](https://travis-ci.org/MUSSLES/sspipeline.svg?branch=master)](https://travis-ci.org/MUSSLES/sspipeline) ![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg?style=flat-square) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)

## Synopsis

TODO

### Important Notes:

- This project is in early stages of development and there will be bugs. Many methods must be used with care and could be improved significantly. The developers take no responsibility for inappropriate application of the code or incorrect conclusions drawn as a result of their application. Users must take responsibility for ensuring results obtained are sensible. We hope that by releasing the code at this stage the community can move forward more quickly together.
- This project is **only** tested on Python 3.6! It can possibly work on other Python versions, but please use at your own risk!

## Directory Structure

./

- SSPipeline "home" directory

./docs/

- ./docs/joss_paper

    - home to the SSPipeline JOSS paper (currently not submitted)

- ./docs/source

    - sphinx-doc source code for the SSPipeline documentation

./sspipeline/

- all the source code for SSPipeline

./tests/

- the test(s) that Travis runs to make sure that everything is okay

## Motivation

The motivation for the SSPipeline is detailed in the [project paper](https://github.com/MUSSLES/sspipeline/blob/master/docs/joss_paper/paper.pdf):

    Effective management of coastal risks demands projections of flood hazards that account for
    a wide variety of potential sources of uncertainty. Two typical approaches for estimating
    flood hazards include (1) direct physical process-based modeling of the storms themselves,
    and (2) statistical modeling of the distributions and relevant characteristics of extreme
    sea level events. Recently, flexible and efficient mechanistically-motivated models for sea-
    level change have become widely used for characterizing uncertainty in projections of mean
    sea levels (Oppenheimer & Alley, 2016). Although the information obtained from modeling mean
    sea levels if useful, there is also a need for additional research for measuring extreme sea
    levels. The above, is a motivating factor in the focus within the SSPipeline (Storm Surge
    Pipeline) project, which characterizes uncertainty in estimates of extreme sea levels, using
    a statistical modeling approach. Specifically, the SSPipeline project includes processes for
    raw sea level data and fits a statistical distribution to the extreme sea levels, which
    permits estimation of the probabilities associated with extreme sea levels.

    To satisfy the demand for fast estimation of flood hazard and characterization of
    uncertainty, we implemented an API that only requires a user to configure a text file, which
    includes arguments for the tide gauge data set, some statistical modeling paramters, and
    output options. The the program will run, from a single terminal command, resulting in a
    suite of calibration and diagnostic routines. Importantly, the output consists of a set of
    diagnostic plots, data sets of calibrated parameters, and storm surge return level
    estimates. Secondly, the program is modular so that developers can extend the options for
    statistical modeling or calibrate the methods employed if they so choose.

## Installation

### For the Impatient

Disclaimer: Since this project is still in the developmental stage, and we are not updating the package on PyPi as much as we would like to, so this way of installation might be a bit old (being impatient always has it's downsides):

```sh
pip install sspipeline
```

### Longer-term Support

Note that since we're still developing SSPipeline, 

To obtain the codes:

```sh
git clone https://github.com/mussles/sspipeline.git
```

Next, you have two choices: 1) you can install SSPipeline permanently, this can be nice, although you can't edit the code; or 2) you can install the source code in editable form, so that the command line tool automatically reloads whenever you edit any code. For option 1:

```sh
pip install .
```

For option 2:

```sh
pip install -e .
```

Disclaimer: You might have to use `pip3` instead of `pip`.

## Code Example: Projecting sea level for Grande Isle, Louisiana, USA

Below, is just showing you how to run the code in our [example repository](https://github.com/MUSSLES/sspipeline-example).

```sh
# clone the repository
git clone https://github.com/mussles/sspipeline-example.git
# move to the example directory
cd sspipeline-example
# run the example
bash run.sh run
```  

## Citations

If SSPipeline has enabled significant parts of an academic publication, please acknowledge that by citing the software. Until a specific publication is written about SSPipeline please cite the github URL: www.github.com/MUSSLES/sspipeline

## License Info

This code is offered under the [GPLv3 License](LICENSE).
