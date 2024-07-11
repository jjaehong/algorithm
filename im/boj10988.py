import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 이소이 문제
# 앞으로 읽어도 이소이, 거꾸로 읽어도 이소이

# 1
text = input()
isParell = True
N = len(text)
for i in range(N//2):
    if text[i] != text[N-i-1]:
        isParell = False
        break

if isParell:
    print(1)
else:
    print(0)

# 2
# palindrome = input()
# if palindrome[::1] == palindrome[::-1]:
#     print(1)
# else: 
#     print(0)


