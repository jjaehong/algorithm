# 일곱난장이

# 9명 중 7명 찾기 : sum(9C7) == 100 
# 9명 중 포함안되는 2명 찾기 : 모든 키 합 - sum(9C2) == 100 : 


N = 9
total = 0
heights = []
for i in range(N):
    heights.append(int(input()))
    total += heights[i]
# print(total)

# 9C2
exclude1 = 0
exclude2 = 0
for i in range(N-1):
    for j in range(i+1,N):
        if heights[i] + heights[j] == total-100:
            exclude1, exclude2 = heights[i],heights[j]
            break

heights.remove(exclude1)
heights.remove(exclude2)

heights.sort()

for i in range(7):
    print(heights[i])
