# GUESSME
```
Type: Miscellaneous
Plateform : FCSC
Difficulty : [x] [x] [] [] []
Tools : Python
```
#### PREREQUISITES
```
In FCSC competition, the challenge is hosted and we can acces it with netcat.
That is why sockets are used in the solution.
For our programm we need to use the pwn library.
Moreover we must specified remote host.
```
```
from pwn import *
socket = remote("challenges.france-cybersecurity-challenge.fr", "2001")
```
#### DESCRIPTION
 - The goal of this project is to find the good number.
 - We have 64 tries to find the good number.
 - The good number is between 0 and 18446744073709551614.
 - For more challenge, try to catch the flag in less than 5 minutes.
#### EXPLAINATION
 - To find out the number faster, we can use the dichotomic algorithm.<br/>
```
def dichotomic(value, n):
    myddle = int(value[0] + (value[1] - value[0]) / 2)
    socket.send(str(myddle).encode())
    receive = socket.recv(1024).decode()
    if receive == ">>> +1":
        return dichotomic((myddle, value[1]), n + 1)
    elif receive == ">>> -1":
        return dichotomic((value[0], myddle), n + 1)
    elif receive == ">>> 0":
        return "found: " + str(myddle)
    elif n > 64:
        return "not found"
    else:
        return "Error"
```
- Then, loop in the dichotomic function until the good number is found.
```
for x in range(0, 16):
    value = (0, 18446744073709551614)
    print(dichotomic(value, 0))
```
#### FLAG
`==> FCSC{7b20416c4f019ea4486e1e5c13d2d1667eebac732268b46268a9b64035ab294d}`