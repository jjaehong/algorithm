# 

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    R,S = input().split()
    
    for i in S:
        print(i*int(R), end='')
    print()
        