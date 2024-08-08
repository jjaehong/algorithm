# 베라의 패션(boj15439)
import sys
sys.stdin = open('input.txt','r')

N = int(input())
 
cnt = 0
for i in range(N-1):
    for j in range(i+1,N):
        if N == 1:
            print(0)
            break
        else:
            cnt += 1
print(cnt*2)

## 간단 풀이
# print(N*(N-1))