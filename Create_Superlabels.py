#!/bin/tcsh -xef

cd /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/StandardizedVolROIs

   mkdir SuperLabels
  

 
   fslmaths 8AlabelVol_32k_GM_8_bin.nii -add 8BlabelVol_32k_GM_8_bin.nii FEFlabelVol_32k_GM_8_bin.nii
   
   fslmaths 10MlabelVol_32k_GM_8_bin.nii -add 10LLlabelVol_32k_GM_8_bin.nii FPlabelVol_32k_GM_8_bin.nii
   
    fslmaths 9LlabelVol_32k_GM_8_bin.nii -add 46labelVol_32k_GM_8_bin.nii -add 946dlabelVol_32k_GM_8_bin.nii -add 946vlabelVol_32k_GM_8_bin.nii dlPFClabelVol_32k_GM_8_bin.nii
   
   fslmaths 47LlabelVol_32k_GM_8_bin.nii -add 47OlabelVol_32k_GM_8_bin.nii -add 45AlabelVol_32k_GM_8_bin.nii -add 45BlabelVol_32k_GM_8_bin.nii -add 44labelVol_32k_GM_8_bin.nii vlPFClabelVol_32k_GM_8_bin.nii
   
    fslmaths 32labelVol_32k_GM_8_bin.nii -add 24labelVol_32k_GM_8_bin.nii  ACClabelVol_32k_GM_8_bin.nii
    
    fslmaths 14OlabelVol_32k_GM_8_bin.nii -add 11labelVol_32k_GM_8_bin.nii -add 13labelVol_32k_GM_8_bin.nii OFClabelVol_32k_GM_8_bin.nii
    
    fslmaths 14MlabelVol_32k_GM_8_bin.nii -add 25labelVol_32k_GM_8_bin.nii  vmPFClabelVol_32k_GM_8_bin.nii
    
    cp 4labelVol_32k_GM_8_bin.nii MotorlabelVol_32k_GM_8_bin.nii
    
    cp 6labelVol_32k_GM_8_bin.nii PremotorlabelVol_32k_GM_8_bin.nii
    
    cp 9MlabelVol_32k_GM_8_bin.nii dmPFClabelVol_32k_GM_8_bin.nii
      
   





