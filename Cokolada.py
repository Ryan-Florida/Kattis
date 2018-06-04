from math import log2, floor
def main():
    K = int(input())

    if PowOf2(K):
        print(K, 0)
        return

    n = 2**(floor(log2(K)) + 1)
    b = FindNumberOfBreaks(K, n)
    print(n, b)

def PowOf2(K):
    n = log2(K)
    while(n > 0):
        n -= 1
    return n == 0

def FindNumberOfBreaks(K, n):
    n     /= 2
    b      = 1
    needed = K - n
    while n != needed:
        n /= 2
        b += 1
    return b


main()
