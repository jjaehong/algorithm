T = int(input())
arr = []
for i in range(T):
    string = input()
    last = len(string)
    arr.append(string[0]+string[last-1])


for answer in arr:
    print(answer)
    