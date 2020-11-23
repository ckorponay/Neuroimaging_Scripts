#!/bin/tcsh -xef


#3dROIstats -mask ../SuperLabelAtlas_resampledFixed2.nii -nzvoxels -key '35LY_thresholdedMap00000000000001.nii' > VoxelCount_00000000000001_fixed2

set subjList = (100307 101006 103414 105014 105115 106521 107422 113619 114419 118528 122620 127933 129028 131217 133928 135225 138231 139637 141422 144832 148335 148840 149539 153025 158136 161630 163129 172332 173536 173940 175035 178950 180129 180432 181232 183034 188347 189349 190031 192843 194645 195041 195849 196144 205725 210011 210617 212116 212419 221319 224022 251833 268850 285345 285446 307127 334635 397154 397760 414229 422632 485757 486759 499566 530635 545345 567961 627549 654754 709551 748258 771354 782561 833148 904044 958976 965367)

#set ROIList = (

foreach subj ($subjList)
echo "====> starting processing of $subj"
cd $subj

3dROIstats -mask ../StandardizedVolROIs/SuperLabels/M1_resampled.nii  -quiet -nobriklab -overwrite {$subj}_40LY_r2z+tlrc. > Rmean_M1_from_40LY_{$subj}

#3dROIstats  -quiet -nobriklab -overwrite Clean_rfMRI_REST1_LR_40LY_ts.1D > 40LY_stuff



cd ..

end

#mkdir Zmeans_40LY
mkdir Rmeans_40LY/M1

foreach subj ($subjList)
    cd $subj
         cp Rmean_M1_from_40LY_{$subj} ../Rmeans_40LY/M1
    cd ..
end

cd Rmeans_40LY/M1
1dcat -ok_1D_text -csvout  *from* > Rmeans_M1_to_40LY
 


