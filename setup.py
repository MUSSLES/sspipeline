# -*- coding: utf-8 -*-

import io
import os
import sys
import setuptools

NAME = "pipeline"
DESCRIPTION = "pipeline: TODO"
MAINTAINER = "John Letey"
MAINTAINER_EMAIL = "john.letey@colorado.edu"
URL = "https://github.com/mussles/pipeline"
LICENSE = "GNU General Public License v3"

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with io.open(
    os.path.join(here, "pipeline", "__version__.py"), encoding="utf-8"
) as f:
    exec(f.read(), about)
    VERSION = about["__version__"]

with open("README.rst", "r") as handle:
    long_description = handle.read()

if __name__ == "__main__":
    setuptools.setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        url=URL,
        license=LICENSE,
        packages=setuptools.find_packages(),
        entry_points={"console_scripts": ["pipeline=pipeline:cli_main"]},
        install_requires=["click", "numpy", "pandas", "scipy", "matplotlib"],
        extras_require={
            "docs": [
                "sphinx==1.2.3",  # autodoc was broken in 1.3.1
                "sphinxcontrib-napoleon",
                "sphinx_rtd_theme",
                "numpydoc",
            ],
            "tests": ["pytest", "pytest-cov", "pytest-pep8", "flake8"],
        },
        tests_require=["pytest", "pytest-cov", "pytest-pep8", "flake8"],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Science/Research",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
        ],
        zip_safe=True,
        long_description=long_description,
        long_description_content_type="text/x-rst",
    )
