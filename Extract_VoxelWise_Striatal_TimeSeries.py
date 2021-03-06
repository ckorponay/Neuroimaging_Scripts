#!/bin/tcsh -xef

####Extract the signal intensity at each TR from each voxel in the striatum#####

set subjList = (100307 101006 103414 105014 105115 106521 107422 113619 114419 118528 122620 127933 129028 131217 133928 135225 138231 139637 141422 144832 148335 148840 149539 153025 158136 161630 163129 172332 173536 173940 175035 178950 180129 180432 181232 183034 188347 189349 190031 192843 194645 195041 195849 196144 205725 210011 210617 212116 212419 221319 224022 251833 268850 285345 285446 307127 334635 397154 397760 414229 422632 485757 486759 499566 530635 545345 567961 627549 654754 709551 748258 771354 782561 833148 904044 958976 965367)

foreach subj ($subjList)

cd $subj

3dmaskdump -noijk  -mask ../Group_R_Striatum_mask_bin.nii Clean_rfMRI_REST1_LR.nii.gz > rStriatum_Clean_TimeSeries.1D

1dcat -csvout rStriatum_Clean_TimeSeries.1D > {$subj}_rStriatum_Clean_TimeSeries.csv

3dmaskdump -noijk  -mask ../Group_L_Striatum_mask_bin.nii Clean_rfMRI_REST1_LR.nii.gz > lStriatum_Clean_TimeSeries.1D

1dcat -csvout lStriatum_Clean_TimeSeries.1D > {$subj}_lStriatum_Clean_TimeSeries.csv

cd ../

end


