<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD022 -->

# SSPipeline v0.1.dev0 ![CI Build Status](https://img.shields.io/travis/MUSSLES/sspipeline/master.svg?style=flat-square&label=CI) ![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg?style=flat-square) [![Code style: black](https://img.shields.io/badge/Code%20Style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)

<details><summary>Table of Contents</summary>

- [Motivation](#motivation)
  - [Important Notes](#important-notes)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
  - [For the Impatient](#for-the-impatient)
  - [Developmental Version](#developmental-version)
- [Code Examples](#code-examples)
  - [Pre-Setup Examples](#pre-setup-examples)
  - [Template Example](#template-example)
- [Citation](#citation)
- [License Info](#license-info)

</details>

## Motivation

For a while now, sea-level rise has been gradually becoming a bigger and bigger deal. A lot of people often look at mean sea-levels to depict how much sea-levels are rising on average, but we wanted to look at extreme sea levels (a.k.a storm surges) over annual maxima blocks. This work is extremely helpful for determining how tall to build a levee. With our work, you can determine the return levels for your sea level dataset.

### Important Notes

- This project is in early stages of development and there will be bugs. Many methods must be used with care and could be improved significantly. The developers take no responsibility for inappropriate application of the code or incorrect conclusions drawn as a result of their application. Users must take responsibility for ensuring results obtained are sensible. We hope that by releasing the code at this stage the community can move forward more quickly together.
- This project is **only** tested on Python 3.6! It can possibly work on other Python versions, but please use at your own risk (and your computer's risk too)!

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

    git clone https://github.com/mussles/sspipeline.git

Next, you can install the pipeline via `pip`:

    pip install .

You might have to use `pip3` instead of `pip`. Note that if you want to develop the pipeline, you'll want to install an editable version, so that the pipeline automatically reloads whenever you changes the codes:

    pip install -e .

You can check your pipeline installation by running `sspipeline --help`.

## Code Examples

Before you run the following, make sure that you have the SSPipeline installed (see the [Installation](#installation) section above).

### Pre-Setup Examples

```sh
# move to the example directory
cd example
# run the example
bash bootstrap.sh run
```

You can see exactly what this does [here](example#readme).

### Template Example

Here, we're going to walk you through the different steps that you will need to do in order to successfully use our tool.

Let's start with the data. As you may know, our pipeline only takes in _hourly_ data from The University of Hawaii Sea Level Center (UHSLC). You can go to there website by simply clicking this [link](https://uhslc.soest.hawaii.edu/data/?rq) and find yourself a nice dataset that fits your needs. Wence you have found a dataset that you like, you can either choose to download the hourly csv version of the data, or you can simply execute the following command in your terminal:

    curl -O http://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/hourly/h[UH#][version].csv

This command downloads the dataset to whatever directory you are currently in, assuming that you filled in your datasets appropiate UH# and version correctly.

**_Fill In Some More Here!_**

The foll an example template for a config file (please note that most of these values are default):

```json
{
  "acf_threshold": 0.05,
  "adaption": 300,
  "data": h[UH#][version].csv,
  "gr_threshold": 1.1,
  "iterations": 3000,
  "output_dir": "output/",
  "percentage": 0.9,
  "plot": 1,
  "sequences": 3,
  "transition": [10, 2, 0.01],
  "verbose": 1
}
```

You can copy-pasta this above template directly into a file named `config.json` in your current directory, or you can name it something else. If you place your configuration file in `config.json`, in order to run the pipeline, all you have to do is run:

    sspipeline

Just make sure that you are running this command from the same directory as the one that contains the `config.json` file in it. However, if you decided to put your configuration in a different file, please run the following command:

    sspipeline --config [your configuration file name relative to your current directory]

For example:

    sspipleine --config my_special_dir/another_one/my_weird_config_file.json

Please make sure that your configuration file is always of type JSON.

If you do all of the above correctly, you should have the pipelines output within 5 minutes!

## Citation

If SSPipeline has enabled significant parts of an academic publication, please acknowledge that by citing the software. At the moment, we are currently planning on submitting a paper to the Journal of Open Source Software (JOSS), but until a specific publication is written about SSPipeline, please cite the GitHub URL: www.github.com/MUSSLES/sspipeline.

You can check out a draft of the paper that we will be submitting to JOSS [here](doc/joss_paper/paper.pdf).

## License Info

This code is offered under the [GNU General Public License version 3](LICENSE).
