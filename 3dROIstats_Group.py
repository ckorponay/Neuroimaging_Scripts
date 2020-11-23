#!/bin/tcsh -xef


#set seedList = (28WGA 33WGA 35LY 38LY 39WGA 40LY 45LY 66LY 89WGA 102WGA 170FS 184WGA 252WGA 253WGA 255WGA)

set seedList = (Rstriatum_MDhotspot_FIXED Lstriatum_MDhotspot_FIXED)

#set seedList = (HarOx_ACC HarOx_CentralOpercularCortex HarOx_FrontalMedialCortex  HarOx_FrontalOperculumCortex  HarOx_FrontalOrbital  HarOx_FrontalPole  HarOx_IFGparsOpercularis  HarOx_IFGparsTriangularis HarOx_InsularCortex HarOx_MiddleFrontalGyrus HarOx_ParacingulateGyrus HarOx_PrecentralGyrus  HarOx_SubcallosalCortex HarOx_SuperiorFrontalGyrus  HarOx_SupplementaryMotorCortex)



foreach seed ($seedList)
  cd {$seed}
  
  3dROIstats -mask ../HarvardOxford/HarOx_L_Atlas.nii -nzvoxels -key Group_Rmap_final_{$seed}.nii > ROI_avgR_values_LH
  
  3dROIstats -mask ../HarvardOxford/HarOx_R_Atlas.nii -nzvoxels -key Group_Rmap_final_{$seed}.nii > ROI_avgR_values_RH

#3dROIstats -mask ../SuperLabel_GlasserAtlas_resampled.nii -nzvoxels -key '28WGA_thresholdedMap00000000000001.nii' > VoxelCount_00000000000001_Glasser

#3dROIstats -mask ../SuperLabel_GlasserAtlas_resampled.nii -nzvoxels -key Group_Rmap_final_{$seed}.nii > VoxelCount_Group_Rmap_Glasser

#3dROIstats -mask ../SuperLabelAtlas_resampledFixed2.nii -nzvoxels -key Group_Rmap_final_{$seed}.nii > VoxelCount_Group_Rmap_Wei

#3dROIstats -mask ../SuperLabelAtlas_resampledFixed2.nii -nzvoxels -key {$seed}_Tmap.nii > VoxelCount_Group_Tmap_Wei

#3dROIstats -mask ../SuperLabel_GlasserAtlas_resampled.nii -nzvoxels -key {$seed}_Tmap.nii > VoxelCount_Group_Tmap_Glasser

#3dROIstats -mask ../SuperLabelAtlas_resampledFixed2.nii -nzvoxels -key '35LY_thresholdedMap00000000000001.nii' > VoxelCount_00000000000001_fixed3

#3dROIstats -mask Group_R_Striatum_mask_bin.nii.gz -nzvoxels {$seed}_DIFF.nii > DiffMapAVG_Rstriatum_{$seed}

#3dROIstats -mask ../Group_L_Striatum_mask_bin.nii.gz -nzvoxels Group_Rmap_final_{$seed}.nii > RmapAVG_Rstriatum_{$seed}

cd ../

end


