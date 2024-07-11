# 별찍기 7

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
for i in range(1,N+1):
    print(' '*(N-i)+'*'*(2*i-1))
for j in range(N-1,0,-1):
    print(' '*(N-j)+'*'*(2*j-1))
