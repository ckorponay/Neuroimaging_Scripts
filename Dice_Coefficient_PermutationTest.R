
###Import the binary mask files whose overlap you want to assess

d1 <- read.table(file="OutlierThresh_mask_Discovery_rStriatum.csv", header=F, sep=",")
d2 <- read.table(file="OutlierThresh_mask_Replication_rStriatum.csv", header=F, sep=",")
d3 <- read.table(file="OutlierThresh_mask_AAL_rStriatum.csv", header=F, sep=",")
d4 <- read.table(file="OutlierThresh_mask_Lefty_rStriatum.csv", header=F, sep=",")
d5 <- read.table(file="OutlierThresh_mask_Discovery_lStriatum.csv", header=F, sep=",")
d6 <- read.table(file="OutlierThresh_mask_Replication_lStriatum.csv", header=F, sep=",")
d7 <- read.table(file="OutlierThresh_mask_AAL_lStriatum.csv", header=F, sep=",")
d8 <- read.table(file="OutlierThresh_mask_Lefty_lStriatum.csv", header=F, sep=",")

###Calculate the actual Dice coefficient between two of the mask images####
Voxels_in_A <- sum(d6)
Voxels_in_B <- sum(d7)
Intersection <- d6+d7

Intersection2 <- Intersection == 2

Dice <- 2*sum(Intersection2)/(Voxels_in_A+Voxels_in_B)

####Permutation Test: on each iteraction, randomly scramble the voxel locations of one mask, and calculate the new Dice coefficient; repeat P times, and create a distribution of each iteration's Dice coefficents######
set.seed(1977)  

P <- 10000 

Dice_PERM_Distribution <- matrix(0, P)

for(p in 1:P){

d6_perm <- d6[,sample(ncol(d6))]

Voxels_in_A_perm <- sum(d7)
Voxels_in_B_perm <- sum(d6_perm)
Intersection_perm <- d7+d6_perm

Intersection2_perm <- Intersection_perm == 2

Dice_perm <- 2*sum(Intersection2_perm)/(Voxels_in_A_perm+Voxels_in_B_perm)

Dice_PERM_Distribution[p] <- Dice_perm

}


p_value <- mean(Dice_PERM_Distribution >= Dice)


plot(hist(Dice_PERM_Distribution), 
     xlab=expression(Dice_Coefficient), 
     main="")
abline(v=Dice, col="red", lty="dotted")
text(10,10, "p-value", col="blue", cex=2)
