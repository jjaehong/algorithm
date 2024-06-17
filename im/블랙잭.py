# 블랙잭
# n개 중 r장 뽑기(nCr)


# 입력 값 저장
N,M = map(int,input().split()) # 카드 갯수 : N, 블랙잭 : M(이하)
cards = list(map(int,input().split()))

# max(card 3장의 합) <= M
# 5C3
answer_lst = []
answer = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            answer = cards[i] + cards[j] + cards[k]
            if answer <= M:
                answer_lst.append(answer)
                
print(max(answer_lst))


# 혹은 2장 제외 > M
# 5C2

# # N개 증 2개 뽑는 모든 조합(nC2) 
# for i in range(N-1):
#     for j in range(i+1,N):
#         cards[i] + cards[j]


