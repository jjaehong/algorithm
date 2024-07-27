# C,R = map(int,input().split())
# K = int(input())

# # 남동북서
# # dr = [1,0,-1,0]
# # dc = [0,1,0,-1]

# # 1로 둘러싸인 콘서트장 만들기 (범위 체크 필요없음)
# # concert = [[1] * (C+2)] + [ [1]+[0]*C+[1] for _ in range(R)] + [[1] * (C+2)]


# # 자리 배정이 불가능한 경우 : 0
# if R*C < K:
#     print(0)

# # 자리 배정하면서 K가 되면 그때 좌표 출력
# else:

#     di, dj = [1,0,-1,0], [0,1,0,-1]
#     arr = [[1] * (C+2)] + [[1]+[0]*C+[1] for _ in range(R)] + [[1] * (C+2)]

#     # 시작값, 방향
#     ci,cj,d = 1,1,0
#     for n in range(1,K):
#         arr[ci][cj] = n
#         ni = ci + di[d]
#         nj = cj + dj[d]
#         if arr[ni][nj] == 0:
#             ci,cj = ni,nj
#         else:
#             d = (d + 1) % 4
#             ci,cj = ci+di[d] , cj +dj[d]
#     print(f'{cj} {ci}')

print((4620) % 1000)