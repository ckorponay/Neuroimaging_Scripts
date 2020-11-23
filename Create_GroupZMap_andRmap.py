#!/bin/tcsh -xef

set seedList = (28WGA 33WGA 35LY 38LY 39WGA 40LY 45LY 66LY 89WGA 102WGA 170FS 184WGA 252WGA 253WGA 255WGA)

set subjList = (100307 101006 103414 105014 105115 106521 107422 113619 114419 118528 122620 127933 129028 131217 133928 135225 138231 139637 141422 144832 148335 148840 149539 153025 158136 161630 163129 172332 173536 173940 175035 178950 180129 180432 181232 183034 188347 189349 190031 192843 194645 195041 195849 196144 205725 210011 210617 212116 212419 221319 224022 251833 268850 285345 285446 307127 334635 397154 397760 414229 422632 485757 486759 499566 530635 545345 567961 627549 654754 709551 748258 771354 782561 833148 904044 958976 965367)

#foreach seed ($seedList)
 #cd {$seed}

#Take the mean of all subject z-maps, create a group average Z map
 #3dMean -prefix Group_Zmap_{$seed}.nii '*_r2z+tlrc.*' -overwrite

#Convert the group Z map into a group r map using inverse Fisher transformation
 #3dcalc -a Group_Zmap_{$seed}.nii  -expr '(exp(2*a)-1)/(exp(2*a)+1)' -datum float -prefix Group_Rmap_{$seed}.nii

 #cd ../
#end




#foreach subj ($subjList)
 #   cd $subj
  #  foreach seed ($seedList)
   #      cp {$subj}_{$seed}_r+tlrc.* ../{$seed}
    #end
    #cd ../
#end

foreach seed ($seedList)
 cd {$seed}

#Take the mean of all subject z-maps, create a group average Z map
 3dMean -prefix Group_Rmap_final_{$seed}.nii 100307_{$seed}_r+tlrc.BRIK 100307_{$seed}_r+tlrc.HEAD 101006_{$seed}_r+tlrc.BRIK 101006_{$seed}_r+tlrc.HEAD 103414_{$seed}_r+tlrc.BRIK 103414_{$seed}_r+tlrc.HEAD 105014_{$seed}_r+tlrc.BRIK 105014_{$seed}_r+tlrc.HEAD 105115_{$seed}_r+tlrc.BRIK 105115_{$seed}_r+tlrc.HEAD 106521_{$seed}_r+tlrc.BRIK 106521_{$seed}_r+tlrc.HEAD 107422_{$seed}_r+tlrc.BRIK 107422_{$seed}_r+tlrc.HEAD 113619_{$seed}_r+tlrc.BRIK 113619_{$seed}_r+tlrc.HEAD 114419_{$seed}_r+tlrc.BRIK 114419_{$seed}_r+tlrc.HEAD 118528_{$seed}_r+tlrc.BRIK 118528_{$seed}_r+tlrc.HEAD 122620_{$seed}_r+tlrc.BRIK 122620_{$seed}_r+tlrc.HEAD 127933_{$seed}_r+tlrc.BRIK 127933_{$seed}_r+tlrc.HEAD 129028_{$seed}_r+tlrc.BRIK 129028_{$seed}_r+tlrc.HEAD 131217_{$seed}_r+tlrc.BRIK 131217_{$seed}_r+tlrc.HEAD 133928_{$seed}_r+tlrc.BRIK 133928_{$seed}_r+tlrc.HEAD 135225_{$seed}_r+tlrc.BRIK 135225_{$seed}_r+tlrc.HEAD 138231_{$seed}_r+tlrc.BRIK 138231_{$seed}_r+tlrc.HEAD 139637_{$seed}_r+tlrc.BRIK 139637_{$seed}_r+tlrc.HEAD 141422_{$seed}_r+tlrc.BRIK 141422_{$seed}_r+tlrc.HEAD 144832_{$seed}_r+tlrc.BRIK 144832_{$seed}_r+tlrc.HEAD 148335_{$seed}_r+tlrc.BRIK 148335_{$seed}_r+tlrc.HEAD 148840_{$seed}_r+tlrc.BRIK 148840_{$seed}_r+tlrc.HEAD 149539_{$seed}_r+tlrc.BRIK 149539_{$seed}_r+tlrc.HEAD 153025_{$seed}_r+tlrc.BRIK 153025_{$seed}_r+tlrc.HEAD 158136_{$seed}_r+tlrc.BRIK 158136_{$seed}_r+tlrc.HEAD 161630_{$seed}_r+tlrc.BRIK 161630_{$seed}_r+tlrc.HEAD 163129_{$seed}_r+tlrc.BRIK 163129_{$seed}_r+tlrc.HEAD 172332_{$seed}_r+tlrc.BRIK 172332_{$seed}_r+tlrc.HEAD 173536_{$seed}_r+tlrc.BRIK 173536_{$seed}_r+tlrc.HEAD 173940_{$seed}_r+tlrc.BRIK 173940_{$seed}_r+tlrc.HEAD 175035_{$seed}_r+tlrc.BRIK 175035_{$seed}_r+tlrc.HEAD 178950_{$seed}_r+tlrc.BRIK 178950_{$seed}_r+tlrc.HEAD 180129_{$seed}_r+tlrc.BRIK 180129_{$seed}_r+tlrc.HEAD 180432_{$seed}_r+tlrc.BRIK 180432_{$seed}_r+tlrc.HEAD 181232_{$seed}_r+tlrc.BRIK 181232_{$seed}_r+tlrc.HEAD 183034_{$seed}_r+tlrc.BRIK 183034_{$seed}_r+tlrc.HEAD 188347_{$seed}_r+tlrc.BRIK 188347_{$seed}_r+tlrc.HEAD 189349_{$seed}_r+tlrc.BRIK 189349_{$seed}_r+tlrc.HEAD 190031_{$seed}_r+tlrc.BRIK 190031_{$seed}_r+tlrc.HEAD 192843_{$seed}_r+tlrc.BRIK 192843_{$seed}_r+tlrc.HEAD 194645_{$seed}_r+tlrc.BRIK 194645_{$seed}_r+tlrc.HEAD 195041_{$seed}_r+tlrc.BRIK 195041_{$seed}_r+tlrc.HEAD 195849_{$seed}_r+tlrc.BRIK 195849_{$seed}_r+tlrc.HEAD 196144_{$seed}_r+tlrc.BRIK 196144_{$seed}_r+tlrc.HEAD 205725_{$seed}_r+tlrc.BRIK 205725_{$seed}_r+tlrc.HEAD 210011_{$seed}_r+tlrc.BRIK 210011_{$seed}_r+tlrc.HEAD 210617_{$seed}_r+tlrc.BRIK 210617_{$seed}_r+tlrc.HEAD 212116_{$seed}_r+tlrc.BRIK 212116_{$seed}_r+tlrc.HEAD 212419_{$seed}_r+tlrc.BRIK 212419_{$seed}_r+tlrc.HEAD 221319_{$seed}_r+tlrc.BRIK 221319_{$seed}_r+tlrc.HEAD 224022_{$seed}_r+tlrc.BRIK 224022_{$seed}_r+tlrc.HEAD 251833_{$seed}_r+tlrc.BRIK 251833_{$seed}_r+tlrc.HEAD 268850_{$seed}_r+tlrc.BRIK 268850_{$seed}_r+tlrc.HEAD 285345_{$seed}_r+tlrc.BRIK 285345_{$seed}_r+tlrc.HEAD 285446_{$seed}_r+tlrc.BRIK 285446_{$seed}_r+tlrc.HEAD 307127_{$seed}_r+tlrc.BRIK 307127_{$seed}_r+tlrc.HEAD 334635_{$seed}_r+tlrc.BRIK 334635_{$seed}_r+tlrc.HEAD 397154_{$seed}_r+tlrc.BRIK 397154_{$seed}_r+tlrc.HEAD 397760_{$seed}_r+tlrc.BRIK 397760_{$seed}_r+tlrc.HEAD 414229_{$seed}_r+tlrc.BRIK 414229_{$seed}_r+tlrc.HEAD 422632_{$seed}_r+tlrc.BRIK 422632_{$seed}_r+tlrc.HEAD 485757_{$seed}_r+tlrc.BRIK 485757_{$seed}_r+tlrc.HEAD 486759_{$seed}_r+tlrc.BRIK 486759_{$seed}_r+tlrc.HEAD 499566_{$seed}_r+tlrc.BRIK 499566_{$seed}_r+tlrc.HEAD 530635_{$seed}_r+tlrc.BRIK 530635_{$seed}_r+tlrc.HEAD 545345_{$seed}_r+tlrc.BRIK 545345_{$seed}_r+tlrc.HEAD 567961_{$seed}_r+tlrc.BRIK 567961_{$seed}_r+tlrc.HEAD 627549_{$seed}_r+tlrc.BRIK 627549_{$seed}_r+tlrc.HEAD 654754_{$seed}_r+tlrc.BRIK 654754_{$seed}_r+tlrc.HEAD 709551_{$seed}_r+tlrc.BRIK 709551_{$seed}_r+tlrc.HEAD 748258_{$seed}_r+tlrc.BRIK 748258_{$seed}_r+tlrc.HEAD 771354_{$seed}_r+tlrc.BRIK 771354_{$seed}_r+tlrc.HEAD 782561_{$seed}_r+tlrc.BRIK 782561_{$seed}_r+tlrc.HEAD 833148_{$seed}_r+tlrc.BRIK 833148_{$seed}_r+tlrc.HEAD 904044_{$seed}_r+tlrc.BRIK 904044_{$seed}_r+tlrc.HEAD 958976_{$seed}_r+tlrc.BRIK 958976_{$seed}_r+tlrc.HEAD 965367_{$seed}_r+tlrc.BRIK 965367_{$seed}_r+tlrc.HEAD -overwrite
 
 cd ../
 end
