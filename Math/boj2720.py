# 거스름돈(5$ 이하) 잘 좀 줘라.. 리암아..
# 쿼터(0.25$) / 다임(0.10) / 니켈(0.05) / 페니(0.01)
# 동전 갯수 최소화 -> 남은 금액이 동전 금액보다 크다면, 큰 동전을 계속 뺀다.

import sys
input = sys.stdin.readline
sys.stdin = open('input.txt','r')
# cash = [25, 10, 5, 1]
# T = int(input())
# for i in range(T):
#     change = int(input())
#     hereyouare = []
#     for j in range(4):
#         cnt = 0
#         while change >= cash[j]:
#             change = change - cash[j]
#             cnt += 1
#         hereyouare.append(cnt)
#     print(*hereyouare)        


# 빠른 속도 풀이
# 몫 -> 동전 갯수
# 나머지 -> 동전 금액을 뺀 change
for _ in range(int(sys.stdin.readline())):
    m = int(sys.stdin.readline())
    Q, q=[m//25, m%25]
    D, d=[q//10, q%10]
    N, P=[d//5, d%5]
    print(Q, D, N, P)