# Install the package including all development dependencies
pip install -e .[dev] --user

# Copy the config sample file
cp ./scripts/config.sample.py ./scripts/config.py

# Copy the credentials sample file
cp ./scripts/credentials.py ./scripts/credentials.py