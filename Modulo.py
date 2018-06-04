from sys import stdin

lst = []
for line in stdin:
    test = int(line)%42
    if not (test in lst):
        lst.append(test)
print(len(lst))
