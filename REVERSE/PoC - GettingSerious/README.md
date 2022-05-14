# GETTING-SERIOUS
```
Type : Reverse Engineering
Plateform : PoC Innovation
Difficulty : [x] [] [] [] []
Tools : Ghidra / Cutter
```
#### STEP 1
- Run program with Cutter or Ghidra
- List all functions in the program
#### STEP 2
- Read and analyse main function
- Get all variable content:
```
local_a8 = 0x696373417b436f50;
local_a0 = 0x6972545f73495f69;
local_98 = 0x65696b63;
local_94 = 0x7d72;
 ```
#### STEP 3
- Convert each variable to big endian: </br>
https://blockchain-academy.hs-mittweida.de/litte-big-endian-converter/ </br>
```
local_a8 = 0x506F437B41736369;
local_a0 = 0x695F49735F547269;
local_98 = 0x636B6965;
local_94 = 0x727D;
```
- Convert hexadecimal to decimal then decimal to ascii

#### FLAG
`==> PoC{Ascii_Is_Trickier}`
