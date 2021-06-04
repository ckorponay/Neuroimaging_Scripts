clc;
clear;
close all;

softwareRoot = '/Applications/MATLAB_R2020a.app';
addpath(genpath(sprintf('%s/spider', softwareRoot)));
addpath '/Users/chk17/Downloads/NIfTI_20140122'


addpath(genpath('/Users/chk17/Documents/MATLAB/'))
clear
%csvRoot = '/Users/chk17/Documents/Laterality_Project/Initial_Sample';
%csvRoot = '/Users/chk17/Documents/Laterality_Project/Replication_Sample';
%csvRoot = '/Users/chk17/Documents/Laterality_Project/Lefty_Sample';
csvRoot = '/Users/chk17/Desktop/DesktopRoundup331';
%csvFile = sprintf('%s/SeventySeven_HCP_Subjs_Language_Difficulty.csv', csvRoot);
%csvFile = sprintf('%s/SeventySeven_HCP_Subjs_Flanker.csv', csvRoot);
%csvFile = sprintf('%s/SeventySeven_HCP_Subjs_Handedness.csv', csvRoot);
%csvFile = sprintf('%s/HCP_ReplicationSample_n77.csv', csvRoot);
%csvFile = sprintf('%s/HCP_Lefties.csv', csvRoot);
%csvFile = sprintf('%s/485_Controls.csv', csvRoot);
%csvFile = sprintf('%s/Age_Gender_Matched_HCPsample_to485.csv', csvRoot);
csvFile = sprintf('%s/Age_Gender_Matched_HCPsample_to485_SUDSesh2andControls.csv', csvRoot);
%csvFile = sprintf('%s/485_SUD.csv', csvRoot);
fileId = fopen(csvFile);
csv = textscan(fileId, '%s', 'Delimiter', ',');
fclose(fileId);

csv2Root = '/Users/chk17/Desktop/DesktopRoundup331/Desktop_PHS013420';
csv2File = sprintf('%s/Seeds.csv', csv2Root);
file2Id = fopen(csv2File);
csv2 = textscan(file2Id, '%s', 'Delimiter', ',');
fclose(file2Id);

%imgRoot = '/Users/chk17/Library/Mobile Documents/com~apple~CloudDocs/Desktop/HCP_Data';
%imgRoot = '/Users/chk17/Library/Mobile Documents/com~apple~CloudDocs/Desktop/HCP_Data/Replication_Sample';
%imgRoot = '/Users/chk17/Library/Mobile Documents/com~apple~CloudDocs/Desktop/HCP_Data/Lefty_Sample';
imgRoot = '/Users/chk17/Library/Mobile Documents/com~apple~CloudDocs/HCP_Data';
%mask = load_nii(sprintf('%s/Group_R_Striatum_mask_bin.nii', imgRoot));
%mask = load_nii(sprintf('%s/Group_rStriatum_Mask/Group_rStriatum_Mask_bin.nii.gz', imgRoot));
%mask = load_nii(sprintf('/Users/chk17/Downloads/485/data/derivatives/fmriprep_20.2.0/fmriprep/Group_R_striatum_mask/Group_rStriatum_mask_bin.nii.gz'));
mask = load_nii(sprintf('%s/Group_L_Striatum_mask_bin.nii', imgRoot));
%mask = load_nii(sprintf('%s/Intersect.nii', imgRoot));
maskIdx = find(mask.img(:) > 0);

numVolIds = length(csv{:, 1});
numSeeds = length(csv2{:, 1});
numVoxels = length(maskIdx);


subjIds = cell(numVolIds, 1);
SeedsIds = cell(numSeeds, 1);



%W = zeros(30,77);
%W = zeros(30,79);



for i = 1:numVolIds
   
     Y(i, 1) = (csv{:, 1}(i));
    
end


%%%%%%Randomly split the group into two groups, calculate each group's AVG
%%%%%%voxel-wise Z-map for each ROI, calculate the MD at each voxel, save
%%%%%%the MD map; do this 10,000 times; save the MD map vector of each
%%%%%%permutation, then plot distribution of them all, find .001. 

P = 10000


Z_final = zeros(P,numVoxels);

for p = 1:P

fprintf('\nStarting Iteration %d', p);

%%for SUD group
%rand_indices = randperm(79);
%intraGroup_1 = Y(rand_indices(1:39),:);
%intraGroup_2 = Y(rand_indices(40:end),:);

%%for Control group
%rand_indices = randperm(33);
%intraGroup_1 = Y(rand_indices(1:16),:);
%intraGroup_2 = Y(rand_indices(17:end),:);

%%for SUDandControl group
%rand_indices = randperm(112);
%intraGroup_1 = Y(rand_indices(1:33),:);
%intraGroup_2 = Y(rand_indices(34:end),:);

rand_indices = randperm(79);
intraGroup_1 = Y(rand_indices(1:33),:);
intraGroup_2 = Y(rand_indices(34:end),:);

numVolIds_intraGroup_1 = length(intraGroup_1);
numVolIds_intraGroup_2 = length(intraGroup_2);

W1 = zeros(numVolIds_intraGroup_1,numVoxels);
Z1 = zeros(numSeeds,numVoxels);

W2 = zeros(numVolIds_intraGroup_2,numVoxels);
Z2 = zeros(numSeeds,numVoxels);


for j = 1:numSeeds
    seedId = csv2{:,1}{j,1};

 for i = 1:numVolIds_intraGroup_1
    subjId = intraGroup_1{i,1};
   
    X1 = zeros(1, numVoxels);


    %imgFile = sprintf('%s/SUD_%s/%s_%s_r2z.nii', imgRoot, seedId, subjId, seedId);
    %imgFile = sprintf('%s/Control_%s/%s_%s_r2z.nii', imgRoot, seedId, subjId, seedId);
    imgFile = sprintf('%s/L_All_%s/L_%s_%s_r2z.nii.gz', imgRoot, seedId, subjId, seedId);
   
   
    gm = load_nii(imgFile);
    gm = gm.img(maskIdx);
    %gm = gm.vol(maskIdx) %/ csv{:, 3}(i);
    %gmNorm = (gm - min (gm)) / (max(gm) - min(gm));
    %X(i, 1:numVoxels) = gm;
    X1(1, 1:numVoxels) = gm;

      
   W1(i,:) = X1;
    
  end
  %for getting the mean Z score of each ROI across all voxels
 
  Z1(j,:) = mean(W1, 1);
  
  end
  %for getting the mean Z score of each ROI across all voxels
  
  
  %%need to do same as above for intraGroup2, then calculate the MD of each
  %%voxel using Z1-Z2, and storing tha result as one row in Z_FINal
  for j = 1:numSeeds
    seedId = csv2{:,1}{j,1};

 for i = 1:numVolIds_intraGroup_2
    subjId = intraGroup_2{i,1};
   
    X2 = zeros(1, numVoxels);

 
    %imgFile = sprintf('%s/SUD_%s/%s_%s_r2z.nii', imgRoot, seedId, subjId, seedId);
    %imgFile = sprintf('%s/Control_%s/%s_%s_r2z.nii', imgRoot, seedId, subjId, seedId);
    imgFile = sprintf('%s/L_All_%s/L_%s_%s_r2z.nii.gz', imgRoot, seedId, subjId, seedId);
    
   
    
    gm = load_nii(imgFile);
    gm = gm.img(maskIdx);
    %gm = gm.vol(maskIdx) %/ csv{:, 3}(i);
    %gmNorm = (gm - min (gm)) / (max(gm) - min(gm));
    %X(i, 1:numVoxels) = gm;
    X2(1, 1:numVoxels) = gm;

      
   W2(i,:) = X2; 
    
  end
  %for getting the mean Z score of each ROI across all voxels
 
  Z2(j,:) = mean(W2, 1);
  
  end
  
  for b=1:numVoxels
      MD1=abs(Z1(1,b)-Z2(1,b));
      MD2=abs(Z1(2,b)-Z2(2,b));
      MD3=abs(Z1(3,b)-Z2(3,b));
      MD4=abs(Z1(4,b)-Z2(4,b));
      MD5=abs(Z1(5,b)-Z2(5,b));
      MD6=abs(Z1(6,b)-Z2(6,b));
      MD7=abs(Z1(7,b)-Z2(7,b));
      MD8=abs(Z1(8,b)-Z2(8,b));
      MD9=abs(Z1(9,b)-Z2(9,b));
      MD10=abs(Z1(10,b)-Z2(10,b));
      MD11=abs(Z1(11,b)-Z2(11,b));
      MD12=abs(Z1(12,b)-Z2(12,b));
      MD13=abs(Z1(13,b)-Z2(13,b));
      MD14=abs(Z1(14,b)-Z2(14,b));
      MD15=abs(Z1(15,b)-Z2(15,b));
      MD16=abs(Z1(16,b)-Z2(16,b));
      MD17=abs(Z1(17,b)-Z2(17,b));
      MD18=abs(Z1(18,b)-Z2(18,b));
      MD19=abs(Z1(19,b)-Z2(19,b));
      MD20=abs(Z1(20,b)-Z2(20,b));
      MD21=abs(Z1(21,b)-Z2(21,b));
      MD22=abs(Z1(22,b)-Z2(22,b));
      MD23=abs(Z1(23,b)-Z2(23,b));
      MD24=abs(Z1(24,b)-Z2(24,b));
      MD25=abs(Z1(25,b)-Z2(25,b));
      MD26=abs(Z1(26,b)-Z2(26,b));
      MD27=abs(Z1(27,b)-Z2(27,b));
      MD28=abs(Z1(28,b)-Z2(28,b));
      MD29=abs(Z1(29,b)-Z2(29,b));
      MD30=abs(Z1(30,b)-Z2(30,b));
      
      MD_Total=MD1+MD2+MD3+MD4+MD5+MD6+MD7+MD8+MD9+MD10+MD11+MD12+MD13+MD14+MD15+MD16+MD17+MD18+MD19+MD20+MD21+MD22+MD23+MD24+MD25+MD26+MD27+MD28+MD29+MD30;
     
  
  
  Z_final(p,b) = MD_Total;
  
  end
  

end

  writematrix(Z_final, ['HCP_noDrugs_randGroup_MDs_lStriatum_SUDSesh2andControls.csv'])
 
   