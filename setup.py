#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 The MUSSLES developers
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

import setuptools

exec(open("sspipeline/version.py").read())  # grab version info

with open("readme.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="sspipeline",
    version=__version__,
    author=__author__,
    author_email=__email__,
    description="A pipeline for estimating and characterizing uncertainty in coastal storm surge levels",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3",
    url="https://github.com/MUSSLES/sspipeline",
    packages=["sspipeline"],
    entry_points={"console_scripts": ["sspipeline=sspipeline:cli_main"]},
)
