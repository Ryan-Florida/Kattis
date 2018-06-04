from sys import stdin
trash = stdin.readline()
for line in stdin:
    seq   = [int(n) for n in line.split()][:-1]
    count = 0
    for i in range(len(seq) - 1):
        if seq[i + 1] > 2*seq[i]:
            count += seq[i + 1] - 2*seq[i]
    print(count)
