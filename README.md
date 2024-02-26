# WIRED 2024 - MNE Python Tutorial lead by Maansi Desai, Alexandre Gramfort, and Apolline Mellot

# Getting Started
Welcome to the WIRED 2023 MNE Python Tutorial! If you're reading this, hopefully you are getting started learning how to use python and jupyter notebooks to do some analysis of neuroscience data! In this tutorial, we will be using a BIDS dataset collected from a combination of intracranial (sEEG data). The tutorials here are organized into Jupyter notebooks that will go through a series of concepts that will give you the foundation for what you need to preprocess and plot epochs using MNE-Python. 

# Datasets we will be using to demonstrate preprocessing intracranial data and plotting evoked responses:
1) Data collected from two pediatric sEEG patients in the Hamilton Lab [https://openneuro.org/datasets/ds004993/versions/1.0.2]. This is 300 MB
2) Berezutskaya iEEG and fMRI data from movie viewing [https://openneuro.org/datasets/ds003688/versions/1.0.7]. This is 5GB

Please make sure you download both of these datasets locally. 

# List of notebooks
## 01_ieeg_preprocessing_MNE
First notebook which will load, plot, rereference, and inspect data for artifact rejection.

## 02_ieeg_preprocessing_MNE_epochs
The second notebook will involve learning about how to epoch your data.  Epoched data allows you to calculate averaged responses to events of interest (event-related potentials) and can be conducted based on the onset of the sentence, a phonene onset, or word onset (as examples to consider).
