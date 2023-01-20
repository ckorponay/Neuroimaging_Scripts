#!/bin/tcsh -xef

cd path/to/preprocessed/restingstate/files

set subjList = (subj1 subj2 subj3 etc)

set seedList = (ACC insula vlPFC etc)

foreach subj ($subjList)
     echo "====> starting processing of $subj"
     cd $subj      #this is the path to the folder where the subjects' preprocessed resting-state NIFTI file lives
     


#========= populate the ROI masks with the subject's preprocessed timeseries data  ==========================
foreach seed ($seedList)

3dmaskave -quiet -overwrite -mask path/to/ROImasks/{$seed}.nii {$subj}_PreproccessedRestingFile.nii > {$subj}_PreproccessedRestingFile_{$seed}_ts.1D

end



#========= compute connectivity between the ROI and every striatal voxel - end up with a voxel-wise striatal connectivity value map  ==========================
foreach seed ($seedList)

3dDeconvolve -input /path/to/preprocessed/restingstate/files/{$subj}_PreproccessedRestingFile.nii -mask path/to/ROImasks/StriatalMask.nii -num_stimts 1  -stim_file 1  {$subj}_PreproccessedRestingFile_{$seed}_ts.1D -rout -tout -x1D X.xmat.{$seed}.1D -x1D_uncensored X.nocensor.xmat.{$seed}.1D -bucket stats.{$seed}.{$subj}_StriatalMask -overwrite

3dcalc -a stats.{$seed}.{$subj}_StriatalMask+tlrc.'[4]' -b stats.{$seed}.{$subj}_StriatalMask+tlrc.'[2]' -datum float -expr "ispositive(b)*sqrt(a)-isnegative(b)*sqrt(a)" -prefix {$subj}_{$seed}_r_StriatalMask -overwrite

3dcalc -a {$subj}_{$seed}_r_StriatalMask+tlrc. -expr "0.5*log((1+a)/(1-a))" -datum float -prefix {$subj}_{$seed}_r2z_StriatalMask.nii -overwrite


end

end



