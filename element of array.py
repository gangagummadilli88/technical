n = int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
    count0 = arr.count(0)
even = [x for x in arr if x != 0]
result=even +[0]*count0
print(*result)
