# 줄 세우기(2605)
# 한 줄로 선 후 차례대로 번호뽑기

# 0 / 0,1 / 0,1,2 / 뽑은 번호(card[i])만큼 앞자리로 보내서 줄을 서기
# ==> 이미 존재하는 앞 번호들을 card[i]만큼 뒤로 밀어서 덮어씌우기


# card 0 1 1 3 2
# arr  1 2 3 4 5
# 1
# 2 1
# 2 3 1
# 4 2 3 1
# 4 2 3 1  

'''
5
0 1 1 3 2
'''


N = int(input())
cards = list(map(int,input().split()))
students = [i for i in range(1,N+1)] # 학생들 배열 12345..
arr = [False]*(N) # 줄 배열

# 총 배열 돌아
for i in range(N):

    card,student = cards[i],students[i]
    # 앞 카드들을 뒤로 보내고 카드숫자만큼 앞으로 가
    if card != 0:
        for j in range(i,i-card,-1):
            arr[j] = arr[j-1]
        arr[i-card] = student
    else:
        arr[i] = student
print(*arr)