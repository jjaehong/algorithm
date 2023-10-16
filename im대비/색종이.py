# 색종이
# 검은영역 넓이 출력

# 흰색 도화지 : 각 가로, 세로 크기 : 100
# 검은색 색종이 : 각 가로, 세로 크기 : 10

board = [[0]*100 for _ in range(100)]
N = int(input()) # 색종이 갯수

for _ in range(N):
    c, r = map(int,input().split()) # 왼쪽 아랫 점의 좌표

    # 해당 영역을 1로 표시
    # 변의 길이 : c:c+10, r:r+10
    for i in range(r,r+10):
        for j in range(c,c+10):
            board[i][j] = 1

    # 1을 cnt하기
    ans = 0
    for lst in board:
        ans += sum(lst)

print(ans)