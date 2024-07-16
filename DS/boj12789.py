# 도키도키 간식드리미


# 번호표 순서로만 간식을 줌
# 오른길 : 큐(popleft 해서 스택에 append 가능) 
# 아랫길 : 스택
# 비교 : 스택 top과 큐 front 더 작은 값을 내보내기
# 모두 내보내기 가능할 시 : Nice / 불가능할 시 : Sad

# 검사
# 큐끼리 비교
# 스택끼리 비교
# 큐와 스택 비교


import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))
dq = deque(x)
stack = []
if dq[0] == 1:
    dq.popleft()

# q와 stack이 안비어있으면 계속함 : 비교를 계속해야해.ㄴㄴㄴㄴㅇ
target = 1
# N개
while target == N:
        
    # 연속된 숫자일 때 완전히 pop
    if dq and dq[0] == target:
        dq.popleft()
        target += 1    
    elif stack and stack[-1] == target:
        stack.pop()
        target += 1
        
    # 큐 앞뒤idx 숫자 검사
    if len(dq) >= 2  and dq[0] > dq[1]:
        big = dq.popleft()
        stack.append(big)

if len(dq) == 0 and len(stack) == 0 :
    print('Nice')
else:
    print('Sad')


