# 동전0
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# Ai는 Ai-1의 배수라는 말 때문에 그리디로 풀 수 있음
N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
cnt = 0
for i in range(N-1,-1,-1):
    if K < coins[i]:
        continue
    while K >= coins[i]:
        cnt += (K // coins[i])
        K = K % coins[i]
    # print(f'coin: {coins[i]}, K: {K}, cnt: {cnt}')
print(cnt)
    