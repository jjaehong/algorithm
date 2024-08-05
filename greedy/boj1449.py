# 수리공 항승

import sys
sys.stdin = open('input.txt','r')

# 파이프 물 새는 곳 : 가장 왼쪽에서 정수만큼 떨어진 거리만 물이 샘
# 길이가 L인 테이프를 무한개 가지고 있음
# 물을 막을 때 그 위치 좌우 0.5만큼 간격을 줘야함
# 필요한 테이프의 최소 개수는?

# 앞에서부터 가다가 구멍이 있으면 테이프로 막음(x + L)
# 그리고 다시 시작

# N, L = map(int, input().split())
# location = list(map(int, input().split()))
# coord = [False] * 1001
# for i in location:
#     coord[i] = True

# ans = 0
# x = 0
# while x < 1001:
#     if coord[x]:
#         ans += 1
#         x += L
#     else:
#         x += 1
# print(ans)



## 만약 물이 새는 곳의 위치가 1억이 넘는다면? -> 위와 같은 풀이는 시간초과 날 듯 !
N, L = map(int, input().split())
locations = list(map(int, input().split())) # 좌표 압축
locations.sort()

start = locations[0]
cnt = 1

for i in locations[1:]:
    if i - start + 1 <= L:
        continue
    else:
        start = i
        cnt += 1
        
print(cnt)


