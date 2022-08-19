k = int(input())
n = 0
for c in range(1,k):
    for b in range(1,c):
        for a in range(1,b):
            if c**2 == b**2 + a**2:
                n += 1
print(n)