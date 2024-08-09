# 재귀의 귀재(boj25501)

# 팰린드롬(회문) : 앞에서 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열
# 예시 ABABA, AAA
# isPalindrome 함수의 반환값과 recursion 함수의 호출 횟루를 한줄에 공백으로 구분하여 출력

import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt','r')

# # string, left, right
# def recursion(s, l, r):
#     global cnt
#     if l >= r: 
#         cnt +=1 
#         return 1
#     elif s[l] != s[r]:
#         cnt += 1
#         return 0
#     # s[l] == s[r]이면 계속 검사
#     else:
#         cnt += 1
#         return recursion(s, l+1, r-1)

# def isPalindrome(s):
#     return recursion(s, 0, len(s)-1)

# T = int(input())
# for _ in range(T):
#     cnt = 0
#     x = input()
#     print(isPalindrome(x), cnt)


def isPalindrome(s):
    # 회문 비교, s : 문자열, s[::-1] : 문자열 뒤집은거
    if s == s[::-1]: return 1
    return 0

def cnt(S):
    s, e = 0, len(S)-1
    while s<=e:
        if S[s]==S[e]: s, e = s+1, e-1
        else: return s+1

T = int(input())
for _ in range(T):
    S = input().strip()
    if isPalindrome(S):
        print(1, len(S)//2+1)
    else: print(0, cnt(S))