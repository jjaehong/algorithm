# 색종이2
# 검은영역 둘레의 길이 출력
# 전체 순회하면서 1을 만나면 8방향 검사 : 0의 개수 => 1~5면 변임!

import sys
sys.stdin = open('input.txt','r')

# 동남서북
dr = [0,1,0,-1]
dc = [1,0,-1,0]

board = [[0]*102 for _ in range(102)]
N = int(input())
for _ in range(N):
    c,r = map(int,input().split())

    # 1로 색종이 표시
    for i in range(r,r+10):
        for j in range(c,c+10):
            board[i][j] = 1

    # 변의 길이
    answer = 0

    for i in range(102):
        for j in range(102):
            if board[i][j] == 1:
                # 0의 개수 세기
                cnt = 0
                for d in range(4):
                    nr = i + dr[d]
                    nc = j + dc[d]
                    if board[nr][nc] == 0:
                        cnt += 1
                # 상하좌우 0이 2개면 => 모서리
                if cnt == 2:
                    answer += 2
                # 상하좌우 0이 1개면 => 변
                elif cnt == 1:
                    answer += 1
print(answer)


