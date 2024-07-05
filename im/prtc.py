import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

x = input().split()

print(len(list(x)))

