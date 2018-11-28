<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD022 -->
<!-- markdownlint-disable MD040 -->

# SSPipeline v0.1.dev0 [![CI Build Status](https://img.shields.io/travis/MUSSLES/sspipeline/master.svg?style=flat&colorA=0a0a0a)](https://travis-ci.org/MUSSLES/sspipeline) [![Python 3.6](https://img.shields.io/badge/Python-3.6-0a0a0a.svg?style=flat&colorA=0a0a0a)](https://python.org) [![Code style: black](https://img.shields.io/badge/Code%20Style-black-0a0a0a.svg?style=flat&colorA=0a0a0a)](https://github.com/ambv/black)

<details><summary>Table of Contents (click to expand)</summary>

- [Motivation](#motivation)
  - [Important Notes](#important-notes)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
  - [For the Impatient](#for-the-impatient)
  - [Developmental Version](#developmental-version)
- [Examples & Usage](#examples-&-usage)
  - [Pre-Setup Examples](#pre-setup-examples)
  - [General Example](#general-example)
- [Citation](#citation)
- [License](#license)

</details>

## Motivation

Effective management of coastal risks demands projections of flood hazards that account for a wide variety of potential sources of uncertainty. Two typical approaches for estimating flood hazards include (1) direct physical process-based modeling of the storms themselves and (2) statistical modeling of the distributions and relevant characteristics of extreme sea level events. Recently, flexible and efficient mechanistically-motivated models for sea-level change have become widely used for characterizing uncertainty in projections of mean sea levels. In order to complement these models for mean sea levels, there is also a need for fast and flexible estimates of extreme sea levels, and corresponding uncertainties. This is the motivating factor in the focus within the SSPipeline (Storm Surge Pipeline) project, that characterizes uncertainty in estimates of extreme sea levels, using a statistical modeling approach. Specifically, the SSPipeline project ingests and processes raw sea-level data and fits a statistical distribution to the extreme sea levels, which in turn permits estimation of the probabilities associated with these extremes.

### Important Notes

- This project is in early stages of development and there will be bugs. Many methods must be used with care and could be improved significantly. The developers take no responsibility for inappropriate application of the code or incorrect conclusions drawn as a result of their application. Users must take responsibility for ensuring results obtained are sensible. We hope that by releasing the code at this stage the community can move forward more quickly together.
- This project is **only** tested on Python 3.6! It can possibly work on other Python versions, but use at your own risk, and please let us know about any issues.

## Directory Structure

./

- SSPipeline "home" directory

[`./doc/`](doc)

- home to both the SSPipeline JOSS paper (currently not submitted) and the SSPipeline documentation source code.

[`./example/`](example#readme)

- an example for SSPipeline

[`./sspipeline/`](sspipeline#readme)

- all the source code for SSPipeline

## Installation

### For the Impatient

Disclaimer: Since this project is still in the developmental stage, and we are not updating the package on PyPi as much as we would like to, so this way of installation might be a bit old (being impatient always has it's downsides):

    pip install sspipeline

### Developmental Version

To obtain the codes:

```
git clone https://github.com/mussles/sspipeline.git
```

Next, you can go into the `sspipeline` directory, and install the pipeline via `pip`:

```
cd sspipeline
pip install .
```

You might have to use `pip3` instead of `pip`. Note that if you want to develop the pipeline, you'll want to install an editable version, so that the pipeline automatically reloads whenever you changes the codes:

```
pip install -e .
```

You can check your pipeline installation by running `sspipeline --help`.

## Examples & Usage

Before you take a look at the examples, make sure that you have the pipeline installed (see the [Installation](#installation) section above).

### Pre-Setup Examples

These examples were put together to show you what the output of the pipeline looks like. To run them:

```
sh
# move to the example directory
cd example
# run the example
bash bootstrap.sh run
```

You can see more about this [here](example#readme).

### General Example

First, in the spirit of the pre-set-up examples, let us create a new directory for our test case (here, demonstrating using the data set for Wilmington, NC, ID=h750a). We also create sub-directories for the data and the output, and directories within the output directory, for plots and parameter output.

```
cd pipeline
mkdir h750a
cd h750a
mkdir data
mkdir output
cd output
mkdir plots
mkdir parameters
cd ..
```

Input tide gauge data sets to the pipeline must be hourly datasets set up in the format of the [University of Hawaii Sea Level Center (UHSLC)](https://uhslc.soest.hawaii.edu/data/?rq). You can either choose to download the hourly CSV version of your chosen data, or you can simply execute the following command in your terminal:

```
curl -# https://uhslc.soest.hawaii.edu/data/csv/rqds/[region]/hourly/h[UH#][version].csv > ./data/[local name].csv
```

This command downloads the dataset to whatever directory you are run the command in, but that assumes that you filled in your datasets appropiate UH# and version correctly, which can be found on the website. Wherever you place this data set should match the relative path set for `data` in the config.json file below. For example, to grab the data for Wilmington, NC, and place it in a file called wilmington.csv in the `data` directory, this command is:

```
curl -# https://uhslc.soest.hawaii.edu/data/csv/rqds/atlantic/hourly/h750a.csv > ./data/wilmington.csv
```

After you have downloaded your sea level dataset from UHSLC, you can start to fill out your pipeline configuration. Below, is a list of all the possible parameters that you can pass in to the pipeline, and whether or not they are optional:

- `data` is **not** an optional parameter, and you should always pass this in! Please note that this should be where the dataset file is located in your PATH relative to where you will be running the pipeline from, and not where the configuration file is located.
- `iterations` is an optional parameter with default 10000. This is the number of iterations for each Markov chain.
- `adaption` is technically an optional parameter, since just as long as you pass in `iterations`, the pipeline will by default take 10% of `iterations` and set it to `adaption`. This is the number of iterations at which to begin the adaptation of the proposal covariance matrix (step sizes for multivariate normal random walk).
- `sequences` is an optional parameter with defualt 3. This is the number of Markov chain sequences to simulate. Must be at least two in order to use the potential scale reduction factor to evaluate Markov chain convergence.
- `transition` is **not** an optional parameter, and you should always pass this in! This is the initial Markov chain proposal step sizes (using Gaussian random walk). Must be a list of length = number of parameters to calibrate.
- `gr_theshold` is an optional parameter with default 1.1. This is the threshold for the potential scale reduction factor, below which we diagnose convergence to the posterior/stationary distribution.
- `acf_theshold` is an optional parameter with default 0.05. This is the threshold for the autocorrelation function. Once the maximum ACF (among all parameters and chains) is below this threshold, we diagnose that sampling at that lag yields (relatively) independent draws from the Markov chains.
- `output_dir` is an optional parameter with default "output". This is where the output from the pipeline will be stored, relative to the current directory.
- `percentage` is an optional parameter with default 0.9. Years with fewer than this percentage of data points present will be removed from the analysis.
- `plot` is an optional parameter with default 1. This represents whether or not to output diagnostic plots.
- `verbose` is an optional parameter with default 0 (which means don't be verbose).

Thus, we can use all of the above parameters, and make a template configuration file (note that this uses the JSON format):

```
{
  "data": "data/wilmington.csv",
  "output_dir": "output/",
  "percentage": 0.9,
  "iterations": 5000,
  "sequences": 4,
  "adaption": 500,
  "acf_threshold": 0.05,
  "gr_threshold": 1.1,
  "transition": [
    10,
    2,
    0.01
  ],
  "verbose": 1,
  "plot": 1
}
```

You can copy-paste this above template directly into a file named `config.json` in your current directory, or if you like, you can name it whatever you like and place it wherever you like as well. If you place your configuration file in `config.json` in your current directory (in this example, assumed to be the h750a directory we created above), to run the pipeline, execute the below command in that same directory:

```
sspipeline
```

Make sure that you are running this command from the same directory as the one that contains the `config.json` file in it. However, if you decided to put your configuration in a different file, please run the following command:

```
sspipeline --config [your configuration file name relative to your current directory]
```

For example:

```
sspipleine --config my_special_dir/another_one/my_weird_config_file.json
```

Please make sure that your configuration file is always of type JSON.

If everything is running smoothly, the pipeline default cases and gentle modifications thereof run in about 5-10 minutes on a modern laptop computer (for three sequences at 10,000 iterations each).

## Caveats and known potential hurdles

1.  If you Python packages/libraries are out-of-date, then it is recommended that you update them before
running the sspipeline. Namely, the `hist` (histogram) method distinguishes between `normed` (deprecated) and
`density` arguments to generate a density histogram, and this can cause problems (we use the `density`
argument here, which might not work with older libraries).

## Citation

If SSPipeline has enabled significant parts of an academic publication, please acknowledge that by citing the software. You can cite the project by using one of the following identifiers:

- [Earth ArXiv](https://eartharxiv.org/t6358), DOI: 10.31223/osf.io/t6358

## License

[![GPLv3](https://img.shields.io/badge/license-GPLv3-0a0a0a.svg?style=flat&colorA=0a0a0a)](LICENSE)
