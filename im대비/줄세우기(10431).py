# 줄세우기(10431)

# 키 순서대로 번호를 부여함
# 반 아이들은 항상 20명,

# 아무나 한 명 뽑아 줄의 맨 앞에 세움
# '내' 앞에 키큰 학생이 없으면 그대로 서기
# '내' 앞에 키큰 한생 1명 이상 있으면 맨 앞에 선다.
# 그리고 앞에 있던 학생들은 한칸씩 뒤로 밀려남
# 이런 방식으로 마지막 까지 오름차순으로 정렬

# 학생들이 뒤로 물러난 걸음 수의 총합은?

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    heights = list(map(int,input().split()))[1:]
    

    cnt = 0
    # 총 배열 돌면서
    for i in range(1,20):
        # 앞에서부터 검사, 나보다 키 큰 사람 있으면 검사 후 앞에보내기 
        for j in range(0,i):
            if heights[i] < heights[j]:
                # heights.sort()
                cnt += 1
        
    print(heights[1:])
    print(f'{tc} {cnt}')
                







