# 평균

import sys
sys.stdin = open('input.txt','r')

N = int(input())
scores = list(map(int, input().split()))

sum_v = 0
max_v = 0
for i in range(N):
    sum_v += scores[i]
    max_v = scores[i] if max_v < scores[i] else max_v

print(sum_v/(max_v*N)*100)
# print((sum(scores) * 100) / (N*max(scores)))




