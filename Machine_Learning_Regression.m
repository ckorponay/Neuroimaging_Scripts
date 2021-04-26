%%%%%% Predict task performance based on voxel-wise input using machine learning ######

%Created by Cole Korponay

clc;
clear;
close all;

softwareRoot = '/Applications/MATLAB_R2020a.app';

addpath(genpath('/Users/chk17/Documents/MATLAB/'))
%clear
csvRoot = '/Users/chk17/Downloads';

%%%%%%%%%%%%% Load in Training sample, select best features, train model  ###############

csvFile = sprintf('%s/SeventySeven_HCP_Subjs_ProcSpeed.csv', csvRoot);
%csvFile = sprintf('%s/HCP_ReplicationSample_n77_ProcSpeed.csv', csvRoot);

fileId = fopen(csvFile);
csv = textscan(fileId, '%s %f', 'Delimiter', ',');
fclose(fileId);


imgRoot = '/Users/chk17/Library/Mobile Documents/com~apple~CloudDocs/HCP_Data';

mask = load_nii(sprintf('%s/Group_L_Striatum_mask_bin.nii.gz', imgRoot));
%mask = load_nii(sprintf('%s/Group_R_Striatum_mask_bin.nii.gz', imgRoot));
maskIdx = find(mask.img(:) > 0);

numVolIds = length(csv{:, 1});
numVoxels = length(maskIdx);


X = zeros(numVolIds, numVoxels);
Y = zeros(numVolIds, 1);
subjIds = cell(numVolIds, 1);

for i = 1:numVolIds
    subjId = csv{:,1}{i,1};
    fprintf('\nLoading %s', subjId);
    imgFile = sprintf('%s/IndividualSubj_MDfiles_Zscores/lStriatum/%s_RvL_ManhattanDistance_Lstriatum_Z.nii', imgRoot, subjId);
    %imgFile = sprintf('%s/IndividualSubj_MDfiles_Zscores/rStriatum/%s_RvL_ManhattanDistance_Rstriatum_Z.nii', imgRoot, subjId);
 

    gm = load_nii(imgFile);
    gm = gm.img(maskIdx);
    
    X(i, 1:numVoxels) = gm;

   
     Y(i, 1) = (csv{:, 2}(i));
    
end    

%%%% get best F-test features
[idx,scores]=fsrftest(X,Y);
keep_Ftests=idx(1:475);
best_features_Ftest=X(:,keep_Ftests);




%%%% Train Model
num_features=size(X, 2);
num_obs=size(X,1);
data=[Y X];
group_labels=double(data(:,1));

svm_model2=fitrsvm(X(:,keep_Ftests),group_labels,'OptimizeHyperparameters','auto', 'HyperparameterOptimizationOptions', struct('AcquisitionFunctionName', 'expected-improvement-plus', 'KFold', 10));




%%%%%%%%%%%%% Load in Test sample, test model on test sample ###############

csvFile = sprintf('%s/SeventySeven_HCP_Subjs_ProcSpeed.csv', csvRoot);
%csvFile = sprintf('%s/HCP_ReplicationSample_n77_ProcSpeed.csv', csvRoot);

X = zeros(numVolIds, numVoxels);
Y = zeros(numVolIds, 1);
subjIds = cell(numVolIds, 1);

for i = 1:numVolIds
    subjId = csv{:,1}{i,1};
    fprintf('\nLoading %s', subjId);
    imgFile = sprintf('%s/IndividualSubj_MDfiles_Zscores/lStriatum/%s_RvL_ManhattanDistance_Lstriatum_Z.nii', imgRoot, subjId);
    %imgFile = sprintf('%s/IndividualSubj_MDfiles_Zscores/rStriatum/%s_RvL_ManhattanDistance_Rstriatum_Z.nii', imgRoot, subjId);
    %imgFile = sprintf('%s/IndividualSubj_MDfiles_Zscores/MD_DIFF/%s_ManhattanDistance_DIFF_Z_masked.nii', imgRoot, subjId);
    %imgFile = sprintf('%s/IndividualSubj_MDfiles_Zscores_ReplicationSample/MD_DIFF/%s_ManhattanDistance_DIFF_Z_masked.nii', imgRoot, subjId);

    gm = load_nii(imgFile);
    gm = gm.img(maskIdx);
    
    X(i, 1:numVoxels) = gm;

   
     Y(i, 1) = (csv{:, 2}(i));
    
end  



%%%% test original model on new Data
yHat =  predict(svm_model2, X(:,keep_Ftests));
[rho2,pval2] = corr(yHat, csv{:, 2})



%%%%%%%%%%%%%%to visualize best features%%%%%%%%%%%%%%%%%%%%
visKeep(keep_Ftests) = svm_model2.Beta;


in_brain=find(mask.img(:)>0);

all_sub_svm_coeffs = abs(visKeep);

%%
%create new full brain space variable, into which you will put the svm
%coeffs
full_brain_space=mask.img.*0;

%stick svm_coeffs into full brain space variable using same indexing variab
%le from above
full_brain_space(in_brain)=all_sub_svm_coeffs;


%make new header file for writing out
imgFile = sprintf('%s/Group_R_Striatum_mask_bin.nii.gz', imgRoot);
    gm = load_nii(imgFile);
new_hdr=gm;
%put new volume into new header
new_hdr.vol=full_brain_space;
new_hdr.img=full_brain_space;

%write out svm coeff 3d dataset. go ahead and view this file in afni so you
%can see that it looks like any other file you might view in afni
save_nii(new_hdr,'MD_Predictions_Ftest_Final25yup.nii');