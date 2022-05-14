# REVERSE-ME
```
Type : Reverse Engineering
Plateform : PoC Innovation
Difficulty : [] [] [] [] []
Tools : Ghidra / Cutter
```
#### STEP 1
- Run program with Cutter or Ghidra
- List all functions in the program
#### STEP 2
- Read and analyse main function
- The flag appear in plain text in many conditions
```
  sVar1 = strlen(local_88);
  if (((long)local_bc == sVar1) &&
     (sVar1 = strlen("PoC{0h_Y0u_G0773n_57r0ng3r}"), (long)local_bc == sVar1)) {
    puts("Congratulation, you can validate the challenge with this flag.");
  }
```

#### FLAG
`==> PoC{0h_Y0u_G0773n_57r0ng3r}`
