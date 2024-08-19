# GW170817 inference with Dingo-BNS

This demo performs inference for GW170817 with the settings from the [LVK parameter 
estimation paper](https://link.aps.org/doi/10.1103/PhysRevX.9.011001) (with some small 
differences, such as omitting marginalization over detector calibration uncertainty).
A corresponding Dingo-BNS model is provided, so this demo can be run without training.
Inference can be run on stanard hardware, a GPU is not required.


### Preparation

Activate the virtual environment with the Dingo-BNS installation (see project README 
for installation instructions). Navigate into the present `GW170817` directory.  

### Data download

To download the data, run 
```shell
python downloads.py
```
This creates a directory `downloads` containing the trained Dingo-BNS model and 
the measured data (a noise PSD and a GW strain file for each of the three detectors `H1, 
L1, V1`). The model is downloaded from [zenodo](https://zenodo.org/records/13321251) 
and the data is downloaded from ligo dcc 
([strain](https://dcc.ligo.org/LIGO-P1700349/public), 
[PSDs](https://dcc.ligo.org/LIGO-P1900011/public)).


### Running Dingo-BNS

Optionally, modify the config file `inference-dingo-pipe/GW170817.ini` to optimize for 
your hardware. Set `request-cpus-importance-sampling` to the number of available 
CPU cores (default 8) and set `device = 'cuda` if a GPU is available (default `'cpu'`).
With a modern GPU (e.g., H100), the `batch-size` can usually be set to the same value 
as `num-samples` to speed up inference.

To run inference, navigate to the analysis directory with
```shell 
cd inference-dingo-pipe
```
and run `dingo_pipe` with
```shell
dingo_pipe GW170817.ini
```


### Expected output
The above command runs `dingo_pipe` locally, creating several directories. The result 
files are stored in the `result` folder, which also contains plots that visualize the 
importance weights and a corner plot comparing the neural network prediction to the 
importance sampled result.

For the present configuration, the importance sampling efficiency should be around 10%.


### Inference time
The inference script should run in less than a minute.
This time is dominated by data loading and processing operations 
(e.g., import of libraries, loading neural network weights from disk, plotting). 
Such operations would be accelerated in a low latency setting.

The inference time itself (neural network sampling and importance sampling) depends on 
the hardware and the requested number of samples. 
With 8 CPUs, neural network sampling takes ~7 seconds and importance sampling ~3 seconds 
for `num-samples = 10_000`. 
With an H100 GPU and `num-samples = 50_000`, neural network sampling takes ~0.4 seconds 
(note that the first forward pass is always a bit slower due to various 
initializations and optimizations by the pytorch backend, so for optimal performance 
in low latency applications, the neural network should be initialized beforehand).
Note that the jax likelihood implementation is not yet merged into the public branch, 
so this demo currently uses the slower CPU-only likelihood implementation.
