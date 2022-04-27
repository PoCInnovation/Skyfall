# TRANSLATE-ME
```
Type : Reverse Engineering
Plateform : PoC Innovation
Difficulty : [] [] [] [] []
Tools : Ghidra / GDB-Peda
```
#### INTRO
Write a C binary which produces the translate_me binary.</br>
If your binary is correct, call a PoC helper to get the flag !</br>
(binary info : ELF x86 32bits)
#### SOLUTION
- File : `solution.c`
- To compile : `gcc -o solution solution.c`
- To validate : `(./translate_me ; echo $?) && (./solution ; echo $?)`</br>
--> The 2 return values must be equal to 47
#### FLAG
`==> PoC{ckwa1flag?}`
