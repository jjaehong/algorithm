import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

k,q,l,v,n,p = map(int, input().split())

answer = [0 for _ in range(6)]

if k != 1:
    answer[0] = 1 - k
if q != 1:
    answer[1] = 1 - q
if l != 2:
    answer[2] = 2 - l
if v != 2:
    answer[3] = 2 - v
if n != 2:
    answer[4] = 2 - n
if p != 8:
    answer[5] = 8 - p

print(*answer)