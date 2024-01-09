import sys

maxNum = -1

for i in range(9):
    row = list(map(int, input().split()))
    if max(row) > maxNum:
        maxNum = max(row)
        x = i+1
        y = row.index(maxNum)+1

print(maxNum)
print(x,y)
