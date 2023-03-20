#!/bin/bash

# Install the package including all development dependencies
pip install --user -e .[dev] 

# Copy the config sample file
cp "./scripts/config.sample.py" "./scripts/config.py"

# Copy the credentials sample file
cp "./scripts/credentials.sample.py" "./scripts/credentials.py"
