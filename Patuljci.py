from sys import stdin

dwarves = [int(i) for i in stdin.readlines()]
dSum = sum(dwarves)
for d1 in dwarves:
    for d2 in dwarves:
        if (d1 != d2) and (dSum - d1 - d2 == 100):
            dwarves.remove(d1)
            dwarves.remove(d2)
            break
for dwarf in dwarves:
    print(dwarf)
