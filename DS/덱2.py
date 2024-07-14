import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

from collections import deque

dq = deque()

N = int(input())
for _ in range(N):
    command = list(map(int, input().split()))
    
    # appendleft
    if command[0] == 1:
        dq.appendleft(command[1])
    
    # append
    if command[0] == 2:
        dq.append(command[1])
    
    # popleft
    if command[0] == 3:
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    
    # pop
    if command[0] == 4:
        if dq:
            print(dq.pop())
        else:
            print(-1)
    
    # size
    if command[0] == 5:
        print(len(dq))
    
    # empty
    if command[0] == 6:
        if dq:
            print(0)
        else:
            print(1)
            
    # index
    if command[0] == 7:
        if dq:
            print(dq[0])
        else:
            print(-1)
            
    if command[0] == 8:
        if dq:
            print(dq[-1])
        else:
            print(-1)