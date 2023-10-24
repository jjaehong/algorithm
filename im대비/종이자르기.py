# 종이자르기(2628)

# 종이를 N번 자른 후 가장 큰 종이조각의 넓이(max)?
# 이 문제를 보면 어떻게 풀어야 할 지 아이디어가 안떠오른다..
# 그림을 그려보고 하나의 방법을 부여잡고 하는 것이 아니라, 하다가 안될 것 같으면 빠르게 다른 방향으로 생각해봐야한다.
# 좌표 갖고 하는 방법, 길이 갖고 하는 방법 등등..

import sys
sys.stdin = open('input.txt', 'r')

C,R = map(int,input().split())
N = int(input())
lst_r = [0,R]
lst_c = [0,C]
# 가능한 가로/세로 cut 위치를 저장후 정렬
for _ in range(N):
    d, idx = map(int,input().split()) # 방향(가로,세로), 위치
    if d == 0:
        lst_r.append(idx)
    else:
        lst_c.append(idx)
        
lst_r.sort()
lst_c.sort()

# print(lst_r)
# print(lst_c)


# 최대 넓이값 초기화
max_v = 0
for i in range(1,len(lst_r)):
    max_r = lst_r[i] - lst_r[i-1]
    for j in range(1,len(lst_c)):
        max_c = lst_c[j]-lst_c[j-1]
        # 최대 넓이 갱신
        max_v = max(max_v,(max_r * max_c))
print(max_v)




