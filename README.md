# SSPipeline v0.1.dev0 <img alt="CI Build Status" src="https://img.shields.io/travis/MUSSLES/sspipeline/master.svg?style=flat-square&label=CI"> ![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg?style=flat-square) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)

## Synopsis

TODO

### Important Notes:

- This project is in early stages of development and there will be bugs. Many methods must be used with care and could be improved significantly. The developers take no responsibility for inappropriate application of the code or incorrect conclusions drawn as a result of their application. Users must take responsibility for ensuring results obtained are sensible. We hope that by releasing the code at this stage the community can move forward more quickly together.
- This project is **only** tested on Python 3.6! It can possibly work on other Python versions, but please use at your own risk!

## Directory Structure

./

- SSPipeline "home" directory

./doc/

- ./doc/joss_paper

    - home to the SSPipeline JOSS paper (currently not submitted)

- ./doc/source

    - sphinx-doc source code for the SSPipeline documentation

./example/

- an example for SSPipeline

./sspipeline/

- all the source code for SSPipeline

## Motivation

TODO

## Installation

### For the Impatient

Disclaimer: Since this project is still in the developmental stage, and we are not updating the package on PyPi as much as we would like to, so this way of installation might be a bit old (being impatient always has it's downsides):

```sh
pip install sspipeline
```

### Bleeding Edge

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

Note: You might have to use `pip3` instead of `pip`.

## Code Example: Analyzing storm surges for Grand Isle, Louisiana, USA

Before you continue, make sure that you have SSPipeline installed. You can check this by typing `sspipeline --help`. Make sure that you're in the home directory of this repository, in other words, where this files is located.

```sh
# move to the example directory
cd example
# run the example
bash bootstrap.sh run
```

### Things to do differently

TODO

## Citation

If SSPipeline has enabled significant parts of an academic publication, please acknowledge that by citing the software. At the moment, we are currently planning on submitting a paper to the Journal of Open Source Software (JOSS), but until a specific publication is written about SSPipeline, please cite the GitHub URL: www.github.com/MUSSLES/sspipeline.

You can however check out a proof of the paper that we will be submitting to JOSS [here](https://github.com/MUSSLES/sspipeline/blob/master/doc/joss_paper/paper.pdf).

## License Info

This code is offered under the [GNU General Public License version 3](LICENSE).
