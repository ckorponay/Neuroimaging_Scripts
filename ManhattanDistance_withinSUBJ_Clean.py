#!/bin/tcsh -xef

###For each subject, create a voxel-wise map of the Manhattan Distance between each voxel's ipsilateral connectivity profile and contralateral connectivity profile###

set subjList = (125525 162329 249947 713239 857263 919966 151627 159845 792766  130013 135528 140925 199251 217429 159340 480141 520228 164636 185139 186848 325129 570243 756055 885975 101915 150928 454140 635245 818859 136227 154835 179952 200614 341834 449753 522434 923755 147737 209935 385450 908860 127731 138534 448347 665254 715041 889579 136126 170934 186141 283543 561444 656253 792867 123420 200513 298455 760551 120111 565452 107725 145531 166640 195445 300719 523032 825553 899885 192641 205119 214524 128127 168341 192035 208428 581450 720337)


set seedList = (HarOx_ACC HarOx_CentralOpercularCortex HarOx_FrontalMedialCortex  HarOx_FrontalOperculumCortex  HarOx_FrontalOrbital  HarOx_FrontalPole  HarOx_IFGparsOpercularis  HarOx_IFGparsTriangularis HarOx_InsularCortex HarOx_MiddleFrontalGyrus HarOx_ParacingulateGyrus HarOx_PrecentralGyrus  HarOx_SubcallosalCortex HarOx_SuperiorFrontalGyrus  HarOx_SupplementaryMotorCortex)


foreach subj ($subjList)

   cd $subj

   foreach seed ($seedList)


#-----TAKE ABS(DIFFERENCE) BETWEEN corresponding pairs of LH Seed and RH Seed
3dcalc -a {$subj}_{$seed}_R_r2z+tlrc. -b {$subj}_{$seed}_L_r2z+tlrc. -expr "abs(a-b)" -datum float -prefix {$subj}_{$seed}_DIFF_rStriatum_Z+tlrc. -overwrite

3dcalc -a L_{$subj}_{$seed}_R_r2z+tlrc. -b L_{$subj}_{$seed}_L_r2z+tlrc. -expr "abs(a-b)" -datum float -prefix {$subj}_{$seed}_DIFF_lStriatum_Z+tlrc. -overwrite

   end

#-----Sum the Differences
3dcalc -a {$subj}_HarOx_ACC_DIFF_rStriatum_Z+tlrc. -b {$subj}_HarOx_CentralOpercularCortex_DIFF_rStriatum_Z+tlrc. -c {$subj}_HarOx_FrontalMedialCortex_DIFF_rStriatum_Z+tlrc. -d {$subj}_HarOx_FrontalOperculumCortex_DIFF_rStriatum_Z+tlrc. -e {$subj}_HarOx_FrontalOrbital_DIFF_rStriatum_Z+tlrc. -f {$subj}_HarOx_FrontalPole_DIFF_rStriatum_Z+tlrc. -g {$subj}_HarOx_IFGparsOpercularis_DIFF_rStriatum_Z+tlrc. -h {$subj}_HarOx_IFGparsTriangularis_DIFF_rStriatum_Z+tlrc. -i {$subj}_HarOx_InsularCortex_DIFF_rStriatum_Z+tlrc. -j {$subj}_HarOx_MiddleFrontalGyrus_DIFF_rStriatum_Z+tlrc. -k {$subj}_HarOx_ParacingulateGyrus_DIFF_rStriatum_Z+tlrc. -l {$subj}_HarOx_PrecentralGyrus_DIFF_rStriatum_Z+tlrc. -m {$subj}_HarOx_SubcallosalCortex_DIFF_rStriatum_Z+tlrc. -n {$subj}_HarOx_SuperiorFrontalGyrus_DIFF_rStriatum_Z+tlrc. -o {$subj}_HarOx_SupplementaryMotorCortex_DIFF_rStriatum_Z+tlrc. -expr "a+b+c+d+e+f+g+h+i+j+k+l+m+n+o" -datum float -prefix {$subj}_RvL_ManhattanDistance_Rstriatum_Z+tlrc. -overwrite

 3dAFNItoNIFTI {$subj}_RvL_ManhattanDistance_Rstriatum_Z+tlrc. -overwrite
 
 3dcalc -a {$subj}_HarOx_ACC_DIFF_lStriatum_Z+tlrc. -b {$subj}_HarOx_CentralOpercularCortex_DIFF_lStriatum_Z+tlrc. -c {$subj}_HarOx_FrontalMedialCortex_DIFF_lStriatum_Z+tlrc. -d {$subj}_HarOx_FrontalOperculumCortex_DIFF_lStriatum_Z+tlrc. -e {$subj}_HarOx_FrontalOrbital_DIFF_lStriatum_Z+tlrc. -f {$subj}_HarOx_FrontalPole_DIFF_lStriatum_Z+tlrc. -g {$subj}_HarOx_IFGparsOpercularis_DIFF_lStriatum_Z+tlrc. -h {$subj}_HarOx_IFGparsTriangularis_DIFF_lStriatum_Z+tlrc. -i {$subj}_HarOx_InsularCortex_DIFF_lStriatum_Z+tlrc. -j {$subj}_HarOx_MiddleFrontalGyrus_DIFF_lStriatum_Z+tlrc. -k {$subj}_HarOx_ParacingulateGyrus_DIFF_lStriatum_Z+tlrc. -l {$subj}_HarOx_PrecentralGyrus_DIFF_lStriatum_Z+tlrc. -m {$subj}_HarOx_SubcallosalCortex_DIFF_lStriatum_Z+tlrc. -n {$subj}_HarOx_SuperiorFrontalGyrus_DIFF_lStriatum_Z+tlrc. -o {$subj}_HarOx_SupplementaryMotorCortex_DIFF_lStriatum_Z+tlrc. -expr "a+b+c+d+e+f+g+h+i+j+k+l+m+n+o" -datum float -prefix {$subj}_RvL_ManhattanDistance_Lstriatum_Z+tlrc. -overwrite

 3dAFNItoNIFTI {$subj}_RvL_ManhattanDistance_Lstriatum_Z+tlrc. -overwrite

   cd ..
   
   end



