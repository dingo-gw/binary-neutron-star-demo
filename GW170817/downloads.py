import numpy as np
import os
import requests
from tqdm import tqdm


def download_file(url, filename):
    """Download file with progress bar.

    From https://stackoverflow.com/questions/40544123/how-to-use-tqdm-in-python-to-show-progress-when-downloading-data-online."""
    r = requests.get(url, stream=True)

    with open(filename, "wb") as f:
        pbar = tqdm(
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
            total=int(r.headers["Content-Length"]),
        )
        pbar.clear()  #  clear 0% info
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                pbar.update(len(chunk))
                f.write(chunk)
        pbar.close()
    return filename


os.makedirs("downloads", exist_ok=True)

print("\n\n### Dingo model ###")
url = "https://zenodo.org/records/13321251/files/dingo-bns-model_GW170817.pt?download=1"
filename = "downloads/dingo-bns-model_GW170817.pt"
print("Downloading model from zenodo. This may take a while, as the model is large.")
download_file(url, filename)

print("\n\n### PSDs ###")
url = "https://dcc.ligo.org/public/0158/P1900011/001/GWTC1_GW170817_PSDs.dat"
filename = "downloads/GWTC1_GW170817_PSDs.dat"
print("Downloading PSDs from LIGO DCC.")
download_file(url, filename)
print("Repackaging PSDs.")
psds = np.loadtxt(filename)
ifos = {1: "H1", 2: "L1", 3: "V1"}
for idx, ifo in ifos.items():
    np.savetxt(f"downloads/GWTC1_GW170817_PSD_{ifo}.txt", psds[:, [0, idx]])

print("\n\n### GW frame files ###")
print("Downloading GW frame files from LIGO DCC.")
for ifo in ["H1", "L1", "V1"]:
    frame_file = f"{ifo[:1]}-{ifo}_LOSC_CLN_4_V1-1187007040-2048.gwf"
    url = "https://dcc.ligo.org/public/0146/P1700349/001/" + frame_file
    filename = "downloads/" + frame_file
    download_file(url, filename)
