# SHUFFLE
```
Type : Cryptography
Plateform : FCSC
Difficulty : [x] [x] [] [] []
Tools : Python
```
#### STEP 1
 - We got an ecrypted shuffle flag in output.txt
 - Create parsing function to convert str flag into word tab
```
def parsing(flag):
    tab = list()
    for i in flag:
        tab.append(ord(i))
    return tab
 ```
#### STEP 2
 - Generate new seed to change random number for shuffle encryption
 - Then, apply shuffle hash to the flag passed in parameter
```
def getshuffle(tab, seed):
    random.seed(seed)
    perm = list(range(len(tab)))
    random.shuffle(perm)
    random.seed()
    return perm
```
#### STEP 3
- Make a python main to call previous functions
- In the base code we can see a range seed number from 0 to 256</br>
--> Make a loop and display all unshuffled results
```
if __name__ == '__main__':
    for seed in range(0, 256):
        tab = parsing("f668cf029d2dc4234394e3f7a8S9f15f626Cc257Ce64}2dcd93323933d2{F1a1cd29db")
        perm = getshuffle(tab, seed)
        res = [None] * (len(tab))
        for i, j in enumerate(perm):
            res[j] = tab[i]
        tab[:] = res
        display(res)
```
#### STEP 4
 - Run program and save it's output :
`python3 solution.py > result.txt`
 - Find `FCSC` patern in generated file :
`cat result.txt | grep 'FCSC'`
#### FLAG
`==> FCSC{d93d32485aec7dc7622f13cd93b922363911c36d2ffd4f829f4e3264d0ac6952}`