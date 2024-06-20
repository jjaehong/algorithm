# 베스트셀러

# 1초 - 1억
# N개 1000개 

# 최대값의 문자열 출력 -> 키-값으로 저장 필요 -> 딕셔너리로 저장
# dict.keys()
# dict.values()
# dict.items()

import sys
sys.stdin = open('input.txt','r')


N = int(input())
d = {}
mx = 0
for i in range(N):
    book = input()
    
    if book in d:
        d[book] += 1 
    else:
        d[book] = 1
    
    # mx = max(d.values())
    mx = max(mx, d[book])    

candidate = []
for k, v in d.items():
    if v == mx:
        candidate.append(k)


print(sorted(candidate)[0])

# candidate.sort()
# print(candidate[0])

