# 직사각형을 만드는 방법(8320)
# 정사각형 n개 -> 만들 수 있는 직사각형 갯수


# 1. 완전검색
# 가능한 경우를 모두 순회
# 가능한 모든 세로(행), 가로(열) 체크(그림 그리면서)

N = int(input()) 

answer1 = 0
for i in range(1,N+1):
    for j in range(i,N+1):
        if i*j <= N:
            answer1 += 1
print(answer1)


# 2. 그리디
# 규칙성 찾기
# 몫 연산을 통해 처리
answer2 = N
for i in range(2,N):
    # N//i - (i-1): 총 개수 - 겹치는 것    
    n = N//i - (i-1)
    if n < 1:
        break
    answer2 += n
print(answer2)

