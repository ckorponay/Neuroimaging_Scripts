#!/bin/bash

RvL_ManhattanDistance.nii -uthr 0.47 RvL_ManhattanDistance_uTHR.nii

3dBrickStat -count -non-zero RvL_ManhattanDistance_uTHR.nii.gz

3dBrickStat -count -non-zero RvL_ManhattanDistance.nii
