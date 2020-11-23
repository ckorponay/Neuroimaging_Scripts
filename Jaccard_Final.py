#!/bin/tcsh -xef

# Use fslstats to get the number of voxels in roi1
#fslstats ${roi1} -V

# Use fslstats to get the number of voxels in roi2
#fslstats ${roi2} -V

# Use fslstats -k to mask roi2 with roi1, and get the number of voxels in the intersection
fslstats DILATED1.1_vlPFC_Glasser_mask_GM_bin.nii.gz  -k vlPFC_Petrides_mask.nii -V

# Use fslstats -add to add roi1 and roi2, and get the number of voxels in the union

fslmaths DILATED1.1_vlPFC_Glasser_mask_GM_bin.nii.gz -add vlPFC_Petrides_mask.nii -bin union
fslstats union -V
rm union.nii.gz


jaccard_index = ${intersect_voxels}/${union_voxels}

#correlation
3ddot vlPFC_Petrides_mask.nii vlPFC_Glasser_mask.nii
