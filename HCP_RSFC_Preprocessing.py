#!/bin/tcsh -xef

###Take minimally-processed Human Connectome Project (HCP) resting-state scans, apply further preprocessing/cleaning, and create subject-level seed-based connectivity maps##

set subjList = (100307 101006 103414 105014 105115 106521 107422 113619 114419 118528 122620 127933 129028 131217 133928 135225 138231 139637 141422 144832 148335 148840 149539 153025 158136 161630 163129 172332 173536 173940 175035 178950 180129 180432 181232 183034 188347 189349 190031 192843 194645 195041 195849 196144 205725 210011 210617 212116 212419 221319 224022 251833 268850 285345 285446 307127 334635 397154 397760 414229 422632 485757 486759 499566 530635 545345 567961 627549 654754 709551 748258 771354 782561 833148 904044 958976 965367)


set seedList = (HarOx_ACC_L HarOx_ACC_R HarOx_CentralOpercularCortex_L HarOx_CentralOpercularCortex_R HarOx_FrontalMedialCortex_L HarOx_FrontalMedialCortex_R HarOx_FrontalOperculumCortex_L HarOx_FrontalOperculumCortex_R HarOx_FrontalOrbital_L HarOx_FrontalOrbital_R HarOx_FrontalPole_L HarOx_FrontalPole_R HarOx_IFGparsOpercularis_L HarOx_IFGparsOpercularis_R HarOx_IFGparsTriangularis_L HarOx_IFGparsTriangularis_R HarOx_InsularCortex_L HarOx_InsularCortex_R HarOx_MiddleFrontalGyrus_L HarOx_MiddleFrontalGyrus_R HarOx_ParacingulateGyrus_L HarOx_ParacingulateGyrus_R HarOx_PrecentralGyrus_L HarOx_PrecentralGyrus_R HarOx_SubcallosalCortex_L HarOx_SubcallosalCortex_R HarOx_SuperiorFrontalGyrus_L HarOx_SuperiorFrontalGyrus_R HarOx_SupplementaryMotorCortex_L HarOx_SupplementaryMotorCortex_R)


foreach subj ($subjList)
     echo "====> starting processing of $subj"
     cd $subj

 #========= create censor file motion_${subj}_censor.1D, for censoring motion ==========================
1d_tool.py -infile Movement_Regressors1_LR.txt -set_nruns 1 -select_cols '0..5'                                \
    -show_censor_count -censor_prev_TR                                        \
    -censor_motion 0.5 motion_$subj -overwrite
    
# ==================================segment anatomy into classes CSF/GM/WM  ==================================

3dcalc -a aparc.a2009s+aseg.nii.gz -expr 'equals(a,2)+equals(a,41)' -prefix WM_mask.nii -overwrite
3dcalc -a aparc.a2009s+aseg.nii.gz -expr 'equals(a,4)+equals(a,43)' -prefix CSF_mask.nii -overwrite


3dresample -master  rfMRI_REST1_LR.nii.gz -rmode NN  -input WM_mask.nii -prefix mask_WM_resam -overwrite
3dresample -master  rfMRI_REST1_LR.nii.gz -rmode NN  -input CSF_mask.nii -prefix mask_CSF_resam -overwrite


3dmaskSVD -vnorm -sval 3 -polort 2 -mask mask_WM_resam+tlrc. rfMRI_REST1_LR.nii.gz > rm.ROI.WMe.1D
3dmaskSVD -vnorm -sval 3 -polort 2 -mask mask_CSF_resam+tlrc. rfMRI_REST1_LR.nii.gz > rm.ROI.CSFe.1D

 

 
 #=========Project out nuisance time series ==========================
3dTproject -input rfMRI_REST1_LR.nii.gz -prefix Clean_rfMRI_REST1_LR.nii.gz   \
       -censor motion_{$subj}_censor.1D    \
       -cenmode ZERO    \
       -polort 3    \
       -passband .01 .1   \
       -blur 6 -mask brainmask_fs.2.1_LR.nii.gz -ort Movement_Regressors1_LR.txt'[0]' -ort Movement_Regressors1_LR.txt'[1]' -ort Movement_Regressors1_LR.txt'[2]'  -ort Movement_Regressors1_LR.txt'[3]' -ort Movement_Regressors1_LR.txt'[4]'  -ort Movement_Regressors1_LR.txt'[5]' -ort Movement_Regressors1_LR.txt'[6]' -ort Movement_Regressors1_LR.txt'[7]' -ort Movement_Regressors1_LR.txt'[8]' -ort Movement_Regressors1_LR.txt'[9]' -ort Movement_Regressors1_LR.txt'[10]'  -ort Movement_Regressors1_LR.txt'[11]'  -ort rm.ROI.WMe.1D  -ort rm.ROI.CSFe.1D -overwrite



#========= populate already-created Seeds with cleaned timeseries data  ==========================
foreach seed ($seedList)

3dmaskave -quiet -mask ../../HarvardOxford/{$seed}.nii Clean_rfMRI_REST1_LR.nii.gz > Clean_rfMRI_REST1_LR_{$seed}_ts.1D

end


 #========= OR, create seeds and then populate with cleaned timeseries data  ==========================
#echo  57 15 9 | 3dUndump -prefix R_Rostral_44_mask -srad 8 -master Clean_rfMRI_REST1_LR.nii.gz -xyz -

#3dmaskave -quiet -mask R_Rostral_44_mask+tlrc.  Clean_rfMRI_REST1_LR.nii.gz > Clean_rfMRI_REST1_LR_Rostral44_ts.1D \


#echo  51 8 11 | 3dUndump -prefix R_Caudal_44_mask -srad 8 -master Clean_rfMRI_REST1_LR.nii.gz -xyz -

#3dmaskave -quiet -mask R_Caudal_44_mask+tlrc.  Clean_rfMRI_REST1_LR.nii.gz > Clean_rfMRI_REST1_LR_Caudal44_ts.1D \




foreach seed ($seedList)

# ------------------------------
# run the regression analysis

3dDeconvolve -input  Clean_rfMRI_REST1_LR.nii.gz -mask brainmask_fs.2.1_LR.nii.gz  -num_stimts 1  -stim_file 1  Clean_rfMRI_REST1_LR_{$seed}_ts.1D -rout -tout -x1D X.xmat.{$seed}.1D -xjpeg X.{$seed}.jpg -x1D_uncensored X.nocensor.xmat.{$seed}.1D -bucket stats.{$seed}.{$subj} -overwrite

3dcalc -a stats.{$seed}.{$subj}+tlrc.'[4]' -b stats.{$seed}.{$subj}+tlrc.'[2]' -datum float -expr "ispositive(b)*sqrt(a)-isnegative(b)*sqrt(a)" -prefix {$subj}_{$seed}_r -overwrite

3dcalc -a {$subj}_{$seed}_r+tlrc. -expr "0.5*log((1+a)/(1-a))" -datum float -prefix {$subj}_{$seed}_r2z+tlrc -overwrite


end

cd ..

end



