import sys
sys.stdin = open('input.txt','r')


# 그룹 단어의 수
# ccazzzzbb -> 연속해서 나타남

N = int(input())
group_word = N
for i in range(N):
    
    word = input()
    
    for j in range(len(word)-1):
        # 문자 연속성 검사
        if word[j] == word[j+1]:
            continue
        # 연속성이 없다면, 그 문자가 뒤에 문자들 중에 있어? -> 있으면 그룹 단어 아님
        elif word[j] in word[j+1:]:
          group_word -= 1
          break
print(group_word)



