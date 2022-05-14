# LETS-THINK
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
local_a8 = 0x44323a24561e4a2b;
local_a0 = 0x544d3e49203a4747;
local_98 = 0x404f4f401d3a4f4b;
local_94 = 0x584d;
```
#### STEP 2
 - Convert each variable to big endian:
```
local_a8 = 0x2B4A1E56243A3244;
local_a0 = 0x47473A20493E4D54;
local_98 = 0x4B4F3A1D404F4F40;
local_94 = 0x4D58;
```
STEP 3
 - Add 0x25 for each hex character `./calculate_hex_operator 2B 4A 1E 56 ...` <br/>
`--> 506f437b495f57696c6c5f456e63727970745f4265747465727d`
 - Convert hexadecimal string to ascii string

#### FLAG
`==> PoC{I_Will_Encrypt_Better}`
