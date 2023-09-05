#!/usr/bin/python3
c = 0
for i in range(122, 96, -1):
    c += 1
    if c % 2 == 0:
        i = chr(i + (ord('A') - ord('a')))
    else:
        i = chr(i)
    print(i, end="")
