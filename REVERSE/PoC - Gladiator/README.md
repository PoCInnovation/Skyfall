# GLADIATOR
```
Type : Reverse Engineering
Plateform : PoC Innovation
Difficulty : [x] [x] [] [] []
Tools : GDB-peda / Cutter
```
```
PREREQUISITES
==> mv secret /tmp/secret
```
#### STEP 1
 - Load file with GDB-peda and found the address of the function `main`
 - From main go into `step1` function and found visible string `"PoC<3"`
 - Run program with PoC argument : `./gladiator "PoC<3"`

#### STEP 2
 - Open Cutter and run program into graph mode</br>
  Tips : Don't forgen to enable write mode (default read-only)
 - View `step2` function from address `0x00001405`
 - Inspect condition and edit `jmp` at `0x000014c6`</br>
--> drop at : str.You_re_the_first_one_to_the_lion

#### STEP 3
 - Like step 2, go into `step3` function and change value of `je` condition </br>
 - From `0x0000133a` to `0x00001358`</br>
--> drop at : str.Well_you_ve_won_this_arena

#### FLAG
`==> PoC{R3ver53_!S_Ez!!}`
