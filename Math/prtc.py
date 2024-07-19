# import sys
# sys.stdin = open('input.txt','r')
# input = sys.stdin.readline

N = int(input())

# 갯수(s): 1, 6, 12, 18, 24  
# N, end : 1, 7, 19, 37, 61
# room   : 1, 2, 3,  4,  5


room = 0
end = 1
while N > end:
    room += 1
    end = end + 6 * room

print(room + 1) 