import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

li = [i+1 for i in range(30)]


for _ in range(28):
    submit = int(input())
    li.remove(submit)


print(min(li))
print(max(li))

