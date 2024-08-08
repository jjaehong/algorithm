# 다리 놓기
# 서 : N / 동 : M
# MCN = m ! // (m-n)! * n!
import sys
sys.stdin = open('input.txt','r')

def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)
        

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(factorial(M) // (factorial(M-N) * factorial(N)))
    