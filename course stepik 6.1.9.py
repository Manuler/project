result = []
for i in range(15, 100):
    if 3 * ((i//10) * (i%10)) == i:
        result.append(i)
print(result)