###Import the binary mask files that demarcate the voxels that surpassed the laterality "outlier threshold" for each group

d1 <- read.table(file="OutlierThresh_mask_Discovery_rStriatum.csv", header=F, sep=",")
d2 <- read.table(file="OutlierThresh_mask_Replication_rStriatum.csv", header=F, sep=",")
d3 <- read.table(file="OutlierThresh_mask_AAL_rStriatum.csv", header=F, sep=",")
d4 <- read.table(file="OutlierThresh_mask_Lefty_rStriatum.csv", header=F, sep=",")
d5 <- read.table(file="OutlierThresh_mask_Discovery_lStriatum.csv", header=F, sep=",")
d6 <- read.table(file="OutlierThresh_mask_Replication_lStriatum.csv", header=F, sep=",")
d7 <- read.table(file="OutlierThresh_mask_AAL_lStriatum.csv", header=F, sep=",")
d8 <- read.table(file="OutlierThresh_mask_Lefty_lStriatum.csv", header=F, sep=",")

###Import the AutoCorrelation-Preserving, Permuted MD Maps, created using BrainSmash in Python#####

d9 <- read.table(file="ACpreserving_rStriatum_MDmap_permutations_Discovery.csv", header=F, sep=",")
d10 <- read.table(file="ACpreserving_lStriatum_MDmap_permutations_Discovery.csv", header=F, sep=",")
d11 <- read.table(file="ACpreserving_rStriatum_MDmap_permutations_Replication.csv", header=F, sep=",")
d12 <- read.table(file="ACpreserving_lStriatum_MDmap_permutations_Replication.csv", header=F, sep=",")
d13 <- read.table(file="ACpreserving_rStriatum_MDmap_permutations_AAL.csv", header=F, sep=",")
d14 <- read.table(file="ACpreserving_lStriatum_MDmap_permutations_AAL.csv", header=F, sep=",")
d15 <- read.table(file="ACpreserving_rStriatum_MDmap_permutations_Lefty.csv", header=F, sep=",")
d16 <- read.table(file="ACpreserving_lStriatum_MDmap_permutations_Lefty.csv", header=F, sep=",")

###IQR Thresholds:
# Discovery_rStriatum = 1.1415
d9[d9<1.1415] <- 0
d9[d9>1.1415] <- 1
# Discovery_lStriatum = 1.1671
d10[d10<1.1671] <- 0
d10[d10>1.1671] <- 1
# Replication_rStriatum = 1.1452
d11[d11<1.1452] <- 0
d11[d11>1.1452] <- 1
# Replication_lStriatum = 1.20315
d12[d12<1.20315] <- 0
d12[d12>1.20315] <- 1
# AAL_rStriatum = 1.282
d13[d13<1.282] <- 0
d13[d13>1.282] <- 1
# AAL_lStriatum = 1.40195
d14[d14<1.40195] <- 0
d14[d14>1.40195] <- 1
# Lefty_rStriatum = 1.17465
d15[d15<1.17465] <- 0
d15[d15>1.17465] <- 1
# Lefty_lStriatum = 1.20015
d16[d16<1.20015] <- 0
d16[d16>1.20015] <- 1


###Calculate real Dice coefficient between two of the mask images####
Voxels_in_A <- sum(d1)
Voxels_in_B <- sum(d2)
Intersection <- d1+d2

Intersection2 <- Intersection == 2

Dice <- 2*sum(Intersection2)/(Voxels_in_A+Voxels_in_B)


####Permutation Test######


P <- length(d9[,1]) 

Dice_PERM_Distribution <- matrix(0, P)

for(p in 1:P){
  
  Voxels_in_A_perm <- sum(d1)
  Voxels_in_B_perm <- sum(d11[p,])
  Intersection_perm <- d1+d11[p,]
  
  Intersection2_perm <- Intersection_perm == 2
  
  Dice_perm <- 2*sum(Intersection2_perm)/(Voxels_in_A_perm+Voxels_in_B_perm)
  
  Dice_PERM_Distribution[p] <- Dice_perm
  
}


p_value <- mean(Dice_PERM_Distribution >= Dice)