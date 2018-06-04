from sys import stdin
from math import cos, sin, tan, pi
g = 9.81
rad = pi/180
trash = stdin.readline()
y = lambda v0, O, x1: x1*tan(O*rad) - 0.5*g*(x1/cos(O*rad)/v0)**2
for line in stdin:
    v0, O, x1, h1, h2 = [float(num) for num in line.split()]
    height = y(v0, O, x1)
    if (height <= h1 + 1) or (height >= h2 - 1):
        print("Not Safe")
    else:
        print("Safe")
