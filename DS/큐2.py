# 큐2
# boj18258

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque

dq = deque()

N = int(input())
for i in range(N):
    command = list(input().split())
    
    # push
    if command[0] == 'push':
        dq.append(int(command[1]))
    
    # pop, pop(0) 
    if command[0] == 'pop':
        if dq:    
            print(dq.popleft())
        else:
            print(-1) 
    
    # size
    if command[0] == 'size':
        print(len(dq))
    
    # empty
    if command[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    
    # front
    if command[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
            
    # back
    if command[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)