#!/usr/bin/env python3
##
## PoC-Skyfall, 2022
## SHUFFLE
## File description:
## Uncrypt shuffle random hash
##

import random

def display(res):
    for i in res:
        print(chr(i), end='')

def parsing(flag):
    tab = list()
    for i in flag:
        tab.append(ord(i))
    return tab

def getshuffle(tab, seed):
    random.seed(seed)
    perm = list(range(len(tab)))
    random.shuffle(perm)
    random.seed()
    return perm

if __name__ == '__main__':
    for seed in range(0, 256):
        tab = parsing("f668cf029d2dc4234394e3f7a8S9f15f626Cc257Ce64}2dcd93323933d2{F1a1cd29db")
        perm = getshuffle(tab, seed)
        res = [None] * (len(tab))
        for i, j in enumerate(perm):
            res[j] = tab[i]
        tab[:] = res
        display(res)
