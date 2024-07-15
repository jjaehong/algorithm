# 큐스택
# boj24511

# 1번 -> 2번 -> 3번 -> N번 => Xn pop하기
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

N = int(input())
A = list(map(int, input().split())) # 자료구조 표시 : 큐(0), 스택(1)
B = list(map(int, input().split())) # i번 자료구조의 초기값(원소)
M = int(input())
C = list(map(int,input().split())) # 삽입할 원소(1번 자료구조에 삽입)


dq = deque()
for i in range(N):
    if A[i] == 0:
        dq.append(B[i])
for j in range(M):
    dq.appendleft(C[j])
    
for _ in range(M):
    print(dq.pop(), end = ' ')
