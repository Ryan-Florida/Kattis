val1, val2 = [int(x) for x in input().strip('\n').split(" ")]
a = [0 for _ in range(val1)]

for j in range(val2):
    i, x, y = [int(t) for t in input().split(" ")]
    if i == 0:
        print(int(sum(a[x - 1:y])%(1e9 + 7)))
    elif i == 1:
        for j in range(y - x + 1):
            a[j + x - 1] += (j + 1)*(j + 2)*(j + 3)
    elif i == 2:
        for j in range(y - x + 1):
            a[j + x - 1] -= (j + 1)*(j + 2)*(j + 3)
