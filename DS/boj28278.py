# 스택 2
# 스택에 대한 이해, sys.stdin.readline의 중요성

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    
    x = list(map(int, input().split()))
    
    # push
    if x[0] == 1:
        stack.append(x[1])
    
    # pop
    if x[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    # size
    if x[0] == 3:
        print(len(stack))
    
    # empty   
    if x[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    
    # top
    if x[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
