from sys import stdin

def GetDigitSum(N):
    digits = []
    while N > 0:
        digits.append(N%10)
        N //= 10
    return sum(digits)

L = int(stdin.readline())
D = int(stdin.readline())
X = int(stdin.readline())
for N in range(L, D):
    if GetDigitSum(N) == X:
        break
for M in range(D, L, -1):
    if GetDigitSum(M) == X:
        break
print(N)
print(M)
