# 직사각형을 만드는 방법(8320)

# 정사각형 n개 -> 만들 수 있는 직사각형 갯수



#  n * (n-1)
# 2*2 <= 4
# 2*2, 2*3 <= 6
# 2*2, 2*3 3*3 <= 9
# 2*2, 2*3 3*3 3*4 <= 12
# 16
# 20
# 25
# 30

N = int(input()) 

answer = []
for i in range(1,):
    for j in range(1,N+1):
        answer.append(i*j)

print(answer)