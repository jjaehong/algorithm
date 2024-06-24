# 절댓값 힙
import sys
sys.stdin = open('input.txt','r')

# 빠른 입출력 시
import sys
import heapq as hq
input = sys.stdin.readline

## 우선순위 큐 + 튜플
# pq = []
# N = int(input()) 
# for _ in range(N):
#     x = int(input())
#     if x:
#         # 절댓값과 원본값을 모두 비교하기 위해서 이를 튜플로 묶어서 저장
#         hq.heappush(pq, (abs(x), x))
#     else:
#         print(hq.heappop(pq)[1] if pq else 0)


## x를 우선순위 큐에 넣어서 푸는 방식
min_heap = [] # 양수 : 1, 2, 3, 8, 13, 99, 242
max_heap = [] # 음수 : -1, -4, -10, -142
for _ in range(int(input())):
    x = int(input())
    if x:
        if x > 0:
            hq.heappush(min_heap,x)
        else:
            hq.heappush(max_heap,-x)
    else:
        if min_heap:
            if max_heap:
                if min_heap[0] < abs(max_heap[0]):
                    print(hq.heappop(min_heap))
                else:
                    print(-hq.heappop(max_heap))
            else:
                print(hq.heappop(min_heap))
        else:
            if max_heap:
                print(-hq.heappop(max_heap))
            else:
                print(0)
                