# 큐2

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque

q = deque()

N = int(input())
for i in range(N):
    command = list(input().split())
    
    # push
    if command[0] == 'push':
        q.append(int(command[1]))
    
    # pop, pop(0) 
    if command[0] == 'pop':
        if q:    
            print(q.popleft())
        else:
            print(-1) 
    
    # size
    if command[0] == 'size':
        print(len(q))
    
    # empty
    if command[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    
    # front
    if command[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
            
    # back
    if command[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)