# 팩토리얼 = 재귀함수

def factorial(N):
    if N == 0:
        return 1
    else:
        result = factorial(N-1)
        print(N, result, N * result)
        return N * result

        
N = int(input())
ans = factorial(N)
print(ans)

