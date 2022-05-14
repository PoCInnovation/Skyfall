# LAST-ONE
```
Type : Reverse Engineering
Plateform : PoC Innovation
Difficulty : [x] [] [] [] []
Tools : Ghidra / Cutter
```
#### STEP 1
 - Disassembly program
 - Get all variables content in main function
```
local_a8 = 0x2805182f0c341827;
local_a0 = 0x2803070e05141932;
local_98 = 0xa1c16122028043e;
```
#### STEP 2
 - Convert to big endian:
`2718340C2F180528321914050E0703283E04282012161C0A`
 - Go to CyberChef : https://gchq.github.io/CyberChef/
```
1 - From hex (specify input type)
2 - Xor 0x77 (apply xor opérator from each value)
```

#### FLAG
`==> PoC{Xor_Encrypt_Is_Weak}`
