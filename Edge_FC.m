% clean up env for clean run
clearvars; close all; clc

%% make edge time series, eFC, and related concepts

%perform the following AFNI commands in the terminal to generate an
%individual subject's Cleaned timeseries for each voxel in the striatum (the input to this script):
 
  %1. 3dmaskdump -noijk  -mask ../Group_R_Striatum_mask_bin.nii Clean_rfMRI_REST1_LR.nii.gz > rStriatum_Clean_TimeSeries.1D
  %2. 1dcat -csvout rStriatum_Clean_TimeSeries.1D > rStriatum_Clean_TimeSeries.csv

% add helper functions to path
addpath(genpath('fcn'));
addpath '/Users/chk17/Downloads/NIfTI_20140122'
addpath '/Users/chk17/Downloads/BCT'
      
% load example time series, system labels, and names
%load example_data
ts = readtable('/Users/chk17/Library/Mobile Documents/com~apple~CloudDocs/HCP_Data/100307/rStriatum_Clean_TimeSeries.csv','NumHeaderLines',1);
ts = table2array(ts); 
ts = double(ts);
ts = ts';

% create edge time series from regional time series
[T,N] = size(ts);
M = N*(N - 1)/2;
ets = fcn_edgets(ts);

% uncomment to calculate efc - memory intensive
efc = fcn_edgets2edgecorr(ets);

% run kmeans -- note that in principle any clustering algorithm can be
% applied to edge time series or the efc matrix
k = 10;  %for striatum, k=6 or 7 might be better
ci = kmeans(ets',k,...
    'distance','sqeuclidean',...
    'maxiter',1000);

% map edge communities into matrix
mat = zeros(N);
mat(triu(ones(N),1) > 0) = ci;
mat = mat + mat';      %%%this shows what community each node belongs to via its edge with each other node;
                       %%%can create a pie-graph of each row to show the
                       %%%percentage by which the node in that row belongs
                       %%%to each community
                       
     %%creates the "Community Fingerprint" for each voxel, showing the percent it belongs to each of the K communities
Community_Fingerprint = zeros(N,k+1);
for i=1:N
 Community_Fingerprint(i,:) = histcounts(mat(i,:),k+1);
end 

Community_Fingerprint(:,1) = [];
Community_Fingerprint = Community_Fingerprint/(N-1);    

%% calculate community similarity

s = fcn_profilesim(mat);    %%shows how similar the community pie chart of each node is to each other node

%% calculate normalized entropy

[u,v] = find(triu(ones(N),1));
[~,enorm] = fcn_node_entropy(ci,u,v,N);  %%shows the entropy of each region (the degree to which it participates in many communities)


%%%%%%%%project voxel map into brain space%%%%%%%%%%%%%%
in_brain=find(mask.img(:)>0);
full_brain_space=mask.img.*0;
%full_brain_space(in_brain)=enorm;  %for visualizing voxel-wise entropy 
%full_brain_space(in_brain)=s(900,:); %for visualzing the similarity of each voxel's community profile to that of the selected voxel
%full_brain_space(in_brain)=mat(900,:); %for visualizing the community each voxel is in with the selected voxel
full_brain_space(in_brain)=Community_Fingerprint(:,10)+1; %for visualizing the percent each voxel belongs to the seleted community
imgFile = sprintf('%s/Group_R_Striatum_mask_bin.nii.gz', imgRoot);
gm = load_nii(imgFile);
new_hdr=gm;
new_hdr.vol=full_brain_space;
new_hdr.img=full_brain_space;
%save_nii(new_hdr,'eFC_Entropy_rStriatum_100307.nii');
%save_nii(new_hdr,'eFC_CommunityPieChartSimlarlity_V900_rStriatum_100307.nii');
%save_nii(new_hdr,'eFC_CommunityClustering_V900_rStriatum_100307.nii');
save_nii(new_hdr,'eFC_PercentBelongingTo_Community10_rStriatum_100307.nii');

%% make some figures

[gx,gy,idx] = grid_communities(lab); % BCT function

figure, imagesc(mat(idx,idx)); axis square; hold on; plot(gx,gy,'k','linewidth',2); title('Edge communities')
figure, imagesc(s(idx,idx)); axis square; hold on; plot(gx,gy,'k','linewidth',2); title('Edge community similarity')
figure, boxplot(enorm,lab,'labels',net,'labelorientation','inline'); title('Norm entropy per system')

%% visualize edge time series

[~,idx] = sort(ci); dffidx = find(diff(ci(idx)));
figure, imagesc(ets(:,idx)',[-4,4]); hold on;
for i = 1:length(dffidx)
    plot([0.5,T + 0.5],dffidx(i)*ones(1,2),'k');
end
title('Edge time series')

%% visualize efc matrix

if exist('efc','var')
    figure, imagesc(efc(idx,idx),[-1,1]);
end

%% make surface plot

enorm_rank = tiedrank(enorm); % for visualization, rank transform entropy

% load 32k surfaces
load fcn/surfinfo
cr = zeros(size(gr.cdata));
cl = zeros(size(gl.cdata));
cr(gr.cdata ~= 0) = enorm_rank(gr.cdata(gr.cdata ~= 0));
cl(gl.cdata ~= 0) = enorm_rank(gl.cdata(gl.cdata ~= 0));

cmap = fcn_cmaphot;

% based on if 'gifti' repo is in system path, sr and sl structures could be
% different; thus, quick check here. 
if isfield(sr,'data') 
    figure, th = trisurf(sr.data{2}.data+1,sr.data{1}.data(:,1),sr.data{1}.data(:,2),sr.data{1}.data(:,3),cr);
    set(th,'edgecolor','none'); axis image; set(gca,'clim',[min(enorm_rank),max(enorm_rank)]);
    view(gca,3);axis equal;axis off;view(90,0);material dull;camlight headlight;lighting gouraud
    colormap(cmap);

    figure, th = trisurf(sl.data{2}.data+1,sl.data{1}.data(:,1),sl.data{1}.data(:,2),sl.data{1}.data(:,3),cr);
    set(th,'edgecolor','none'); axis image; set(gca,'clim',[min(enorm_rank),max(enorm_rank)]);
    view(gca,3);axis equal;axis off;view(-90,0);material dull;camlight headlight;lighting gouraud
    colormap(cmap);
else 
    figure, th = trisurf(sr.faces,sr.vertices(:,1),sr.vertices(:,2),sr.vertices(:,3),cr);
    set(th,'edgecolor','none'); axis image; set(gca,'clim',[min(enorm_rank),max(enorm_rank)]);
    colormap(cmap); colorbar;

    figure, th = trisurf(sl.faces,sl.vertices(:,1),sl.vertices(:,2),sl.vertices(:,3),cl);
    set(th,'edgecolor','none'); axis image; set(gca,'clim',[min(enorm_rank),max(enorm_rank)]);
    colormap(cmap); colorbar;
end
