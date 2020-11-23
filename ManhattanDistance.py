#!/bin/tcsh -xef

#set subjList = (100307 101006 103414 105014 105115 106521 107422 113619 114419 118528 122620 127933 129028 131217 133928 135225 138231 139637 141422 144832 148335 148840 149539 153025 158136 161630 163129 172332 173536 173940 175035 178950 180129 180432 181232 183034 188347 189349 190031 192843 194645 195041 195849 196144 205725 210011 210617 212116 212419 221319 224022 251833 268850 285345 285446 307127 334635 397154 397760 414229 422632 485757 486759 499566 530635 545345 567961 627549 654754 709551 748258 771354 782561 833148 904044 958976 965367)
#set subjList = (100307 101006 103414 105014 105115 106521 107422 113619 114419 118528)


#set seedList = (HarOx_ACC HarOx_CentralOpercularCortex HarOx_FrontalMedialCortex  HarOx_FrontalOperculumCortex  HarOx_FrontalOrbital  HarOx_FrontalPole  HarOx_IFGparsOpercularis  HarOx_IFGparsTriangularis HarOx_InsularCortex HarOx_MiddleFrontalGyrus HarOx_ParacingulateGyrus HarOx_PrecentralGyrus  HarOx_SubcallosalCortex HarOx_SuperiorFrontalGyrus  HarOx_SupplementaryMotorCortex)

set seedList = (HarOx_SuperiorFrontalGyrus)


#---------------------------
#Take the mean of all subject r-maps, create a group average R map
foreach seed ($seedList)


 #3dMean -prefix Group_Rmap_final_{$seed}.nii 100307_{$seed}_r+tlrc.BRIK 100307_{$seed}_r+tlrc.HEAD 101006_{$seed}_r+tlrc.BRIK 101006_{$seed}_r+tlrc.HEAD 103414_{$seed}_r+tlrc.BRIK 103414_{$seed}_r+tlrc.HEAD 105014_{$seed}_r+tlrc.BRIK 105014_{$seed}_r+tlrc.HEAD 105115_{$seed}_r+tlrc.BRIK 105115_{$seed}_r+tlrc.HEAD 106521_{$seed}_r+tlrc.BRIK 106521_{$seed}_r+tlrc.HEAD 107422_{$seed}_r+tlrc.BRIK 107422_{$seed}_r+tlrc.HEAD 113619_{$seed}_r+tlrc.BRIK 113619_{$seed}_r+tlrc.HEAD 114419_{$seed}_r+tlrc.BRIK 114419_{$seed}_r+tlrc.HEAD 118528_{$seed}_r+tlrc.BRIK 118528_{$seed}_r+tlrc.HEAD
 
# cd ../
# end




#-----TAKE ABS(DIFFERENCE) BETWEEN THE LEFT AND RIGHT ROIs
3dcalc -a {$seed}_R/Group_Rmap_final_{$seed}_R.nii -b {$seed}_L/Group_Rmap_final_{$seed}_L.nii -expr "abs(a-b)" -datum float -prefix {$seed}_DIFF.nii

end

###---Calculate Manhattan Distance
#3dcalc -a HarOx_ACC_DIFF.nii -b HarOx_CentralOpercularCortex_DIFF.nii -c HarOx_FrontalMedialCortex_DIFF.nii -d HarOx_FrontalOperculumCortex_DIFF.nii -e HarOx_FrontalOrbital_DIFF.nii -f HarOx_FrontalPole_DIFF.nii -g HarOx_IFGparsOpercularis_DIFF.nii -h HarOx_IFGparsTriangularis_DIFF.nii -i HarOx_InsularCortex_DIFF.nii -j HarOx_MiddleFrontalGyrus_DIFF.nii -k HarOx_ParacingulateGyrus_DIFF.nii -l HarOx_PrecentralGyrus_DIFF.nii -m HarOx_SubcallosalCortex_DIFF.nii -n HarOx_SuperiorFrontalGyrus_DIFF.nii -o HarOx_SupplementaryMotorCortex_DIFF.nii -expr "a+b+c+d+e+f+g+h+i+j+k+l+m+n+o" -datum float -prefix RvL_ManhattanDistance_Rstriatum_updated.nii


#3dcalc -a L_HarOx_ACC_DIFF.nii -b L_HarOx_CentralOpercularCortex_DIFF.nii -c L_HarOx_FrontalMedialCortex_DIFF.nii -d L_HarOx_FrontalOperculumCortex_DIFF.nii -e L_HarOx_FrontalOrbital_DIFF.nii -f L_HarOx_FrontalPole_DIFF.nii -i L_HarOx_InsularCortex_DIFF.nii -j L_HarOx_MiddleFrontalGyrus_DIFF.nii -k L_HarOx_ParacingulateGyrus_DIFF.nii -l L_HarOx_PrecentralGyrus_DIFF.nii -m L_HarOx_SubcallosalCortex_DIFF.nii -n L_HarOx_SuperiorFrontalGyrus_DIFF.nii -o L_HarOx_SupplementaryMotorCortex_DIFF.nii -expr "a+b+c+d+e+f+i+j+k+l+m+n+o" -datum float -prefix RvL_ManhattanDistance_Lstriatum_noIFG.nii
