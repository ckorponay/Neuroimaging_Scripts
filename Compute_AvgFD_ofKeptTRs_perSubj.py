#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 23:31:31 2021

@author: chk17
"""

####Using fMRIPrep output, find each subject's average framewise displacement, using only non-censored TRs##### 


subjectList = ('sub-DSHUSGP5',
'sub-VO5OWDFZ',
'sub-NJQDQUXE',
'sub-XMV6BK3B',
'sub-TORFT4TU',
'sub-OKCTYCC6',
'sub-SBFN2V62',
'sub-RZSUFL4K',
'sub-T6O3IWPJ',
'sub-QKGIT7SR',
'sub-KYEQTI3O',
'sub-DGLVI2LO',
'sub-ZP4OTNBB',
'sub-FJHDX5IK',
'sub-HKD7OLDH',
'sub-J4ER7FND',
'sub-74OJVKXQ',
'sub-G44HDPRR',
'sub-JD6P5XXB',
'sub-JGLZHEF6',
'sub-NWMHZ3XV',
'sub-24E5O5HD',
'sub-M6NL3WOP',
'sub-WL47OO7H',
'sub-FF2V32GM',
'sub-PRLGSUII',
'sub-HM25RXGI',
'sub-CCW2JCII',
'sub-HRHPSXHY',
'sub-MRZLO6NY',
'sub-75X3I64X',
'sub-XUWYZ2YZ',
'sub-AEJWBSIB',
'sub-LU25B3EX',
'sub-QZYS4JNS',
'sub-HI4JYNOC',
'sub-3T47XKCD',
'sub-FAOFZWSZ',
'sub-33HYKD6V',
'sub-WTHDLYGS',
'sub-NTL6Z5QX',
'sub-NMBLCROE',
'sub-HP2NI3MR',
'sub-IKAJ2UXF',
'sub-DPZNMDWH',
'sub-MJA53T6N',
'sub-KTG4CELR',
'sub-S2PURVUQ',
'sub-WTNDMQAE',
'sub-NMVNCA57',
'sub-RD4VTC7F',
'sub-VOEYFKQL',
'sub-Z73RHXVZ',
'sub-3WNXNOIM',
'sub-I4DC5V5Z',
'sub-B5U3KVGH',
'sub-JV3IJWGZ',
'sub-7I7UH5I4',
'sub-RV62GCL3',
'sub-REA73OA6',
'sub-XRK3CPGU',
'sub-TWZLYWYK',
'sub-Y5FDF5OS',
'sub-SBB5AIAL',
'sub-CU53LWV5',
'sub-45WE4VWV',
'sub-7CKNTSFP',
'sub-FY2PAN3N',
'sub-ETD7AYZZ',
'sub-A7MQ6DGT',
'sub-BDK53Y62',
'sub-SYEEUTEL',
'sub-KZVCNSPV',
'sub-AG6EXHRL',
'sub-C6YU555I',
'sub-PFFN7C6B',
'sub-ZGAU3OES',
'sub-T2RCUMZL',
'sub-MMP2OPZH',
'sub-V67CV2OT',
'sub-PJUPNBAM',
'sub-SKBY5ALZ',
'sub-ZCBTYZ6I',
'sub-56EWJURG',
'sub-NNFUFIPG',
'sub-YZXJPDX7',
'sub-AKHOY3UH',
'sub-QUN4GT3M',
'sub-E6HEUODN',
'sub-V5QHNBSH',
'sub-FWQKH5UL',
'sub-4BBDI62B',
'sub-CVAKNQOJ',
'sub-YF7GX2SS',
'sub-7H6W6KFZ',
'sub-CYYZDAAA',
'sub-KGDWBBAJ',
'sub-4ALM5WXW',
'sub-PSADWNDM',
'sub-JJU72DNY',
'sub-X7OL34TY',
'sub-JTGVG5WJ',
'sub-YYJETPIQ',
'sub-WVGICHTU',
'sub-ZVIA45ZD',
'sub-DIG4A577',
'sub-SBMESIHC',
'sub-RIOEHEWU',
'sub-TZPLZADX',
'sub-ARUFOFFX',
'sub-WLYPL3QY',
'sub-7RYHMDAO')

import pandas as pd; \
import numpy as np; \
i=0
Mean_FD = pd.DataFrame(np.zeros((112, 1)))

for item in subjectList:
    
  

    import os
    import sys
   
    

    subj = item


    os.chdir('/Users/chk17/Downloads/485/data/derivatives/fmriprep_20.2.0/fmriprep/{}/func'.format(subj))
    a=pd.read_csv('{}_task-rest_run-1_desc-confounds_timeseries.tsv'.format(subj),sep='\t').framewise_displacement; \
        
    os.chdir('/Users/chk17/Downloads/485/data/derivatives/fmriprep_20.2.0/fmriprep/{}'.format(subj))  
    b=pd.read_csv('motion_{}_censor.csv'.format(subj),sep='\t')    
    
    a = a.astype(float); \
    b = b.astype(float); \
        
    ab = pd.concat([a, b], axis=1)
    
    ab = ab[ab['Col#0'] != 0]
    
    Mean_FD.loc[i] = ab['framewise_displacement'].mean()
    
    i=i+1

    

        
