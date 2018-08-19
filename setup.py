# -*- coding: utf-8 -*-

import setuptools
import versioneer

with open("README.md", "r") as handle:
    long_description = handle.read()

if __name__ == "__main__":
    setuptools.setup(
        name='pipeline',
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        description='TODO',
        author='John Letey',
        author_email='john.letey@colorado.edu',
        url="https://github.com/MUSSLES/pipeline",
        license='GNU General Public License v3',
        packages=setuptools.find_packages(),
        entry_points={"console_scripts": ["pipeline=pipeline:cli_main"]},
        install_requires=[
            'click',
            'numpy',
            'pandas',
            'scipy'
        ],
        extras_require={
            'docs': [
                'sphinx==1.2.3',  # autodoc was broken in 1.3.1
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
            'tests': [
                'pytest',
                'pytest-cov',
                'pytest-pep8',
                'flake8'
            ],
        },

        tests_require=[
            'pytest',
            'pytest-cov',
            'pytest-pep8',
            'flake8'
        ],

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
        ],
        zip_safe=True,
        long_description=long_description,
        long_description_content_type="text/markdown",
    )
