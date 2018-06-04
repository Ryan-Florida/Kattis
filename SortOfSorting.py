from sys import stdin
def Sort(names):
    if len(names) == 1:
        return names
    for i in range(len(names) - 1):
        for i in range(len(names) - 1):
            if names[i][0:2] > names[i + 1][0:2]:
                names[i], names[i + 1] = names[i + 1], names[i]
    return names

flag = int(stdin.readline())
while(flag != 0):
    names = []
    for i in range(flag):
        names.append(stdin.readline().rstrip())
    names = Sort(names)
    for name in names:
        print(name)
    print()
    flag = int(stdin.readline())
