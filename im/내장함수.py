import sys
sys.stdin = open('input.txt','r')
# input = sys.stdin.readline -> 이거 쓰니까 틀림;

# 내장함수 정리

# 리스트,문자열.count('값',start,end) -> 값의 갯수, 오오오오 ㄱ래용?
# 리스트,문자열.index('값') -> 값의 위치(idx)

alphabet = input().upper()
alpha_list = list(set(alphabet))
cnt = []
for i in alpha_list:    
    cnt.append(alphabet.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(alpha_list[cnt.index(max(cnt))])
