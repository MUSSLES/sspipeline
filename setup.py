#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 The MUSSLES Developers
#
# This file is part of MUSSLES.
#
# MUSSLES is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MUSSLES is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MUSSLES.  If not, see <http://www.gnu.org/licenses/>.

import io
import os
from setuptools import setup, find_packages

NAME = "sspipeline"
DESCRIPTION = "SSPipeline: A pipeline for estimating and characterizing uncertainty in coastal storm surge levels"
MAINTAINER = "John Letey"
MAINTAINER_EMAIL = "john.letey@colorado.edu"
URL = "https://github.com/mussles/sspipeline"
LICENSE = "GPL"


here = os.path.abspath(os.path.dirname(__file__))


def read(path, encoding="utf-8"):
    with io.open(path, encoding=encoding) as f:
        content = f.read()
    return content


LONG_DESCRIPTION = read(os.path.join(here, "README.md"))

# Want to read in package version number from __version__.py
# about = {}
# with io.open(os.path.join(here, "sspipeline", "__version__.py"), encoding="utf-8") as f:
#     exec(f.read(), about)
#     VERSION = about["__version__"]

setup(
    name=NAME,
    version="sspipeline:__version__",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    author=MAINTAINER,
    author_email=MAINTAINER_EMAIL,
    license=LICENSE,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: GPL License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(),
    install_requires=[
        "click",
        "tqdm",
        "numpy",
        "pandas",
        "scipy",
        "matplotlib",
        "sphinx",
        "sphinx_rtd_theme",
        "numpydoc",
    ],
    entry_points={"console_scripts": ["sspipeline=sspipeline:main"]},
    setup_requires=["setuptools>=38.6.0"],
)
