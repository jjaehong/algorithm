# 색종이2
# 검은영역 둘레의 길이 출력

# 왼위, 오른아래
dr = [-1,1]
dc = [-1,1]

board = [[0]*100 for _ in range(100)]
N = int(input())
for _ in range(N):
    c,r = map(int,input().split())

    # 1로 색종이 표시
    for i in range(r,r+10):
        for j in range(c,c+10):
            board[i][j] = 1

    for i in range(100):
        for j in range(100):
            for d in range(2):
                nr = i + dr[d]
                nc = j + dc[d]
                if (board[nr][nc] == None) or (board[nr][nc] == 0):
                    board[i][j] = 1
print(board)


