# 삼성시의 버스노선
# 카운트 배열

T = int(input())
for tc in range(1,T+1):
 
    cnt = [0] * 5001 # 버스정류장 수
 
    N = int(input()) # 버스노선 N개
 
    for _ in range(N):
        s,e = map(int,input().split()) # i번째 버스노선 s -> e
        for i in range(s,e+1):
            cnt[i] += 1
    # print(cnt)
 
 
    P = int(input())
    answer = []
    for _ in range(P):
        stop = int(input()) # 버스정류장 번호
        answer.append(str(cnt[stop]))
    print(f'#{tc} {" ".join(answer)}')