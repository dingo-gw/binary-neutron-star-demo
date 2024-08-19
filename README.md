# Dingo-BNS: Gravitational-wave inference for binary neutron stars 

This repository contains demos for running the machine learning framework Dingo-BNS, 
which performs fast and accurate inference of gravitational waves from binary neutron 
stars.


## System requirements

Dingo-BNS is based on the python package [dingo](https://github.com/dingo-gw/dingo). 
With the installation instructions below, all required software for running Dingo-BNS 
will be installed automatically (for specific requirements see 
[here](https://github.com/dingo-gw/dingo/blob/bns_add_dingo_pipe_max/pyproject.toml)). 
The demos in this repository have been tested on Ubuntu 22 with python 3.8, but Dingo-BNS 
should work on any operating system. The demos in this repository can be run on CPUs, 
but fastest inference is achieved with modern GPUs.


## Setup

For the setup, follow the steps below.

1. Create a new project directory for this demo and navigate to this directory.
2. Clone the demo repository.
   ```shell
    git clone https://github.com/dingo-gw/binary-neutron-star-demo.git
   ```
3. Install Dingo-BNS.
    ```shell
    chmod +x binary-neutron-star-demo/installation.sh 
    ./binary-neutron-star-demo/installation.sh
    ```

This creates a virtual python environment with an installation of Dingo. 
Installation on Ubuntu 22 takes about 15 minutes.
After successful installation, the project directory should contain three subdirectories, 
`binary-neutron-star-demo` (demo directory), `dingo` (dingo installation), 
`dingo-bns-env` (virtual environment).

In the future, we will merge Dingo-BNS into the main branch, such that it can be 
installed in the usual way from PyPI or conda. At present, however, Dingo-BNS is not yet 
merged into main, but instead contained in a separate 
[branch](https://github.com/dingo-gw/dingo/tree/bns_add_dingo_pipe_max). The 
installation script thus downloads the Dingo development repo, switches to the 
Dingo-BNS branch and then installs Dingo manually. 


## Citation
```
@article{Dax:2024mcn,
    author = {Dax, Maximilian and Green, Stephen R. and Gair, Jonathan and Gupte, Nihar and P\"urrer, Michael and Raymond, Vivien and Wildberger, Jonas and Macke, Jakob H. and Buonanno, Alessandra and Sch\"olkopf, Bernhard},
    title = "{Real-time gravitational-wave inference for binary neutron stars using machine learning}",
    eprint = "2407.09602",
    archivePrefix = "arXiv",
    primaryClass = "gr-qc",
    reportNumber = "LIGO-P2400294",
    month = "7",
    year = "2024"
}
```
