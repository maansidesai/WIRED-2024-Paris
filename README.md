# WIRED 2024 - MNE Python Tutorial lead by Maansi Desai, Alexandre Gramfort, and Apolline Mellot

### Authors:
* [Maansi Desai, PhD](https://maansidesai.github.io/)
Postdoctoral Researcher in the [Hamilton Lab](https://slhs.utexas.edu/research/hamilton-lab)
Department of Speech, Language, and Hearing Sciences
The University of Texas at Austin
* [Alex Gramfort](https://alexandre.gramfort.net/), Research Scientist, Meta Reality Labs, Paris, France
* [Apolline Mellot](https://github.com/apmellot), PhD Student at Inria, Université Paris-Saclay, France

## Getting Started
Welcome to the WIRED 2024 [MNE Python](https://mne.tools/stable/index.html) Tutorial! If you're reading this, hopefully you are getting started learning how to use python and jupyter notebooks to do some analysis of neuroscience data! In this tutorial, we will be using several [BIDS](https://bids-specification.readthedocs.io/en/stable/)-formatted [intracranial datasets](https://bids-specification.readthedocs.io/en/stable/modality-specific-files/intracranial-electroencephalography.html). The tutorials here are organized into Jupyter notebooks that will go through a series of concepts that will give you the foundation for what you need to preprocess and plot epochs using [MNE-Python](https://mne.tools/stable/index.html). 

## Installation Instructions
* First you should install [MNE-python](https://mne.tools/stable/install/index.html). We recommend using the standalone installer.
* Start up MNE-prompt (or your MNE environment), and install the required python libraries in `requirements.txt`:
```bash
pip install -r requirements.txt
```
* Install the [openneuro-py](https://github.com/hoechenberger/openneuro-py) client (see the link for more detailed instructions).
```bash
# via conda:
conda install -c conda-forge openneuro-py
# or via pip:
pip install openneuro-py
```
* Download the datasets for this tutorial. We recommend that you place them in a data folder in the repo (this will be ignored by `git` by default -- the files are too big for git repositories). The installation below will install all the data from our sample dataset and one subject's data from Berezutskaya et al. If you wish to download more data, you may do that on your own.
```bash
# Launch MNE-prompt, then do the following
cd /path/to/WIRED-2024-Paris/notebooks
mkdir data
cd data
openneuro-py download --dataset ds003688 --include sub-06
openneuro-py download --dataset ds004993
```

## Datasets we will be using to demonstrate preprocessing intracranial data and plotting evoked responses:
1) Data collected from three pediatric sEEG patients in the Hamilton Lab [https://openneuro.org/datasets/ds004993/versions/1.0.2]. This is ~300 MB
2) Berezutskaya iEEG and fMRI data from movie viewing [https://openneuro.org/datasets/ds003688/versions/1.0.7]. This is 155 MB for one participant, and 15 GB for the whole dataset.

## List of notebooks
### 01_ieeg_preprocessing_MNE
First notebook which will load, plot, rereference, and inspect data for artifact rejection.

### 02_ieeg_preprocessing_MNE_epochs
The second notebook will involve learning about how to epoch your data.  Epoched data allows you to calculate averaged responses to events of interest (event-related potentials) and can be conducted based on the onset of the sentence, a phonene onset, or word onset (as examples to consider).
