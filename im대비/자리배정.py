# 자리배정(10157)

# 2차원 배열에 달팽이 방식으로 자리배치
# K 번째 관객에게 배정될 좌석번호 c,r 구하기


# 달팽이 방식
# 델타(남동북서) 활용해서 값이 없으면 북으로 쭉가서 값을 입력, 값이 이미 있거나 범위 밖이면 방향전환! 이를 반복 

# 코드 최적화 
# 우리에게 익숙한 방식으로 바꿔서 표현! : 북동남서 => 남동북서
# 범위 밖 => 1로 둘러싸인 콘서트장 만들기('값이 있으면'과 동일하게 유효성 검사하기 위해)


C,R = map(int,input().split())
K = int(input())

# 남동북서
dr = [1,0,-1,0]
dc = [0,1,0,-1]

# 주변을 1로 둘러싸인 콘서트장 만들기 (범위 체크 필요없음)
concert = [[1] * (C+2)] + [ [1]+[0]*C+[1] for _ in range(R)] + [[1] * (C+2)]


# 자리 배정이 불가능한 경우 : 0
if R*C < K:
    print(0)

# 자리 배정하면서 K가 되면 그때 좌표 출력
else:

    # 시작값, 방향
    r,c,d = 1,1,0

    # K번째 전까지 좌표 출력
    for n in range(1,K):
        concert[r][c] = n
        nr = r + dr[d]
        nc = c + dc[d]
        # 비어있으면 이동가능
        if concert[nr][nc] == 0:
            r,c = nr,nc
        # 범위 밖 또는 이미 기록한 위치
        else:
            d = (d + 1) % 4             # 방향 전환
            r,c = r + dr[d], c + dc[d]  # 방향 전환된 위치에서 이동
            
    print(f'{c} {r}')


    
    

