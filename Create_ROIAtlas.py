#!/bin/tcsh -xef


#cd /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/StandardizedVolROIs/SuperLabels

cd /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/GlasserAtlas


#3dcalc -a FEFlabelVol_32k_GM_8_bin.nii -b FPlabelVol_32k_GM_8_bin.nii -c dlPFClabelVol_32k_GM_8_bin.nii -d vlPFClabelVol_32k_GM_8_bin.nii -e ACClabelVol_32k_GM_8_bin.nii -f OFClabelVol_32k_GM_8_bin.nii -g vmPFClabelVol_32k_GM_8_bin.nii -h M1labelVol_32k_GM_8_bin.nii -i PremotorlabelVol_32k_GM_8_bin.nii -j dmPFClabelVol_32k_GM_8_bin.nii -expr 'step(a) + 2*step(b) + 3*step(c) + 4*step(d) + 5*step(e) + 6*step(f) + 7*step(g) + 8*step(h) + 9*step(i) + 10*step(j)' -prefix SuperLabelAtlas.nii

#3dcalc -a FEF_resampled.nii -b FP_resampled.nii -c dlPFC_resampled.nii -d vlPFC_resampled.nii -e ACC_resampled.nii -f OFC_resampled.nii -g vmPFC_resampled.nii -h M1_resampled.nii -i Premotor_resampled.nii -j dmPFC_resampled.nii -expr 'step(a) + 2*step(b) + 3*step(c) + 4*step(d) + 5*step(e) + 6*step(f) + 7*step(g) + 8*step(h) + 9*step(i) + 10*step(j)' -prefix SuperLabelAtlas_resampledFixed2.nii

#3dcalc -a FEF_Glasser_mask.nii -b FP_Glasser_mask.nii -c dlPFC_Glasser_mask.nii -d vlPFC_Glasser_mask.nii -e ACC_Glasser_mask.nii -f OFC_Glasser_mask.nii -g vmPFC_Glasser_mask.nii -h Motor_Glasser_mask.nii -i Premotor_Glasser_mask.nii -j dmPFC_Glasser_mask.nii -expr 'step(a) + 2*step(b) + 3*step(c) + 4*step(d) + 5*step(e) + 6*step(f) + 7*step(g) + 8*step(h) + 9*step(i) + 10*step(j)' -prefix SuperLabel_GlasserAtlas.nii

#3dcalc -a FEF_Glasser_mask.nii -b FP_Glasser_mask.nii -c dlPFC_Glasser_mask.nii -d vlPFC_Glasser_mask.nii -e ACC_Glasser_mask.nii -f OFC_Glasser_mask.nii -g vmPFC_Glasser_mask.nii -h Motor_Glasser_mask.nii -i Premotor_Glasser_mask.nii -j dmPFC_Glasser_mask.nii -expr 'step(a) + 2*step(b) + 3*step(c) + 4*step(d) + 5*step(e) + 6*step(f) + 7*step(g) + 8*step(h) + 9*step(i) + 10*step(j)' -prefix SuperLabel_GlasserAtlas.nii

3dcalc -a HarOx_ACC_L.nii -b HarOx_CentralOpercularCortex_L.nii -c HarOx_FrontalMedialCortex_L.nii -d HarOx_FrontalOperculumCortex_L.nii -e HarOx_FrontalOrbital_L.nii -f HarOx_FrontalPole_L.nii -g HarOx_IFGparsOpercularis_L.nii -h HarOx_IFGparsTriangularis_L.nii -i HarOx_InsularCortex_L.nii -j HarOx_MiddleFrontalGyrus_L.nii -k HarOx_ParacingulateGyrus_L.nii -l HarOx_PrecentralGyrus_L.nii -m HarOx_SubcallosalCortex_L.nii -n HarOx_SuperiorFrontalGyrus_L.nii -o HarOx_SupplementaryMotorCortex_L.nii -expr 'step(a) + 2*step(b) + 3*step(c) + 4*step(d) + 5*step(e) + 6*step(f) + 7*step(g) + 8*step(h) + 9*step(i) + 10*step(j) + 11*step(k) + 12*step(l) + 13*step(m) + 14*step(n) + 15*step(o)' -prefix HarOx_L_Atlas.nii




 #mris_calc -o /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/GlasserAtlas/SuperLabel_GlasserAtlas_rhGM.nii /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/GlasserAtlas/SuperLabel_GlasserAtlas.nii mul /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/GM_rh_mask_AVG_resampled.nii

#3dcalc -a FEF_resampled.nii  -b dlPFC_resampled.nii  -c Premotor_resampled.nii  -expr 'step(a) + 2*step(b) + 3*step(c)' -prefix FEFdlPFCPremotor_resampled.nii

#cd /Users/chk17/Library/Mobile\ Documents/com\~apple\~CloudDocs/Desktop/HCP_Data/StandardizedVolROIs


#3dcalc -a 8AlabelVol_32k_GM_8_bin.nii -b 8BlabelVol_32k_GM_8_bin.nii -c 10MlabelVol_32k_GM_8_bin.nii -d 10LLlabelVol_32k_GM_8_bin.nii -e 9LlabelVol_32k_GM_8_bin.nii -f 46labelVol_32k_GM_8_bin.nii -g 946dlabelVol_32k_GM_8_bin.nii -h 946vlabelVol_32k_GM_8_bin.nii -i 47LlabelVol_32k_GM_8_bin.nii -j 47OlabelVol_32k_GM_8_bin.nii -k 45AlabelVol_32k_GM_8_bin.nii -l 45BlabelVol_32k_GM_8_bin.nii -m 44labelVol_32k_GM_8_bin.nii -n 32labelVol_32k_GM_8_bin.nii -o 24labelVol_32k_GM_8_bin.nii -p 14OlabelVol_32k_GM_8_bin.nii -q 11labelVol_32k_GM_8_bin.nii -r 13labelVol_32k_GM_8_bin.nii -s 14MlabelVol_32k_GM_8_bin.nii -t 25labelVol_32k_GM_8_bin.nii -u 4labelVol_32k_GM_8_bin.nii -v 6labelVol_32k_GM_8_bin.nii -w 9MlabelVol_32k_GM_8_bin.nii -expr 'step(a) + 2*step(b) + 3*step(c) + 4*step(d) + 5*step(e) + 6*step(f) + 7*step(g) + 8*step(h) + 9*step(i) + 10*step(j) + 11*step(k) + 12*step(l) + 13*step(m) + 14*step(n) + 15*step(o) + 16*step(p) + 17*step(q) + 18*step(r) + 19*step(s) + 20*step(t) + 21*step(u) + 22*step(v) + 23*step(w)' -prefix LabelAtlas.nii


