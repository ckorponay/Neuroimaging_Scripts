#!/bin/tcsh -xef


#3dcalc -a HarOx_ACC_R/Group_Rmap_final_HarOx_ACC_R.nii -b HarOx_CentralOpercularCortex_R/Group_Rmap_final_HarOx_CentralOpercularCortex_R.nii -c HarOx_FrontalMedialCortex_R/Group_Rmap_final_HarOx_FrontalMedialCortex_R.nii -d HarOx_FrontalOperculumCortex_R/Group_Rmap_final_HarOx_FrontalOperculumCortex_R.nii -e HarOx_FrontalOrbital_R/Group_Rmap_final_HarOx_FrontalOrbital_R.nii -f HarOx_FrontalPole_R/Group_Rmap_final_HarOx_FrontalPole_R.nii -g HarOx_IFGparsOpercularis_R/Group_Rmap_final_HarOx_IFGparsOpercularis_R.nii -h HarOx_IFGparsTriangularis_R/Group_Rmap_final_HarOx_IFGparsTriangularis_R.nii -i HarOx_InsularCortex_R/Group_Rmap_final_HarOx_InsularCortex_R.nii -j HarOx_MiddleFrontalGyrus_R/Group_Rmap_final_HarOx_MiddleFrontalGyrus_R.nii -k HarOx_ParacingulateGyrus_R/Group_Rmap_final_HarOx_ParacingulateGyrus_R.nii -l HarOx_PrecentralGyrus_R/Group_Rmap_final_HarOx_PrecentralGyrus_R.nii -m HarOx_SubcallosalCortex_R/Group_Rmap_final_HarOx_SubcallosalCortex_R.nii -n HarOx_SuperiorFrontalGyrus_R/Group_Rmap_final_HarOx_SuperiorFrontalGyrus_R.nii -o HarOx_SupplementaryMotorCortex_R/Group_Rmap_final_HarOx_SupplementaryMotorCortex_R.nii -expr "a+b+c+d+e+f+g+h+i+j+k+l+m+n+o" -datum float -prefix Sum_rMaps_RH_rStriatum.nii

set seedList = (HarOx_ACC HarOx_CentralOpercularCortex HarOx_FrontalMedialCortex  HarOx_FrontalOperculumCortex  HarOx_FrontalOrbital  HarOx_FrontalPole  HarOx_IFGparsOpercularis  HarOx_IFGparsTriangularis HarOx_InsularCortex HarOx_MiddleFrontalGyrus HarOx_ParacingulateGyrus HarOx_PrecentralGyrus  HarOx_SubcallosalCortex HarOx_SuperiorFrontalGyrus  HarOx_SupplementaryMotorCortex)

#foreach seed ($seedList)

#cd {$seed}_R

#3dcalc -a Group_Rmap_final_{$seed}_R.nii -b ../Sum_rMaps_RH_rStriatum.nii -expr "a/b" -datum float -prefix Percent_Group_Rmap_final_{$seed}_R.nii

#cd ..

#end

foreach seed ($seedList)

cd {$seed}_R

3dcalc -a Percent_Group_Rmap_final_{$seed}_R.nii -expr "a*log(a)" -datum float -prefix Log_Percent_Group_Rmap_final_{$seed}_R.nii

cd ..

end

3dcalc -a HarOx_ACC_R/Log_Percent_Group_Rmap_final_HarOx_ACC_R.nii -b HarOx_CentralOpercularCortex_R/Log_Percent_Group_Rmap_final_HarOx_CentralOpercularCortex_R.nii -c HarOx_FrontalMedialCortex_R/Log_Percent_Group_Rmap_final_HarOx_FrontalMedialCortex_R.nii -d HarOx_FrontalOperculumCortex_R/Log_Percent_Group_Rmap_final_HarOx_FrontalOperculumCortex_R.nii -e HarOx_FrontalOrbital_R/Log_Percent_Group_Rmap_final_HarOx_FrontalOrbital_R.nii -f HarOx_FrontalPole_R/Log_Percent_Group_Rmap_final_HarOx_FrontalPole_R.nii -g HarOx_IFGparsOpercularis_R/Log_Percent_Group_Rmap_final_HarOx_IFGparsOpercularis_R.nii -h HarOx_IFGparsTriangularis_R/Log_Percent_Group_Rmap_final_HarOx_IFGparsTriangularis_R.nii -i HarOx_InsularCortex_R/Log_Percent_Group_Rmap_final_HarOx_InsularCortex_R.nii -j HarOx_MiddleFrontalGyrus_R/Log_Percent_Group_Rmap_final_HarOx_MiddleFrontalGyrus_R.nii -k HarOx_ParacingulateGyrus_R/Log_Percent_Group_Rmap_final_HarOx_ParacingulateGyrus_R.nii -l HarOx_PrecentralGyrus_R/Log_Percent_Group_Rmap_final_HarOx_PrecentralGyrus_R.nii -m HarOx_SubcallosalCortex_R/Log_Percent_Group_Rmap_final_HarOx_SubcallosalCortex_R.nii -n HarOx_SuperiorFrontalGyrus_R/Log_Percent_Group_Rmap_final_HarOx_SuperiorFrontalGyrus_R.nii -o HarOx_SupplementaryMotorCortex_R/Log_Percent_Group_Rmap_final_HarOx_SupplementaryMotorCortex_R.nii -expr "-(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o)" -datum float -prefix Entropy_RH_rStriatum.nii
