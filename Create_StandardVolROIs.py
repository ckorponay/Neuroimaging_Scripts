#!/bin/tcsh -xef

#Create one set of volumetric ROIs (from labels in FreeSurfer) on a sample's average anatomical in standard space

#set labelList = (4 6 8Ad 8Av 8B 9L 9M 10L 10M 10V 11 13 14M 14O 24 25 32 44 45A 45B 46 47L 47O 946d 946v)

set labelList = (insula frontalpole rostralmiddlefrontal rostralanteriorcingulate parstriangularis parsorbitalis parsopercularis paracentral medialorbitofrontal lateralorbitofrontal caudalmiddlefrontal caudalanteriorcingulate superiorfrontal precentral)
#create average subject anatomical in standard space
#3dMean -prefix AvgT1w.nii 100307/T1w.nii.gz 101006/T1w.nii.gz 103414/T1w.nii.gz 105014/T1w.nii.gz 105115/T1w.nii.gz 106521/T1w.nii.gz 107422/T1w.nii.gz 113619/T1w.nii.gz 114419/T1w.nii.gz 118528/T1w.nii.gz 122620/T1w.nii.gz 127933/T1w.nii.gz 129028/T1w.nii.gz 131217/T1w.nii.gz 133928/T1w.nii.gz 135225/T1w.nii.gz 138231/T1w.nii.gz 139637/T1w.nii.gz 141422/T1w.nii.gz 144832/T1w.nii.gz 148335/T1w.nii.gz 148840/T1w.nii.gz 149539/T1w.nii.gz 153025/T1w.nii.gz 158136/T1w.nii.gz 161630/T1w.nii.gz 163129/T1w.nii.gz 172332/T1w.nii.gz 173536/T1w.nii.gz 173940/T1w.nii.gz 175035/T1w.nii.gz 178950/T1w.nii.gz 180129/T1w.nii.gz 180432/T1w.nii.gz 181232/T1w.nii.gz 183034/T1w.nii.gz 188347/T1w.nii.gz 189349/T1w.nii.gz 190031/T1w.nii.gz 192843/T1w.nii.gz 194645/T1w.nii.gz 195041/T1w.nii.gz 195849/T1w.nii.gz 196144/T1w.nii.gz 205725/T1w.nii.gz 210011/T1w.nii.gz 210617/T1w.nii.gz 212116/T1w.nii.gz 212419/T1w.nii.gz 221319/T1w.nii.gz 224022/T1w.nii.gz 251833/T1w.nii.gz 268850/T1w.nii.gz 285345/T1w.nii.gz 285446/T1w.nii.gz 307127/T1w.nii.gz 334635/T1w.nii.gz 397154/T1w.nii.gz 397760/T1w.nii.gz 414229/T1w.nii.gz 422632/T1w.nii.gz 485757/T1w.nii.gz 486759/T1w.nii.gz 499566/T1w.nii.gz 530635/T1w.nii.gz 545345/T1w.nii.gz 567961/T1w.nii.gz 627549/T1w.nii.gz 654754/T1w.nii.gz 709551/T1w.nii.gz 748258/T1w.nii.gz 771354/T1w.nii.gz 782561/T1w.nii.gz 833148/T1w.nii.gz 904044/T1w.nii.gz 958976/T1w.nii.gz 965367/T1w.nii.gz
#create average subject GM mask in standard space
#3dMean -prefix GM_rh_mask_AVG.nii 100307/GM_rh_mask.nii 101006/GM_rh_mask.nii 103414/GM_rh_mask.nii 105014/GM_rh_mask.nii 105115/GM_rh_mask.nii 106521/GM_rh_mask.nii 107422/GM_rh_mask.nii 113619/GM_rh_mask.nii 114419/GM_rh_mask.nii 118528/GM_rh_mask.nii 122620/GM_rh_mask.nii 127933/GM_rh_mask.nii 129028/GM_rh_mask.nii 131217/GM_rh_mask.nii 133928/GM_rh_mask.nii 135225/GM_rh_mask.nii 138231/GM_rh_mask.nii 139637/GM_rh_mask.nii 141422/GM_rh_mask.nii 144832/GM_rh_mask.nii 148335/GM_rh_mask.nii 148840/GM_rh_mask.nii 149539/GM_rh_mask.nii 153025/GM_rh_mask.nii 158136/GM_rh_mask.nii 161630/GM_rh_mask.nii 163129/GM_rh_mask.nii 172332/GM_rh_mask.nii 173536/GM_rh_mask.nii 173940/GM_rh_mask.nii 175035/GM_rh_mask.nii 178950/GM_rh_mask.nii 180129/GM_rh_mask.nii 180432/GM_rh_mask.nii 181232/GM_rh_mask.nii 183034/GM_rh_mask.nii 188347/GM_rh_mask.nii 189349/GM_rh_mask.nii 190031/GM_rh_mask.nii 192843/GM_rh_mask.nii 194645/GM_rh_mask.nii 195041/GM_rh_mask.nii 195849/GM_rh_mask.nii 196144/GM_rh_mask.nii 205725/GM_rh_mask.nii 210011/GM_rh_mask.nii 210617/GM_rh_mask.nii 212116/GM_rh_mask.nii 212419/GM_rh_mask.nii 221319/GM_rh_mask.nii 224022/GM_rh_mask.nii 251833/GM_rh_mask.nii 268850/GM_rh_mask.nii 285345/GM_rh_mask.nii 285446/GM_rh_mask.nii 307127/GM_rh_mask.nii 334635/GM_rh_mask.nii 397154/GM_rh_mask.nii 397760/GM_rh_mask.nii 414229/GM_rh_mask.nii 422632/GM_rh_mask.nii 485757/GM_rh_mask.nii 486759/GM_rh_mask.nii 499566/GM_rh_mask.nii 530635/GM_rh_mask.nii 545345/GM_rh_mask.nii 567961/GM_rh_mask.nii 627549/GM_rh_mask.nii 654754/GM_rh_mask.nii 709551/GM_rh_mask.nii 748258/GM_rh_mask.nii 771354/GM_rh_mask.nii 782561/GM_rh_mask.nii 833148/GM_rh_mask.nii 904044/GM_rh_mask.nii 958976/GM_rh_mask.nii 965367/GM_rh_mask.nii

#cd /Applications/freesurfer/7.1.0/subjects/fsaverage/surf
cd /Users/chk17/Desktop/subjects/fsaverage/surf

 foreach label ($labelList)
  #convert .label files to gifti files
  mris_convert --label rh.{$label}.label {$label} rh.white /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/StandardizedVolROIs/rh.{$label}.label.gii
  
  #get labels from fsaverage space to fs_LR space
  wb_command -label-resample /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/StandardizedVolROIs/rh.{$label}.label.gii /Users/chk17/Downloads/standard_mesh_atlases/resample_fsaverage/fsaverage_std_sphere.R.164k_fsavg_R.surf.gii /Users/chk17/Downloads/standard_mesh_atlases/resample_fsaverage/fs_LR-deformed_to-fsaverage.R.sphere.32k_fs_LR.surf.gii ADAP_BARY_AREA /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/StandardizedVolROIs/{$label}_32k_fs_LR.label.gii -area-metrics /Users/chk17/Downloads/standard_mesh_atlases/resample_fsaverage/fsaverage.R.midthickness_va_avg.164k_fsavg_R.shape.gii /Users/chk17/Downloads/standard_mesh_atlases/resample_fsaverage/fs_LR.R.midthickness_va_avg.32k_fs_LR.shape.gii
  #map from surface to volume
  wb_command -label-to-volume-mapping /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/StandardizedVolROIs/{$label}_32k_fs_LR.label.gii /Users/chk17/Downloads//100307.R.white.32k_fs_LR.surf.gii /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/AvgT1w.nii /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/StandardizedVolROIs/{$label}labelVol_32k_8.nii -nearest-vertex 8
  
  
  #mri_binarize
  
  #restrict to the gray matter
   mris_calc -o /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/StandardizedVolROIs/{$label}labelVol_32k_GM_8.nii /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/StandardizedVolROIs/{$label}labelVol_32k_8.nii mul /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/GM_rh_mask_AVG.nii
   
   
  
  #threshold and binarize the masks to get rid of overhang outside the gray matter
  fslmaths /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/StandardizedVolROIs/{$label}labelVol_32k_GM_8.nii  -thr 0.3 -bin /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/StandardizedVolROIs/{$label}labelVol_32k_GM_8_bin.nii
  
  end





