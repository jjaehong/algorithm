# 평균

import sys
sys.stdin = open('input.txt','r')

N = int(input())
scores = list(map(int, input().split()))
print((sum(scores) * 100) / (N*max(scores)))