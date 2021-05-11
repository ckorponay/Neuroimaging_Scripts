%%%Compute voxel-wise Manhattan between the connectivity fingerprints of
%%%two groups

clc;
clear;
close all;

softwareRoot = '/Applications/MATLAB_R2020a.app';
addpath '/Users/chk17/Downloads/NIfTI_20140122'

addpath(genpath('/Users/chk17/Documents/MATLAB/'))

%%%%%%Add subject name list
csvRoot = '/Users/chk17/Downloads/485';
csvFile = sprintf('%s/485_SUDandControls.csv', csvRoot);
fileId = fopen(csvFile);
csv = textscan(fileId, '%s %f', 'Delimiter', ',');
fclose(fileId);

%%%%%%Add seed name list
csv2Root = '/Users/chk17/Desktop/DesktopRoundup331/Desktop_PHS013420';
csv2File = sprintf('%s/Seeds.csv', csv2Root);
file2Id = fopen(csv2File);
csv2 = textscan(file2Id, '%s', 'Delimiter', ',');
fclose(file2Id);

%%%%%% set image root, load mask, and store subject/mask/seed details 
imgRoot = '/Users/chk17/Downloads/485/data/derivatives/fmriprep_20.2.0/fmriprep';

%mask = load_nii(sprintf('%s/Group_L_striatum_mask/Group_lStriatum_mask_bin.nii.gz', imgRoot));
mask = load_nii(sprintf('%s/Group_R_striatum_mask/Group_rStriatum_mask_bin.nii.gz', imgRoot));

maskIdx = find(mask.img(:) > 0);

numVolIds = length(csv{:, 1});
numSeeds = length(csv2{:, 1});
numVoxels = length(maskIdx);


subjIds = cell(numVolIds, 1);
SeedsIds = cell(numSeeds, 1);







%%%%%% Calculate each group's AVG voxel-wise Z-map for each ROI, 
%%%%%% calculate the Manhattan distance at each voxel

for i = 1:numVolIds
   
     Y(i, 1) = (csv{:, 1}(i));
    
end

P =1

Z_final = zeros(P,numVoxels);

for p = 1:P

fprintf('\nStarting Iteration %d', p);

intraGroup_1 = Y(1:79);
intraGroup_2 = Y(80:end);

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

    %imgFile = sprintf('%s/L_All_%s/L_%s_%s_r2z.nii', imgRoot, seedId, subjId, seedId);
    imgFile = sprintf('%s/All_%s/%s_%s_r2z.nii', imgRoot, seedId, subjId, seedId);
  
   
    gm = load_nii(imgFile);
    gm = gm.img(maskIdx);
 
    X1(1, 1:numVoxels) = gm;

      
   W1(i,:) = X1;
    
  end

 
  Z1(j,:) = mean(W1, 1);
  
  end
  
  
  for j = 1:numSeeds
    seedId = csv2{:,1}{j,1};

  for i = 1:numVolIds_intraGroup_2
    subjId = intraGroup_2{i,1};
   
    X2 = zeros(1, numVoxels);

    %imgFile = sprintf('%s/L_All_%s/L_%s_%s_r2z.nii', imgRoot, seedId, subjId, seedId);
    imgFile = sprintf('%s/All_%s/%s_%s_r2z.nii', imgRoot, seedId, subjId, seedId);
   
    
    gm = load_nii(imgFile);
    gm = gm.img(maskIdx);
   
    X2(1, 1:numVoxels) = gm;

      
   W2(i,:) = X2;
    
  end

 
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

writematrix(Z_final, ['SUDvControl_RealMDmap_rStriatum.csv'])