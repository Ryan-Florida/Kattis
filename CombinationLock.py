from sys import stdin

for line in stdin:
    degrees = 1080
    start, combo = int(line.split()[0])*9, [9*int(num) for num in line.split()[1:]]
    if combo[0] == combo[1]:
        break
    degrees += (start    - combo[0])%360
    degrees += (combo[1] - combo[0])%360
    degrees += (combo[1] - combo[2])%360
    print(degrees)
