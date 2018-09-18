<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD022 -->
# SSPipeline v0.1.dev0 ![CI Build Status](https://img.shields.io/travis/MUSSLES/sspipeline/master.svg?style=flat-square&label=CI) ![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg?style=flat-square) [![Code style: black](https://img.shields.io/badge/Code%20Style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)

<details><summary>Table of Contents</summary>

- [Synopsis](#synopsis)
  - [Important Notes](#important-notes)
- [Directory Structure](#directory-structure)
- [Motivation](#motivation)
- [Installation](#installation)
  - [For the Impatient](#for-the-impatient)
  - [Developmental Version](#developmental-version)
- [Code Examples](#code-examples)
- [Citation](#citation)
- [License Info](#license-info)

</details>

## Synopsis

TODO

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

## Motivation

For a while now, sea-level rise has been gradually becoming a bigger and bigger deal. A lot of people often look at mean sea-levels to depict how much sea-levels are rising on average, but we wanted to look at extreme sea levels (a.k.a storm surges) over annual maxima blocks, because this is extremely helpful when determining how tall to build a levee.

## Installation

### For the Impatient

Disclaimer: Since this project is still in the developmental stage, and we are not updating the package on PyPi as much as we would like to, so this way of installation might be a bit old (being impatient always has it's downsides):

    pip install sspipeline

### Developmental Version

To obtain the codes:

    git clone https://github.com/mussles/sspipeline.git

Next, you can either install SSPipeline permanently to your computer or you can install SSPipeline in editable form, so that the command line tool automatically reloads whenever you edit any code. For the former option:

    pip install .

For the latter option:

    pip install -e .

Note: You might have to use `pip3` instead of `pip`.

You can check your installation this by running `sspipeline --help`.

## Code Examples

Before you run the following, make sure that you have the SSPipeline installed (see the [Installation](#installation) section above).

```sh
# move to the example directory
cd example
# run the example
bash bootstrap.sh run
```

## Citation

If SSPipeline has enabled significant parts of an academic publication, please acknowledge that by citing the software. At the moment, we are currently planning on submitting a paper to the Journal of Open Source Software (JOSS), but until a specific publication is written about SSPipeline, please cite the GitHub URL: www.github.com/MUSSLES/sspipeline.

Note: You can check out a draft of the paper that we will be submitting to JOSS [here](doc/joss_paper/paper.pdf).

## License Info

This code is offered under the [GNU General Public License version 3](LICENSE).
