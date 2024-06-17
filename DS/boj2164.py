# 카드2

# 문제 해석
# 제일 위에 있는 카드를 먼저 버리고, 그 다음 위의 카드를 맨 밑으로 옮기는 것을 반복
# 가장 마지막에 남게 되는 카드는?


# 큐로 풀이
from collections import deque

N = int(input())
dq = deque(range(1, N+1))
    
# 조건이 true면 계속 실행 -> len(dq) == 0 이면 종료
while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())
print(dq.popleft())


# # 배열로 풀이 -> 시간 초과
# N = int(input())
# # * : 언패킹해서 값을 넣어줌
# arr = [*range(1, N+1)]
# while len(arr) > 1:
#     arr.pop(0)
#     arr.append(arr.pop(0))
# print(arr.pop())

# ## 500000을 넘기면 답이 안나오는 이유 -> 시간초과