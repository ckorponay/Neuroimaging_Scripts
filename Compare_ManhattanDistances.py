#!/bin/tcsh -xef

#flip striatal map into the opposite hemisphere, in order to line up R and L striatal voxels for comparison
3dLRflip -LR -prefix ppp RvL_ManhattanDistance.nii

3dAFNItoNIFTI ppp+tlrc.

#create an intersection mask to mask the comparison analysis within, in order to ensure that only voxels with both R and L values get compared

3dmask_tool -input ppp.nii RvL_ManhattanDistance_Lstriatum.nii -prefix Intersect.nii -inter

### take the difference of the Manhattan Distance values at each paired voxel

3dcalc -a RvL_ManhattanDistance_Lstriatum.nii -b ppp.nii -expr "abs(a-b)" -datum float -prefix MD_diff.nii


###Need to mask the output to the intersect mask

 mris_calc -o MD_diff_masked.nii MD_diff.nii mul Intersect.nii
 
 
 #Now, need to permute the DIFFERENCE of two Manhattan Distance values in R 
