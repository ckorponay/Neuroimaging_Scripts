#!/bin/tcsh -xef



set ControlList = (sub-V67CV2OT sub-PJUPNBAM sub-SKBY5ALZ sub-ZCBTYZ6I sub-56EWJURG sub-NNFUFIPG sub-YZXJPDX7 sub-AKHOY3UH sub-QUN4GT3M sub-E6HEUODN sub-V5QHNBSH sub-FWQKH5UL sub-4BBDI62B sub-CVAKNQOJ sub-YF7GX2SS sub-7H6W6KFZ sub-CYYZDAAA sub-KGDWBBAJ sub-4ALM5WXW sub-PSADWNDM sub-JJU72DNY sub-X7OL34TY sub-JTGVG5WJ sub-YYJETPIQ sub-WVGICHTU sub-ZVIA45ZD sub-DIG4A577 sub-SBMESIHC sub-RIOEHEWU sub-TZPLZADX sub-ARUFOFFX sub-WLYPL3QY sub-7RYHMDAO)

#sesh2SUD with excess motion subjects removed
set subjList = (sub-24E5O5HD sub-3T47XKCD sub-3WNXNOIM sub-45WE4VWV sub-74OJVKXQ sub-7CKNTSFP sub-7I7UH5I4 sub-AEJWBSIB sub-AG6EXHRL sub-B5U3KVGH sub-BDK53Y62 sub-C6YU555I sub-CCW2JCII sub-ETD7AYZZ sub-FAOFZWSZ sub-FJHDX5IK sub-G44HDPRR sub-HI4JYNOC sub-HKD7OLDH sub-HP2NI3MR sub-HRHPSXHY sub-I4DC5V5Z sub-JD6P5XXB sub-JV3IJWGZ sub-KYEQTI3O sub-M6NL3WOP sub-MMP2OPZH sub-MRZLO6NY sub-NJQDQUXE sub-NMVNCA57 sub-NTL6Z5QX sub-OKCTYCC6 sub-PFFN7C6B sub-QZYS4JNS sub-RD4VTC7F sub-REA73OA6 sub-RZSUFL4K sub-S2PURVUQ sub-T2RCUMZL sub-T6O3IWPJ sub-VO5OWDFZ sub-WTNDMQAE sub-XMV6BK3B sub-Z73RHXVZ sub-ZGAU3OES sub-ZP4OTNBB)


set seedList = (HarOx_ACC HarOx_CentralOpercularCortex HarOx_FrontalMedialCortex  HarOx_FrontalOperculumCortex  HarOx_FrontalOrbital  HarOx_FrontalPole  HarOx_IFGparsOpercularis  HarOx_IFGparsTriangularis HarOx_InsularCortex HarOx_MiddleFrontalGyrus HarOx_ParacingulateGyrus HarOx_PrecentralGyrus  HarOx_SubcallosalCortex HarOx_SuperiorFrontalGyrus  HarOx_SupplementaryMotorCortex)



foreach seed ($seedList)


#-----TAKE ABS(DIFFERENCE) BETWEEN THE LEFT AND RIGHT ROIs
3dcalc -a 485/data/derivatives/fmriprep_20.2.0/fmriprep/Control_{$seed}_R/Control_r2zmap_rStriatum_{$seed}_R.nii -b 485_Sess2/485bids2/derivatives/fmriprep_20.2.0/fmriprep/SUD_Sesh2_{$seed}_R/SUD_r2zmap_rStriatum_{$seed}_R.nii -expr "abs(a-b)" -datum float -prefix {$seed}_R_controlsudSesh2DIFF_rStriatum.nii

3dcalc -a 485/data/derivatives/fmriprep_20.2.0/fmriprep/Control_{$seed}_L/Control_r2zmap_rStriatum_{$seed}_L.nii -b 485_Sess2/485bids2/derivatives/fmriprep_20.2.0/fmriprep/SUD_Sesh2_{$seed}_L/SUD_r2zmap_rStriatum_{$seed}_L.nii -expr "abs(a-b)" -datum float -prefix {$seed}_L_controlsudSesh2DIFF_rStriatum.nii

end

###---Calculate Manhattan Distance
3dcalc -a HarOx_ACC_R_controlsudSesh2DIFF_rStriatum.nii -b HarOx_CentralOpercularCortex_R_controlsudSesh2DIFF_rStriatum.nii -c HarOx_FrontalMedialCortex_R_controlsudSesh2DIFF_rStriatum.nii -d HarOx_FrontalOperculumCortex_R_controlsudSesh2DIFF_rStriatum.nii -e HarOx_FrontalOrbital_R_controlsudSesh2DIFF_rStriatum.nii -f HarOx_FrontalPole_R_controlsudSesh2DIFF_rStriatum.nii -g HarOx_IFGparsOpercularis_R_controlsudSesh2DIFF_rStriatum.nii -h HarOx_IFGparsTriangularis_R_controlsudSesh2DIFF_rStriatum.nii -i HarOx_InsularCortex_R_controlsudSesh2DIFF_rStriatum.nii -j HarOx_MiddleFrontalGyrus_R_controlsudSesh2DIFF_rStriatum.nii -k HarOx_ParacingulateGyrus_R_controlsudSesh2DIFF_rStriatum.nii -l HarOx_PrecentralGyrus_R_controlsudSesh2DIFF_rStriatum.nii -m HarOx_SubcallosalCortex_R_controlsudSesh2DIFF_rStriatum.nii -n HarOx_SuperiorFrontalGyrus_R_controlsudSesh2DIFF_rStriatum.nii -o HarOx_SupplementaryMotorCortex_R_controlsudSesh2DIFF_rStriatum.nii -expr "a+b+c+d+e+f+g+h+i+j+k+l+m+n+o" -datum float -prefix ControlvSUDSesh2_ManhattanDistance_Rcortex_Rstriatum.nii

3dcalc -a HarOx_ACC_L_controlsudSesh2DIFF_rStriatum.nii -b HarOx_CentralOpercularCortex_L_controlsudSesh2DIFF_rStriatum.nii -c HarOx_FrontalMedialCortex_L_controlsudSesh2DIFF_rStriatum.nii -d HarOx_FrontalOperculumCortex_L_controlsudSesh2DIFF_rStriatum.nii -e HarOx_FrontalOrbital_L_controlsudSesh2DIFF_rStriatum.nii -f HarOx_FrontalPole_L_controlsudSesh2DIFF_rStriatum.nii -g HarOx_IFGparsOpercularis_L_controlsudSesh2DIFF_rStriatum.nii -h HarOx_IFGparsTriangularis_L_controlsudSesh2DIFF_rStriatum.nii -i HarOx_InsularCortex_L_controlsudSesh2DIFF_rStriatum.nii -j HarOx_MiddleFrontalGyrus_L_controlsudSesh2DIFF_rStriatum.nii -k HarOx_ParacingulateGyrus_L_controlsudSesh2DIFF_rStriatum.nii -l HarOx_PrecentralGyrus_L_controlsudSesh2DIFF_rStriatum.nii -m HarOx_SubcallosalCortex_L_controlsudSesh2DIFF_rStriatum.nii -n HarOx_SuperiorFrontalGyrus_L_controlsudSesh2DIFF_rStriatum.nii -o HarOx_SupplementaryMotorCortex_L_controlsudSesh2DIFF_rStriatum.nii -expr "a+b+c+d+e+f+g+h+i+j+k+l+m+n+o" -datum float -prefix ControlvSUDSesh2_ManhattanDistance_Lcortex_Rstriatum.nii

3dcalc -a ControlvSUDSesh2_ManhattanDistance_Rcortex_Rstriatum.nii -b ControlvSUDSesh2_ManhattanDistance_Lcortex_Rstriatum.nii -expr "a+b" -datum float -prefix ControlvSUDSesh2_ManhattanDistance_RandLcortex_Rstriatum.nii



