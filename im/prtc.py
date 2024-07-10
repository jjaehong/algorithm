import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

answer = set()
for _ in range(10):
    x = int(input())
    y = x % 42
    answer.add(y)

print(len(answer))