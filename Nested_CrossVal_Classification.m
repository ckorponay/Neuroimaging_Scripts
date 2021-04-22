clc;
clear;
close all;

softwareRoot = '/Applications/MATLAB_R2020a.app';
addpath(genpath(sprintf('%s/spider', softwareRoot)));
addpath(genpath('/Users/chk17/Documents/MATLAB/'))

%%Load in Subject IDs and their handedness (R or L)

csvRoot = '/Users/chk17/Documents/Documents_PHS013420/Laterality_Project/Lefty_Sample';
csvFile = sprintf('%s/Handedness_Classification.csv', csvRoot);

fileId = fopen(csvFile);
csv = textscan(fileId, '%s %s', 'Delimiter', ',');
fclose(fileId);

%%Load in mask data
imgRoot = '/Users/chk17/Library/Mobile Documents/com~apple~CloudDocs/HCP_Data';
mask = load_nii(sprintf('%s/Intersect_Handedness_Classification_RandL_Striatum_mask.nii.gz', imgRoot));
maskIdx = find(mask.img(:) > 0);
numVolIds = length(csv{:, 1});
numVoxels = length(maskIdx);

%%Initialize data matrices
X = zeros(numVolIds, numVoxels);
Y = zeros(numVolIds, 1);
subjIds = cell(numVolIds, 1);

%%Load in subject voxel-wise Manhattan distance maps 

for i = 1:numVolIds
    subjId = csv{:,1}{i,1};
    fprintf('\nLoading %s', subjId);
    imgFile = sprintf('%s/Handedness_Classification/RandL_Striatum/%s_RvL_ManhattanDistance_RandLstriatum_Z.nii', imgRoot, subjId);
    gm = load_nii(imgFile);
    gm = gm.img(maskIdx);
    X(i, 1:numVoxels) = gm;
    
    if(strcmpi(csv{:, 2}(i), 'L'))
        Y(i, 1) = -1;
    else
        Y(i, 1) = 1;
    end
end 

%%Randomly distribute subjects into 10 folds for cross-validation

Subject_Indices = transpose(randperm(154))
Baseline = 1:154

Fold1_in = Subject_Indices
Fold1_in(1:15) = []
Fold1_out = setdiff(Baseline, Fold1_in)

Fold2_in = Subject_Indices
Fold2_in(16:30) = []
Fold2_out = setdiff(Baseline, Fold2_in)

Fold3_in = Subject_Indices
Fold3_in(31:45) = []
Fold3_out = setdiff(Baseline, Fold3_in)

Fold4_in = Subject_Indices
Fold4_in(46:60) = []
Fold4_out = setdiff(Baseline, Fold4_in)

Fold5_in = Subject_Indices
Fold5_in(61:75) = []
Fold5_out = setdiff(Baseline, Fold5_in)

Fold6_in = Subject_Indices
Fold6_in(76:90) = []
Fold6_out = setdiff(Baseline, Fold6_in)

Fold7_in = Subject_Indices
Fold7_in(91:106) = []
Fold7_out = setdiff(Baseline, Fold7_in)

Fold8_in = Subject_Indices
Fold8_in(107:122) = []
Fold8_out = setdiff(Baseline, Fold8_in)

Fold9_in = Subject_Indices
Fold9_in(123:138) = []
Fold9_out = setdiff(Baseline, Fold9_in)

Fold10_in = Subject_Indices
Fold10_in(139:154) = []
Fold10_out = setdiff(Baseline, Fold10_in)


Folds_in = {Fold1_in; Fold2_in; Fold3_in; Fold4_in; Fold5_in; Fold6_in; Fold7_in; Fold8_in; Fold9_in; Fold10_in}
Folds_out = {Fold1_out; Fold2_out; Fold3_out; Fold4_out; Fold5_out; Fold6_out; Fold7_out; Fold8_out; Fold9_out; Fold10_out}

%%Perform nested cross-validation

for i = 1:10 
    
    Xcrossval = X(Folds_in{i},:)
    Ycrossval = Y(Folds_in{i},:)
    
    %%%% get best F-test features
[idx,scores]=fsrftest(Xcrossval,Ycrossval);
keep_Ftests=idx(1:947); %%25% best features
best_features_Ftest=Xcrossval(:,keep_Ftests);

    %%% optimize hyperparameters

data=[Ycrossval Xcrossval];
group_labels=double(data(:,1));

svm_model2=fitcsvm(Xcrossval(:,keep_Ftests),group_labels,'OptimizeHyperparameters','auto', 'HyperparameterOptimizationOptions', struct('AcquisitionFunctionName', 'expected-improvement-plus', 'KFold', 10));

    %%% apply model to left-out test fold 

yHat(Folds_out{i}) =  predict(svm_model2, X(Folds_out{i},keep_Ftests));  %%need to change last term here to the Folds_Out correpsonding to the Folds_In for that iteration


end


%%Compute accuracy of test predictions

Z = zeros(numVolIds,1)
for i = 1:numVolIds
Z(i,:)= Y(i) == yHat(i);
end

ACCURACY = mean(Z)*100

