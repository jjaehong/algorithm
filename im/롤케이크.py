# 롤케이크(3985)


# 김상근 : 길이 L미터 롤케잌 만듬 -> N명에게 나누어줌
# 롤 케잌 : 1~L, P~K번 조각을 원함

import sys
sys.stdin= open('input.txt','r')

L = int(input())
N = int(input())
cake = [0] * L
# N명의 사람들이
# max_cnt = 0
idx = 0
for i in range(1,N+1):
    P,K = map(int,input().split())


    expect = (P-K+1)
    
    [i for i in range(P,K)]
    max_cnt = 0
    cnt = 0
    if max_cnt < cnt:
        max_cnt = cnt
        idx = i
        
    # 원하는 부위 골라
    for j in range(P-1,K):
        if cake[j] == 0:
            cake[j] = i
            cnt += 1

    print(max_cnt)
    
# print(cake)
# print(len(expect))
# print(idx)


# print(cnt)
# print(max_cnt)


    
