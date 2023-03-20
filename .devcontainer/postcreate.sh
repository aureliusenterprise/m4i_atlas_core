#!/bin/bash
pip install -e .[dev]
cp "./scripts/config.sample.py" "./scripts/config.py"
cp "./scripts/credentials.sample.py" "./scripts/credentials.py"
