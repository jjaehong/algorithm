# 색종이(10163)

# 보드에 N개의 색종이를 덮을 때
# 각 색종이의 넓이를 구해라!

import sys
sys.stdin = open('input.txt','r')

# 보드판
board = [[0]*1001 for _ in range(1001)]

max_r = max_c = 0 

N = int(input()) # 색종이 장수
for level in range(1,N+1):
    sc,sr,c,r = map(int, sys.stdin.readline().split())# 가장 왼쪽 아래 칸의 좌표와 너비,높이

    # 격자판 최대범위
    max_r = (sr+r) if max_r < (sr+r) else max_r
    max_c = (sc+c) if max_c < (sc+c) else max_c

    # N장 색종이 덮기
    for y in range(sr,sr+r):
        board[y][sc:sc+c] = [level]*c
        # print([level]*c)

# 각 색종이 넓이 세기
cnt = [0]*(N+1)
for i in range(max_r):
    for j in range(max_c):
        cnt[board[i][j]] += 1

# cnt.pop(0) 
for answer in cnt[1:N+1]:
    print(answer)