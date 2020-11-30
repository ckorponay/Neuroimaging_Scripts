clc;
clear;
close all;

softwareRoot = '/Applications/MATLAB_R2020a.app';
addpath(genpath(sprintf('%s/spider', softwareRoot)));



addpath(genpath('/Users/chk17/Documents/MATLAB/'))
clear
csvRoot = '/Users/chk17/Downloads';
csvFile = sprintf('%s/journal.pbio.1002469.s008_REVISED.csv', csvRoot);
fileId = fopen(csvFile);
csv = textscan(fileId, '%s %s', 'Delimiter', ',');
fclose(fileId);


imgRoot = '/Users/chk17/Library/Mobile Documents/com~apple~CloudDocs/Desktop/HCP_Data';
mask = load_nii(sprintf('%s/Group_R_Striatum_mask_bin.nii', imgRoot));
maskIdx = find(mask.img(:) > 0);

numVolIds = length(csv{:, 1});
numVoxels = length(maskIdx);


X = zeros(numVolIds, numVoxels);
%X = zeros(numVolIds, numVoxels + 2);  %turn on for other variables
Y = zeros(numVolIds, 1);
subjIds = cell(numVolIds, 1);

% Normalization of the predicting variables.
%age = csv{:, 4};
%ageNorm = (age - min(age)) / (max(age) - min(age));
%race = csv{:, 5};
%raceNorm = (race - min(race)) / (max(race) - min(race));

for i = 1:numVolIds
    subjId = csv{:,1}{i,1};
    fprintf('\nLoading %s', subjId);
    imgFile = sprintf('%s/%s/%s_RvL_ManhattanDistance_Rstriatum.nii', imgRoot, subjId, subjId);
    gm = load_nii(imgFile);
    gm = gm.img(maskIdx);
    %gm = gm.vol(maskIdx) %/ csv{:, 3}(i);
    %gmNorm = (gm - min (gm)) / (max(gm) - min(gm));
    X(i, 1:numVoxels) = gm;
    %X(i, 1:numVoxels) = gmNorm;  %normalization
    %X(i, numVoxels) = [gm.vol(maskIdx) / csv{:, 3}(i);  
    %X(i, numVoxels + 1: numVoxels + 2) = [ageNorm(i) raceNorm(i)];  %turn
    %on for other variables
      %X(i, :) = gm.vol(maskIdx);
    if(strcmpi(csv{:, 2}(i), 'F'))
        Y(i, 1) = -1;
    else
        Y(i, 1) = 1;
    end
end    



%%
%this is generating a dataset with high dimensionality and low sample size
num_features=size(X, 2);
num_obs=size(X,1);

%generate random data
%data=randn(num_obs,num_features);
data=[Y X];


%%
%this is setting up stuff for the cross-validation loop

%dichotomize the outcome variable
group_labels=double(data(:,1)>0);

%define features
features=data(:,2:end);

%pick how many features you want to keep overall, here i'm choosing 99%
best_feature_perc=.99;
%pick how many features you want to keep per each iteraction of the
%recursive feature elimination, here i'm choosing 99%
keep_per_iter_perc=.99;
%total number of features to keep
num_features_to_keep=round(size(features,2).*best_feature_perc);

%%
%this is doing the SVM


%preallocate variables 
all_subs_svm_coeffs=zeros(num_obs,size(features,2));
store_svm_cv_acc=zeros(num_obs,3);

for cv=1:numel(group_labels)
    %define testing and training indices
    test=cv;
    train=setdiff(1:numel(group_labels),cv);
    
    
    %initialize variables
    keep=1:size(features,2);
    full_feature_space_tracking=keep.*0;
    
    iter=0;
    %iteratively do this until have pruned all of the 
    while numel(keep)>num_features_to_keep
        fprintf('\n Feature selection for %d in iteration %d', test, iter);
        iter=iter+1;
       
        %using a cost function of 1, can change this
        svm_model=fitcsvm(features(train,keep),group_labels(train));
        
        %calculate SVM feature weights
        svm_coeffs=svm_model.Beta;
        
        %identify top percent of biggest feature weights
        [s i]=sort(abs(svm_coeffs),'descend');
        best_features=i(1:round(numel(i).*keep_per_iter_perc));
        
        %store in the full feature space which features are being selected
        %from this step
        full_feature_space_tracking(iter,keep(best_features))=1;
        
        %update keep based on full feature space
        keep=find(full_feature_space_tracking(iter,:)==1);
    end

    %retrain new model using the identified best features
    svm_model=fitcsvm(features(train,keep),group_labels(train));
    
    %calculate SVM feature weights
    svm_coeffs=svm_model.Beta;
    all_subs_svm_coeffs(cv,keep)=svm_coeffs;
    
    %now test model on left out case
    [label, score] = predict(svm_model, features(test,keep));
    
    %store accuracy and hyperplane distance
    store_svm_cv_acc(cv,:)=[label, score];
end


Real_Labels = readtable('/Users/chk17/Downloads/RealLabels_Gender.csv');
RealLabels = table2array(Real_Labels)

Z = zeros(77,1)
                        
for i = 1:77
Z(i,:)= RealLabels(i) == store_svm_cv_acc(i,1);
end

ACCURACY = mean(Z)*100



sv = svm_model.SupportVectors;
figure
gscatter(X(:,1),X(:,2),Y)
hold on
plot(sv(:,1),sv(:,2),'ko','MarkerSize',10)
legend('versicolor','virginica','Support Vector')
hold off
