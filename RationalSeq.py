from sys import stdin

trash = stdin.readline()
t = Tree(1, 1)
print(t.leftChild)
t.addChild()
print(t.leftChild[1][1])
