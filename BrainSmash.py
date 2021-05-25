#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 22:01:22 2021

@author: chk17
"""

### Use BrainSMASH to create permuted null voxel-wise striatum maps that preserve spatial autocorrelation ###


#####  First, get the a) brain map coordinates and b) brain map values for the two input files needed for BrainSmash:

## 1. 3dmaskdump -mask Group_R_Striatum_mask_bin.nii.gz -xyz -noijk -o PracticeData.1D IndividualSubj_MDfiles_Zscores/rStriatum/Discovery_Group_MDmap_Rstriatum_computedfromIndSubjs_Z.nii

## 2. 1dcat -tsvout PracticeData.1D > PracticeData1.tsv

## 3. Open in Excel, separate into a coordinates file and a values file, and save each as .txt files



## instructions for next parts here: https://brainsmash.readthedocs.io/en/latest/example.html


import pandas as pd; \
import numpy as np; \
import os
import sys
import scipy
import matplotlib
import nibabel

os.chdir('/Users/chk17')
    

### generate memory-mapped distance matrix files

from brainsmash.workbench.geo import volume

coord_file = "Desktop/voxel_coordinates_Lefty_rS.txt"
output_dir = "Desktop/"

filenames = volume(coord_file, output_dir)



### visually inspect the variogram fit, and alter parameters until good fit


from brainsmash.mapgen.eval import sampled_fit

brain_map = "Desktop/brain_map_Lefty_rS.txt"

# These are three of the key parameters affecting the variogram fit
kwargs = {'ns': 500,
          'knn': 500,
          'pv': 70
          }

# Running this command will generate a matplotlib figure
sampled_fit(brain_map, filenames['D'], filenames['index'], nsurr=100, **kwargs)




### once fit is good, generate the autocorrelation-preserving permuted brain maps

from brainsmash.mapgen.sampled import Sampled

gen = Sampled(x=brain_map, D=filenames['D'], index=filenames['index'], resample=True, **kwargs)
surrogate_maps = gen(n=10000)


### export permutated maps to CSV to then conduct permutation stat test in R

np.savetxt("ACpreserving_rStriatum_MDmap_permutations_Lefty.csv", surrogate_maps, delimiter=",")




