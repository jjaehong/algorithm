# N개의 바구니에 1~N번 공을 M번 바꾼다.
# (바구니 2개안에 들어있는 공을 서로 교환)

import sys
sys.stdin = open('input.txt','r')

input = sys.stdin.readline
N,M = list(map(int, input().split()))

basket = [i+1 for i in range(N)]

for _ in range(M):
    i,j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)
    