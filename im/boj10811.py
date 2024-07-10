# 바구니 뒤집기

# 핵심 : 역순 만들기(뒤집기) -> 슬라이싱

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, M = map(int,input().split())
basket = [i+1 for i in range(N)]

for _ in range(M):
    i,j = map(int, input().split())
    tmp = basket[i-1:j]
    tmp.reverse()
    basket[i-1:j] = tmp    
    
for i in range(N):
    print(basket[i], end=' ')
    
    
    
