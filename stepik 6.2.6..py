start, goal, days = map(int, input().split())
flag = False
while days:
    days -= 1
    start += start * 0.1
    if start >= goal:
        flag= True
        break
print(flag)



start, goal, days = map(int, input().split())
for i in range(1, days+1):
    start = start + (0.10 * start)
if start >= goal:
    print(True)
else:
    print(False)
