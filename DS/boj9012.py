# 괄호

# 문제 해석
# PS : ')', '('
# VPS : 괄호 모양이 올바르게 구성됐을 때,
# x,y가 VPS -> xy도 VPS
# VPS 판별하여 YES or NO로 출력하기

# 문제 풀이
# 괄호 문제는 열린괄호 갯수와 닫힌괄호 갯수를 비교해야하니 스택이 어울림
# YES, NO 판별 => boolean

# 문제 상황
# 스택이 비어있다고 해서 무조건 VPS 상황은 아니다.
# 스택이 비어있지만 false가 되는 상황을 예외처리해야함.
# 예시 (())()')'

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for i in range(T):
    stack = []
    isVPS = True
    ps = input()
    for ch in ps:
        if ch == ')':
            if stack:
                stack.pop()
            else:
                isVPS = False
                break
        else:
            stack.append(ch)
            
    
    # for ch in ps:
    #     if ch == '(':
    #         stack.append(ch)
    #     else:
    #         if stack:
    #             stack.pop()
    #         else:
    #             isVPS = False
    #             break
            
    if len(stack) > 0:
        isVPS = False
    
    print( 'YES' if isVPS else 'NO')

        