# 색종이(10163)

# 보드에 N개의 색종이를 놓았을 때
# 각 색종이의 넓이를 구해라!
# 겹쳐지는 부분이 있다면 그 넓이를 빼야함.

import sys
sys.stdin = open('input.txt','r')

# 보드판
board = [[0]*1001 for _ in range(1001)]

N = int(input()) # 색종이 장수
for _ in range(N):
    sc,sr,c,r = map(int,input().split())# 가장 왼쪽 아래 칸의 좌표와 너비,높이

    # 색종이 놓기
    for i in range(sr,sr+r):
        for j in range(sc,sc+c):
            board[i][j] += 1
    


# print(board)
    total = 0
    for i in range(1001):
        for j in range(1001):
            for k in range(N):
                
            if board[i][j] 
    for lst in board:
        if lst[]
        total += sum(lst)

    print(total)