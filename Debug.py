from sys import stdin
r, c = [int(n) for n in stdin.readline().split()]
matrix = [[int(i) for i in stdin.readline().rstrip('\n')] for k in range(r)]
subMat = [[[] for _ in range(3)] for _ in range(3)]
subMat[0][0].append(1)
subMat[0][0].append(0)
subMat
print(subMat)
#for row in matrix:
    #for element in row:
        #print(element[::-1])
