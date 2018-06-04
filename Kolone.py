from sys import stdin
trash = stdin.readline()
ant1  = stdin.readline().rstrip('\n')
ant2  = stdin.readline().rstrip('\n')
t     = int(stdin.readline())

line  = ant1[::-1] + ant2
if t == 0:
    print(line)
else:
    pass
