#!/bin/bash

echo "Building dist..."
python3 setup.py sdist
mkdir -p docs/source/_static/dists
mv dist/*.tar.gz docs/source/_static/dists
rm -rf dist
echo "Successfully built dist!"

echo "Building documentation..."
cd docs
make clean
make html
cd ../
echo "Successfully built the documentation!"