N = int(input())
nums = list(map(int, input().split()))
v = int(input())
cnt = 0
for i in nums:
    if v == i:
       cnt += 1 

print(cnt)