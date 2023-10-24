# 색종이(10163)

# 보드에 N개의 색종이를 놓았을 때
# 각 색종이의 넓이를 구해라!
# 겹쳐지는 부분이 있다면 그 넓이를 빼야함.

import sys
sys.stdin = open('input.txt','r')

# 보드판
arr = [[0]*1001 for _ in range(1001)]

max_r = max_c = 0 
N = int(input()) # 색종이 장수
for n in range(1,N+1):
    sj,si,w,h = map(int, sys.stdin.readline().split()) # 가장 왼쪽 아래 칸의 좌표와 너비,높이
    max_r = (si+h) if max_r < (si+h) else max_r
    max_c = (sj+w) if max_c < (sj+w) else max_c
    for i in range(si,si+h):
        arr[i][sj:sj+w] = [n]*w


cnt = [0]*(N+1)
for i in range(max_r):
    for j in range(max_c):
        cnt[arr[i][j]] += 1

# cnt.pop(0) 
for answer in cnt[1:N+1]:
    print(answer)
