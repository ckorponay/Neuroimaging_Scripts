#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:13:54 2021

@author: chk17
"""

####Using fMRIPrep output, create a Motion Censor vector file that "zero's out" the first 3 TRs and TRs where framewise displacement is greater than 0.5mm######

subjectList = ('sub-FF2V32GM', 'sub-Q2UGSVVV', 'sub-FGXR2I6I', 'sub-QGMYZZUA', 'sub-FJHDX5IK', 'sub-QKGIT7SR', 'sub-FT4E6HRU', 
               'sub-QPEVF27U', 'sub-FWQKH5UL', 'sub-QUN4GT3M', 'sub-FY2PAN3N', 'sub-QZYS4JNS', 'sub-24E5O5HD', 'sub-G44HDPRR', 
               'sub-RD4VTC7F', 'sub-2P3CPNWV', 'sub-HI4JYNOC', 'sub-REA73OA6', 'sub-33HYKD6V', 'sub-HKD7OLDH', 'sub-RIOEHEWU', 
               'sub-3T47XKCD', 'sub-HM25RXGI', 'sub-RV62GCL3', 'sub-3WNXNOIM', 'sub-HP2NI3MR', 'sub-RZSUFL4K', 'sub-45WE4VWV', 
               'sub-HRHPSXHY', 'sub-S2PURVUQ', 'sub-4ALM5WXW', 'sub-I4DC5V5Z', 'sub-SBB5AIAL', 'sub-4BBDI62B', 'sub-IHRHSYTZ', 
               'sub-SBFN2V62', 'sub-4BEMSUHA', 'sub-IKAJ2UXF', 'sub-SBMESIHC', 'sub-56EWJURG', 'sub-J4ER7FND', 'sub-SKBY5ALZ',
               'sub-74OJVKXQ', 'sub-JD6P5XXB', 'sub-SYEEUTEL', 'sub-75X3I64X', 'sub-JGLZHEF6', 'sub-T2RCUMZL', 'sub-7CKNTSFP',
               'sub-JJU72DNY', 'sub-T6O3IWPJ', 'sub-7H6W6KFZ', 'sub-JTGVG5WJ', 'sub-TORFT4TU', 'sub-7I7UH5I4', 'sub-JV3IJWGZ', 
               'sub-TWZLYWYK', 'sub-7RYHMDAO', 'sub-JWUKWODD', 'sub-TZPLZADX', 'sub-KCVLQKC2', 'sub-V5QHNBSH', 'sub-A2JBU5RL',
               'sub-A7MQ6DGT', 'sub-KGDWBBAJ', 'sub-V67CV2OT', 'sub-AEJWBSIB', 'sub-KIE6MAL2', 'sub-VO5OWDFZ', 'sub-AG6EXHRL',
               'sub-KTG4CELR', 'sub-VOEYFKQL', 'sub-AKHOY3UH', 'sub-KYEQTI3O', 'sub-WL47OO7H', 'sub-ARUFOFFX', 'sub-KZVCNSPV',  
               'sub-WLYPL3QY', 'sub-B5U3KVGH', 'sub-LSGXLOT2', 'sub-WTHDLYGS', 'sub-B7TRHCAU', 'sub-LU25B3EX', 'sub-WTNDMQAE',
               'sub-BDK53Y62', 'sub-M6NL3WOP', 'sub-WVGICHTU', 'sub-BTG5FUHX', 'sub-MJA53T6N', 'sub-X7OL34TY', 'sub-BZTIJIMA', 
               'sub-MMP2OPZH', 'sub-XMV6BK3B', 'sub-C6YU555I', 'sub-MRZLO6NY', 'sub-XRK3CPGU', 'sub-CCW2JCII', 'sub-MVVSEQCV', 
               'sub-XSQR6SFW', 'sub-CU53LWV5', 'sub-NJQDQUXE', 'sub-XUWYZ2YZ', 'sub-CVAKNQOJ', 'sub-NMBLCROE', 'sub-Y5FDF5OS', 
               'sub-CYYZDAAA', 'sub-NMVNCA57', 'sub-YF7GX2SS', 'sub-DGLVI2LO', 'sub-NNFUFIPG', 'sub-YYJETPIQ', 'sub-DIG4A577', 
               'sub-NTL6Z5QX', 'sub-YZXJPDX7', 'sub-DPZNMDWH', 'sub-NWMHZ3XV', 'sub-Z5H6AKRX', 'sub-DSHUSGP5', 'sub-OKCTYCC6', 
               'sub-Z73RHXVZ', 'sub-DUPWYZDS', 'sub-PFFN7C6B', 'sub-ZCBTYZ6I', 'sub-E6HEUODN', 'sub-PJUPNBAM', 'sub-ZGAU3OES', 
               'sub-ETD7AYZZ', 'sub-PRLGSUII', 'sub-ZP4OTNBB', 'sub-FAOFZWSZ', 'sub-PSADWNDM', 'sub-ZVIA45ZD')

for item in subjectList:

    import os
    import sys


    subj = item


    os.chdir('/Users/chk17/Downloads/485/data/derivatives/fmriprep_20.2.0/fmriprep/{}/func'.format(subj))

    \
    
    ####Remove the first 3 TRs######
    
    import pandas as pd; \
    a=pd.read_csv('{}_task-rest_run-1_desc-confounds_timeseries.tsv'.format(subj),sep='\t').framewise_displacement; \
    a[0] = 999; \
    a[1] = 999; \
    a[2] = 999; \
    a = a.astype(float); \
    
    sys.stdout = open("motion_{}_censor_Initial.1D".format(subj),"w")    
    
    ####Remove TRs where framewise displacement is greater than 0.5mm##########
    
    print((a<0.5).astype(int).to_string(index=False)) 
        

   



