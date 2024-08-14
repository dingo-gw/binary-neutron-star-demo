#!/bin/bash

# Create and activate a new virtual environment
python3 -m venv dingo-bns-env
source dingo-bns-env/bin/activate

# Clone the Dingo repository and checkout the Dingo-BNS branch
git clone https://github.com/dingo-gw/dingo.git
cd dingo
git checkout bns_add_dingo_pipe_max

# Install Dingo in the virtual environment
pip install -e .