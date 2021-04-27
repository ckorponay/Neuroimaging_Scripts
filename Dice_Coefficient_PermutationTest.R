### PURPOSE: given two clusters of voxels, quantify their overlap (using the Dice coefficient), and then assess the statistical significance of their overlap using permutation testing ######


###Import the binary mask files whose overlap you want to assess

d6 <- read.table(file="Voxel_Cluster_1.csv", header=F, sep=",")
d7 <- read.table(file="Voxel_Cluster_2.csv", header=F, sep=",")


###Calculate the actual Dice coefficient between the two mask images####
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
