# PATCH-ME
```
Type : Reverse Engineering
Plateform : PoC Innovation
Difficulty : [] [] [] [] []
Tools : Cutter
```
#### STEP 1
- Run program with Cutter
- Go into graph mode and look architecture</br>
--> We can see that a function is not called
#### STEP 2
- Pass Cutter in writing mode
- From main function edit `jne` instruction</br>
--> Change jne address to point to the print flag function
- Re-open programm in read-only mode and run it

#### FLAG
`==> PoC{GG}`
